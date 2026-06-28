import pandas as pd

# ✅ correct header fix
df = pd.read_excel("Call-Center-Sentiment-Sample-Data.xlsx", header=5)

# clean columns
df.columns = df.columns.str.strip()

print("\nCOLUMNS:")
print(df.columns)

print("\nTOP DATA:")
print(df.head())

print("\nSENTIMENT COUNT:")
print(df["Sentiment"].value_counts())

print("\nCITY WISE CALLS:")
print(df["City"].value_counts())

print("\nCHANNEL WISE CALLS:")
print(df["Channel"].value_counts())

print("\nAVG CALL DURATION:")
print(df["Call Duration (Minutes)"].mean())