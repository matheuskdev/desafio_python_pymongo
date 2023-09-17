import pymongo

# Conecte-se ao seu cluster MongoDB no MongoDB Atlas
client = pymongo.MongoClient("URL_DO_SEU_CLUSTER_MONGODB_ATLAS")

# Crie um banco de dados chamado "banco_nosql"
db = client["banco_nosql"]

# Crie uma coleção chamada "bank" para armazenar documentos de cliente
colecao = db["bank"]

# Insira documentos de exemplo
documento1 = {
    "nome": "João",
    "cpf": "12345678900",
    "endereco": "Rua A",
    "contas": [
        {"tipo": "Corrente", "agencia": "001", "num": 1001, "saldo": 5000},
        {"tipo": "Poupança", "agencia": "002", "num": 2002, "saldo": 3000}
    ]
}

documento2 = {
    "nome": "Maria",
    "cpf": "98765432100",
    "endereco": "Rua B",
    "contas": [
        {"tipo": "Corrente", "agencia": "003", "num": 3003, "saldo": 8000}
    ]
}

# Insira os documentos na coleção
colecao.insert_many([documento1, documento2])

# Recuperar informações com base nos pares chave-valor
resultado = colecao.find({"nome": "João"})
for doc in resultado:
    print("Nome:", doc["nome"])
    print("CPF:", doc["cpf"])
    print("Endereço:", doc["endereco"])
    print("Contas:")
    for conta in doc["contas"]:
        print(f"Tipo: {conta['tipo']}, Agência: {conta['agencia']},\
              Número: {conta['num']}, Saldo: {conta['saldo']}")
