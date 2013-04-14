import unittest

from macroscopy.core.macros import *
from macroscopy.core.lift import *
from macroscopy.macros.string_interp import *


class Tests(unittest.TestCase):
    def test_string_interpolate(self):
        with q as code:
            a, b = 1, 2
            c = s%"%{a} apple and %{b} bananas"
            assert(c == "1 apple and 2 bananas")

        test_ast(code)

    def test_string_interpolate_2(self):
        with q as code:
            apple_count = 10
            banana_delta = 4
            c = s%"%{apple_count} %{'apples'} and %{apple_count + banana_delta} %{''.join(['b', 'a', 'n', 'a', 'n', 'a', 's'])}"

            assert(c == "10 apples and 14 bananas")

        test_ast(code)


def test_ast(txt):
    node = expand_ast(txt)
    exec unparse(node)
