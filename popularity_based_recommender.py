def calculate_growth_value(row, curr_time, growth_values):

    import pandas as pd

    time_diff = curr_time - row["date_time"]
    if time_diff < pd.Timedelta(minutes=5):
        return row["registrations"] * growth_values[5]
    elif time_diff < pd.Timedelta(minutes=10):
        return row["registrations"] * growth_values[10]
    elif time_diff < pd.Timedelta(minutes=15):
        return row["registrations"] * growth_values[15]
    else:
        return row["growth_value"]


def popularity_based_recommender(k):

    import pymysql
    import pandas as pd
    import numpy as np

    # Connect to the MySQL database
    conn = pymysql.connect(host='localhost',
                            user='root',
                            password='1234',
                            database='eventmate')

    registrations = pd.read_sql('SELECT * FROM registrations', conn)   

    import time

    # fetch current time
    curr_time = pd.to_datetime("11:30:00")

    registrations["date_time"] = pd.to_datetime(registrations["date_time"])

    recent_registrations = registrations[registrations["date_time"] >= curr_time - pd.Timedelta(minutes = 15)]
    
    recent_registrations["growth_value"] = 0

    growth_values = {
        5: 0.5,
        10: 0.3,
        15: 0.2
    }

    growth_value_df = recent_registrations.apply(calculate_growth_value, axis=1, args=(curr_time, growth_values))
    recent_registrations["growth_value"] = growth_value_df

    growth_factor = recent_registrations.groupby("EventID").sum("growth_value")

    growth_factor = growth_factor.sort_values(by="growth_value", ascending=False).reset_index()
    recommendations = growth_factor[0:k+1]["EventID"]

    return recommendations

