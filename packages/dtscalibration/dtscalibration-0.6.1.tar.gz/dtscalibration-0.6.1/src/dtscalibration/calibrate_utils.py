# coding=utf-8
import dask.array as da
import numpy as np
import scipy.sparse as sp
from scipy.sparse import linalg as ln


def calibration_single_ended_ols(ds, st_label, ast_label, verbose=False):
    """

    Parameters
    ----------
    ds : DataStore
    st_label : str
    ast_label : str
    verbose : bool

    Returns
    -------

    """
    cal_ref = ds.ufunc_per_section(
        label=st_label, ref_temp_broadcasted=True, calc_per='all')
    st = ds.ufunc_per_section(label=st_label, calc_per='all')
    ast = ds.ufunc_per_section(label=ast_label, calc_per='all')
    z = ds.ufunc_per_section(label='x', calc_per='all')

    assert not np.any(st <= 0.), 'There is uncontrolled noise in the ST signal'
    assert not np.any(
        ast <= 0.), 'There is uncontrolled noise in the AST signal'

    nx = z.size

    nt = ds[st_label].data.shape[1]

    p0_est = np.asarray([482., 0.1] + nt * [1.4])

    # Eqs for F and B temperature
    data1 = 1 / (cal_ref.T.ravel() + 273.15)  # gamma
    data2 = np.tile(-z, nt)  # dalpha
    data3 = np.tile([-1.], nt * nx)  # C
    data = np.concatenate([data1, data2, data3])

    # (irow, icol)
    coord1row = np.arange(nt * nx, dtype=int)
    coord2row = np.arange(nt * nx, dtype=int)
    coord3row = np.arange(nt * nx, dtype=int)

    coord1col = np.zeros(nt * nx, dtype=int)
    coord2col = np.ones(nt * nx, dtype=int)
    coord3col = np.repeat(np.arange(2, nt + 2, dtype=int), nx)

    rows = [coord1row, coord2row, coord3row]
    cols = [coord1col, coord2col, coord3col]
    coords = (np.concatenate(rows), np.concatenate(cols))

    # try scipy.sparse.bsr_matrix
    X = sp.coo_matrix((data, coords), shape=(nt * nx, nt + 2), copy=False)

    y = np.log(st / ast).T.ravel()
    # noinspection PyTypeChecker
    p0 = ln.lsqr(X, y, x0=p0_est, show=verbose, calc_var=True)

    return nt, z, p0


def calibration_single_ended_wls(
        ds,
        st_label,
        ast_label,
        st_var,
        ast_var,
        calc_cov=True,
        solver='sparse',
        verbose=False):
    """

    Parameters
    ----------
    ds : DataStore
    st_label
    ast_label
    st_var
    ast_var
    calc_cov : bool
      whether to calculate the covariance matrix. Required for calculation of confidence
      boiundaries. But uses a lot of memory.
    solver : {'sparse', 'stats'}
      Always use sparse to save memory. The statsmodel can be used to validate sparse solver
    verbose : bool

    Returns
    -------

    """
    cal_ref = ds.ufunc_per_section(
        label=st_label, ref_temp_broadcasted=True, calc_per='all')

    st = ds.ufunc_per_section(label=st_label, calc_per='all')
    ast = ds.ufunc_per_section(label=ast_label, calc_per='all')
    z = ds.ufunc_per_section(label='x', calc_per='all')

    assert not np.any(st <= 0.), 'There is uncontrolled noise in the ST signal'
    assert not np.any(
        ast <= 0.), 'There is uncontrolled noise in the AST signal'

    nx = z.size

    nt = ds[st_label].data.shape[1]

    p0_est = np.asarray([482., 0.1] + nt * [1.4])

    # Eqs for F and B temperature
    data1 = 1 / (cal_ref.T.ravel() + 273.15)  # gamma
    data2 = np.tile(-z, nt)  # dalpha
    data3 = np.tile([-1.], nt * nx)  # C
    data = np.concatenate([data1, data2, data3])

    # (irow, icol)
    coord1row = np.arange(nt * nx, dtype=int)
    coord2row = np.arange(nt * nx, dtype=int)
    coord3row = np.arange(nt * nx, dtype=int)

    coord1col = np.zeros(nt * nx, dtype=int)
    coord2col = np.ones(nt * nx, dtype=int)
    coord3col = np.repeat(np.arange(2, nt + 2, dtype=int), nx)

    rows = [coord1row, coord2row, coord3row]
    cols = [coord1col, coord2col, coord3col]
    coords = (np.concatenate(rows), np.concatenate(cols))

    # try scipy.sparse.bsr_matrix
    X = sp.coo_matrix((data, coords), shape=(nt * nx, nt + 2), copy=False)

    y = np.log(st / ast).T.ravel()

    w = (1 / st**2 * st_var + 1 / ast**2 * ast_var).T.ravel()

    if solver == 'sparse':
        p_sol, p_var, p_cov = wls_sparse(
            X, y, w=w, x0=p0_est, calc_cov=calc_cov, verbose=verbose)

    elif solver == 'stats':
        p_sol, p_var, p_cov = wls_stats(
            X, y, w=w, calc_cov=calc_cov, verbose=verbose)

    elif solver == 'external':
        return X, y, w, p0_est

    else:
        raise ValueError("Choose a valid solver")

    if calc_cov:
        return nt, z, p_sol, p_var, p_cov
    else:
        return nt, z, p_sol, p_var


def calibration_double_ended_ols(
        ds, st_label, ast_label, rst_label, rast_label, verbose=False):
    """

    Parameters
    ----------
    ds
    st_label
    ast_label
    rst_label
    rast_label
    verbose

    Returns
    -------

    """
    cal_ref = ds.ufunc_per_section(
        label=st_label, ref_temp_broadcasted=True, calc_per='all')

    st = ds.ufunc_per_section(label=st_label, calc_per='all')
    ast = ds.ufunc_per_section(label=ast_label, calc_per='all')
    rst = ds.ufunc_per_section(label=rst_label, calc_per='all')
    rast = ds.ufunc_per_section(label=rast_label, calc_per='all')
    z = ds.ufunc_per_section(label='x', calc_per='all')

    assert not np.any(st <= 0.), 'There is uncontrolled noise in the ST signal'
    assert not np.any(
        ast <= 0.), 'There is uncontrolled noise in the AST signal'
    assert not np.any(
        rst <= 0.), 'There is uncontrolled noise in the REV-ST signal'
    assert not np.any(
        rast <= 0.), 'There is uncontrolled noise in the REV-AST signal'

    nx = z.size

    _xsorted = np.argsort(ds.x.data)
    _ypos = np.searchsorted(ds.x.data[_xsorted], z)
    x_index = _xsorted[_ypos]

    nt = ds[st_label].data.shape[1]
    no = ds[st_label].data.shape[0]

    p0_est = np.asarray([482.] + nt * [1.4] + no * [0.])

    # Eqs for F and B temperature
    data1 = np.repeat(1 / (cal_ref.T.ravel() + 273.15), 2)  # gamma
    data3 = np.tile([-1., -1.], nt * nx)  # C
    data5 = np.tile([-1., 1.], nt * nx)  # alpha
    data9 = np.ones(nt * no, dtype=float)  # alpha
    data = np.concatenate([data1, data3, data5, data9])

    # (irow, icol)
    coord1row = np.arange(2 * nt * nx, dtype=int)
    coord3row = np.arange(2 * nt * nx, dtype=int)
    coord5row = np.arange(2 * nt * nx, dtype=int)

    coord9row = np.arange(2 * nt * nx, 2 * nt * nx + nt * no, dtype=int)

    coord1col = np.zeros(2 * nt * nx, dtype=int)
    coord3col = np.repeat(np.arange(nt, dtype=int) + 1, 2 * nx)
    coord5col = np.tile(np.repeat(x_index, 2) + nt + 1, nt)

    coord9col = np.tile(np.arange(no, dtype=int) + nt + 1, nt)

    rows = [coord1row, coord3row, coord5row, coord9row]
    cols = [coord1col, coord3col, coord5col, coord9col]
    coords = (np.concatenate(rows), np.concatenate(cols))

    # try scipy.sparse.bsr_matrix
    X = sp.coo_matrix(
        (data, coords), shape=(2 * nx * nt + nt * no, nt + 1 + no), copy=False)

    y1F = np.log(st / ast).T.ravel()
    y1B = np.log(rst / rast).T.ravel()
    y1 = da.stack([y1F, y1B]).T.ravel()
    y2F = np.log(ds[st_label].data / ds[ast_label].data).T.ravel()
    y2B = np.log(ds[rst_label].data / ds[rast_label].data).T.ravel()
    y2 = (y2B - y2F) / 2
    y = da.concatenate([y1, y2])
    # noinspection PyTypeChecker
    assert not np.any(
        np.isnan(y)), 'There are nan values in the measured (anti-) Stokes'

    p0 = ln.lsqr(X, y, x0=p0_est, show=verbose, calc_var=True)

    return nt, z, p0


def calibration_double_ended_wls(
        ds,
        st_label,
        ast_label,
        rst_label,
        rast_label,
        st_var,
        ast_var,
        rst_var,
        rast_var,
        calc_cov=True,
        solver='sparse',
        verbose=False):
    """


    Parameters
    ----------
    verbose
    ds : DataStore
    st_label
    ast_label
    rst_label
    rast_label
    st_var
    ast_var
    rst_var
    rast_var
    calc_cov
    solver : {'sparse', 'stats'}

    Returns
    -------

    """

    cal_ref = ds.ufunc_per_section(
        label=st_label, ref_temp_broadcasted=True, calc_per='all')

    st = ds.ufunc_per_section(label=st_label, calc_per='all')
    ast = ds.ufunc_per_section(label=ast_label, calc_per='all')
    rst = ds.ufunc_per_section(label=rst_label, calc_per='all')
    rast = ds.ufunc_per_section(label=rast_label, calc_per='all')
    z = ds.ufunc_per_section(label='x', calc_per='all')

    assert not np.any(st <= 0.), 'There is uncontrolled noise in the ST signal'
    assert not np.any(
        ast <= 0.), 'There is uncontrolled noise in the AST signal'
    assert not np.any(
        rst <= 0.), 'There is uncontrolled noise in the REV-ST signal'
    assert not np.any(
        rast <= 0.), 'There is uncontrolled noise in the REV-AST signal'

    nx = z.size

    _xsorted = np.argsort(ds.x.data)
    _ypos = np.searchsorted(ds.x.data[_xsorted], z)
    x_index = _xsorted[_ypos]

    no, nt = ds[st_label].data.shape

    p0_est_alpha = est_alpha_double(ds, st_label, ast_label, rst_label,
                                    rast_label, 50).data.tolist()
    p0_est = np.asarray([482.] + nt * [1.4] + p0_est_alpha)

    # Data for F and B temperature, 2 * nt * nx items
    data1 = np.repeat(1 / (cal_ref.T.ravel() + 273.15), 2)  # gamma
    data3 = -da.ones(2 * nt * nx, chunks=nt * nx)
    data5 = da.stack(
        (-da.ones(nt * nx, chunks=nt * nx),
         da.ones(nt * nx, chunks=nt * nx))).T.ravel()

    # Data for alpha, nt * no items
    data9 = da.ones(nt * no, chunks=(nt * no,))  # alpha

    data = da.concatenate([data1, data3, data5, data9])

    # Coords (irow, icol)
    coord1row = da.arange(2 * nt * nx, dtype=int, chunks=(nt * nx,))  # gamma
    coord3row = da.arange(2 * nt * nx, dtype=int, chunks=(nt * nx,))  # C
    coord5row = da.arange(2 * nt * nx, dtype=int, chunks=(nt * nx,))  # alpha

    coord9row = da.arange(
        2 * nt * nx, 2 * nt * nx + nt * no, dtype=int,
        chunks=(nt * no,))  # alpha

    coord1col = da.zeros(2 * nt * nx, dtype=int, chunks=(nt * nx,))  # gamma
    coord3col = np.repeat(da.arange(nt, dtype=int, chunks=(nt,)) + 1,
                          2 * nx).rechunk(nt * nx)  # C
    coord5col = da.tile(np.repeat(x_index, 2) + nt + 1, nt).rechunk(
        nt * nx)  # alpha
    coord9col = da.tile(
        da.arange(no, dtype=int, chunks=(nt * no,)) + nt + 1, nt)  # alpha

    rows = [coord1row, coord3row, coord5row, coord9row]
    cols = [coord1col, coord3col, coord5col, coord9col]
    coords = (da.concatenate(rows).compute(), da.concatenate(cols).compute())

    # try scipy.sparse.bsr_matrix
    X = sp.coo_matrix(
        (data, coords), shape=(2 * nx * nt + nt * no, nt + 1 + no), copy=False)

    # Spooky way to interleave and ravel arrays in correct order. Works!
    y1F = np.log(st / ast).T.ravel()
    y1B = np.log(rst / rast).T.ravel()
    y1 = da.stack([y1F, y1B]).T.ravel()

    y2F = np.log(ds[st_label].data / ds[ast_label].data).T.ravel()
    y2B = np.log(ds[rst_label].data / ds[rast_label].data).T.ravel()
    y2 = (y2B - y2F) / 2
    y = da.concatenate([y1, y2])

    assert not np.any(
        np.isnan(y)), 'There are nan values in the measured (anti-) Stokes'

    # Calculate the reprocical of the variance (not std)
    w1F = (1 / st**2 * st_var + 1 / ast**2 * ast_var).T.ravel()
    w1B = (1 / rst**2 * rst_var + 1 / rast**2 * rast_var).T.ravel()
    w1 = da.stack([w1F, w1B]).T.ravel()

    w2 = (
        0.5 / ds[st_label].data**2 * st_var +
        0.5 / ds[ast_label].data**2 * ast_var +
        0.5 / ds[rst_label].data**2 * rst_var +
        0.5 / ds[rast_label].data**2 * rast_var).T.ravel()
    w = da.concatenate([w1, w2])

    if solver == 'sparse':
        p_sol, p_var, p_cov = wls_sparse(
            X, y, w=w, x0=p0_est, calc_cov=calc_cov, verbose=verbose)

    elif solver == 'stats':
        p_sol, p_var, p_cov = wls_stats(
            X, y, w=w, calc_cov=calc_cov, verbose=verbose)

    elif solver == 'external':
        p_sol, p_var, p_cov = None, None, None
        return X, y, w, p0_est

    if calc_cov:
        return nt, z, p_sol, p_var, p_cov
    else:
        return nt, z, p_sol, p_var


def wls_sparse(X, y, w=1., calc_cov=False, verbose=False, **kwargs):
    """

    Parameters
    ----------
    X
    y
    w
    calc_cov
    verbose
    kwargs

    Returns
    -------

    """
    # The var returned by ln.lsqr is normalized by the variance of the error. To
    # obtain the correct variance, it needs to be scaled by the variance of the error.

    w_std = np.asarray(np.sqrt(w))
    wy = np.asarray(w_std * y)

    w_std = np.broadcast_to(
        np.atleast_2d(np.squeeze(w_std)).T, (X.shape[0], 1))

    if not sp.issparse(X):
        wX = w_std * X
    else:
        wX = X.multiply(w_std)

    # noinspection PyTypeChecker
    out_sol = ln.lsqr(wX, wy, show=verbose, calc_var=True, **kwargs)

    p_sol = out_sol[0]

    # The residual degree of freedom, defined as the number of observations
    # minus the rank of the regressor matrix.
    nobs = len(y)
    npar = X.shape[1]  # ==rank

    degrees_of_freedom_err = nobs - npar
    # wresid = np.exp(wy) - np.exp(wX.dot(p_sol))  # this option is better. difference is small
    wresid = wy - wX.dot(p_sol)  # this option is done by statsmodel
    err_var = np.dot(wresid, wresid) / degrees_of_freedom_err

    if calc_cov:
        arg = wX.T.dot(wX)

        if sp.issparse(arg):
            arg = arg.todense()

        p_cov = np.array(np.linalg.inv(arg) * err_var)

        p_var = np.diagonal(p_cov)
        return p_sol, p_var, p_cov

    else:
        p_var = out_sol[-1] * err_var  # normalized covariance
        return p_sol, p_var


def wls_stats(X, y, w=1., calc_cov=False, verbose=False):
    """

    Parameters
    ----------
    X
    y
    w
    calc_cov
    verbose

    Returns
    -------

    """
    import statsmodels.api as sm

    y = np.asarray(y)
    w = np.asarray(w)

    if sp.issparse(X):
        X = X.todense()

    mod_wls = sm.WLS(y, X, weights=w)
    res_wls = mod_wls.fit()

    if verbose:
        print(res_wls.summary())

    p_sol = res_wls.params
    p_cov = res_wls.cov_params()
    p_var = res_wls.bse**2

    if calc_cov:
        return p_sol, p_var, p_cov
    else:
        return p_sol, p_var


def est_alpha_double(ds, st_label, ast_label, rst_label, rast_label, n):
    """

    Parameters
    ----------
    ds
    st_label
    ast_label
    rst_label
    rast_label
    n : int
        Number of time steps to average, ceiled by the
        available time steps.

    Returns
    -------

    """
    if n > ds.time.size:
        n = ds.time.size

    islice = np.linspace(
        start=0,
        stop=ds.time.size - 1,
        num=n,
        dtype=int)

    st = ds[st_label].isel(time=islice).mean(dim='time')
    ast = ds[ast_label].isel(time=islice).mean(dim='time')
    rst = ds[rst_label].isel(time=islice).mean(dim='time')
    rast = ds[rast_label].isel(time=islice).mean(dim='time')

    return (np.log(rst / rast) - np.log(st / ast)) / 2
