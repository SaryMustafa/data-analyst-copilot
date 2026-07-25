from data_loader import load_csv
from analyzer import analyze_data
from exporter import save_report

def main():
    df = load_csv("data/test.csv")

    report = analyze_data(df)

    print("DATASET REPORT")
    print("----------------")

    print(f"Rows: {report['rows']}")
    print(f"Columns: {report['columns']}")

    print("\nMissing values:")
    for column, value in report["missing_values"].items():
        print(f"{column}: {value}")

    print("\nDuplicates:")
    print(f"Full duplicates: {report['duplicates']}")
    print(f"Without ID: {report['duplicates_without_id']}")
    print("\nNumeric summary:")
    for column, stats in report["numeric_summary"].items():
    	print(f"\n{column}:")
    	for metric, value in stats.items():
        	print(f"{metric}: {value:.2f}")

    save_report(report, "reports/report.json")	

if __name__ == "__main__":
    main()
