from datetime import datetime, timezone


def obter_data_hora_atual():
    """Retorna a data e hora atual no formato ISO 8601."""
    return datetime.now(timezone.utc).isoformat()


def obter_valor_em_conta():
    """Função para calcular o valor atual em conta."""
    return 0.0  # Placeholder, a lógica para calcular o saldo ainda precisa ser implementada    
        
