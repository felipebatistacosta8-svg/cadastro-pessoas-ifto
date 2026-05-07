# --- CLASSE MÃE (ABSTRATA) ---
class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def exibir_dados(self):
        return f"Nome: {self.nome} | CPF: {self.cpf}"


# --- CLASSES QUE HERDAM DE PESSOA ---

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, salario, funcao):
        super().__init__(nome, cpf)
        self.salario = salario
        self.funcao = funcao

    def exibir_dados(self):
        return f"[FUNCIONÁRIO] {super().exibir_dados()} | Função: {self.funcao} | Salário: R$ {self.salario:.2f}"


class Estudante(Pessoa):
    def __init__(self, nome, cpf, curso):
        super().__init__(nome, cpf)
        self.curso = curso

    def exibir_dados(self):
        return f"[ESTUDANTE] {super().exibir_dados()} | Curso: {self.curso}"


class Visitante(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)

    def exibir_dados(self):
        return f"[VISITANTE] {super().exibir_dados()} (Controle de Acesso)"


# --- SISTEMA PRINCIPAL (CADASTRO) ---

def sistema_ifto():
    # Lista para armazenar os cadastros (Simulando um banco de dados)
    banco_de_dados = []

    # Exemplo de inserção de dados
    p1 = Funcionario("Carlos Oliveira", "111.222.333-44", 4500.00, "Professor de TI")
    p2 = Funcionario("Maria Souza", "555.666.777-88", 3200.00, "Administrativo")
    e1 = Estudante("Lucas Pereira", "999.888.777-66", "Sistemas de Informação")
    v1 = Visitante("Roberto Alencar", "000.111.222-33")

    # Adicionando na lista
    banco_de_dados.append(p1)
    banco_de_dados.append(p2)
    banco_de_dados.append(e1)
    banco_de_dados.append(v1)

    print("-" * 30)
    print("CADASTRO DE PESSOAS - CAMPUS IFTO")
    print("-" * 30)

    # Polimorfismo: o mesmo método 'exibir_dados' funciona para todos
    for pessoa in banco_de_dados:
        print(pessoa.exibir_dados())

if __name__ == "__main__":
    sistema_ifto()