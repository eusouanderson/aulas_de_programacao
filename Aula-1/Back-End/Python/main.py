# # Introdução ao Python

# Exemplo: Hello World
# Este código imprime a mensagem "Hello, World!" na tela.
print("Hello, World!")


# # Tipos de Dados

# Números
# Aqui, estamos declarando diferentes tipos numéricos.
x = 5         # inteiro
y = 3.14      # float
z = 1 + 2j    # número complexo

# Strings
# Neste exemplo, declaramos uma string.
name = "Python"

# Booleanos
# Variável que armazena um valor booleano (verdadeiro ou falso).
is_active = True

# Imprimindo os tipos de dados das variáveis
print(type(x), type(y), type(name), type(is_active))


# # Estruturas de Controle

# Condicional: verificando a idade
age = 20
if age < 18:
    print("Menor de idade")
elif age < 65:
    print("Adulto")
else:
    print("Idoso")


# Laços: executando um bloco de código várias vezes

# Laço for
# Este laço itera de 0 a 4 e imprime cada número.
for i in range(5):
    print(i)

# Laço while
# Aqui, usamos um laço while para imprimir números de 0 a 4.
count = 0
while count < 5:
    print(count)
    count += 1  # Incrementa count em 1


# # Funções

# Definindo uma função que cumprimenta uma pessoa pelo nome
def greet(name):
    return f"Hello, {name}!"

# Chamando a função greet com o nome "Alice"
print(greet("Alice"))


# # Estruturas de Dados

# Trabalhando com listas
# Aqui, estamos criando uma lista de frutas e adicionando uma nova fruta.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Adiciona "orange" à lista
print(fruits)


# Trabalhando com dicionários
# Um dicionário armazena pares chave-valor.
student = {
    "name": "John",
    "age": 25,
    "courses": ["Math", "Science"]
}

# Acessando valores do dicionário
print(student["name"])         # Imprime o nome do estudante
print(student.get("courses"))  # Imprime as disciplinas do estudante


# # Módulos e Pacotes

# Importando o módulo math para usar funções matemáticas
import math

# Usando a função sqrt para calcular a raiz quadrada
print(math.sqrt(16))  # Raiz quadrada de 16
print(math.pi)         # Valor de pi


# # Manipulação de Arquivos

# Escrevendo em um arquivo
# Este bloco cria um arquivo e escreve "Hello, World!" nele.
with open('example.txt', 'w') as f:
    f.write("Hello, World!\n")

# Lendo de um arquivo
# Aqui, estamos lendo o conteúdo do arquivo que acabamos de criar.
with open('example.txt', 'r') as f:
    content = f.read()
    print(content)


# # Tratamento de Exceções

# Exemplo de como tratar uma exceção
try:
    result = 10 / 0  # Tenta dividir por zero
except ZeroDivisionError:
    print("Você não pode dividir por zero!")  # Mensagem de erro
finally:
    print("Execução concluída.")  # Este bloco é executado sempre


# # Programação Orientada a Objetos

# Definindo uma classe Dog (Cachorro)
class Dog:
    def __init__(self, name):
        self.name = name  # Inicializa o nome do cachorro
    
    def bark(self):
        return "Woof!"  # Método que faz o cachorro "latir"

# Criando uma instância da classe Dog
my_dog = Dog("Buddy")
print(my_dog.name)  # Imprime o nome do cachorro
print(my_dog.bark())  # Faz o cachorro "latir"


# # Usando Bibliotecas Externas

# Importando a biblioteca requests para fazer requisições HTTP
import requests

# Fazendo uma requisição GET para a API do GitHub
response = requests.get('https://api.github.com')
print(response.status_code)  # Imprime o código de status da resposta
print(response.json())       # Imprime o conteúdo JSON da resposta
