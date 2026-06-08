import pandas as pd 
#location summary function
def create_location_summary(filtered_df):
    location_summary = filtered_df.groupby('Loc_code').agg({'Enrollment_ratio': 'mean','Demand_gap': 'sum','Crs_enrollment':'count'})
    location_summary = location_summary.rename(columns={'Enrollment_ratio': 'Average_Utilization',
                                                         'Demand_gap': 'Total_Demand_Gap','Crs_enrollment':'Course_Count'})
    return location_summary

#department summary function
def create_department_summary(filtered_df):
    department_summary = filtered_df.groupby('Department').agg({'Enrollment_ratio': 'mean','Demand_gap': 'sum','Crs_enrollment':'count'})
    department_summary = department_summary.rename(columns={'Enrollment_ratio': 'Average_Utilization',
                                                         'Demand_gap': 'Total_Demand_Gap','Crs_enrollment':'Course_Count'})
    return department_summary