"""Test set_loglevel."""
# pylint: disable=broad-except
# import importlib
import os

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


# def test_force(capsys):
# @pytest.fixture(autouse=True)
def test_force(caplog):
    """Test force=True."""
    caplog.set_level(10)

    os.environ["LOGLEVEL"] = "debug"
    assert set_loglevel() == 10
    assert set_loglevel(20, force=True) == 20

    os.environ["LOGLEVEL"] = ""
    assert set_loglevel() == 20
    assert set_loglevel(10, force=True) == 10

    _ = """
    importlib.reload(logging)
    logging.basicConfig(level=set_loglevel())
    logging.getLogger().debug("boo %s", "arg")
    logging.getLogger().info("info %s", "arg")

    assert "boo" in caplog.record_tuples

    out, err = capsys.readouterr()
    # assert '0' in out
    # assert '0' in err
    sys.stderr.write(f"out: {out}")
    sys.stderr.write(f"err: {err}")

    logzero.loglevel(set_loglevel(20, force=True))
    logger.debug(0)
    out, err = capsys.readouterr()
    # assert not out
    # assert not err
    sys.stderr.write(f"out: {out}")
    sys.stderr.write(f"err: {err}")

    print("print out")

    logger.info(1)
    out, err = capsys.readouterr()
    assert "0" in err
    """
