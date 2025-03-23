
import requests
import pandas as pd

ERGAST_BASE = "https://ergast.com/api/f1"

# Classificação atual de pilotos
def classificacao_pilotos(atual=True, temporada="2024"):
    url = f"{ERGAST_BASE}/current/driverStandings.json" if atual else f"{ERGAST_BASE}/{temporada}/driverStandings.json"
    response = requests.get(url)
    data = response.json()
    pilotos = data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
    lista = []
    for p in pilotos:
        nome = p['Driver']['familyName']
        equipe = p['Constructors'][0]['name']
        pontos = int(p['points'])
        lista.append((nome, equipe, pontos))
    df = pd.DataFrame(lista, columns=["Piloto", "Equipe", "Pontos"])
    return df.sort_values(by="Pontos", ascending=False)

# Classificação atual de construtores
def classificacao_equipes(atual=True, temporada="2024"):
    url = f"{ERGAST_BASE}/current/constructorStandings.json" if atual else f"{ERGAST_BASE}/{temporada}/constructorStandings.json"
    response = requests.get(url)
    data = response.json()
    equipes = data['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']
    lista = []
    for e in equipes:
        nome = e['Constructor']['name']
        pontos = int(e['points'])
        lista.append((nome, pontos))
    df = pd.DataFrame(lista, columns=["Equipe", "Pontos"])
    return df.sort_values(by="Pontos", ascending=False)

# Resultados da última corrida
def ultima_corrida():
    url = f"{ERGAST_BASE}/current/last/results.json"
    response = requests.get(url)
    data = response.json()
    results = data['MRData']['RaceTable']['Races'][0]
    nome = results['raceName']
    data_gp = results['date']
    circuito = results['Circuit']['circuitName']
    lista = []
    for r in results['Results']:
        piloto = r['Driver']['familyName']
        posicao = int(r['position'])
        equipe = r['Constructor']['name']
        status = r['status']
        lista.append((posicao, piloto, equipe, status))
    df = pd.DataFrame(lista, columns=["Posição", "Piloto", "Equipe", "Status"])
    return nome, data_gp, circuito, df.sort_values("Posição")
