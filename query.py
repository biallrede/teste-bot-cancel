import pandas as pd 
from credentials import credenciais_banco_hubsoft

def query_cancel_vol():
    conn = credenciais_banco_hubsoft()
    query = '''
SELECT CASE WHEN REG.nome_tag ISNULL THEN 'REGIONAL - NÃO DEFINIDA' ELSE REG.nome_tag END AS regional
	  ,end3.nome as cidade
	  ,D.codigo_cliente
	  ,D.nome_razaosocial
	  ,A.id_cliente_servico
	  ,B.descricao AS motivo_cancelamento
--	  ,C.observacao
FROM cliente_servico A

LEFT JOIN motivo_cancelamento B ON B.id_motivo_cancelamento = A.id_motivo_cancelamento
LEFT JOIN protocolo_cancelamento C ON C.id_cliente_servico = A.id_cliente_servico
LEFT JOIN cliente D ON D.id_cliente = A.id_cliente

LEFT JOIN
	(SELECT * FROM
		(SELECT A.id_cliente_servico
			   ,B.descricao AS nome_tag
			   ,ROW_NUMBER() OVER(PARTITION BY A.id_cliente_servico ORDER BY A.id_cliente_servico ASC) AS linha
		 FROM cliente_servico_grupo A
		 LEFT JOIN grupo_cliente_servico B ON B.id = A.id_grupo_cliente_servico
		 WHERE B.descricao LIKE 'REGIONAL%'
		   AND B.ativo = true
		) A 
	 WHERE A.linha = 1
	) REG ON REG.id_cliente_servico = A.id_cliente_servico
	
LEFT JOIN
	(SELECT id_cliente_servico
		   ,id_endereco_numero
     FROM cliente_servico_endereco
     WHERE tipo = 'instalacao'
   ) end1 ON end1.id_cliente_servico = A.id_cliente_servico
LEFT JOIN endereco_numero end2 ON end2.id_endereco_numero = end1.id_endereco_numero
LEFT JOIN cidade end3 ON end3.id_cidade = end2.id_cidade

WHERE A.data_habilitacao NOTNULL 							-- Serviço Habilitado
  AND A.id_servico_status IN (9, 30)						-- Status 'Cancelado', 'Cancelado Sem Retirada'
  AND B.gera_grafico = true									-- Motivo de Cancelamento Válido
  AND B.id_motivo_cancelamento NOT IN (20, 42)				-- Apenas Cancelamentos Voluntários
  AND A.id_servico NOT IN (5165, 8134, 4179, 4219, 9451)	-- Aluguel de Porta, Locação de Infraestrutura, Rede Neutra  
  AND A.data_cancelamento::date = CURRENT_DATE
  AND C.data_cadastro::timestamp BETWEEN to_char(CURRENT_TIMESTAMP - interval '30 minutes', 'YYYY-MM-DD HH24:MI')::timestamp	-- Últimos 30 min
									 AND to_char(CURRENT_TIMESTAMP, 'YYYY-MM-DD HH24:MI')::timestamp
'''
    
	
    resultado = pd.read_sql(query,conn)
    conn.close()
    return resultado