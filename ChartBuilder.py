import plotly.graph_objects as go
from plotly.subplots import make_subplots

class ChartBuilder:

    def price_action(self, df):
        fig = make_subplots(
            rows=2, cols=1,
            shared_xaxes=True,
            row_heights=[0.7, 0.3]
        )

        fig.add_trace(go.Candlestick(
            x=df.index,
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close'],
            name="Price"
        ), row=1, col=1)

        fig.add_trace(go.Bar(
            x=df.index,
            y=df['Volume'],
            name="Volume"
        ), row=2, col=1)

        return fig

    def trend_chart(self, df):
        fig = go.Figure()

        fig.add_trace(go.Scatter(x=df.index, y=df['Close'], name="Close"))
        fig.add_trace(go.Scatter(x=df.index, y=df['SMA20'], name="SMA20"))
        fig.add_trace(go.Scatter(x=df.index, y=df['SMA50'], name="SMA50"))

        return fig

    def risk_chart(self, df):
        fig = make_subplots(rows=1, cols=2)

        fig.add_trace(go.Histogram(x=df['Daily Return'], name="Returns"), row=1, col=1)

        fig.add_trace(go.Scatter(
            x=df.index,
            y=df['Volatility'],
            name="Volatility"
        ), row=1, col=2)

        return fig

    def relative_performance(self, df):
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=df.index,
            y=df['Normalized Close'],
            name="Normalized"
        ))

        return fig