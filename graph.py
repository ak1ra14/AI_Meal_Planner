# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots
# from info_helper import InformationHelper

# class NutrientGrapher:

#     def __init__(self):
#         self.info_helper = InformationHelper()

#     def plot_nutrient_graph(self, data):
#         df = pd.DataFrame(data)
#         # Create subplot with secondary y-axis
#         fig = make_subplots(specs=[[{"secondary_y": True}]])

#         # Add trace for macronutrients
#         fig.add_trace(
#             go.Bar(
#                 x=df[df["Type"] == "Macro"]["Nutrient"],
#                 y=df[df["Type"] == "Macro"]["Amount"],
#                 name="Macronutrients",
#                 marker_color="royalblue",
#             ),
#             secondary_y=False,
#         )

#         # Add trace for micronutrients
#         fig.add_trace(
#             go.Bar(
#                 x=df[df["Type"] == "Micro"]["Nutrient"],
#                 y=df[df["Type"] == "Micro"]["Daily Value"],
#                 name="Micronutrients",
#                 marker_color="lightgreen",
#             ),
#             secondary_y=True,
#         )

#         # Add horizontal line at 100% DV for micronutrients
#         fig.add_hline(y=100, line_dash="dot", line_color="red", secondary_y=True)

#         # Customize layout
#         fig.update_layout(
#             title_text="Daily Nutrient Intake",
#             xaxis_title="Nutrients",
#             barmode="group",
#             legend_title="Nutrient Type",
#         )

#         # Set y-axes titles
#         fig.update_yaxes(title_text="Amount (g)", secondary_y=False)
#         fig.update_yaxes(title_text="% Daily Value", secondary_y=True)

#         # Display the chart in Streamlit
#         st.plotly_chart(fig)

#         # Display data table
#         st.subheader("Nutrient Data")
#         st.dataframe(df)

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from info_helper import InformationHelper

class NutrientGrapher:

    def __init__(self):
        self.info_helper = InformationHelper()

    def plot_nutrient_graph(self, data):
        df = pd.DataFrame(data)

        # Separate macronutrients and micronutrients
        macro_df = df[df["Type"] == "Macro"].sort_values("Amount", ascending=False)
        micro_df = df[df["Type"] == "Micro"].sort_values("Daily Value", ascending=False)

        # Create two separate figures
        fig_macro = go.Figure()
        fig_micro = go.Figure()

        # Macronutrient graph (Pie chart)
        fig_macro.add_trace(
            go.Pie(
                labels=macro_df["Nutrient"],
                values=macro_df["Amount"],
                name="Macronutrients",
                marker_colors=['#FFA07A', '#98FB98', '#87CEFA'],  # Light colors for better visibility
                textinfo='label+percent',
                hoverinfo='label+value+percent',
                textposition='inside',
                insidetextorientation='radial',
                hole=0.3,  # Creates a donut chart
            )
        )

        # Micronutrient graph (Bar chart)
        fig_micro.add_trace(
            go.Bar(
                x=micro_df["Nutrient"],
                y=micro_df["Daily Value"],
                name="Micronutrients (% DV)",
                marker_color="lightgreen",
                hovertemplate="<b>%{x}</b><br>Daily Value: %{y:.1f}%<extra></extra>"
            )
        )

        # Add horizontal line at 100% DV for micronutrients
        fig_micro.add_shape(
            type="line",
            x0=-0.5,
            x1=len(micro_df)-0.5,
            y0=100,
            y1=100,
            line=dict(color="red", width=2, dash="dot"),
        )

        # Customize layouts
        fig_macro.update_layout(
            title_text="Macronutrients Distribution",
            height=500,
        )

        fig_micro.update_layout(
            title_text="Micronutrients (% Daily Value)",
            height=500,
            xaxis_title="Nutrients",
            yaxis_title="% Daily Value",
            xaxis_tickangle=45,
            yaxis_gridcolor='lightgray',
        )

        # Display the charts in Streamlit
        st.subheader("Recipe Nutrient Intake")
        st.plotly_chart(fig_macro, use_container_width=True)
        st.plotly_chart(fig_micro, use_container_width=True)

        # Display data tables
        st.subheader("Macronutrient Data")
        st.dataframe(macro_df[["Nutrient", "Amount"]].style.format({"Amount": "{:.2f}g"}))

        st.subheader("Micronutrient Data")
        st.dataframe(micro_df[["Nutrient", "Daily Value"]].style.format({"Daily Value": "{:.2f}%"}))

        # Add explanatory text
        st.markdown("""
        **Notes:**
        - The pie chart shows the distribution of macronutrients in grams (g).
        - The bar chart shows micronutrients as a percentage of the Daily Value (% DV).
        - The red dotted line in the micronutrient chart represents 100% of the Daily Value.
        """)
        