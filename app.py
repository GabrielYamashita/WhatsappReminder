## Imports:
import os
import json
import time
import datetime
from pytz import timezone
from twilio.rest import Client
from dotenv import load_dotenv


## Settings:
account_sid = os.environ.get('ACCOUNT_SID') # account sid para o heroku
auth_token = os.environ.get('AUTH_TOKEN') # auth token para o heroku

# load_dotenv() # carrega as variáveis de ambiente
# account_sid = os.getenv('ACCOUNT_SID') # account sid para rodar localmente
# auth_token = os.getenv('AUTH_TOKEN') # auth token para rodar localmente

# Client:
client = Client(account_sid, auth_token) # inicializa cliente do Twilio


## Funções:
def check(diaSemana, tempo, data, dia): # checa os parâmetros da hora atual, e depois manda o lembrete
    for info in data['YABOT']: # checa cada info de data
        dia_mes = info['dia_mes'] # recebe o dia do mês
        date = info['dias_num'] # recebe o dia da semana
        schedule = info['horario'] # recebe o horário
        message = info['message'] # recebe a mensagem
        
        if dia_mes == None:
            for i in date:
                if i == diaSemana or i == 0: # checa o dia da semana
                    if tempo == schedule: # checa o hor-ário atual
                        manda_mensagem(message, tempo)

        else:
            for i in dia_mes:
                if i == dia:
                    if tempo == schedule:
                        manda_mensagem(message, tempo)


def manda_mensagem(mensagem): # função para mandar a mensagem
    from_whatsapp_number = 'whatsapp:+14155238886'
    to_whatsapp_number = 'whatsapp:+5511991982436'

    message = client.messages.create(body=mensagem,
                                     from_=from_whatsapp_number,
                                     to=to_whatsapp_number)
    # print(f'SID: {message.sid}, \nTIME: {tempo}')


def add_json():
    pass


## Main:
def main():
    ## Tempo:
    utc = datetime.datetime.now(datetime.timezone.utc) # setando o tempo para UTC
    BRSP = timezone('America/Sao_Paulo') # escolhendo o fuso horário
    now = utc.astimezone(BRSP) # adicionando o fuso horário de SP
    segundo = now.second

    if segundo == 0:
        # Carregando o JSON:
        with open('messages.json', encoding='utf-8') as f:
            data = json.load(f) # armazenando na variável data

        # Variáveis:
        dia = now.day # dia atual do mês
        diaSemana = now.isoweekday() # dia da semana atual
        tempo = now.strftime('%H:%M') # horário atual
        
        # Função:
        print(f"TIME: {tempo}")
        check(diaSemana, tempo, data, dia)

        # Espera 1 segundo:
        time.sleep(1)
