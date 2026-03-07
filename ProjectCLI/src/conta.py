from logic import salvar_no_arquivo
from date import obter_data_hora_atual

def adicionar(valor, descricao, tipo):
    time = obter_data_hora_atual()
    dados = {
        "tipo": tipo, 
        "descricao": descricao,
        "valor": valor,
        "data_hora": time
    }
    salvar_no_arquivo(dados)
