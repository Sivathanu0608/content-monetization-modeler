import pandas as pd
from sklearn.preprocessing import LabelEncoder


def preprocess_data(df):
    print("Initial shape:", df.shape)

    # ---------- REMOVE DUPLICATES ----------
    df = df.drop_duplicates()
    print("After removing duplicates:", df.shape)

    # ---------- HANDLE MISSING VALUES ----------
    # Numeric columns
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())

    # Categorical columns
    cat_cols = ['category', 'device', 'country']
    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    # ---------- FEATURE ENGINEERING ----------
    # Engagement Rate
    df['engagement_rate'] = (df['likes'] + df['comments']) / (df['views'] + 1)

    # Watch time per minute
    df['watch_time_ratio'] = df['watch_time_minutes'] / (df['video_length_minutes'] + 1)

    # ---------- ENCODE CATEGORICAL ----------
    label_encoders = {}

    for col in cat_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    print("Preprocessing completed")

    return df, label_encoders