import numpy as np
import pytest

import pycsou.operator.map.ufunc as pycmu
import pycsou_tests.operator.conftest as conftest

# Trigonometric Functions


class TestSin(conftest.DiffMapT):
    @pytest.fixture
    def dim(self):
        return 40

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Sin(shape=data_shape)

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(0, 2 * np.pi, data_shape[0])
        B = np.sin(A)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))

    @pytest.fixture
    def data_math_diff_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))


class TestCos(conftest.DiffMapT):
    @pytest.fixture
    def dim(self):
        return 40

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Cos(shape=data_shape)

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(0, 2 * np.pi, data_shape[0])
        B = np.cos(A)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))

    @pytest.fixture
    def data_math_diff_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))


class TestTan(conftest.MapT):
    r"""
    Tangent function diverges for :math:`\mp(2k+1)k\pi/2`, with
    :math:`k \in \mathbb{N}`. Testing is done on :math`[-3*\pi/2+0.2,
    -\pi/2-0.2] \cup [-\pi/2+0.2, \pi/2-0.2] \cup [\pi/2+0.2,
    3*\pi/2-0.2]`.
    """

    @pytest.fixture
    def dim(self):
        return 7

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Tan(shape=data_shape)

    @pytest.fixture(
        params=[
            dict(
                in_=dict(arr=np.linspace(-3 * np.pi / 2 + 0.2, -np.pi / 2 - 0.2, 5)),
                out=np.tan(np.linspace(-3 * np.pi / 2 + 0.2, -np.pi / 2 - 0.2, 5)),
            ),
            dict(
                in_=dict(arr=np.linspace(-np.pi / 2 + 0.1, np.pi / 2 - 0.1, 5)),
                out=np.tan(np.linspace(-np.pi / 2 + 0.1, np.pi / 2 - 0.1, 5)),
            ),
            dict(
                in_=dict(arr=np.linspace(np.pi / 2 + 0.2, 3 * np.pi / 2 - 0.2, 5)),
                out=np.tan(np.linspace(np.pi / 2 + 0.2, 3 * np.pi / 2 - 0.2, 5)),
            ),
        ]
    )
    def data_apply(self, request):
        return request.param

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))


class TestArcsin(conftest.MapT):
    """
    Inverse sine function defined for :math:`[-1,1]`.
    """

    @pytest.fixture
    def dim(self):
        return 7

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Arcsin(shape=data_shape)

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(-1, 1, data_shape[0])
        B = np.arcsin(A)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return np.clip(self._random_array((N_test, data_shape[0])), -1, 1)


class TestArccos(conftest.MapT):
    """
    Inverse cosine function defined for :math:`[-1,1]`.
    """

    @pytest.fixture
    def dim(self):
        return 7

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Arccos(shape=data_shape)

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(-1, 1, data_shape[0])
        B = np.arccos(A)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return np.clip(self._random_array((N_test, data_shape[0])), -1, 1)


class TestArctan(conftest.DiffMapT):
    @pytest.fixture
    def dim(self):
        return 10

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Arctan(shape=data_shape)

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(-100, 100, data_shape[0])
        B = np.arctan(A)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))

    @pytest.fixture
    def data_math_diff_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))


# Hyperbolic Functions


class TestSinh(conftest.DiffMapT):
    @pytest.fixture
    def dim(self):
        return 100

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Sinh(shape=data_shape)

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(-3, 3, data_shape[0])
        B = np.sinh(A)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))

    @pytest.fixture
    def data_math_diff_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))


class TestCosh(conftest.DiffMapT):
    @pytest.fixture
    def dim(self):
        return 100

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Cosh(shape=data_shape)

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(-3, 3, data_shape[0])
        B = np.cosh(A)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))

    @pytest.fixture
    def data_math_diff_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))


class TestTanh(conftest.DiffMapT):
    @pytest.fixture
    def dim(self):
        return 100

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Tanh(shape=data_shape)

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(-3, 3, data_shape[0])
        B = np.tanh(A)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))

    @pytest.fixture
    def data_math_diff_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))


class TestArcsinh(conftest.DiffMapT):
    @pytest.fixture
    def dim(self):
        return 100

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Arcsinh(shape=data_shape)

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(-10, 10, data_shape[0])
        B = np.arcsinh(A)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))

    @pytest.fixture
    def data_math_diff_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))


class TestArccosh(conftest.MapT):
    r"""
    Inverse hyperbolic cosine function defined for :math:`[1,\infty)`.
    """

    @pytest.fixture
    def dim(self):
        return 7

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Arccosh(shape=data_shape)

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(1, 5, data_shape[0])
        B = np.arccosh(A)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return np.clip(self._random_array((N_test, data_shape[0])) + 3, a_min=1, a_max=4)


class TestArctanh(conftest.MapT):
    """
    Inverse hyperbolic tangent function defined for :math:`(-1,1)`.
    """

    @pytest.fixture
    def dim(self):
        return 7

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Arctanh(shape=data_shape)

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(-1 + 0.01, 1 - 0.01, data_shape[0])
        B = np.arctanh(A)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return np.clip(self._random_array((N_test, data_shape[0])), a_min=-1 + 0.01, a_max=1 - 0.01)


# Exponentials and logarithms


class TestExp(conftest.DiffMapT):
    @pytest.fixture
    def dim(self):
        return 10

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Exp(shape=data_shape)

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(-4, 4, data_shape[0])
        B = np.exp(A)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))

    @pytest.fixture
    def data_math_diff_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))


class TestLog(conftest.DiffMapT):
    r"""
    Natural logarithm function defined for :math:`(0,\infty)`.
    """

    @pytest.fixture
    def dim(self):
        return 100

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Log(shape=data_shape)

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(0.1, 10, data_shape[0])
        print("A: ", A)
        B = np.log(A)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return np.abs(self._random_array((N_test, data_shape[0])))

    @pytest.fixture
    def data_math_diff_lipschitz(self, data_shape):
        N_test = 5
        return np.abs(self._random_array((N_test, data_shape[0])))


class TestLog10(conftest.DiffMapT):
    r"""
    Base 10 logarithm function defined for :math:`(0,\infty)`.
    """

    @pytest.fixture
    def dim(self):
        return 100

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Log10(shape=data_shape)

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(0.1, 10, data_shape[0])
        B = np.log10(A)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return np.abs(self._random_array((N_test, data_shape[0])))

    @pytest.fixture
    def data_math_diff_lipschitz(self, data_shape):
        N_test = 5
        return np.abs(self._random_array((N_test, data_shape[0])))


class TestLog2(conftest.DiffMapT):
    r"""
    Base 2 logarithm function defined for :math:`(0,\infty)`.
    """

    @pytest.fixture
    def dim(self):
        return 100

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Log2(shape=data_shape)

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(0.1, 10, data_shape[0])
        B = np.log2(A)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return np.abs(self._random_array((N_test, data_shape[0])))

    @pytest.fixture
    def data_math_diff_lipschitz(self, data_shape):
        N_test = 5
        return np.abs(self._random_array((N_test, data_shape[0])))


# Sums, Products and Differences


class TestProd(conftest.MapT):
    @pytest.fixture
    def dim(self):
        return 5

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, 0)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Prod()

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(1, 5, data_shape[0])
        B = np.prod(A, axis=-1)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))


class TestSum(conftest.MapT):
    @pytest.fixture
    def dim(self):
        return 10

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, 0)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Sum()

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(5, 10, data_shape[0])
        B = np.sum(A, axis=-1)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))


class TestCumprod(conftest.MapT):
    @pytest.fixture
    def dim(self):
        return 5

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Cumprod(shape=data_shape)

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(1.0, 5.0, data_shape[0])
        B = np.cumprod(A, axis=-1)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))


class TestCumsum(conftest.MapT):
    @pytest.fixture
    def dim(self):
        return 5

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Cumsum(shape=data_shape)

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(1.0, 5.0, data_shape[0])
        B = np.cumsum(A, axis=-1)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))


# Miscellaneous


class TestClip(conftest.MapT):
    @pytest.fixture
    def dim(self):
        return 100

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Clip(shape=data_shape)

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(-100, 100, data_shape[0])
        B = np.clip(A, a_min=0.0, a_max=1.0)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))


class TestSqrt(conftest.MapT):
    r"""
    Square root function defined for :math:`[0,\infty)`.
    """

    @pytest.fixture
    def dim(self):
        return 100

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Sqrt(shape=data_shape)

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(0, 100, data_shape[0])
        B = np.sqrt(A)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return np.abs(self._random_array((N_test, data_shape[0])))


class TestCbrt(conftest.MapT):
    @pytest.fixture
    def dim(self):
        return 100

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Cbrt(shape=data_shape)

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(-10, 10, data_shape[0])
        B = np.cbrt(A)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))


class TestSquare(conftest.DiffMapT):
    @pytest.fixture
    def dim(self):
        return 100

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Square(shape=data_shape)

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(-2, 2, data_shape[0])
        B = np.square(A)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))

    @pytest.fixture
    def data_math_diff_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))


class TestAbs(conftest.DiffMapT):
    @pytest.fixture
    def dim(self):
        return 100

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Abs(shape=data_shape)

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(-4, 4, data_shape[0])
        B = np.abs(A)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        temp = self._random_array((N_test, data_shape[0]))
        return temp

    @pytest.fixture
    def data_math_diff_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))


class TestSign(conftest.MapT):
    @pytest.fixture
    def dim(self):
        return 100

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Sign(shape=data_shape)

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(-100, 100, data_shape[0])
        B = np.sign(A)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))


class TestHeaviside(conftest.MapT):
    @pytest.fixture
    def dim(self):
        return 10000

    @pytest.fixture
    def data_shape(self, dim):
        return (dim, dim)

    @pytest.fixture
    def op(self, data_shape):
        return pycmu.Heaviside(shape=data_shape)

    @pytest.fixture
    def data_apply(self, data_shape):
        A = np.linspace(-100, 100, data_shape[0])
        B = np.heaviside(A, 0)
        return dict(
            in_=dict(arr=A),
            out=B,
        )

    @pytest.fixture
    def data_math_lipschitz(self, data_shape):
        N_test = 5
        return self._random_array((N_test, data_shape[0]))