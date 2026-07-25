from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

# Load cleaned data
project_df = pd.read_csv("data/processed/cleaned_energy_data.csv")

app = Dash(__name__)

# Renewable electricity trend
yearly = (
    project_df.groupby("year")["renewables_electricity"]
    .sum()
    .reset_index()
)

fig1 = px.line(
    yearly,
    x="year",
    y="renewables_electricity",
    title="Renewable Electricity Generation"
)

# Solar trend
solar = (
    project_df.groupby("year")["solar_electricity"]
    .sum()
    .reset_index()
)

fig2 = px.line(
    solar,
    x="year",
    y="solar_electricity",
    title="Solar Electricity Trend"
)

# Wind trend
wind = (
    project_df.groupby("year")["wind_electricity"]
    .sum()
    .reset_index()
)

fig3 = px.line(
    wind,
    x="year",
    y="wind_electricity",
    title="Wind Electricity Trend"
)

app.layout = html.Div([
    html.H1(
        "Renewable Energy Adoption Tracker",
        style={"textAlign": "center"}
    ),

    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2),
    dcc.Graph(figure=fig3)
])

if __name__ == "__main__":
    app.run(debug=True)