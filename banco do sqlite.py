from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Define endereço para se conectar ao banco.
engine = create_engine('sqlite:///BANCO.db')
# engine = create_engine('sqlite://pedro:123@localhost/le-banc.db')



# modela e define tabela para o banco
Base = declarative_base()


class Login(Base):
    __tablename__ = 'logins'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)


# persiste as tabelas no banco/cria de fato as tabelas no banco
Base.metadata.create_all(engine)


# cria uma sessão para manipular o banco.
Session = sessionmaker(bind=engine)
session = Session()

while True:
    opcao = input('digite a opção desejada\n [1]criar\n [2]ler\n')
    if opcao == '1':
        Nome = input('nome da pessoa:\n')
        Email = input('email da pessoa:\n')
        senha = input('senha de login:\n')
        login = Login(nome=Nome, email=Email, senha=senha)
        session.add(login)
        session.commit()
        print('login criado com sucesso')
    elif opcao == '2':
        logins = session.query(Login)
        for login in logins:
            print(f'id={login.id}, nome={login.nome}, email={login.email}, senha={login.senha}')
    else:
        print('opcao invalida')
