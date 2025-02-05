
# importing cleaned dataframe from create_dataframe file
from create_dataframe import final_df
import streamlit as st
import numpy as np
# import calplot
import matplotlib.pyplot as plt
import matplotlib
# import pandas as pd
import july
from july.utils import date_range
import datetime
import math


# Display the chart in Streamlit
st.set_page_config(layout="wide") 
# st.title('Jordan\'s CFA Level 2 Dashboard')
st.markdown("<h1 style='text-align: center;'>Jordan\'s CFA Level 2 Dashboard</h1>", unsafe_allow_html=True)
col1, col2 = st.columns([0.6, 0.4])


#------- Visualization 1: Calendar Heatmap -------#
with col1: 
    # dates = date_range("2024-10-01", "2025-05-31")
    max_month = max(final_df["Date"]).month
    start_month_number = 10
    num_months = max_month + (12 - start_month_number) + 1 # include current month
    num_rows = math.ceil(num_months / 2)
    num_cols = 2 

    fig,axs = plt.subplots(num_rows, num_cols, figsize=(5,5))
    dates = date_range("2024-10-01", "2025-05-31")
    july.month_plot(dates, final_df["Total hours"], month=10, ax=axs[0, 0],cmap="Reds")

    july.month_plot(dates, final_df["Total hours"], month=11, ax=axs[0, 1],cmap="Reds")

    # dates = date_range("2024-12-01", "2025-12-31")
    # july.month_plot(dates, final_df["Total hours"], title='Hours Studied Heatmap', ax=axs[1],cmap="Reds")

    # dates = date_range("2024-11-01", "2025-11-30")
    # july.month_plot(dates, final_df["Total hours"], title='Hours Studied Heatmap', ax=axs[1],cmap="Reds")

    # dates = date_range("2024-11-01", "2025-11-30")
    # july.month_plot(dates, final_df["Total hours"], title='Hours Studied Heatmap', ax=axs[1],cmap="Reds")

    # # Display the heatmap
    # fig.suptitle(f"Hours Heatmap", fontsize=14)
    st.pyplot(fig)


#------- Visualization 1: Donut Chart -------#
with col2: 
    # Find the maximum "Total Hours"
    # max_hours = final_df['Total hours'].max()
    max_day_hours = float(final_df.groupby('Date').agg({"Total hours": "sum"}).max())


    # Create a card-like visualization using markdown and styling
    st.markdown("""
            <style>
            .card {
                padding: 30px;
                margin: 35px;
                background-color: #f0f8ff;
                border-radius: 10px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
                text-align: center;
            }
            .card h2 {
                font-size: 36px;
                color: #4CAF50;
            }
            .card p {
                font-size: 24px;
                color: #333;
            }
        </style>
        <div class="card">
            <h2>Daily Hours Record</h2>
            <p><strong>""" + f"{max_day_hours:.2f}" + """</strong> hours</p>
        </div>
    """, unsafe_allow_html=True)


    total_hours = 400
    completed_hours = final_df['Total hours'].sum()
    remaining_hours = total_hours - completed_hours

    # Calculate the percentage complete
    percentage_complete = (completed_hours / total_hours) * 100

    # Plotting the donut chart with Matplotlib
    fig, ax = plt.subplots(figsize=(6, 6))

    # Data for the chart
    sizes = [completed_hours / 10, remaining_hours / 10]
    labels = ['Completed', 'Remaining']

    # Create a donut chart by adding a "hole"
    ax.pie(sizes, labels=labels, startangle=90, wedgeprops=dict(width=0.4), colors=["blue", "#ADD8E6"]) #['#D76A50', '#FEECE3']

    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.axis('equal')

    # Add title with the percentage complete in the center
    ax.set_title(f"Completion Status: {percentage_complete:.2f}% Complete", fontsize=14)

    st.pyplot(fig)