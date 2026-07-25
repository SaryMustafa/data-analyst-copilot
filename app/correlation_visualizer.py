import matplotlib.pyplot as plt


def create_correlation_heatmap(df):

    numeric_df = df.select_dtypes(
        include="number"
    )

    if numeric_df.shape[1] < 2:
        return


    corr = numeric_df.corr()


    plt.figure(figsize=(8,6))

    plt.imshow(corr)

    plt.colorbar()

    plt.xticks(
        range(len(corr.columns)),
        corr.columns,
        rotation=45
    )

    plt.yticks(
        range(len(corr.columns)),
        corr.columns
    )


    for i in range(len(corr.columns)):
        for j in range(len(corr.columns)):

            plt.text(
                j,
                i,
                round(corr.iloc[i,j],2),
                ha="center",
                va="center"
            )


    plt.title(
        "Correlation Matrix"
    )

    plt.tight_layout()


    plt.savefig(
        "reports/correlation_heatmap.png"
    )

    plt.close()

