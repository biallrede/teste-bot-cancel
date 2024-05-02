import threading
import time
from apscheduler.schedulers.background import BackgroundScheduler
from mensagem import configura_mensagem
import schedule
import logging


scheduler = BackgroundScheduler()

def rotina1():
    token = '6559966693:AAEfriM_9iTjUSmdCjUF2Xu1jzfSTHMuC9Y' #token do bot
    chat_id = '-4189980510'    #id do grupo que o bot está configurado para enviar as mensagens
    configura_mensagem(token, chat_id) #função que envia as mensagens 
    logging.basicConfig(filename='log.txt', level=logging.INFO) #armazena os logs de rotina no arquivo log.txt
    logging.info('Rotina 1 executada em: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) #armazena a data e hora da execução da rotina

# def rotina2():
#     token = '6207063421:AAH8_WqG69z8cmlTGLXSRYffxghVv5qYsTw' #token do bot
#     chat_id = '-906098757'    #id do grupo que o bot está configurado para enviar as mensagens
#     configura_mensagem(token, chat_id) #função que envia as mensagens 
#     logging.basicConfig(filename='log.txt', level=logging.INFO) #armazena os logs de rotina no arquivo log.txt
#     logging.info('Rotina 1 executada em: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) #armazena a data e hora da execução da rotina


# Agendando as rotinas para executar em horários específicos
    
# schedule.every().day.at("16:46").do(rotina1) #especifica o horário para executar a rotina1 - Utilizado para teste
# schedule.every().day.at("08:00").do(rotina2)
# schedule.every().day.at("16:10").do(rotina3)

# Agendando a execução da rotina1 a cada hora, das 9h às 22:50h

def main():
    while True:
        for i in range(7, 23):
            schedule.every().day.at(f"{i:02d}:00").do(rotina1) # Roda no minuto 00
            schedule.every().day.at(f"{i:02d}:05").do(rotina1) # Roda no minuto 00
            schedule.every().day.at(f"{i:02d}:10").do(rotina1) # Roda no minuto 00
            schedule.every().day.at(f"{i:02d}:15").do(rotina1) # Roda no minuto 00
            schedule.every().day.at(f"{i:02d}:20").do(rotina1) # Roda no minuto 00
            schedule.every().day.at(f"{i:02d}:25").do(rotina1) # Roda no minuto 00
            schedule.every().day.at(f"{i:02d}:30").do(rotina1) # Roda no minuto 00
            schedule.every().day.at(f"{i:02d}:35").do(rotina1) # Roda no minuto 00
            schedule.every().day.at(f"{i:02d}:40").do(rotina1) # Roda no minuto 00
            schedule.every().day.at(f"{i:02d}:45").do(rotina1) # Roda no minuto 30
            schedule.every().day.at(f"{i:02d}:50").do(rotina1) # Roda no minuto 30
            schedule.every().day.at(f"{i:02d}:55").do(rotina1) # Roda no minuto 30

        scheduler.start()
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    main()
    


