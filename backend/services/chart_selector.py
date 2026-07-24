def select_charts(dimensions, measures, dates):
    """
    Automatically selects the best dashboard charts.
    """

    charts = []

    # -------------------------
    # Time Series
    # -------------------------
    if dates and measures:
        charts.append({
            "type": "line",
            "title": f"{measures[0]} Over Time",
            "x": dates[0],
            "y": measures[0]
        })

    # -------------------------
    # Bar Chart
    # -------------------------
    if dimensions and measures:
        charts.append({
            "type": "bar",
            "title": f"{measures[0]} by {dimensions[0]}",
            "x": dimensions[0],
            "y": measures[0]
        })

    # -------------------------
    # Pie Chart
    # -------------------------
    if dimensions and measures:
        charts.append({
            "type": "pie",
            "title": f"{dimensions[0]} Distribution",
            "labels": dimensions[0],
            "values": measures[0]
        })

    # -------------------------
    # Scatter Plot
    # -------------------------
    if len(measures) >= 2:
        charts.append({
            "type": "scatter",
            "title": f"{measures[0]} vs {measures[1]}",
            "x": measures[0],
            "y": measures[1]
        })

    # -------------------------
    # Horizontal Bar
    # -------------------------
    if len(dimensions) >= 2 and measures:
        charts.append({
            "type": "horizontalBar",
            "title": f"{measures[0]} by {dimensions[1]}",
            "x": measures[0],
            "y": dimensions[1]
        })

    return charts