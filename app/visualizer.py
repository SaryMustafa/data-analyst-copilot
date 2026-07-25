import matplotlib.pyplot as plt
import seaborn as sns


def create_sales_distribution(df):

    plt.figure(figsize=(8, 5))

    sns.histplot(
        data=df,
        x="sales",
        kde=True
    )

    plt.title("Sales Distribution")

    plt.savefig(
        "reports/sales_distribution.png",
        bbox_inches="tight"
    )

    plt.close()

def create_missing_values_chart(df):

    missing = df.isna().sum()

    missing = missing[missing > 0]

    if len(missing) == 0:
        return

    plt.figure(figsize=(8, 5))

    sns.barplot(
        x=missing.index,
        y=missing.values
    )

    plt.title("Missing Values")

    plt.ylabel("Count")

    plt.savefig(
        "reports/missing_values.png",
        bbox_inches="tight"
    )

    plt.close()
