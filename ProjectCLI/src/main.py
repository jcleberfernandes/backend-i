import typer 
from conta import adicionar
from date import obter_valor_em_conta

app = typer.Typer()


@app.command()
def menu():
    print("Bem-vindo ao Gerenciador de Despesas CLI!")
    saldo = 0
    while True:
        print("\n=== MENU ===")
        print("1. Adicionar dinheiro na conta")
        print("2. Registrar um gasto")
        print("3. Ver saldo atual (em breve)")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                valor = float(input("Insira o valor em conta: "))
                descricao = input("Insira a descrição: ")
                tipo = "entrada"
                saldo = saldo + valor
                adicionar(valor, descricao, tipo)

            case "2":
                valor = float(input("Insira o valor gasto: "))
                descricao = input("Insira a descrição: ")
                tipo = "saida"
                saldo = saldo - valor
                adicionar(valor, descricao, tipo)

            case "3":
                print(f"Saldo atual: R$ {saldo}")

            case "4":
                print("Saindo... Até logo!")
                break

            case _:
                print("Opção inválida!")


if __name__ == "__main__":
    app()