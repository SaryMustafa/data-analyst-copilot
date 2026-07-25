def analyze_data(df):
    report = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": df.isna().sum().to_dict(),
	"duplicates": int(df.duplicated().sum()),
	"duplicates_without_id": int(
   		 df.drop(columns=["id"]).duplicated().sum()),       
	 "data_types": df.dtypes.astype(str).to_dict(),
        "numeric_summary": df.describe().to_dict()    
         }

    return report
