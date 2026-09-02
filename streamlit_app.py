import streamlit as st
import pyodbc
def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=LAPTOP-SRAV2QR1\\MSSQLSERVER01;"
        "DATABASE=Euroleague_Pancake;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    conn = get_connection()
    query = "SELECT * FROM dbo.Attack"   # άλλαξε το όνομα του πίνακα σου
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# -----------------------------
# STREAMLIT UI
# -----------------------------
st.title("Euroleague Pancake Dashboard")
st.write("Live data from SQL Server")

df = load_data()

st.subheader("Raw Data")
st.dataframe(df)

st.set_page_config(layout='wide',page_title="Tiganitas Sotiris Dashboard Portofolio",page_icon="")

st.title("My dashboards portfolio📈📊")
st.write("#### ")
st.write(
    "### - 🏀 Euroleague Stats:"
)

st.write("##### * RShinyapp (R software) ~ https://tiganitassot.shinyapps.io/Euroleague/ ")
st.write("It takes approximately 2 minutes to load all stats")

st.write("##### * Streamlit app (Python software) ~ https://euroleaguebasketball.streamlit.app/ ")
st.write(" It loads all stats quicker than RShiny")
st.write("#### ")
st.write(
    "### - ⚽ Greek Superleague Stats")
st.write("##### https://football-data-analysis.streamlit.app/ ")
st.write("#### ")
st.write(
    "### - 💡 Belyse Lights: Analyzes the orders of the eshop")
st.write("##### https://belyselights.streamlit.app/ ")
st.write("#### ")

st.write(
    "### - 📋 Insurance Broker portofolio: Analyzes the insurance policies and the development of the company")
st.write("##### https://stportofoliomanage.streamlit.app/ ")

st.write("#### ")
st.write(
    "### - 📋 Insurance Broker portofolio: Analyzes the insurance policies and the development of the company")
st.write("##### https://insurancebrokerftportofolio.streamlit.app/ ")

st.write("#### ")
st.write('#### - For more information contact to tiganitassotiris@gmail.com')
