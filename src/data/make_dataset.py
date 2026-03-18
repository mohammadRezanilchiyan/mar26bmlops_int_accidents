import pandas as pd
from pathlib import Path

DATA_PATH = Path("data")
PREPROC_PATH = DATA_PATH / "preprocessed"
PREPROC_PATH.mkdir(exist_ok=True)  # create folder if missing

# Columns to keep (as in your original code)
USAGERS_COLS = ['num_acc','place','catu','grav','sexe','trajet','locp','actp','etatp','an_nais','num_veh']
CARAC_COLS = ['num_acc','an','mois','jour','hrmn','lum','agg','int','atm','col','lat','long']
VEH_COLS = ['num_acc','num_veh','catv','obs','obsm','choc','manv']
LIEUX_COLS = ['num_acc','catr','circ','nbv','vosp','prof','plan','surf','infra','situ']

def load_table(folder, cols):
    files = sorted((DATA_PATH / folder).glob("*.csv"))
    dfs = []
    for f in files:
        df = pd.read_csv(f, sep=";", low_memory=False)
        df.columns = df.columns.str.lower()
        cols_exist = [c for c in cols if c in df.columns]
        df = df[cols_exist]
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

def main():
    print("Loading tables...")
    usagers = load_table("usagers", USAGERS_COLS)
    vehicules = load_table("vehicules", VEH_COLS)
    caracteristiques = load_table("caracteristiques", CARAC_COLS)
    lieux = load_table("lieux", LIEUX_COLS)

    print("Merging tables...")
    df = usagers.merge(vehicules, on=["num_acc","num_veh"], how="left")
    df = df.merge(caracteristiques, on="num_acc", how="left")
    df = df.merge(lieux, on="num_acc", how="left")

    # Save merged full dataset
    df.to_csv(DATA_PATH / "accidents_full.csv", index=False)
    print("Merged dataset saved:", df.shape)

    # --- Split train/test ---
    print("Splitting train/test...")
    train_df = df[df['an'] <= 2018]
    test_df = df[df['an'] >= 2019]

    # Example: target is 'grav' (severity)
    target_col = 'grav'
    X_train = train_df.drop(columns=[target_col])
    y_train = train_df[target_col]
    X_test = test_df.drop(columns=[target_col])
    y_test = test_df[target_col]

    # Save preprocessed files
    X_train.to_csv(PREPROC_PATH / "X_train.csv", index=False)
    y_train.to_csv(PREPROC_PATH / "y_train.csv", index=False)
    X_test.to_csv(PREPROC_PATH / "X_test.csv", index=False)
    y_test.to_csv(PREPROC_PATH / "y_test.csv", index=False)

    print("Preprocessed datasets saved in:", PREPROC_PATH)

if __name__ == "__main__":
    main()