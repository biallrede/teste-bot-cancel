import pandas as pd
from bot import enviar_mensagem
from query import query_cancel_vol
import datetime


# Função para configurar a mensagem a ser enviada

def configura_mensagem(token,chat_id): 


# Separação por Regionais

        df_cancel = query_cancel_vol()

        print(df_cancel)
        for i in df_cancel.index:
                mensagem_regional = '''

📍 <b>{}</b>
🏘️ {}

👤 <b>{}</b>
Código Cliente: <b>{}</b>
ID Cliente Serviço: <b>{}</b>
Motivo Cancelamento: <b>{}</b>

'''.format(df_cancel['regional'][i],
           df_cancel['cidade'][i],
           df_cancel['nome_razaosocial'][i],
           df_cancel['codigo_cliente'][i],
           df_cancel['id_cliente_servico'][i],
           df_cancel['motivo_cancelamento'][i],
           )
       
                enviar_mensagem(token, chat_id, mensagem_regional)
                print(mensagem_regional)

        # configura_mensagem(1,1)       # Testar no arquivo 'mensagem.py' com 'print()'