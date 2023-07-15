
### This is a test assignment project for two handlers of hh.ru API

#### This project uses version of Python 3.11.*

#### you can install requirements using
`pip install -r requirements.txt`

#### dev requirements can be installed via
`pip install -r requirements_dev.txt`

#### run tests with 
`pytest tests`

#### to run tests with small html report please use
`pytest tests/ --html-report=tests/reports`

#### to get detailed html report first run
`python -m pytest tests --alluredir=tests/reports --html-report=tests/reports`
#### then
`python ./allure_info_to_html.py`

