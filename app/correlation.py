def calculate_correlations(df):

    numeric_df = df.select_dtypes(
        include="number"
    )

    if numeric_df.shape[1] < 2:
        return {}

    correlations = (
        numeric_df
        .corr()
        .round(2)
        .to_dict()
    )

    return correlations
