#estética
#identar código é uma forma de manter o código organizado, legível e manutenível.
#mas python ela exerce um segundo papel, através da indentação o interpretador consegue determinar
#onde um bloco de código começa e termina, ou seja, a indentação é obrigatória
# e não opcional como em outras linguagens de programação.

#Bloco de comando
# -> para definir o início e o fim de um bloco de código, em outras linguagens
# utilizamos chaves ({}) ou palavras-chave como "begin" e "end".
# -> em Python, a indentação é usada para definir blocos de código.
# Exemplo de uso de indentação


# Indentação e blocos de código
# A indentação é importante em Python, pois define blocos de código.
# Em Python, a indentação é obrigatória e define o escopo dos blocos de código.
# Exemplo de uso de indentação

def sacar(self, valor : float) -> None:
    if self.saldo >= valor:
        self.saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
    #fim do bloco if
    else:
        print("Saldo insuficiente para realizar o saque.")
    #fim do bloco else
#fim do bloco da função sacar

#em Java:
#void sacar(double valor) {
#    if(this.saldo >= valor) {
#        this.saldo -= valor;
#        System.out.println("Saque de R$" + valor + " realizado com sucesso.");
#    } else {
#        System.out.println("Saldo insuficiente para realizar o saque.");
#    }
#}