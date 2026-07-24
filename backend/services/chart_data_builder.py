import pandas as pd


MAX_POINTS = 20
MAX_SCATTER_POINTS = 500


def build_chart_data(df, chart):
    """
    Build chart-ready data from a chart definition.
    Limits returned data for performance.
    """

    chart_type = chart["type"]

    # ---------------- Line ----------------
    if chart_type == "line":

        x = chart["x"]
        y = chart["y"]

        data = (
            df.groupby(x)[y]
            .sum()
            .reset_index()
            .head(MAX_POINTS)
        )

        return {
            **chart,
            "data": data.to_dict(orient="records")
        }

    # ---------------- Bar ----------------
    elif chart_type == "bar":

        x = chart["x"]
        y = chart["y"]

        data = (
            df.groupby(x)[y]
            .sum()
            .reset_index()
            .sort_values(y, ascending=False)
            .head(MAX_POINTS)
        )

        return {
            **chart,
            "data": data.to_dict(orient="records")
        }

    # ---------------- Pie ----------------
    elif chart_type == "pie":

        labels = chart["labels"]
        values = chart["values"]

        data = (
            df.groupby(labels)[values]
            .sum()
            .reset_index()
            .sort_values(values, ascending=False)
            .head(10)
        )

        return {
            **chart,
            "data": data.to_dict(orient="records")
        }

    # ---------------- Scatter ----------------
    elif chart_type == "scatter":

        x = chart["x"]
        y = chart["y"]

        data = (
            df[[x, y]]
            .dropna()
            .sample(
                min(MAX_SCATTER_POINTS, len(df)),
                random_state=42
            )
        )

        return {
            **chart,
            "data": data.to_dict(orient="records")
        }

    # ---------------- Horizontal Bar ----------------
    elif chart_type == "horizontalBar":

        x = chart["x"]
        y = chart["y"]

        data = (
            df.groupby(y)[x]
            .sum()
            .reset_index()
            .sort_values(x, ascending=False)
            .head(MAX_POINTS)
        )

        return {
            **chart,
            "data": data.to_dict(orient="records")
        }

    return chart