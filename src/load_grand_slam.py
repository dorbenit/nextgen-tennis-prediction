import pandas as pd
import os

# Path to the folder containing yearly ATP match files
data_path = r"C:\Users\dorbe\PycharmProjects\Tennis\data\matches"

# Define the range of years to load
years = range(2010, 2025)
dfs = []

for year in years:
    file = f"atp_matches_{year}.csv"
    file_path = os.path.join(data_path, file)

    if os.path.exists(file_path):
        print(f"Loading file: {file}")
        df = pd.read_csv(file_path, low_memory=False)

        if 'tourney_level' in df.columns:
            gs_df = df[df['tourney_level'] == 'G'].copy()
            gs_df['season'] = year
            dfs.append(gs_df)
            print(f"Added {len(gs_df)} Grand Slam matches from {year}")
        else:
            print(f"Warning: 'tourney_level' column not found in {file}")
    else:
        print(f"File not found: {file_path}")

# Concatenate all years
grand_slam_df = pd.concat(dfs, ignore_index=True)

# Print summary
print("\nData sample:")
print(grand_slam_df.head())

print("\nColumn info:")
print(grand_slam_df.info())

print("\nMatches per season:")
print(grand_slam_df['season'].value_counts().sort_index())

# Save merged Grand Slam data
output_path = os.path.join(data_path, "grand_slam_2010_2024.csv")
grand_slam_df.to_csv(output_path, index=False)

print(f"\nSaved merged file to: {output_path} ({len(grand_slam_df)} rows)")
print(grand_slam_df.head())