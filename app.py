import streamlit as st
import os
import subprocess
import sys

from src.DataProcessor import DataProcessor
from ChartBuilder import ChartBuilder

st.set_page_config(
    page_title="StockStory",
    page_icon="S",
    layout="wide"
)

st.markdown("""
<style>
.stat-card {
    background: #f8f8f8;
    border-radius: 10px;
    padding: 1rem 1.25rem;
}
.stat-label {font-size: 12px; color: #888; margin-bottom: 4px;}
.stat-value {font-size: 20px; font-weight: 600; color: #111;}
.stat-sub {font-size: 11px; color: #aaa; margin-top: 2px;}
.ticker-header {display: flex; align-items: baseline; gap: 12px; margin-bottom: 0.5rem;}
.change-up {color: #1a9e6e; background: #e6f5ee; padding: 3px 10px; border-radius: 6px; font-size: 13px;}
.change-down {color: #c0392b; background: #fce8e8; padding: 3px 10px; border-radius: 6px; font-size: 13px;}
</style>
""", unsafe_allow_html=True)


def compile_java():
    is_windows = sys.platform == "win32"
    sep = ";" if is_windows else ":"
    parser_dir = os.path.join("src", "parser")

    # Generate parser from grammar
    subprocess.run(
        ["java", "-cp", "antlr-4.13.1-complete.jar",
         "org.antlr.v4.Tool", "Stock.g4"],
        cwd=parser_dir, capture_output=True
    )

    # Compile all Java
    result = subprocess.run(
        ["javac", "-cp", f"antlr-4.13.1-complete.jar{sep}{parser_dir}",
         f"{parser_dir}/StockLexer.java",
         f"{parser_dir}/StockParser.java",
         f"{parser_dir}/StockListener.java",
         f"{parser_dir}/StockBaseListener.java",
         f"{parser_dir}/StockRecord.java",
         f"{parser_dir}/StockStoryListener.java",
         "src/Main.java",
         "-d", parser_dir],
        capture_output=True, text=True
    )
    return result


def run_pipeline(uploaded_file):
    os.makedirs("outputs", exist_ok=True)
    input_path = os.path.join("outputs", uploaded_file.name)
    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())

    ticker = uploaded_file.name.split('.')[0].upper()
    json_path = os.path.join("outputs", f"{ticker}_records.json")

    is_windows = sys.platform == "win32"
    sep = ";" if is_windows else ":"
    parser_dir = os.path.join("src", "parser")
    classpath = f"antlr-4.13.1-complete.jar{sep}{parser_dir}"

    # Compile if Main.class is missing
    if not os.path.exists(os.path.join(parser_dir, "Main.class")):
        result = compile_java()
        if result.returncode != 0:
            st.error("Java compilation failed:")
            st.code(result.stderr)
            return None, None

    result = subprocess.run(
        ["java", "-cp", classpath, "Main", input_path, json_path],
        capture_output=True, text=True,
        shell=is_windows
    )

    if result.returncode != 0 or not os.path.exists(json_path):
        st.error(f"Java parser failed for {ticker}:")
        st.code(result.stderr or result.stdout or "No output from Java process.")
        return None, None

    processor = DataProcessor(ticker)
    df = processor.load_json_data(json_path)
    if df is None:
        st.error(f"Failed to load data for {ticker}.")
        return None, None

    df = processor.process_all()
    return ticker, df


def stat_cards(ticker, df, color):
    st.markdown(f"""
    <div class="ticker-header">
        <span style="font-size:22px;font-weight:600;color:{color}">{ticker}</span>
        <span style="font-size:13px;color:#888">{len(df)} trading days</span>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    avg_vol = df['Volume'].mean()
    vol_label = f"{avg_vol/1e6:.1f}M" if avg_vol >= 1e6 else f"{avg_vol/1e3:.0f}K"
    avg_volatility = df['Volatility'].mean()

    with c1:
        st.markdown(f"""<div class="stat-card">
            <div class="stat-label">52-week high</div>
            <div class="stat-value">${df['High'].max():.2f}</div>
            <div class="stat-sub">intraday high</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="stat-card">
            <div class="stat-label">52-week low</div>
            <div class="stat-value">${df['Low'].min():.2f}</div>
            <div class="stat-sub">intraday low</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""<div class="stat-card">
            <div class="stat-label">Avg. volume</div>
            <div class="stat-value">{vol_label}</div>
            <div class="stat-sub">daily shares</div>
        </div>""", unsafe_allow_html=True)
    with c4:
        st.markdown(f"""<div class="stat-card">
            <div class="stat-label">Avg. volatility</div>
            <div class="stat-value">{avg_volatility:.2f}%</div>
            <div class="stat-sub">20-day rolling std</div>
        </div>""", unsafe_allow_html=True)


# --- Sidebar ---
with st.sidebar:
    st.markdown('<h2 style="color:#002060">StockStory</h2>', unsafe_allow_html=True)
    st.divider()
    st.caption("Primary ticker")
    file1 = st.file_uploader("Upload CSV 1", type=["csv"], label_visibility="collapsed")
    st.divider()
    st.caption("Compare with (optional)")
    file2 = st.file_uploader("Upload CSV 2", type=["csv"], label_visibility="collapsed")

# --- Main ---
ticker1, df1, ticker2, df2 = None, None, None, None

if file1:
    ticker1, df1 = run_pipeline(file1)
if file2:
    ticker2, df2 = run_pipeline(file2)

if df1 is not None:
    cb = ChartBuilder()
    comparing = df2 is not None

    # --- Ticker headers & stats ---
    if comparing:
        col_a, col_b = st.columns(2)
        with col_a:
            stat_cards(ticker1, df1, "#378ADD")
        with col_b:
            stat_cards(ticker2, df2, "#D85A30")
    else:
        stat_cards(ticker1, df1, "#378ADD")

    st.divider()

    # --- Row 1: Price Action ---
    if comparing:
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(f"**Price action — {ticker1}**")
            st.plotly_chart(cb.price_action(df1), use_container_width=True, key="pa1")
        with col_b:
            st.markdown(f"**Price action — {ticker2}**")
            st.plotly_chart(cb.price_action(df2), use_container_width=True, key="pa2")
    else:
        st.markdown("**Price action**")
        st.plotly_chart(cb.price_action(df1), use_container_width=True, key="pa1")

    # --- Row 2: Trend ---
    if comparing:
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(f"**Trend — {ticker1}**")
            st.plotly_chart(cb.trend_chart(df1), use_container_width=True, key="tr1")
        with col_b:
            st.markdown(f"**Trend — {ticker2}**")
            st.plotly_chart(cb.trend_chart(df2), use_container_width=True, key="tr2")
    else:
        st.markdown("**Trend — SMA 20 / SMA 50**")
        st.plotly_chart(cb.trend_chart(df1), use_container_width=True, key="tr1")

    # --- Row 3: Risk ---
    if comparing:
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(f"**Risk — {ticker1}**")
            st.plotly_chart(cb.risk_chart(df1), use_container_width=True, key="rk1")
        with col_b:
            st.markdown(f"**Risk — {ticker2}**")
            st.plotly_chart(cb.risk_chart(df2), use_container_width=True, key="rk2")
    else:
        st.markdown("**Risk — returns & volatility**")
        st.plotly_chart(cb.risk_chart(df1), use_container_width=True, key="rk1")

    # --- Row 4: Relative Performance (overlaid when comparing) ---
    st.markdown("**Relative performance**" + (f" — {ticker1} vs {ticker2}" if comparing else ""))
    if comparing:
        st.plotly_chart(
            cb.relative_performance_comparison(df1, df2, ticker1, ticker2),
            use_container_width=True, key="rp"
        )
    else:
        st.plotly_chart(cb.relative_performance(df1), use_container_width=True, key="rp")

else:
    st.markdown('<h2 style="color:#002060">StockStory</h2>', unsafe_allow_html=True)
    st.markdown("Upload a raw OHLCV `.csv` file in the sidebar to get started.")
    st.info("Expected columns: `Date, Open, High, Low, Close, Volume`")