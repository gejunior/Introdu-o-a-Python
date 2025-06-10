#em java ñ permite herança mutipla
from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto:#classe abstrata
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        return super().marca
    
class ControleTV(ControleRemoto):
    def ligar(self):
        print("ligando a TV")
    
    def desligar(self):
        print("desligando a TV")
    
    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("ligando o Ar") 
    
    def desligar(self):
        print("desligando o Ar")

    @property
    def marca(self):
        return "philco"

controle = ControleTV()
controle.ligar()
controle.desligar()

c2 = ControleArCondicionado()
c2.ligar()
c2.desligar()