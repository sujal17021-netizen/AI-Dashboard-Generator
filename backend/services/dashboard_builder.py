from services.column_detector import detect_columns
from services.chart_selector import select_charts
from services.kpi_generator import generate_kpis
from services.chart_data_builder import build_chart_data


def build_dashboard(df):

    print("BUILD STEP 1")
    columns = detect_columns(df)

    print("BUILD STEP 2")
    kpis = generate_kpis(df)

    print("BUILD STEP 3")
    chart_definitions = select_charts(
        columns["dimensions"],
        columns["measures"],
        columns["dates"]
    )

    print("BUILD STEP 4")

    charts = []

    for chart in chart_definitions:
        print("Building:", chart["type"])
        charts.append(build_chart_data(df, chart))

    print("BUILD STEP 5")

    dashboard = {
        "title": "Generated Dashboard",
        "columns": columns,
        "kpis": kpis,
        "charts": charts,
        "totalRows": len(df),
        "totalColumns": len(df.columns)
    }

    print("BUILD STEP 6")

    return dashboard