#=========================================================
# IMPORTS
#=========================================================

import re

from services.column_synonyms import (

    COLUMN_SYNONYMS,

    DASHBOARD_TYPES,

    CHART_TYPES

)


#=========================================================
# DEFAULT RESPONSE
#=========================================================

def get_default_response():

    return {

        "intent":"custom",

        "metrics":[],

        "dimensions":[],

        "dashboard_type":None,

        "chart_type":None,

        "top_n":None,

        "kpi_only":False,

        "charts_only":False,

        "compare":False,

        "forecast":False,

        "growth_analysis":False,

        "anomaly_detection":False,

        "insights":False,

        "recommendations":False,

        "surprise_me":False,

        "filters":[]

    }



#=========================================================
# FIND TOP N
#=========================================================

def extract_top_n(prompt):

    numbers = re.findall(r"\d+",prompt)

    if len(numbers)>0:

        return int(numbers[0])

    return None



#=========================================================
# FIND WORDS INSIDE DICTIONARY
#=========================================================

def find_matches(prompt,dictionary):

    results=[]

    prompt=prompt.lower()

    for category,words in dictionary.items():

        for word in words:

            if word.lower() in prompt:

                results.append(category)

                break

    return results



#=========================================================
# FIND DASHBOARD TYPE
#=========================================================

def find_dashboard_type(prompt):

    prompt=prompt.lower()

    for dashboard,words in DASHBOARD_TYPES.items():

        for word in words:

            if word.lower() in prompt:

                return dashboard

    return None



#=========================================================
# FIND CHART TYPE
#=========================================================

def find_chart_type(prompt):

    prompt=prompt.lower()

    for chart,words in CHART_TYPES.items():

        for word in words:

            if word.lower() in prompt:

                return chart

    return None



#=========================================================
# MAIN PROMPT PARSER
#=========================================================

def parse_prompt(prompt):

    response = get_default_response()

    prompt = prompt.lower()


    #-----------------------------------------------------
    # Surprise Me
    #-----------------------------------------------------

    if "surprise me" in prompt:

        response["surprise_me"]=True



    #-----------------------------------------------------
    # Forecast
    #-----------------------------------------------------

    if "predict" in prompt:

        response["forecast"]=True


    if "forecast" in prompt:

        response["forecast"]=True



    #-----------------------------------------------------
    # Compare
    #-----------------------------------------------------

    if "compare" in prompt:

        response["compare"]=True



    #-----------------------------------------------------
    # Growth Analysis
    #-----------------------------------------------------

    if "growth" in prompt:

        response["growth_analysis"]=True



    #-----------------------------------------------------
    # KPI ONLY
    #-----------------------------------------------------

    if "kpi" in prompt:

        response["kpi_only"]=True



    #-----------------------------------------------------
    # CHART ONLY
    #-----------------------------------------------------

    if "chart" in prompt and "only" in prompt:

        response["charts_only"]=True



    #-----------------------------------------------------
    # INSIGHTS
    #-----------------------------------------------------

    if "insights" in prompt:

        response["insights"]=True



    #-----------------------------------------------------
    # RECOMMENDATIONS
    #-----------------------------------------------------

    if "recommendation" in prompt:

        response["recommendations"]=True



    #-----------------------------------------------------
    # ANOMALY DETECTION
    #-----------------------------------------------------

    if "anomaly" in prompt:

        response["anomaly_detection"]=True



    #-----------------------------------------------------
    # TOP N
    #-----------------------------------------------------

    if "top" in prompt:

        response["top_n"]=extract_top_n(prompt)



    #-----------------------------------------------------
    # METRICS AND DIMENSIONS
    #-----------------------------------------------------

    results = find_matches(

        prompt,

        COLUMN_SYNONYMS

    )


    for item in results:

        if item not in response["metrics"]:

            response["metrics"].append(item)



    #-----------------------------------------------------
    # DASHBOARD TYPE
    #-----------------------------------------------------

    dashboard_type = find_dashboard_type(

        prompt

    )


    if dashboard_type:

        response["dashboard_type"]=dashboard_type

        response["intent"]=dashboard_type



    #-----------------------------------------------------
    # CHART TYPE
    #-----------------------------------------------------

    chart_type = find_chart_type(

        prompt

    )


    if chart_type:

        response["chart_type"]=chart_type



    #-----------------------------------------------------
    # MONTH
    #-----------------------------------------------------

    if "month" in prompt:

        response["dimensions"].append(

            "month"

        )


    #-----------------------------------------------------
    # YEAR
    #-----------------------------------------------------

    if "year" in prompt:

        response["dimensions"].append(

            "year"

        )


    #-----------------------------------------------------
    # QUARTER
    #-----------------------------------------------------

    if "quarter" in prompt:

        response["dimensions"].append(

            "quarter"

        )


    #-----------------------------------------------------
    # DATE
    #-----------------------------------------------------

    if "date" in prompt:

        response["dimensions"].append(

            "date"

        )


    return response