from services.dashboard_builder import build_dashboard


def generate_auto_dashboard(df):
    """
    Generate dashboard from a DataFrame.
    """

    return build_dashboard(df)