import pandas as pd


def generate_kpis(df: pd.DataFrame):

    kpis = []

    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:

        kpis.append({
            "title": f"Total {column}",
            "value": float(df[column].sum())
        })

        kpis.append({
            "title": f"Average {column}",
            "value": float(df[column].mean())
        })

        kpis.append({
            "title": f"Maximum {column}",
            "value": float(df[column].max())
        })

        kpis.append({
            "title": f"Minimum {column}",
            "value": float(df[column].min())
        })

    return kpis