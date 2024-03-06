import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import yfinance as yf
import plotly.express as px

# Gauti duomenis apie Apple akcijas
data = yf.download('AAPL', '2023-01-01', '2024-01-01').reset_index()
data['performance'] = data['Open'] - data['Close']

# Sukurti Dash aplikaciją
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Sudėti HTML išdėstymą
app.layout = dcc.Graph(
    figure={
        'data': [
            {'x': data['Date'], 'y': data['performance'], 'type': 'bar'},
        ],
        'layout': {
            'title': 'Daily Perfomance of Tesla'
        }
    }
)

# Paleisti aplikaciją
if __name__ == '__main__':
    app.run_server(debug=True)