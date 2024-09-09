import random

# NOTE: cria a classe
class Pessoa:
    #os atributos são sempre definidos dentro do método constrtutor
    #NOTE: método construtor
    def __init__(self, nome, humor):
        self.nome = nome
        self.humor = humor

    def cumprimentar(self, nome1, nome2, humor):
        if humor:
            return f'Olá {nome1}, meu nome é {nome2}. Prazer em te conhecer!'
        else:
            return f'Vai se f... {nome2}'
        
    def resposta_cumprimentar(self, nome1, nome2, humor):
        if humor:
            return f'O prazer é meu, {nome2}'
        else:
            return f'Vai se lascar vc {nome1}'

            
if __name__ == '__main__':
    #entrada de dados
    humores = (True, False)
    nome1 = input('Informe o nome da primeira pessoa: ')
    nome2 = input('Informe o nome da segunda pessoa: ')

    #instanciando o objeto
    usuario1 = Pessoa(nome2, humores[random.randit(0,1)]) #soteia e adiciona o true e false
    usuario2 = Pessoa(nome1, humores[random.randit(0,1)])


    
    #saida de dados
    print(usuario1.cumprimentar(nome1,nome2 )
    print(usuario2.resposta_cumprimentar(nome1, nome2)                                                                       
    