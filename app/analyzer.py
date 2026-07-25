def analyze_data(df):

    outliers = {}

    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)

        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        values = df[
            (df[column] < lower_bound) |
            (df[column] > upper_bound)
        ][column].tolist()

        if values:
            outliers[column] = values


    report = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": df.isna().sum().to_dict(),

        "duplicates": int(df.duplicated().sum()),

        "duplicates_without_id": int(
            df.drop(columns=["id"], errors="ignore")
            .duplicated()
            .sum()
        ),

        "data_types": df.dtypes.astype(str).to_dict(),

        "numeric_summary": df.describe().to_dict(),

        "outliers": outliers
    }

    return report
