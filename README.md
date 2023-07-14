# hh
Test assignment hh.ru API


to run
pip install -r requirements.txt

for dev
pip install -r requirements-dev.txt

test with 
pytest tests

test with small report
pytest tests/ --html-report=tests/reports

test with detailed report
first run
python -m pytest tests/test_employers.py --alluredir=tests/reports --html-report=tests/reports
then
python ./allure_info_to_html.py

