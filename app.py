# Imports:
import json
import time
import os
import datetime
import datetime
from pytz import timezone
from twilio.rest import Client
# from dotenv import load_dotenv


# Settings:
# load_dotenv()
account_sid = os.environ('ACCOUNT_SID')
auth_token = os.environ('AUTH_TOKEN')
client = Client(account_sid, auth_token) # inicializa cliente do Twilio


# Funções:
def check(diaSemana, tempo, data): # checa os parâmetros da hora atual, e depois manda o lembrete
    for info in data['YABOT']:
        dia_mes = info['dia_mes']
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

    print(f'SID: {message.sid}, \nTIME: {tempo}')

def add_json():
    # if msg.lower() in ["add"]:
    #     manda_mensagem("teste add")
    pass


# Main():
def main():
    # Tempo:
    now = datetime.datetime.now()
    # utc = datetime.datetime.now(datetime.timezone.utc)
    # BRSP = timezone('America/Sao_Paulo')
    # now = utc.astimezone(BRSP)

    # segundo = now.second

    # Load Data:
    with open('messages.json') as f:
        data = json.load(f)

    # Variáveis:
    diaSemana = datetime.today().isoweekday()
    tempo = now.strftime('%H:%M')
    
    # Função:
    print(f"TIME: {tempo}")
    check(diaSemana, tempo, data)
    print("")

    # Espera 1 segundo:
    time.sleep(1)

