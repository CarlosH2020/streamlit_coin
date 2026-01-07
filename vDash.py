"""
Docstring for [Virtual Currency].vDash
"""

import streamlit as st
import requests


def config_page():
    st.set_page_config(
        page_title="BlockView",
        layout="wide"
    )

config_page()  


def access_website_btc():
    URL_PAGE = "https://www.mercadobitcoin.net/api/BTC/ticker/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    data = requests.get(URL_PAGE).json()
    last_price = float(data["ticker"]["last"])

    btc_tag = f"R$ {last_price:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


    return btc_tag

def access_website_xrp():
    URL_PAGE = "https://www.mercadobitcoin.net/api/XRP/ticker/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    data = requests.get(URL_PAGE).json()
    last_price = float(data["ticker"]["last"])

    xrp_tag = f"R$ {last_price:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


    return xrp_tag

def card_metrics(btc_value: str, xrp_value: str):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Bitcoin (BTC)",
            value=btc_value,
            border=True
        )

    with col2:
        st.metric(label="Ethereum (ETH)", value="—", border=True)

    with col3:
        st.metric(label="Solana (SOL)", value="—", border=True)

    with col4:
        st.metric(label="XRP (XRP)", value=xrp_value, border=True)




btc = access_website_btc()
xrp = access_website_xrp()
card_metrics(btc, xrp)


