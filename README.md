# Academic Enrollment Dashboard

Background and Overview
---
In higher education administration, efficient resource allocation is critical to maintaining financial health and operational balance. Traditional academic course planning relies heavily on retrospective spreadsheet reports. 

Developed within the context of Southeastern University's Registrar Operations, this project introduces an interactive Enrollment Analytics and Capacity Planning Dashboard built using Python and the open-source web-builder package, Streamlit.  (This platform transitions administrative enrollment logs into a self-service business intelligence platform, featuring real-time data orchestration, resource utilization flags, and an algorithmic data-driven scaling simulator.)

Data Structure Overview
---
| Field Name | Data Type | Description |
| :--- | :--- | :--- |
| **Course_and_sectionID** | String | Unique alphanumeric key combining the course prefix and section listing. |
| **Department** | String | Categorical variable representing the academic division (e.g., ACTG, ARTV, BIOL). |
| **Loc_code** | String | Categorical variable identifying the campus or delivery modality (e.g., MAIN, ONLN). |
| **Max_enrollment** | Integer | The administrative capacity boundary for a section. |
| **Crs_enrollment** | Integer | The active headcount of students enrolled in the specific section. |
| **Enrollment_ratio** | Float | Utilization metric, calculated by `Crs_enrollment / Max_enrollment`. |
| **Demand_gap** | Integer | Quantified empty seat inventory metric, calculated by `Max_enrollment - Crs_enrollment`. |

Executive Summary
---
An evaluation of Southeastern University's enrollment data establishes key performance metrics:
 - Total Active Course Portfolio: 1,349 distinct course sections
 - Institutional Capacity Utilization Rate: The university possesses an average enrollment ratio of 58.31%, signaling a notable surplus of unutilized capacity.
 - Total Portfolio Capacity Slack: An aggregate of 15,802 vacant student seats across the entire University further illustrates significant unutilized capacity.

To transform these baseline performance metrics into immediate operational actions, the application uses programmatic filters to identify structural outliers:
  - Underutilized Sections Flag: Automatically isolates sections operating below a critical 15% capacity threshold, highlighting opportunities for class consolidations or cancellations.
  - Over-capacity Sections Flag: Automatically catches supply bottlenecks for sections with capacity of 99% or above, identifying immediate need for section expansions or room allocations. 


Insights Deep Dive
---

Recommendations
---   
