# import pyodbc

# def credenciais_banco_hubsoft():
#     conn = pyodbc.connect('Driver={PostgreSQL ODBC Driver(UNICODE)};'
#                         'Server=18.230.16.241;'
#                         'Port=9432;'
#                         'Database=hubsoft;'
#                         'Uid=erick_leitura;'
#                         'Pwd=73f4cc9b2667d6c44d20d1a0d612b26c5e1763c2;')
    
#     return conn

# def credenciais_banco_alldata():
# # Configuração da conexão com o banco de dados
#     conn = pyodbc.connect(
#         'DRIVER={ODBC Driver 17 for SQL Server};'
#         'Server=201.87.240.196;' 
#         'Database=Alldata;'
#         'UID=Alldata;'
#         'PWD=bdAlldata170#;'
#     )
#     return conn

########################################################################### Credenciais banco Linux ###########################################################################
import psycopg2
 
def credenciais_banco_hubsoft():
    conn = psycopg2.connect(
                        host ='18.230.16.241',
                        port = '9432',
                        database='hubsoft',
                        user='erick_leitura',
                        password='73f4cc9b2667d6c44d20d1a0d612b26c5e1763c2'
                        )
   
    return conn

# def credenciais_banco_alldata():
#     conn = psycopg2.connect(
#                         host ='201.87.240.196',
#                         port = '1433',
#                         database='Alldata',
#                         user='Alldata',
#                         password='bdAlldata170#'
#                         )
   
#     return conn