import streamlit as st
from snowflake.snowpark.context import get_active_session



session = get_active_session()
df_user = session.sql("SELECT CURRENT_USER()")
st.write(df_user)