# app.py - Interface principal do F1 Jornal Interativo com dados reais

import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import datetime
from utils.fantasy import *
from utils.scraping import *
from utils.email_notifier import enviar_email_alerta, enviar_resumo_manchetes
from utils.google_api import adicionar_evento_calendar, salvar_fantasy_sheet
from utils.ergast_api import classificacao_pilotos, classificacao_equipes, ultima_corrida
from utils.fastf1_data import carregar_dados_corrida, melhores_voltas

st.set_page_config(layout="wide", page_title="F1 Jornal Interativo", page_icon="🏁")
st.title("🏎️ F1 Jornal Interativo - Edição com Dados Reais")

abas = st.tabs([
    "📰 Manchetes", "🏆 Classificação", "📈 Fantasy Dicas", "🧑‍✈️ Pilotos",
    "🚗 Equipes", "⚖️ Comparativos", "📊 Telemetria", "🚨 Alerta Pré-Corrida", "📆 Automação"
])

with abas[0]:
    st.subheader("🗞️ Manchetes da Semana")
    manchetes = buscar_manchetes()
    for m in manchetes:
        st.write("-", m)
    if st.button("📩 Enviar Manchetes por E-mail"):
        enviar_resumo_manchetes(manchetes)

with abas[1]:
    st.subheader("🏆 Classificação Real")
    pilotos_df = classificacao_pilotos()
    equipes_df = classificacao_equipes()
    st.markdown("### Pilotos")
    st.dataframe(pilotos_df)
    st.bar_chart(pilotos_df.set_index("Piloto"))
    st.markdown("### Equipes")
    st.dataframe(equipes_df)
    st.bar_chart(equipes_df.set_index("Equipe"))

with abas[2]:
    st.subheader("📈 Sugestão de Escalação")
    pilotos, equipes, custo = sugerir_time_ideal()
    st.markdown("### Pilotos")
    st.dataframe(pilotos)
    st.markdown("### Equipes")
    st.dataframe(equipes)
    st.write(f"💸 Custo total: {custo} milhões")
    if st.button("💾 Salvar no Google Sheets"):
        salvar_fantasy_sheet(pilotos, equipes)

with abas[3]:
    st.subheader("🧑‍✈️ Galeria de Pilotos")
    df = carregar_dados_pilotos()
    st.dataframe(df)

with abas[4]:
    st.subheader("🚗 Galeria de Equipes")
    df = carregar_dados_equipes()
    st.dataframe(df)

with abas[5]:
    st.subheader("⚖️ Comparativo de Companheiros")
    comp = comparar_companheiros()
    st.dataframe(comp)

with abas[6]:
    st.subheader("📊 Telemetria Real (FastF1)")
    gp = st.selectbox("Escolha o GP", ["China", "Austrália", "Bahrain"])
    sessao = carregar_dados_corrida(2024, gp, "R")
    voltas = melhores_voltas(sessao)
    st.markdown("### Melhores Voltas")
    st.dataframe(voltas)

with abas[7]:
    st.subheader("🚨 Alerta Pré-Corrida")
    tipo = st.selectbox("Tipo de Pista", ["Alta Velocidade", "Urbano", "Misto"])
    tempo = st.selectbox("Clima", ["Seco", "Chuva"])
    alerta = gerar_alerta(tipo, tempo)
    st.dataframe(alerta)
    if st.button("📤 Enviar Alerta por E-mail"):
        enviar_email_alerta(alerta, tipo, tempo)

with abas[8]:
    st.subheader("📆 Próxima Corrida e Automação")
    corrida = buscar_proxima_corrida()
    st.write(corrida)
    if st.button("📅 Adicionar ao Google Calendar"):
        adicionar_evento_calendar(corrida)

st.markdown("---")
st.success("✅ Sistema carregado com dados reais e telemetria via FastF1 e Ergast API!")
