import pandas as pd

from app.analyzer import analyze_data


def test_analyze_data():
    df = pd.DataFrame({
        "id": [1, 2, 3],
        "sales": [100, 200, 300]
    })

    report = analyze_data(df)

    assert report["rows"] == 3
    assert report["columns"] == 2
    assert report["duplicates"] == 0

def test_detect_outliers():

    df = pd.DataFrame({
        "id": [1, 2, 3, 4, 5],
        "sales": [100, 200, 300, 400, 99999]
    })

    report = analyze_data(df)

    assert "sales" in report["outliers"]
    assert 99999 in report["outliers"]["sales"]
