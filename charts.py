import plotly.express as px
from theme import PRIMARY, TEXT

def enrollment_ratio_by_location_chart(location_summary):
    fig = px.bar(
        location_summary,
        x = location_summary.index,
        y = 'Average_Utilization',
        title = 'Average Utilization by Location',
        template = 'plotly_white'
    )

    fig.update_traces(marker_color=PRIMARY, marker_line_color=PRIMARY, opacity=0.85)
    fig.update_layout(
        font_color=TEXT,
        title_font_size=16,
        xaxis_title="Location",
        yaxis_title="Avg Utilization",
        margin=dict(l=20, r=20, t=50, b=20),
        height=350
    )
    return fig

def enrollment_ratio_by_department_chart(department_summary):
    fig_2 = px.bar(
        department_summary,
        x = department_summary.index,
        y = 'Average_Utilization',
        title = 'Average Utilization by Department',
        template= 'plotly_white'
    )

    fig_2.update_traces(marker_color=PRIMARY, marker_line_color=PRIMARY, opacity=0.85)
    fig_2.update_layout(
        font_color=TEXT,
        title_font_size=16,
        xaxis_title="Department",
        yaxis_title="Avg Utilization",
        margin=dict(l=20, r=20, t=50, b=20),
        height=350
    )
    return fig_2

def demand_gap_by_location_chart(location_summary):
    fig_3 = px.bar(
        location_summary,
        x = location_summary.index,
        y = 'Total_Demand_Gap',
        title = 'Demand gap by location',
        template= 'plotly_white'
    )
    fig_3.update_traces(marker_color=PRIMARY, marker_line_color=PRIMARY, opacity=0.85)
    fig_3.update_layout(
        font_color=TEXT,
        title_font_size=16,
        xaxis_title="Department",
        yaxis_title="Avg Utilization",
        margin=dict(l=20, r=20, t=50, b=20),
        height=350
    )
    return fig_3