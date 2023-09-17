from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Decimal
from sqlalchemy.orm import declarative_base, Session, relationship

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String)
    endereco = Column(String)
    contas = relationship("Conta", back_populates="cliente")

class Conta(Base):
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    saldo = Column(Decimal)
    id_cliente = Column(Integer, ForeignKey("cliente.id"))
    cliente = relationship("Cliente", back_populates="contas")

# Crie uma conexão com o banco de dados SQLite
engine = create_engine("sqlite:///banco.db")

# Crie as tabelas no banco de dados
Base.metadata.create_all(engine)

# Crie uma sessão para interagir com o banco de dados
with Session(engine) as sessao:
    # Inserir alguns dados de exemplo
    cliente1 = Cliente(nome="João", cpf="12345678900", endereco="Rua A")
    cliente2 = Cliente(nome="Maria", cpf="98765432100", endereco="Rua B")
    conta1 = Conta(tipo="Corrente", agencia="001", num=1001, saldo=5000,
                   cliente=cliente1)
    conta2 = Conta(tipo="Poupança", agencia="002", num=2002, saldo=3000,
                   cliente=cliente2)

    sessao.add_all([cliente1, cliente2, conta1, conta2])
    sessao.commit()

    # Recuperar dados
    clientes = sessao.query(Cliente).all()
    for cliente in clientes:
        print(f"Cliente: {cliente.nome}, CPF: {cliente.cpf},\
              Endereço: {cliente.endereco}")
        for conta in cliente.contas:
            print(f"Conta {conta.tipo}: Agência {conta.agencia},\
                  Número {conta.num}, Saldo {conta.saldo}")
