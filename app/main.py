from ai_analyzer import generate_ai_analysis
from correlation_visualizer import create_correlation_heatmap
from correlation import calculate_correlations
from profile import create_profile
import sys
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
from quality_score import calculate_quality_score

def main():

    if len(sys.argv) > 1:
    	file_path = sys.argv[1]
    else:
    	file_path = "data/test.csv"


    df = load_csv(file_path)
    report = analyze_data(df)

    correlations = calculate_correlations(df)

    report["correlations"] = correlations

    profile = create_profile(df)

    report["profile"] = profile

    insights = generate_insights(report)

    report["insights"] = insights

    quality_score = calculate_quality_score(report)

    report["quality_score"] = quality_score
   
    ai_text = generate_ai_analysis(report)

    report["ai_analysis"] = ai_text

    create_sales_distribution(df)
    create_missing_values_chart(df)

    create_correlation_heatmap(df)

    print_report(report)

    save_report(report, "reports/report.json")

    generate_html_report(report)


if __name__ == "__main__":
    main()
