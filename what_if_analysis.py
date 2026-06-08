import numpy as np

def whatif_enrollment(filtered_df,whatif_input):
  
    filtered_df['Adjusted_enrollment'] = filtered_df['Crs_enrollment']*(1+ whatif_input /100)
    #Adjusted_enrollment = filtered_df['Crs_enrollment']*(1+ whatif_input /100)
    #filtered_df['Adjusted_enrollment_ratio']= Adjusted_enrollment
    filtered_df['Adjusted_enrollment_ratio'] = filtered_df['Adjusted_enrollment'] / filtered_df['Max_enrollment']
    filtered_df['Adjusted_enrollment_ratio']= filtered_df['Adjusted_enrollment_ratio'].replace([np.inf, -np.inf], 0)
    filtered_df['Adjusted_enrollment_ratio']= filtered_df['Adjusted_enrollment_ratio'].fillna(0)

    adjusted_enrollment_df = filtered_df[['YR_CDE',
                                          'TRM_CDE',
                                          'Crs_title',
                                          'Course_and_sectionID',
                                          'Adjusted_enrollment',
                                          'Adjusted_enrollment_ratio',
                                          'Max_enrollment'
                                            ]]

    return adjusted_enrollment_df