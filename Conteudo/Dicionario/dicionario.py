#Dicionario
#Dicionário é uma coleção de pares chave-valor, onde cada chave é única e mapeada para um valor.
#Dicionários são mutáveis, ou seja, podem ser alterados após a criação.
pessoa = { "nome": "João", "idade": 30, "cidade": "São Paulo" }
pessoa = dict(nome="João", idade=30, cidade="São Paulo") #

pessoa["nome"] #acessando o valor da chave "nome"
pessoa["nome"] = "Maria" #alterando o valor da chave "nome"

contatos = {
    "genilson@gmail.com":{"nome": "Genilson", "telefone": "1234-5678"},
    "genilson1@gmail.com":{"nome": "Genilson1", "telefone": "1234-5679"},
    "genilson2@gmail.com":{"nome": "Genilson2", "telefone": "1234-5680"},
    "genilson3@gmail.com":{"nome": "Genilson3", "telefone": "1234-5681"},
}

contatos["genilson2@gmail.com"]["telefone"] #acessando o telefone do contato com o email "

for chave in contatos:
    print(chave) #imprimindo as chaves do dicionário

for chave, valor in contatos.items():#jeito mais certo de iterar sobre chaves e valores
    print(f"{chave}: {valor}") #imprimindo as chaves e valores do dicionário

dict.fromkeys(["nome", "telefone"])#cria um dicionário com as chaves especificadas e valores None
dict.fromkeys(["nome", "telefone"], "vazio")#cria um dicionário com as chaves especificadas e valor "vazio"

#tipo um try catch
contatos.get("chave") #None
contatos.get("chave", {}) #retorna o valor padrão {} se a chave não existir
contatos.get("genilson2@gmail.com", {}) #retorna o valor do contato com o email "

contatos.items() #retorna uma lista de tuplas com as chaves e valores do dicionário
contatos.keys() #retorna uma lista com as chaves do dicionário
contatos.pop("genilson2@gmail.com") #remove o contato com o email
contatos.popitem() #remove e retorna o último item adicionado ao dicionário
contatos.setdefault("nome","Junior") #se o atributo não existir, cria com o valor padrão None
contatos.values() #retorna uma lista com os valores do dicionário
contatos.update({"izabeli@gmail.com": {"nome": "Izabeli", "telefone": "1234-5682"}}) #adiciona ou atualiza o contato com o email
"genilson2@gmail.com" in contatos #verifica se o contato com o email existe no dicionário
del contatos["genilson1@gmail.com"] #remove o contato com o email
