# Pytest

    pytest --version
    python -m pytest
    python -m pytest lib/tests/trading_test.py
    python -m pytest lib/tests/

ou

    pytest
    pytest lib/tests/trading_test.py
    pytest lib/tests/
    pytest lib


reporting:

      -v, --verbose         increase verbosity
      -s : visualiser print

test session debugging and configuration:

       --setup-show          show setup of fixtures while executing tests.

## Tests appEuro

    pytest --setup-show tests/unit/
