"""Utility functions for testing Ruff linting and formatting."""

import datetime

# --------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for information.
# --------------------------------------------------------------------------------------


def test(something: int) -> str:
    """A function that does something.

    Something about `f`. And an example in doctest format:

    >>> f(x)

    Markdown is also supported:

    ```py
    f(x)
    ```

    As are reStructuredText literal blocks::

        f(x)


    And reStructuredText code blocks:

    .. code-block:: python

        f(x)
    """
    return "hello"


def misspell(x: int) -> bool:
    """Return a misspelled word.

    That is super duper long and this could go on forever
    just a little longer.
    """
    t = 7
    return not x > 2


print("Hello world!")
misspell(1)
a = 1

b = 2

p = f"test{'3' + 'nested_string'} including math {5**3 + 10}"


t = datetime.UTC


def foo(a: bool, b: bool, c: bool) -> int:
    """Docstring."""
    if a:
        if b:
            if c:
                temp = 1

            else:
                temp = 2

        else:
            temp = 3

    else:
        temp = 4

    if temp == 4:
        temp = 5

    if temp > 4:
        temp = 2

    if b:
        print("hello")
    else:
        print("Goodbye")

    return temp
