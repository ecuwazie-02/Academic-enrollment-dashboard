# Academic Enrollment Dashboard

Background and Overview
---
In higher education administration, efficient resource allocation is critical to maintaining financial health and operational balance. Traditional academic course planning relies heavily on retrospective spreadsheet reports. 

Developed within the context of Southeastern University's Registrar Operations, this project introduces an interactive Enrollment Analytics and Capacity Planning Dashboard built using Python and the open-source web-builder package, Streamlit.  (This platform transitions administrative enrollment logs into a self-service business intelligence platform, featuring real-time data orchestration, resource utilization flags, and an algorithmic data-driven scaling simulator.)

Data Structure Overview
---
|--------------------|-----------|----------------------------------------------------------------------------------------|
|Field Name          | Data Type | Description                                                                            |
|--------------------|-----------|----------------------------------------------------------------------------------------|
|Course_and_sectionID| String    | Unique alphanumeric key combining the course prefix and section listing                |
|--------------------|-----------|----------------------------------------------------------------------------------------| 
|Department          | String    | Categorical variable representing the academic division (e.g., ACTG, ARTV, BIOL)       |
|--------------------|-----------|----------------------------------------------------------------------------------------|
|Loc_code            | String    | Categorical variable identifying the campus or delivery modality (e.g., MAIN, ONLN)    |
|--------------------|-----------|----------------------------------------------------------------------------------------|
|Max_enrollment      | Integer   | The administrative capacity boundary for a section                                     |
|--------------------|-----------|----------------------------------------------------------------------------------------|
|Crs_enrollment      | Integer   | The active headcount of students enrolled in the specific section                      |
|--------------------|-----------|----------------------------------------------------------------------------------------|
|Enrollment_ratio    | Float     | Utilization metric, calculated by (Crs_enrollment / Max_enrollment)                    |
|--------------------|-----------|----------------------------------------------------------------------------------------|
|Demand_gap          | Integer   | Quantified empty seat inventory metric, calculated by (Max_enrollment - Crs_enrollment)| 
|--------------------|-----------|----------------------------------------------------------------------------------------|

Executive Summary
---

Insights Deep Dive
---

Recommendations
---   
