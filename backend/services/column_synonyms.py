#=========================================================
# BUSINESS COLUMN SYNONYMS
#=========================================================

COLUMN_SYNONYMS = {


#=========================================================
# SALES
#=========================================================

"sales":[

"sales",
"sale",
"revenue",
"income",
"amount",
"turnover",
"gross sales",
"total sales",
"sales amount",
"business revenue",
"total revenue"

],


#=========================================================
# PROFIT
#=========================================================

"profit":[

"profit",
"net profit",
"gross profit",
"earnings",
"net income",
"income generated",
"operating profit",
"business profit"

],


#=========================================================
# LOSS
#=========================================================

"loss":[

"loss",
"net loss",
"business loss"

],



#=========================================================
# PRICE
#=========================================================

"price":[

"price",
"selling price",
"unit price",
"cost price"

],


#=========================================================
# COST
#=========================================================

"cost":[

"cost",
"expense",
"expenses",
"operational cost",
"business cost",
"total cost"

],



#=========================================================
# QUANTITY
#=========================================================

"quantity":[

"quantity",
"qty",
"count",
"number sold",
"volume",
"units",
"total units"

],


#=========================================================
# PRODUCTS
#=========================================================

"product":[

"product",
"products",
"item",
"items",
"goods",
"merchandise",
"sku"

],



#=========================================================
# CUSTOMER
#=========================================================

"customer":[

"customer",
"customers",
"client",
"clients",
"buyer",
"buyers",
"user",
"consumer"

],



#=========================================================
# STORE
#=========================================================

"store":[

"store",
"stores",
"branch",
"branches",
"location",
"shop",
"outlet"

],



#=========================================================
# CATEGORY
#=========================================================

"category":[

"category",
"categories",
"type",
"segment",
"class"

],



#=========================================================
# INVENTORY
#=========================================================

"inventory":[

"inventory",
"stock",
"warehouse",
"inventory count",
"warehouse stock",
"remaining stock"

],



#=========================================================
# ORDER
#=========================================================

"order":[

"order",
"orders",
"purchase",
"transaction"

],



#=========================================================
# PAYMENT
#=========================================================

"payment":[

"payment",
"payments",
"transaction amount",
"received amount"

],



#=========================================================
# SHIPPING
#=========================================================

"shipping":[

"shipping",
"shipment",
"delivery"

],



#=========================================================
# RATINGS
#=========================================================

"rating":[

"rating",
"ratings",
"review score",
"customer rating"

],



#=========================================================
# FEEDBACK
#=========================================================

"feedback":[

"feedback",
"reviews",
"comments"

],



#=========================================================
# EMPLOYEE
#=========================================================

"employee":[

"employee",
"employees",
"staff",
"worker"

],



#=========================================================
# SALARY
#=========================================================

"salary":[

"salary",
"salary amount",
"income paid"

],



#=========================================================
# DEPARTMENT
#=========================================================

"department":[

"department",
"division",
"team"

],



#=========================================================
# MARKETING
#=========================================================

"marketing":[

"marketing",
"campaign",
"advertisement",
"promotion"

],



#=========================================================
# TARGET
#=========================================================

"target":[

"target",
"goal",
"objective"

],



#=========================================================
# PERFORMANCE
#=========================================================

"performance":[

"performance",
"efficiency",
"productivity"

],



#=========================================================
# GROWTH
#=========================================================

"growth":[

"growth",
"increase",
"growth percentage",
"expansion"

],



#=========================================================
# DATE
#=========================================================

"date":[

"date",
"dates",
"time",
"timestamp"

],



#=========================================================
# MONTH
#=========================================================

"month":[

"month",
"months"

],



#=========================================================
# YEAR
#=========================================================

"year":[

"year",
"years"

],



#=========================================================
# QUARTER
#=========================================================

"quarter":[

"quarter",
"quarters",
"q1",
"q2",
"q3",
"q4"

],



#=========================================================
# COUNTRY
#=========================================================

"country":[

"country",
"nation"

],



#=========================================================
# STATE
#=========================================================

"state":[

"state",
"province"

],



#=========================================================
# CITY
#=========================================================

"city":[

"city",
"town"

]

}


#=========================================================
# DASHBOARD TYPES
#=========================================================


DASHBOARD_TYPES = {


"executive":[

"executive",
"ceo",
"management",
"leadership"

],


"financial":[

"financial",
"finance",
"accounts"

],



"marketing":[

"marketing"

],



"sales":[

"sales"

],



"inventory":[

"inventory",
"stock"

],



"hr":[

"human resources",
"employee",
"hr"

],



"healthcare":[

"healthcare",
"hospital"

],



"business":[

"business",
"analytics"

]

}



#=========================================================
# CHART TYPES
#=========================================================


CHART_TYPES = {


"line":[

"line",
"line chart",
"trend",
"monthly trend",
"yearly trend",
"growth"

],



"bar":[

"bar",
"bar chart",
"comparison"

],



"pie":[

"pie",
"pie chart",
"distribution",
"percentage distribution"

],



"scatter":[

"scatter",
"scatter plot"

],



"area":[

"area",
"area chart"

],



"histogram":[

"histogram"

],



"heatmap":[

"heatmap",
"heat map"

]

}



#=========================================================
# HELPER FUNCTIONS
#=========================================================

def get_column_synonyms():

    return COLUMN_SYNONYMS


def get_dashboard_types():

    return DASHBOARD_TYPES


def get_chart_types():

    return CHART_TYPES