from services.column_detector import detect_columns
from services.chart_selector import select_charts
from services.kpi_generator import generate_kpis
from services.chart_data_builder import build_chart_data


def build_dashboard(

        df,

        dashboard_plan=None

):
    """
    Builds a complete dashboard from a DataFrame.
    """

    # Detect dataset structure
    columns = detect_columns(df)

    # Generate KPIs
    kpis = generate_kpis(df)

    # Decide charts
    chart_definitions = select_charts(
        columns["dimensions"],
        columns["measures"],
        columns["dates"]
    )

    # Build chart data
    charts = []

    for chart in chart_definitions:
        charts.append(
            build_chart_data(df, chart)
        )

    dashboard = {
        "title": "Generated Dashboard",
        "columns": columns,
        "kpis": kpis,
        "charts": charts,
        "totalRows": int(len(df)),
        "totalColumns": int(len(df.columns))
    }

    return dashboard