from data_loader import load_csv
from analyzer import analyze_data
from report import print_report
from exporter import save_report


def main():

    df = load_csv("data/test.csv")

    report = analyze_data(df)

    print_report(report)

    save_report(report, "reports/report.json")


if __name__ == "__main__":
    main()
