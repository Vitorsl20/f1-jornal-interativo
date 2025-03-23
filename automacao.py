
import schedule
import time
from utils.fantasy import gerar_alerta
from utils.email_notifier import enviar_email_alerta

TIPO_PISTA = "Alta Velocidade"
CLIMA = "Seco"

def tarefa_agendada():
    alerta = gerar_alerta(TIPO_PISTA, CLIMA)
    enviar_email_alerta(alerta, TIPO_PISTA, CLIMA)

# Agendamento diário às 08:00
schedule.every().day.at("08:00").do(tarefa_agendada)

if __name__ == "__main__":
    print("⏰ Aguardando execução diária do alerta pré-corrida às 08:00...")
    while True:
        schedule.run_pending()
        time.sleep(60)
