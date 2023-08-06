ez-logger
==

`ez-logger` is a python module that offers easy to use API's for performing common logging operations.

API Docs
--

API docs are maintained [here](https://ez-logger.readthedocs.io/en/latest/index.html)

Usage
--

```bash
pip install ez-logger
```

```python
from ez_logger.console_logger import ConsoleLogger
logger = ConsoleLogger()
logger.error('some error occurred')
```

```bash
from ez_logger.file_logger import FileLogger
logger = FileLogger(
   log_file='test.log',
   log_dir='/tmp'
)
logger.error('some error occurred')
```

Refer to [API Docs](https://ez-logger.readthedocs.io/en/latest/index.html) for detailed documentation.

Development
--

```bash
virtualenv venv
source venv/bin/activate

pip install -r requirements.txt
```

Run Tests
--

```bash
python -m pytest -v tests/unit/*.py
```
