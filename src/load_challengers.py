import pandas as pd
import os

# Path to the folder containing yearly Challenger match files
data_path = r"C:\Users\dorbe\PycharmProjects\Tennis\data\qual_matches"

# Define the range of years to load
years = range(1998, 2026)
dfs = []

for year in years:
    file = f"atp_matches_qual_chall_{year}.csv"
    file_path = os.path.join(data_path, file)

    if os.path.exists(file_path):
        print(f"Loading file: {file}")
        df = pd.read_csv(file_path, low_memory=False)

        if 'tourney_level' in df.columns:
            chall_df = df[df['tourney_level'] == 'C'].copy()
            chall_df['season'] = year
            dfs.append(chall_df)
            print(f"Added {len(chall_df)} Challenger matches from {year}")
        else:
            print(f"Warning: 'tourney_level' column not found in {file}")
    else:
        print(f"File not found: {file_path}")

# Concatenate all years
challenger_df = pd.concat(dfs, ignore_index=True)

# Print summary
print("\nData sample:")
print(challenger_df.head())

print("\nColumn info:")
print(challenger_df.info())

print("\nMatches per season:")
print(challenger_df['season'].value_counts().sort_index())

# Save merged Challenger data
output_path = os.path.join(data_path, "challenger_1998_2025.csv")
challenger_df.to_csv(output_path, index=False)

print(f"\nSaved merged file to: {output_path} ({len(challenger_df)} rows)")