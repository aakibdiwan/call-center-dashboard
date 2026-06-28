import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ================= PAGE CONFIG =================
st.set_page_config(page_title="Call Center Pro Dashboard", layout="wide")

# ================= LOAD DATA =================
df = pd.read_excel("Call-Center-Sentiment-Sample-Data.xlsx", header=5)
df.columns = df.columns.str.strip()
df = df.dropna(how="all")

# ================= SIDEBAR FILTERS =================
st.sidebar.title("🔎 Filters")

city_filter = st.sidebar.multiselect(
    "Select City",
    options=df["City"].dropna().unique(),
    default=df["City"].dropna().unique()
)

sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment",
    options=df["Sentiment"].dropna().unique(),
    default=df["Sentiment"].dropna().unique()
)

channel_filter = st.sidebar.multiselect(
    "Select Channel",
    options=df["Channel"].dropna().unique(),
    default=df["Channel"].dropna().unique()
)

# ================= FILTER DATA =================
df = df[
    (df["City"].isin(city_filter)) &
    (df["Sentiment"].isin(sentiment_filter)) &
    (df["Channel"].isin(channel_filter))
]

# ================= TITLE =================
st.title("📊 Call Center Analytics Pro Dashboard")
st.markdown("### Real-time Insights from Call Data")
st.divider()

# ================= KPI CARDS =================
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Calls", len(df))
col2.metric("Avg Duration", round(df["Call Duration (Minutes)"].mean(), 2))
col3.metric("Unique Cities", df["City"].nunique())
col4.metric("Channels Used", df["Channel"].nunique())

st.divider()

# ================= CHARTS =================
c1, c2 = st.columns(2)

# -------- SENTIMENT PIE --------
with c1:
    st.subheader("🎯 Sentiment Distribution")
    fig, ax = plt.subplots()
    df["Sentiment"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax
    )
    ax.set_ylabel("")
    st.pyplot(fig)

# -------- CHANNEL BAR --------
with c2:
    st.subheader("📡 Channel Usage")
    fig, ax = plt.subplots()
    df["Channel"].value_counts().plot(kind="bar", ax=ax, color="orange")
    st.pyplot(fig)

st.divider()

# ================= CITY ANALYSIS =================
st.subheader("🌍 Top Cities (Call Volume)")
fig, ax = plt.subplots()
df["City"].value_counts().head(10).plot(kind="barh", ax=ax, color="green")
ax.invert_yaxis()
st.pyplot(fig)

st.divider()

# ================= SLA ANALYSIS =================
st.subheader("⏱ Response Time Analysis")

if "Response Time" in df.columns:
    fig, ax = plt.subplots()
    df["Response Time"].value_counts().plot(kind="bar", ax=ax, color="purple")
    st.pyplot(fig)
else:
    st.warning("Response Time column not found")

st.divider()

# ================= RAW DATA =================
st.subheader("📄 Filtered Data View")
st.dataframe(df, use_container_width=True)

# ================= INSIGHTS =================
st.divider()
st.subheader("💡 Key Insights")

st.write("✔ Most Common Sentiment:", df["Sentiment"].value_counts().idxmax())
st.write("✔ Most Active City:", df["City"].value_counts().idxmax())
st.write("✔ Most Used Channel:", df["Channel"].value_counts().idxmax())
st.write("✔ Avg Call Duration:", round(df["Call Duration (Minutes)"].mean(), 2))