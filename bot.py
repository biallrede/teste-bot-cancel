import requests
import logging
import time

# enviar mensagens utilizando o bot para um chat específico utilizando a api do telegram
def enviar_mensagem(token, chat_id, msg):
    try:
        
        data = {"chat_id": chat_id, "text": msg, "parse_mode":"HTML"}
        url = "https://api.telegram.org/bot{}/sendMessage".format(token)
        requests.post(url, data)

    except Exception as e:
        # data = {"chat_id": '-986170429', "text": 'Falha no envio da {}: {}'.format(rotina,e), "parse_mode":"HTML"}
        url = "https://api.telegram.org/bot{}/sendMessage".format(token)
        requests.post(url, data)
        logging.basicConfig(filename='log.txt', level=logging.INFO)
        # logging.info('FALHA Execução {} executada em: '.format(rotina) + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
