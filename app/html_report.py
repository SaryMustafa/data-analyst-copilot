import json


def generate_html_report(report):

    insights_html = ""

    for insight in report["insights"]:
        insights_html += f"<li>{insight}</li>"


    html = f"""
    <html>

    <head> 
        <meta charset="UTF-8">
        <title>Data Analysis Report</title>

        <style>
            body {{
                font-family: Arial;
                margin: 40px;
            }}

            h1 {{
                color: #333;
            }}

            .card {{
                padding: 15px;
                margin: 10px 0;
                border: 1px solid #ddd;
                border-radius: 8px;
            }}

            img {{
                width: 700px;
            }}

        </style>

    </head>


    <body>

    <h1>Dataset Analysis Report</h1>


    <div class="card">
        <h2>Dataset overview</h2>

        <p>
        Rows: {report["rows"]}
        </p>

        <p>
        Columns: {report["columns"]}
        </p>

    </div>

    <div class="card">

        <h2>🤖 AI Анализ</h2>
        <p>
        {report.get("ai_analysis", "")}
        </p>

        <ul>
        {insights_html}
        </ul>

    </div>


    <div class="card">

        <h2>Missing values</h2>

        <pre>
{json.dumps(report["missing_values"], indent=4)}
        </pre>

    </div>


    <div class="card">

        <h2>Duplicates</h2>

        <p>
        Full duplicates:
        {report["duplicates"]}
        </p>

        <p>
        Without ID:
        {report["duplicates_without_id"]}
        </p>

    </div>


    <div class="card">

        <h2>Outliers</h2>

        <pre>
{json.dumps(report["outliers"], indent=4)}
        </pre>

    </div>


    <h2>Charts</h2>


    <h3>Sales distribution</h3>

    <img src="sales_distribution.png">


    <h3>Missing values</h3>

    <img src="missing_values.png">


    <h3>Correlation matrix</h3>

    <img src="correlation_heatmap.png">

    </body>

    </html>
    """


    with open(
        "reports/analysis_report.html",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(html)

