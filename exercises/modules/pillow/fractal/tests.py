from testing import *
from testing.tests import *
from testing.assertions import *
from testing.util import *


with cumulative(skip_after_fail=True):
    Complex = tested_module().Complex

    with path('__init__'), cumulative():
        @test('Complex(0, 0) creates complex number with re=0 and im=0')
        def _():
            c = Complex(0, 0)
            must_be_equal(0, c.re)
            must_be_equal(0, c.im)

        @test('Complex(1, 5) creates complex number with re=1 and im=5')
        def _():
            c = Complex(1, 5)
            must_be_equal(1, c.re)
            must_be_equal(5, c.im)
    
    with path('__add__'), cumulative():
        @test('Complex(0, 0) + Complex(0, 0) == Complex(0, 0)')
        def _():
            a = Complex(0, 0)
            b = Complex(0, 0)
            c = a + b

            must_be_equal(0, c.re)
            must_be_equal(0, c.im)

        @test('Complex(0, 0) + Complex(1, 2) == Complex(1, 2)')
        def _():
            a = Complex(0, 0)
            b = Complex(1, 2)
            c = a + b

            must_be_equal(1, c.re)
            must_be_equal(2, c.im)

        @test('Complex(5, 7) + Complex(1, 2) == Complex(6, 9)')
        def _():
            a = Complex(5, 7)
            b = Complex(1, 2)
            c = a + b

            must_be_equal(6, c.re)
            must_be_equal(9, c.im)

    with path('__mul__'), cumulative():
        @test('Complex(0, 0) * Complex(0, 0) == Complex(0, 0)')
        def _():
            a = Complex(0, 0)
            b = Complex(0, 0)
            c = a * b

            must_be_equal(0, c.re)
            must_be_equal(0, c.im)

        @test('Complex(1, 0) * Complex(5, 9) == Complex(5, 9)')
        def _():
            a = Complex(1, 0)
            b = Complex(5, 9)
            c = a * b

            must_be_equal(5, c.re)
            must_be_equal(9, c.im)

        @test('Complex(0, 1) * Complex(5, 9) == Complex(-9, 5)')
        def _():
            a = Complex(0, 1)
            b = Complex(5, 9)
            c = a * b

            must_be_equal(-9, c.re)
            must_be_equal(5, c.im)

        @test('Complex(5, 9) * Complex(1, 0) == Complex(5, 9)')
        def _():
            a = Complex(5, 9)
            b = Complex(1, 0)
            c = a * b

            must_be_equal(5, c.re)
            must_be_equal(9, c.im)
            
        @test('Complex(5, 9) * Complex(0, 1) == Complex(-9, 5)')
        def _():
            a = Complex(5, 9)
            b = Complex(0, 1)
            c = a * b

            must_be_equal(-9, c.re)
            must_be_equal(5, c.im)
            
        @test('Complex(5, 9) * Complex(2, 0) == Complex(10, 18)')
        def _():
            a = Complex(5, 9)
            b = Complex(2, 0)
            c = a * b

            must_be_equal(10, c.re)
            must_be_equal(18, c.im)

        @test('Complex(0, 5) * Complex(2, 0) == Complex(0, 10)')
        def _():
            a = Complex(0, 5)
            b = Complex(2, 0)
            c = a * b

            must_be_equal(0, c.re)
            must_be_equal(10, c.im)

    with path('abs'), cumulative():
        @test('Complex(0, 0).abs() == 0')
        def _():
            c = Complex(0, 0)

            must_be_equal.with_epsilon(0.0001)(0, c.abs())

        @test('Complex(1, 0).abs() == 1')
        def _():
            c = Complex(1, 0)

            must_be_equal.with_epsilon(0.0001)(1, c.abs())

        @test('Complex(2, 0).abs() == 2')
        def _():
            c = Complex(2, 0)

            must_be_equal.with_epsilon(0.0001)(2, c.abs())

        @test('Complex(-1, 0).abs() == 1')
        def _():
            c = Complex(-1, 0)

            must_be_equal.with_epsilon(0.0001)(1, c.abs())
            
        @test('Complex(0, 1).abs() == 1')
        def _():
            c = Complex(0, 1)

            must_be_equal.with_epsilon(0.0001)(1, c.abs())

        @test('Complex(0, 2).abs() == 2')
        def _():
            c = Complex(0, 2)

            must_be_equal.with_epsilon(0.0001)(2, c.abs())

        @test('Complex(3, 4).abs() == 5')
        def _():
            c = Complex(3, 4)

            must_be_equal.with_epsilon(0.0001)(5, c.abs())

        @test('Complex(-3, 4).abs() == 5')
        def _():
            c = Complex(-3, 4)

            must_be_equal.with_epsilon(0.0001)(5, c.abs())

    with tested_function_name('mandelbrot'):
        mandelbrot = reftest(result=must_be_equal.with_epsilon(0.01))

        mandelbrot(Complex(0,0), 50, 10.0)
        mandelbrot(Complex(1,0), 50, 10.0)
        mandelbrot(Complex(10,0), 50, 10.0)
        mandelbrot(Complex(0.1,0), 50, 10.0)
        mandelbrot(Complex(0,0.1), 50, 10.0)
        mandelbrot(Complex(0,0), 100, 10.0)
        mandelbrot(Complex(10,0), 50, 10.0)
        mandelbrot(Complex(0,0), 50, 1.0)
        mandelbrot(Complex(0.1,0), 50, 1.0)
        mandelbrot(Complex(-0.1,0), 50, 1.0)
        mandelbrot(Complex(0,5), 50, 1.0)
