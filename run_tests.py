import doctest

import pytest


def run_tests():
    pytest.main()


def run_doctests():
    doctest.testfile("examples/gardner.md", optionflags=doctest.ELLIPSIS)
