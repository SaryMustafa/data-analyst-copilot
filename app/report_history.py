import json
import os
from datetime import datetime


def save_report_history(report):

    os.makedirs(
        "reports/history",
        exist_ok=True
    )


    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )


    filename = (
        f"reports/history/report_{timestamp}.json"
    )


    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report,
            file,
            ensure_ascii=False,
            indent=4
        )


    return filename
