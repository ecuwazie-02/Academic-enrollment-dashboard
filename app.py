import streamlit as st
import pandas as pd
import numpy as np

from theme import BG, CARD_BG, TEXT, PRIMARY
from summaries import create_location_summary, create_department_summary
from charts import (
    enrollment_ratio_by_location_chart, 
    enrollment_ratio_by_department_chart, 
    demand_gap_by_location_chart
)
from flags import zero_attendance_classes, full_classes
from what_if_analysis import whatif_enrollment

st.set_page_config(page_title="Enrollment Analysis Dashboard", layout="wide")
st.title("Enrollment Analysis Dashboard")
st.markdown('---')

st.markdown("""
<style>

.main {
    background-color: #F8FAFC;
}

div[data-testid="stMetric"] {
    background-color: white;
    border: 1px solid #E2E8F0;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0 1px 3px rgba(0,0,0,.05);
}

h1 {
    color: #0F172A;
}            
</style>
""", unsafe_allow_html=True)

# Load the dataset and clean dataset
path = 'enrollment_dataset.xlsx'
df= pd.read_excel(path)
df= df.rename(columns ={'Course + Section ID': 'Course_and_sectionID',
                        'Enrollment Ratio': 'Enrollment_ratio',
                        'MAX_ENROLLMENT':'Max_enrollment',
                        'CRS_ENROLLMENT': 'Crs_enrollment',
                        'CRS_TITLE': 'Crs_title',
                        'CRS_CDE':'Crs_code',
                        'LOC_CDE': 'Loc_code'})

df= df.replace(np.nan,0)

#Creating column for summaries
df['Demand_gap'] = df['Max_enrollment'] - df['Crs_enrollment']


#Sidebar for filtering
st.sidebar.header("Filter Options")
selected_location = st.sidebar.multiselect("Select Location", options=df['Loc_code'].unique(), key='location_multiselect')
filtered_df = df[df['Loc_code'].isin(selected_location)] if selected_location else df
#st.subheader("Enrollment Data")
with st.expander('View Enrollment Data'):
    st.dataframe(filtered_df)


#KPI Metrics
st.subheader("Key Performance Indicators")
col1, col2, col3 = st.columns(3)
col1.metric('Average Enrollment Ratio', f"{filtered_df['Enrollment_ratio'].mean():.2%}")
col2.metric('Total Demand Gap', f"{filtered_df['Demand_gap'].sum()}")
col3.metric('Total Courses', f"{filtered_df['Crs_enrollment'].count()}")

st.markdown('---')

#charts for dashboard

location_summary = create_location_summary(filtered_df)
department_summary = create_department_summary(filtered_df)

st.subheader("Visual Analytics")
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    fig = enrollment_ratio_by_location_chart(location_summary)
    st.plotly_chart(fig, use_container_width=True)

with chart_col2:
    fig_2 = enrollment_ratio_by_department_chart(department_summary)
    st.plotly_chart(fig_2, use_container_width=True)

data_col1, data_col2 = st.columns([2, 1])
with data_col1:
    fig_3 = demand_gap_by_location_chart(location_summary)
    st.plotly_chart(fig_3, use_container_width=True)
with data_col2:
    st.markdown("#### Quick Summaries")
    with st.expander("Location Summary Data"):
        st.dataframe(location_summary, use_container_width=True)
    with st.expander("Department Summary Data"):
        st.dataframe(department_summary, use_container_width=True)

st.markdown("---")

#Inluding the course flags
st.subheader('Course Exceptions & Management')
flag_col1, flag_col2 = st.columns(2)

with flag_col1:
    empty_df = zero_attendance_classes(filtered_df)
    st.subheader('Underutilized Courses')
    st.metric('Total Underutilized Courses',f"{len(empty_df)}")
    st.dataframe(empty_df)

with flag_col2:
    full_df = full_classes(filtered_df)
    st.subheader('Over-capacity Courses')
    st.metric('Total Over-capacity courses', f"{len(full_df)}")
    st.dataframe(full_df)

st.markdown('---')

#Slider for whatif analysis
st.header('Enrollment Impact Simulator')
slider_col, empty_space1, empty_space2 = st.columns([1,1,1])
with slider_col:
    whatif_input= st.slider('Input the amount you want to adjust enrollment',min_value= -50, max_value = 50, value= 0)

adjusted_enrollment_df = whatif_enrollment(filtered_df, whatif_input)
adjusted_enrollment_df['Simulated_Underutilized'] = adjusted_enrollment_df['Adjusted_enrollment_ratio'] <= 0.15
adjusted_enrollment_df['Simulated_Over_Capacity'] = adjusted_enrollment_df['Adjusted_enrollment_ratio'] >= 1.0

sim_under_count = adjusted_enrollment_df['Simulated_Underutilized'].sum()
sim_over_count = adjusted_enrollment_df['Simulated_Over_Capacity'].sum()

sim_col1, sim_col2 = st.columns([1,3])

with sim_col1:
    st.write(f'Adjusted enrollment by: **{whatif_input}%**')
    st.metric('Average Enrollment Ratio', f"{adjusted_enrollment_df['Adjusted_enrollment_ratio'].mean():.2%}")
    st.metric('Simulated Underutilized', f"{sim_under_count} courses")
    st.metric('Simulated Over-capacity', f"{sim_over_count} courses")
with sim_col2:
    st.markdown("#### Simulated Enrollment Ledger")
    st.dataframe(adjusted_enrollment_df, use_container_width = True)