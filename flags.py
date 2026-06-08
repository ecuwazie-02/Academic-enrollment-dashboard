#function for zero_attendance flag 
def zero_attendance_classes(filtered_df):
    empty_df = filtered_df[filtered_df['Enrollment_ratio']<= 0.15]

    columns_to_show = ['Crs_code', 'Crs_title', 'Department', 'Section','Max_enrollment']

    return empty_df[columns_to_show]

def full_classes(filtered_df):
    full_df = filtered_df[filtered_df['Enrollment_ratio']>= 0.99]

    columns_to_show = ['Crs_code', 'Crs_title', 'Department', 'Section','Max_enrollment']

    return full_df[columns_to_show]