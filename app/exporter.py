import json


def save_report(report, file_path):
    with open(file_path, "w") as file:
        json.dump(report, file, indent=4)

