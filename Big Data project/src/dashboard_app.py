import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

# Data load
try:
    df_weekly = pd.read_parquet('data/weekly_demand.parquet')
except Exception:
    df_weekly = pd.DataFrame()

app.layout = html.Div([
    html.H2('Retail Dashboard - Weekly Demand'),
    dcc.Dropdown(id='product', options=[], placeholder='Choose product...'),
    dcc.Graph(id='weekly_chart')
])

@app.callback(
    dash.dependencies.Output('weekly_chart', 'figure'),
    [dash.dependencies.Input('product', 'value')]
)
def update(product):
    if df_weekly.empty:
        return px.line()
    dff = df_weekly[df_weekly['Description']==product] if product else df_weekly
    fig = px.line(dff, x='Week', y='Quantity', title='Weekly Demand')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
