def analyze_data(df):
    report = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": df.isna().sum().to_dict(),
        "duplicates": int(df.duplicated().sum())   
              }

    return report
