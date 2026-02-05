"""
test src/test_try_copier/main.py

run with:
```
uv run pytest tests/main_test.py
```
"""

import pytest

from test_try_copier import main


def test_main():
    with pytest.raises(NotImplementedError):
        main.main()
