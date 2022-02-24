import sqlite3
import altair as alt
import pandas as pd
import streamlit as st
import os


#sqliteConnection = sqlite3.connect('/tmp/my-db.db')

def _connect():
    from trino import dbapi
    from trino import constants


    from trino.auth import BasicAuthentication

    # auth = (
    #     BasicAuthentication("user", "pass")
    # )
    auth = None
    conn = dbapi.connect(
        host=os.environ.get("VDK_TRINO_HOST"),
        port=int(os.environ.get("VDK_TRINO_PORT")),
        user="user",
        auth=auth,
        catalog=os.environ.get("VDK_TRINO_CATALOG", 'mysql'),
        schema=os.environ.get("VDK_TRINO_SCHEMA", "default"),
        http_scheme=constants.HTTP,
        verify=False,
        request_timeout=600,
    )
    return conn

conn = _connect()

data = pd.read_sql_query(
    f"select id, count(1) as cnt from hello_table group by id", conn
)

chart = (
    alt.Chart(data)
        .mark_bar()
        .encode(
        x="id",
        y=alt.Y("cnt", stack=None),
    )
)
st.altair_chart(chart, use_container_width=True)
