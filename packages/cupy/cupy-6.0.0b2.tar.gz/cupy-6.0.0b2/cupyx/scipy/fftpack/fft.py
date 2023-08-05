import cupy
from cupy.cuda import cufft
from cupy.fft.fft import _fft, _default_fft_func


def fft(x, n=None, axis=-1, overwrite_x=False):
    """Compute the one-dimensional FFT.

    Args:
        x (cupy.ndarray): Array to be transformed.
        n (None or int): Length of the transformed axis of the output. If ``n``
            is not given, the length of the input along the axis specified by
            ``axis`` is used.
        axis (int): Axis over which to compute the FFT.
        overwrite_x (bool): If True, the contents of ``x`` can be destroyed.

    Returns:
        cupy.ndarray:
            The transformed array which shape is specified by ``n`` and type
            will convert to complex if that of the input is another.

    .. seealso:: :func:`scipy.fftpack.fft`
    """
    return _fft(x, (n,), (axis,), None, cufft.CUFFT_FORWARD,
                overwrite_x=overwrite_x)


def ifft(x, n=None, axis=-1, overwrite_x=False):
    """Compute the one-dimensional inverse FFT.

    Args:
        x (cupy.ndarray): Array to be transformed.
        n (None or int): Length of the transformed axis of the output. If ``n``
            is not given, the length of the input along the axis specified by
            ``axis`` is used.
        axis (int): Axis over which to compute the FFT.
        overwrite_x (bool): If True, the contents of ``x`` can be destroyed.

    Returns:
        cupy.ndarray:
            The transformed array which shape is specified by ``n`` and type
            will convert to complex if that of the input is another.

    .. seealso:: :func:`scipy.fftpack.ifft`
    """
    return _fft(x, (n,), (axis,), None, cufft.CUFFT_INVERSE,
                overwrite_x=overwrite_x)


def fft2(x, shape=None, axes=(-2, -1), overwrite_x=False):
    """Compute the two-dimensional FFT.

    Args:
        x (cupy.ndarray): Array to be transformed.
        shape (None or tuple of ints): Shape of the transformed axes of the
            output. If ``shape`` is not given, the lengths of the input along
            the axes specified by ``axes`` are used.
        axes (tuple of ints): Axes over which to compute the FFT.
        overwrite_x (bool): If True, the contents of ``x`` can be destroyed.

    Returns:
        cupy.ndarray:
            The transformed array which shape is specified by ``shape`` and
            type will convert to complex if that of the input is another.

    .. seealso:: :func:`scipy.fftpack.fft2`
    """
    func = _default_fft_func(x, shape, axes)
    return func(x, shape, axes, None, cufft.CUFFT_FORWARD,
                overwrite_x=overwrite_x)


def ifft2(x, shape=None, axes=(-2, -1), overwrite_x=False):
    """Compute the two-dimensional inverse FFT.

    Args:
        x (cupy.ndarray): Array to be transformed.
        shape (None or tuple of ints): Shape of the transformed axes of the
            output. If ``shape`` is not given, the lengths of the input along
            the axes specified by ``axes`` are used.
        axes (tuple of ints): Axes over which to compute the FFT.
        overwrite_x (bool): If True, the contents of ``x`` can be destroyed.

    Returns:
        cupy.ndarray:
            The transformed array which shape is specified by ``shape`` and
            type will convert to complex if that of the input is another.

    .. seealso:: :func:`scipy.fftpack.ifft2`
    """
    func = _default_fft_func(x, shape, axes)
    return func(x, shape, axes, None, cufft.CUFFT_INVERSE,
                overwrite_x=overwrite_x)


def fftn(x, shape=None, axes=None, overwrite_x=False):
    """Compute the N-dimensional FFT.

    Args:
        x (cupy.ndarray): Array to be transformed.
        shape (None or tuple of ints): Shape of the transformed axes of the
            output. If ``shape`` is not given, the lengths of the input along
            the axes specified by ``axes`` are used.
        axes (tuple of ints): Axes over which to compute the FFT.
        overwrite_x (bool): If True, the contents of ``x`` can be destroyed.

    Returns:
        cupy.ndarray:
            The transformed array which shape is specified by ``shape`` and
            type will convert to complex if that of the input is another.

    .. seealso:: :func:`scipy.fftpack.fftn`
    """
    func = _default_fft_func(x, shape, axes)
    return func(x, shape, axes, None, cufft.CUFFT_FORWARD,
                overwrite_x=overwrite_x)


def ifftn(x, shape=None, axes=None, overwrite_x=False):
    """Compute the N-dimensional inverse FFT.

    Args:
        x (cupy.ndarray): Array to be transformed.
        shape (None or tuple of ints): Shape of the transformed axes of the
            output. If ``shape`` is not given, the lengths of the input along
            the axes specified by ``axes`` are used.
        axes (tuple of ints): Axes over which to compute the FFT.
        overwrite_x (bool): If True, the contents of ``x`` can be destroyed.

    Returns:
        cupy.ndarray:
            The transformed array which shape is specified by ``shape`` and
            type will convert to complex if that of the input is another.

    .. seealso:: :func:`scipy.fftpack.ifftn`
    """
    func = _default_fft_func(x, shape, axes)
    return func(x, shape, axes, None, cufft.CUFFT_INVERSE,
                overwrite_x=overwrite_x)


def rfft(x, n=None, axis=-1, overwrite_x=False):
    """Compute the one-dimensional FFT for real input.

    The returned real array contains

    .. code-block:: python

        [y(0),Re(y(1)),Im(y(1)),...,Re(y(n/2))]  # if n is even
        [y(0),Re(y(1)),Im(y(1)),...,Re(y(n/2)),Im(y(n/2))]  # if n is odd

    Args:
        x (cupy.ndarray): Array to be transformed.
        n (None or int): Length of the transformed axis of the output. If ``n``
            is not given, the length of the input along the axis specified by
            ``axis`` is used.
        axis (int): Axis over which to compute the FFT.
        overwrite_x (bool): If True, the contents of ``x`` can be destroyed.

    Returns:
        cupy.ndarray:
            The transformed array.

    .. seealso:: :func:`scipy.fftpack.rfft`
    """
    if n is None:
        n = x.shape[axis]

    shape = list(x.shape)
    shape[axis] = n
    f = _fft(x, (n,), (axis,), None, cufft.CUFFT_FORWARD, 'R2C',
             overwrite_x=overwrite_x)
    z = cupy.empty(shape, f.real.dtype)

    slice_z = [slice(None)] * x.ndim
    slice_f = [slice(None)] * x.ndim

    slice_z[axis] = slice(1)
    slice_f[axis] = slice(1)
    z[slice_z] = f[slice_f].real

    slice_z[axis] = slice(1, None, 2)
    slice_f[axis] = slice(1, None)
    z[slice_z] = f[slice_f].real

    slice_z[axis] = slice(2, None, 2)
    slice_f[axis] = slice(1, n - f.shape[axis] + 1)
    z[slice_z] = f[slice_f].imag

    return z


def irfft(x, n=None, axis=-1, overwrite_x=False):
    """Compute the one-dimensional inverse FFT for real input.

    Args:
        x (cupy.ndarray): Array to be transformed.
        n (None or int): Length of the transformed axis of the output. If ``n``
            is not given, the length of the input along the axis specified by
            ``axis`` is used.
        axis (int): Axis over which to compute the FFT.
        overwrite_x (bool): If True, the contents of ``x`` can be destroyed.

    Returns:
        cupy.ndarray:
            The transformed array.

    .. seealso:: :func:`scipy.fftpack.irfft`
    """
    if n is None:
        n = x.shape[axis]
    m = min(n, x.shape[axis])

    shape = list(x.shape)
    shape[axis] = n // 2 + 1
    if x.dtype in (cupy.float16, cupy.float32):
        z = cupy.zeros(shape, dtype=cupy.complex64)
    else:
        z = cupy.zeros(shape, dtype=cupy.complex128)

    slice_x = [slice(None)] * x.ndim
    slice_z = [slice(None)] * x.ndim

    slice_x[axis] = slice(1)
    slice_z[axis] = slice(1)
    z[slice_z].real = x[slice_x]

    slice_x[axis] = slice(1, m, 2)
    slice_z[axis] = slice(1, m // 2 + 1)
    z[slice_z].real = x[slice_x]

    slice_x[axis] = slice(2, m, 2)
    slice_z[axis] = slice(1, (m + 1) // 2)
    z[slice_z].imag = x[slice_x]

    return _fft(z, (n,), (axis,), None, cufft.CUFFT_INVERSE, 'C2R',
                overwrite_x=overwrite_x)
