import streamlit as st

# st.set_page_config(
#     page_title="Ex-stream-ly Cool App",
#     page_icon="🧊",
#     layout="wide",
#     initial_sidebar_state="expanded",
#     menu_items={
#         'Get Help': 'https://www.extremelycoolapp.com/help',
#         'Report a bug': "https://www.extremelycoolapp.com/bug",
#         'About': "# This is a header. This is an *extremely* cool app!"
#     }
# )

with open('C:/Users/ADMIN_2/Python_Giridhar/App Analytics/Analytics/databasestreamlit/style.css') as f:
    st.markdown(f'<style>{f.read()}<style>', unsafe_allow_html = True)

col1, col2, col3 = st.columns(3)

col1.metric("Temperature","70 F", "12 F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

