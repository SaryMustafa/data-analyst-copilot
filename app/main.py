from data_loader import load_csv
from analyzer import analyze_data


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

    print(f"\nDuplicates: {report['duplicates']}")


if __name__ == "__main__":
    main()
