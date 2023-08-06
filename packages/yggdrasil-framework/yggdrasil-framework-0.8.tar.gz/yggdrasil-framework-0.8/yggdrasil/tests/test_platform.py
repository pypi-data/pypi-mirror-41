r"""Tests for platform compatiblity."""
import nose.tools as nt
from yggdrasil import platform


def test_os():
    r"""Test that only one OS selected."""
    res = platform._is_mac + platform._is_linux + platform._is_win
    nt.assert_equal(res, 1)
