import json
import markdown


def generate_html_report(report):

    insights_html = ""
	
    ai_html = markdown.markdown(
    report.get("ai_analysis", ""),
    extensions=["extra"]
    )

    quality_score = 100

    missing_count = sum(
        report["missing_values"].values()
    )

    if missing_count > 0:
        quality_score -= 10


    if report["duplicates"] > 0:
        quality_score -= 10


    if len(report["outliers"]) > 0:
        quality_score -= 10


    if quality_score < 0:
        quality_score = 0

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
	.stats {{
  		 display: flex;
    		 gap: 20px;
	    }}


	.stats div {{
    		padding: 20px;
    		background: #f5f5f5;
    		border-radius: 10px;
    		text-align: center;
    		width: 150px;
	     }}
	.ai-report {{
  		  line-height: 1.6;
	     }}

	.ai-report h2 {{
   		 color: #444;
	     }}

	.ai-report ul {{
   		 padding-left: 20px;
	     }}


	.stats h3 {{
    		font-size: 32px;
    		margin: 0;
	     }}

            img {{
                width: 700px;
            }}

        </style>

    </head>


    <body>

    <h1>Dataset Analysis Report</h1>

    <div class="card">

    <h2>📊 Data Quality Score</h2>
 
    <h1>
    {report.get("quality_score", 0)}%
    </h1>

    </div>	

    <div class="card">

    <h2>📊 Dataset Overview</h2>

    <div class="stats">

    <div>
    <h3>{report["rows"]}</h3>
    <p>Rows</p>
    </div>

 
    <div>
    <h3>{report["columns"]}</h3>
    <p>Columns</p>
    </div>


    <div>
    <h3>{quality_score}%</h3>
    <p>Data Quality</p> 
    </div>

    </div>

    </div>
    <div class="card">

        <h2>🤖 AI Анализ</h2>

	<div class="ai-report">
	{ai_html}
	</div>

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

