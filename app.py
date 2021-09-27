# Imports:
import json
import time
import os
from datetime import datetime
from twilio.rest import Client
# from dotenv import load_dotenv


# Settings:
load_dotenv()
account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')
client = Client(account_sid, auth_token) # inicializa cliente do Twilio


# Funções:
def check(diaSemana, tempo, data): # checa os parâmetros da hora atual, e depois manda o lembrete
    for info in data['YABOT']:
        date = info['dias_num']
        schedule = info['horario']
        message = info['message']
        for i in date:
            if i == diaSemana or i == 0: # checa o dia da semana
                if tempo == schedule: # checa o horário atual
                    manda_mensagem(message, tempo)

def manda_mensagem(mensagem, tempo): # função para mandar mensagem
    from_whatsapp_number = 'whatsapp:+14155238886'
    to_whatsapp_number = 'whatsapp:+5511991982436'

    message = client.messages.create(body=mensagem,
                                     from_=from_whatsapp_number,
                                     to=to_whatsapp_number)

    print(f'SID: {message.sid}')

def add_json():
    # if msg.lower() in ["add"]:
    #     manda_mensagem("teste add")
    pass


# Main():
def main():
    # Tempo:
    now = datetime.now()
    # segundo = now.second

    # if segundo == 0:
        # Load Data:
    with open('messages.json') as f:
        data = json.load(f)

    # Variáveis:
    diaSemana = datetime.today().isoweekday()
    tempo = now.strftime('%H:%M')
    
    # Função:
    # print(f"Horário: {tempo}")
    # print(f"Dia: {diaSemana}")
    # print("")
    check(diaSemana, tempo, data)
    # print("")

    # Espera 1 segundo:
    time.sleep(1)
