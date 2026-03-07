import json

DB = "conta.json"

def salvar_no_arquivo(dados):

    with open(DB, "r") as file:
        logs = json.load(file)


    logs.append(dados)


    with open(DB, "w", encoding="utf-8") as file:
        json.dump(logs, file, indent=4, ensure_ascii=False)