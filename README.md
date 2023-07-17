
### This is a test assignment project for two handlers of hh.ru API

#### This project uses version of Python 3.11.*

#### after downloading, cd to project root and create venv
`python -m venv /d/python/hh`

#### then activate it by
`source Scripts/activate` or `./scripts/activate` (depending on your platform)

#### you can install requirements using
`pip install -r requirements.txt`

#### dev requirements can be installed via
`pip install -r requirements_dev.txt`

#### run tests with 
`python -m pytest tests`

#### to run tests with small html report please use
`python -m pytest tests --html-report=tests/reports`

#### to get detailed html report first run
`python -m pytest tests --alluredir=tests/reports --html-report=tests/reports`
#### then
`python ./allure_info_to_html.py`

