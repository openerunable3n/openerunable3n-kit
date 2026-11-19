# openerunable3n-kit

Sort a folder of files into per-type subfolders.

Small, dependency-free Python utility package generated for day-to-day file chores.
Standard library only — no third-party imports.

## Install

```bash
pip install -e .
```

## Usage

```bash
python -m openerunable3n_kit.cli --help
```

```python
from openerunable3n_kit.core import Openerunable3nTool

tool = Openerunable3nTool()
print(tool)
```

## Layout

```
openerunable3n_kit/
  __init__.py
  core.py
  cli.py
tests/
  test_core.py
```

## License

MIT © 2026 openerunable3n
