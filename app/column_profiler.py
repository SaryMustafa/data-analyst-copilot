import pandas as pd


def profile_columns(df):

    result = {}

    for column in df.columns:

        info = {}

        info["type"] = str(df[column].dtype)

        info["unique"] = int(
            df[column].nunique()
        )

        info["missing"] = int(
            df[column].isna().sum()
        )


        if pd.api.types.is_numeric_dtype(df[column]):

            info["mean"] = round(
                df[column].mean(),
                2
            )

            info["min"] = df[column].min()

            info["max"] = df[column].max()


        result[column] = info


    return result
