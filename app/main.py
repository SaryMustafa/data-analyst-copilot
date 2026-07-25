from data_loader import load_csv
from analyzer import analyze_data
from report import print_report
from exporter import save_report
from visualizer import (
    create_sales_distribution,
    create_missing_values_chart
)
from html_report import generate_html_report
from insights import generate_insights

def main():

    df = load_csv("data/test.csv")

    report = analyze_data(df)
    insights = generate_insights(report)

    report["insights"] = insights

    create_sales_distribution(df)
    create_missing_values_chart(df)

    print_report(report)

    save_report(report, "reports/report.json")

    generate_html_report(report)


if __name__ == "__main__":
    main()
