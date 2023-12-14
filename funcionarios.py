# Sistema de cadastro de funcionarios
import mysql.connector

def funcionarios():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="funcionarios"
    )

def executar_query(query, values=None):
    db = funcionarios()
    cursor = db.cursor()
    try:
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)

        result = cursor.fetchall()

        db.commit()
        return result
    finally:
        cursor.close()
        db.close()


def cadastrar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    funcao = input("Digite a função do funcionário: ")
    departamento = input("Digite o departamento do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))

    query = "INSERT INTO funcionarios (nome, funcao, departamento, salario) VALUES (%s, %s, %s, %s)"
    values = (nome, funcao, departamento, salario)
    executar_query(query, values)
    print("Funcionário cadastrado com sucesso!")


def pesquisar_por_nome():
    nome = input("Digite o nome do funcionário para pesquisa: ")
    query = "SELECT * FROM funcionarios WHERE nome = %s"
    result = executar_query(query, (nome,))
    
    if result:
        print("Informações do funcionário:")
        for row in result:
            print(f"ID: {row[0]}, Nome: {row[1]}, Função: {row[2]}, Departamento: {row[3]}, Salário: {row[4]}")
    else:
        print("Nenhum funcionário encontrado.")


def listar_todos():
    query = "SELECT * FROM funcionarios;" 
    db = funcionarios()
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    
    
    if result:
        print("Lista de funcionários:")
        for row in result:
            print(f"ID: {row[0]}, Nome: {row[1]}, Função: {row[2]}, Departamento: {row[3]}, Salário: {row[4]}")
    else:
       print("Nenhum funcionário encontrado.")

def deletar_funcionario():
    id_funcionario = int(input("Digite o ID do funcionário a ser deletado: "))
    query = "DELETE FROM funcionarios WHERE id = %s"
    executar_query(query, (id_funcionario,))
    print("Funcionário deletado com sucesso!")

while True:
    print("\nEscolha uma opção:")
    print("1. Cadastrar novo funcionário")
    print("2. Pesquisar por nome")
    print("3. Listar todos os funcionários")
    print("4. Deletar funcionário")
    print("5. Encerrar o sistema")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        cadastrar_funcionario()
    elif opcao == "2":
        pesquisar_por_nome()
    elif opcao == "3":
        listar_todos()
    elif opcao == "4":
        deletar_funcionario()
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")