#=====================================================
# DASHBOARD PLANNER
#=====================================================

def get_default_dashboard():

    return {

        "dashboard_type":"auto",

        "charts":[],

        "kpis":[],

        "recommendations":False,

        "insights":False

    }



#=====================================================
# EXECUTIVE DASHBOARD
#=====================================================

def executive_dashboard():

    return {

        "dashboard_type":"executive",

        "charts":[

            "line",
            "bar",
            "pie"

        ],

        "kpis":[

            "sales",
            "profit",
            "growth"

        ],

        "recommendations":True,

        "insights":True

    }



#=====================================================
# FINANCIAL DASHBOARD
#=====================================================

def financial_dashboard():

    return {

        "dashboard_type":"financial",

        "charts":[

            "line",
            "bar"

        ],

        "kpis":[

            "profit",
            "loss",
            "cost"

        ],

        "recommendations":True,

        "insights":True

    }




#=====================================================
# MARKETING DASHBOARD
#=====================================================

def marketing_dashboard():

    return {

        "dashboard_type":"marketing",

        "charts":[

            "bar",

            "pie"

        ],

        "kpis":[

            "performance",

            "growth",

            "marketing"

        ],

        "recommendations":True,

        "insights":True

    }




#=====================================================
# SALES DASHBOARD
#=====================================================

def sales_dashboard():

    return {

        "dashboard_type":"sales",

        "charts":[

            "line",

            "bar"

        ],

        "kpis":[

            "sales",

            "quantity",

            "growth"

        ],

        "recommendations":True,

        "insights":True

    }




#=====================================================
# SURPRISE ME
#=====================================================

def best_dashboard():

    return {

        "dashboard_type":"best",

        "charts":[

            "line",

            "bar",

            "pie"

        ],

        "kpis":[

            "dynamic"

        ],

        "recommendations":True,

        "insights":True

    }




#=====================================================
# CUSTOM DASHBOARD
#=====================================================

def custom_dashboard(parsed_prompt):


    return {

        "dashboard_type":"custom",

        "metrics":

        parsed_prompt["metrics"],

        "dimensions":

        parsed_prompt["dimensions"],

        "chart":

        parsed_prompt["chart_type"],

        "recommendations":True,

        "insights":True

    }




#=====================================================
# MAIN PLANNER
#=====================================================

def dashboard_planner(parsed_prompt):


    dashboard_type = (

        parsed_prompt["dashboard_type"]

    )


    #------------------------------------------


    if parsed_prompt["surprise_me"]:

        return best_dashboard()


    #------------------------------------------


    if dashboard_type=="executive":

        return executive_dashboard()


    #------------------------------------------


    if dashboard_type=="financial":

        return financial_dashboard()


    #------------------------------------------


    if dashboard_type=="marketing":

        return marketing_dashboard()


    #------------------------------------------


    if dashboard_type=="sales":

        return sales_dashboard()


    #------------------------------------------


    return custom_dashboard(

        parsed_prompt

    )
