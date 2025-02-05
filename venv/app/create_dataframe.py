import pandas as pd

# Read in excel file and format 
file_path = 'CFA_Level_2_Hours.xlsx'

raw_results_df = pd.read_excel(file_path)

# clean results 
trimmed_df = raw_results_df.iloc[:, :4]
trimmed_df["Date"] = trimmed_df["Date"].ffill()

# create final_df name for reference. If cleansing steps are added in the future, can just change the final_df reference
final_df = trimmed_df

print(float(final_df.groupby('Date').agg({"Total hours": "sum"}).max()))