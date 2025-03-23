
# 🏎️ F1 Jornal Interativo — Guia de Instalação

Este é um sistema completo de jornal interativo e Fantasy da Fórmula 1, com:
- Dados reais de pilotos e equipes (Ergast API)
- Telemetria por volta e análise técnica (FastF1)
- Sugestões otimizadas para F1 Fantasy com orçamento de 100M
- Envio automático por e-mail
- Integração com Google Calendar e Google Sheets

---

## 📁 Estrutura da pasta

- app.py → Interface principal via Streamlit
- automacao.py → Envia alertas automáticos com dicas de fantasy
- utils/
  - ergast_api.py → classificação real F1
  - fastf1_data.py → telemetria real
  - google_api.py → integração com Google Calendar + Sheets
  - credentials_calendar.json → chave da conta de serviço (NÃO compartilhar)
- data/
  - historico_fantasy.csv → exemplo de histórico
- config.json → preencha com suas credenciais

---

## ✅ Pré-requisitos

1. Python 3.10 ou superior
2. Instalar dependências:
```bash
pip install streamlit pandas requests schedule google-api-python-client fastf1 fpdf
```

---

## 🚀 Como rodar

### 1. Interface do sistema:
```bash
streamlit run app.py
```

### 2. Envio automático diário:
```bash
python automacao.py
```

---

## ✉️ Configuração do `config.json`

Edite o arquivo `config.json` com:
```json
{
  "gmail_user": "SEU_EMAIL",
  "gmail_password": "SUA_SENHA_DE_APP",
  "spreadsheet_id": "ID_DA_SUA_PLANILHA",
  "calendar_id": "primary"
}
```

---

## ✅ Configuração do Google:
- Ative Google Sheets e Google Calendar API no [Google Cloud Console](https://console.cloud.google.com)
- Compartilhe sua planilha e calendário com o e-mail da conta de serviço

---

Pronto! Seu F1 Jornal Interativo está no ar 🚀
