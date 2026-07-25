import pandas as pd


def create_profile(df):

    profile = {}

    for column in df.columns:

        profile[column] = {
            "type": str(df[column].dtype),
            "missing": int(df[column].isna().sum()),
            "unique_values": int(df[column].nunique())
        }


        if pd.api.types.is_numeric_dtype(df[column]):

            profile[column]["min"] = float(
                df[column].min()
            )

            profile[column]["max"] = float(
                df[column].max()
            )

            profile[column]["mean"] = float(
                df[column].mean()
            )

        else:

            profile[column]["top_values"] = (
                df[column]
                .value_counts()
                .head(5)
                .to_dict()
            )


    return profile
