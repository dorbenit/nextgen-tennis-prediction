import pandas as pd
import os

# Create directory if it doesn't exist
os.makedirs("data/processed", exist_ok=True)
from load_grand_slam import grand_slam_df


def create_sf_label_and_merge(df, min_year=2010, max_year=2024):
    """
    Adds binary labels to the main DataFrame indicating whether each player
    (winner and loser) has ever reached a Grand Slam semi-final between given years.
    """
    sf_matches = df[
        (df['round'] == 'SF') &
        (df['season'] >= min_year) &
        (df['season'] <= max_year)
        ]

    sf_players = pd.unique(pd.concat([sf_matches['winner_id'], sf_matches['loser_id']]))
    all_players = pd.unique(df[['winner_id', 'loser_id']].values.ravel())

    label_df = pd.DataFrame({'player_id': all_players})
    label_df['reached_sf'] = label_df['player_id'].isin(sf_players).astype(int)

    df = df.merge(
        label_df.rename(columns={'player_id': 'winner_id', 'reached_sf': 'winner_reached_sf'}),
        on='winner_id', how='left'
    )
    df = df.merge(
        label_df.rename(columns={'player_id': 'loser_id', 'reached_sf': 'loser_reached_sf'}),
        on='loser_id', how='left'
    )
    return df


if __name__ == "__main__":
    df = grand_slam_df.copy()

    columns_to_drop = ['winner_entry', 'loser_entry', 'loser_seed', 'winner_seed']
    df_clean = df.drop(columns=columns_to_drop)

    columns_to_fill = [
        'minutes', 'l_ace', 'l_svpt', 'l_1stIn', 'l_1stWon', 'l_df', 'l_bpSaved',
        'w_1stIn', 'w_df', 'w_ace', 'w_2ndWon', 'w_1stWon', 'w_svpt',
        'l_2ndWon', 'l_bpFaced', 'w_bpSaved', 'w_bpFaced',
        'w_SvGms', 'l_SvGms',
        'loser_rank', 'loser_rank_points', 'loser_ht',
        'winner_rank', 'winner_rank_points'
    ]
    for col in columns_to_fill:
        median_value = df_clean[col].median()
        df_clean[col] = df_clean[col].fillna(median_value)

    df_clean = create_sf_label_and_merge(df_clean)


    df_clean.to_csv("../data/processed/clean_grand_slam_2010_2024.csv", index=False)

    winner_sf_names = df_clean[df_clean['winner_reached_sf'] == 1][['winner_id', 'winner_name']]
    winner_sf_names.columns = ['player_id', 'name']

    loser_sf_names = df_clean[df_clean['loser_reached_sf'] == 1][['loser_id', 'loser_name']]
    loser_sf_names.columns = ['player_id', 'name']

    sf_names = pd.concat([winner_sf_names, loser_sf_names]).drop_duplicates().sort_values('name').reset_index(drop=True)

    print(sf_names)
