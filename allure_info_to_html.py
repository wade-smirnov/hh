import json
import os
from datetime import datetime

from json2html import json2html

# Getting all json report files
current_directory = os.getcwd() + '\\tests\\reports\\'
files_list = os.listdir(current_directory)
report = [file for file in files_list if file[-5:] == ".html"][0]
json_files = [file for file in files_list if file[-11:] == "result.json"]
container_files = [file for file in files_list if file[-14:] == "container.json"]



# Removing unnessesary info
test_data = []
keys_to_delete = (
    "status",
    "statusDetails",
    "message",
    "trace",
    "start",
    "stop",
    "uuid",
    "historyId",
    "testCaseId",
)
for file in json_files:
    with open(current_directory + file, encoding="utf8") as f:
        temp = json.load(f)
        temp = {k: v for k, v in temp.items() if k not in keys_to_delete}
        if "steps" in temp.keys():
            for step in temp.get("steps"):
                step["start"] = datetime.fromtimestamp(step["start"] / 1000).strftime(
                    "%m/%d/%Y, %H:%M:%S"
                )
                step["stop"] = datetime.fromtimestamp(step["stop"] / 1000).strftime(
                    "%m/%d/%Y, %H:%M:%S"
                )
        test_data.append(temp)


# Reading html report
with open(current_directory + report, encoding="utf8") as report_stream:
    report_data = report_stream.read()


# Adding json data to html report
for test_report in test_data:
    test_name = test_report.get("fullName").rsplit("#", 1)[1]
    index = report_data.find(test_name)
    if index >= 0:
        html_to_insert = (
            "<br><br><details><summary>Detailed report</summary><p>"
            + json2html.convert(json=test_report)
            + "</p></details>"
        )

        report_data = (
            report_data[: index + len(test_name)]
            + html_to_insert
            + report_data[index + len(test_name) :]
        )

# Writing updated html report to file
with open(current_directory + report, "w", encoding="utf8") as report_stream:
    report_stream.write(report_data)

# Removing old json reports
for file in json_files + container_files:
    os.remove(current_directory + file)

print('\n***Done***\n')
