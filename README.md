
# 🏁 F1 Jornal Interativo

Sistema completo de jornal digital para Fórmula 1 com Fantasy, notícias e dados reais.

![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-orange?style=flat&logo=streamlit)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-blue)

---

## 🔥 Funcionalidades

- 📰 Manchetes da semana (scraping ao vivo)
- 🏆 Classificação real de pilotos e construtores (Ergast API)
- 📈 Sugestões otimizadas para F1 Fantasy com orçamento
- 📊 Análise de telemetria (FastF1: voltas, pneus, setores)
- 📤 Envio de alerta por e-mail antes das corridas
- 📅 Integração com Google Calendar
- 📄 Exportação em PDF com resumo semanal
- ☁️ Pronto para deploy no Streamlit Cloud

---

## 🚀 Como rodar

### Requisitos
```bash
pip install -r requirements.txt
```

### Rodar o sistema
```bash
streamlit run app.py
```

### Automatizar alerta diário
```bash
python automacao.py
```

---

## 📂 Estrutura

```
📁 utils/
├── ergast_api.py         # Classificação real
├── fastf1_data.py        # Telemetria
├── google_api.py         # Google Sheets e Calendar
📁 data/
└── historico_fantasy.csv # Histórico de escalações
app.py
automacao.py
config.json
requirements.txt
```

---

## ☁️ Deploy Online

Suba os arquivos no GitHub + `requirements.txt` + `.streamlit/config.toml`  
E rode direto no [Streamlit Cloud](https://share.streamlit.io)

---

## 🔐 Configuração

### `config.json` (adicione suas credenciais)
```json
{
  "gmail_user": "seu_email@gmail.com",
  "gmail_password": "senha_app",
  "spreadsheet_id": "id_da_planilha",
  "calendar_id": "primary"
}
```

---

Feito com ⚙️ por inteligência + paixão pela F1.
