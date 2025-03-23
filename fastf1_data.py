
import fastf1
import pandas as pd
from fastf1 import plotting

# Ativar cache
fastf1.Cache.enable_cache('cache_fastf1')

def carregar_dados_corrida(ano=2024, gp="China", sessao="R"):
    session = fastf1.get_session(ano, gp, sessao)
    session.load()
    return session

# Tabela de tempos por volta
def voltas_por_piloto(session, piloto_nome):
    laps = session.laps.pick_driver(piloto_nome).pick_fastest()
    return laps

# Estratégia de pneus
def estrategia_pneus(session):
    stint_data = session.laps.get_stint_summary()
    return stint_data

# Tempos médios por setor
def tempos_setores(session):
    setores = session.laps[["Driver", "Sector1Time", "Sector2Time", "Sector3Time"]]
    setores = setores.dropna()
    setores["S1"] = setores["Sector1Time"].dt.total_seconds()
    setores["S2"] = setores["Sector2Time"].dt.total_seconds()
    setores["S3"] = setores["Sector3Time"].dt.total_seconds()
    return setores.groupby("Driver")[["S1", "S2", "S3"]].mean().round(2)

# Melhor volta de cada piloto
def melhores_voltas(session):
    laps = session.laps.pick_quicklaps()
    fastest = laps.groupby("Driver")["LapTime"].min().dt.total_seconds().round(2)
    return fastest.sort_values()
