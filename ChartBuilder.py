import plotly.graph_objects as go
from plotly.subplots import make_subplots

BLUE   = "#378ADD"
GREEN  = "#1D9E75"
CORAL  = "#D85A30"
GRAY   = "#888780"
LIGHT  = "#f0f0f0"

LAYOUT = dict(
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(family="sans-serif", size=12, color="#444"),
    margin=dict(l=40, r=20, t=20, b=40),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    xaxis=dict(showgrid=False, showline=True, linecolor=LIGHT),
    yaxis=dict(showgrid=True, gridcolor=LIGHT, showline=False),
    hovermode="x unified"
)

class ChartBuilder:

    def price_action(self, df):
        fig = make_subplots(
            rows=2, cols=1,
            shared_xaxes=True,
            row_heights=[0.72, 0.28],
            vertical_spacing=0.04
        )

        fig.add_trace(go.Candlestick(
            x=df.index,
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close'],
            name="Price",
            increasing_line_color=GREEN,
            decreasing_line_color=CORAL,
            increasing_fillcolor=GREEN,
            decreasing_fillcolor=CORAL,
        ), row=1, col=1)

        colors = [GREEN if c >= o else CORAL
                  for c, o in zip(df['Close'], df['Open'])]

        fig.add_trace(go.Bar(
            x=df.index,
            y=df['Volume'],
            name="Volume",
            marker_color=colors,
            opacity=0.6,
        ), row=2, col=1)

        fig.update_layout(**LAYOUT, height=400)
        fig.update_layout(xaxis_rangeslider_visible=False)
        fig.update_yaxes(showgrid=True, gridcolor=LIGHT, row=1, col=1)
        fig.update_yaxes(showgrid=True, gridcolor=LIGHT, row=2, col=1)
        return fig

    def trend_chart(self, df):
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=df.index, y=df['Close'],
            name="Close",
            line=dict(color=BLUE, width=1.5),
            opacity=0.8
        ))
        fig.add_trace(go.Scatter(
            x=df.index, y=df['SMA20'],
            name="SMA 20",
            line=dict(color=GREEN, width=1.5, dash="dot")
        ))
        fig.add_trace(go.Scatter(
            x=df.index, y=df['SMA50'],
            name="SMA 50",
            line=dict(color=CORAL, width=1.5, dash="dash")
        ))

        fig.update_layout(**LAYOUT, height=320)
        return fig

    def risk_chart(self, df):
        fig = make_subplots(
            rows=1, cols=2,
            subplot_titles=["Return distribution", "Rolling volatility"],
            horizontal_spacing=0.12
        )

        fig.add_trace(go.Histogram(
            x=df['Daily Return'].dropna(),
            name="Daily return",
            marker_color=BLUE,
            opacity=0.75,
            nbinsx=40,
        ), row=1, col=1)

        fig.add_trace(go.Scatter(
            x=df.index,
            y=df['Volatility'],
            name="Volatility",
            line=dict(color=CORAL, width=1.5),
            fill="tozeroy",
            fillcolor="rgba(216,90,48,0.08)"
        ), row=1, col=2)

        fig.update_layout(**LAYOUT, height=300, showlegend=False)
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=True, gridcolor=LIGHT)
        return fig

    def relative_performance(self, df):
        fig = go.Figure()

        fig.add_hline(y=100, line_dash="dot", line_color=GRAY, opacity=0.5)

        fig.add_trace(go.Scatter(
            x=df.index,
            y=df['Normalized Close'],
            name="Normalized close",
            line=dict(color=BLUE, width=2),
            fill="tozeroy",
            fillcolor="rgba(55,138,221,0.08)"
        ))

        fig.update_layout(**LAYOUT, height=300)
        return fig

    def relative_performance_comparison(self, df1, df2, ticker1, ticker2):
        fig = go.Figure()

        fig.add_hline(y=100, line_dash="dot", line_color=GRAY, opacity=0.4)

        fig.add_trace(go.Scatter(
            x=df1.index,
            y=df1['Normalized Close'],
            name=ticker1,
            line=dict(color=BLUE, width=2),
            fill="tozeroy",
            fillcolor="rgba(55,138,221,0.07)"
        ))

        fig.add_trace(go.Scatter(
            x=df2.index,
            y=df2['Normalized Close'],
            name=ticker2,
            line=dict(color=CORAL, width=2),
            fill="tozeroy",
            fillcolor="rgba(216,90,48,0.07)"
        ))

        fig.update_layout(**LAYOUT, height=300)
        return fig