"""Test set_loglevel."""
# pylint: disable=broad-except
from set_loglevel import __version__
from set_loglevel import set_loglevel


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not set_loglevel()
    except Exception:
        assert True
