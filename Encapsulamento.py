class Retangulo:
    altura = 10 # atributo publico
    __largura = 15 # atributo Privado a classe Retangulo

    #Construtor da Classe Retangulo
    def __init__(self,altura,largura):
        self.altura = altura
        self.__largura = largura

    #Nas proximas linhas estamos criando os Getters e Setters para altura e largura
    def getLargura(self):
        return self.__largura

    def setLargura(self, largura):
        self.__largura = largura

    def getAltura(self):
        return self.altura

    def setAltura(self, altura):
        self.altura = altura

# Classe Encapsulamento, que servirá de exemplo como uma classe "estrangeira", que irá utilizar os atributos do Retangulo
class Encapsulamento:
    retangulo = Retangulo(42,50) # Criando um Objeto do tipo Retangulo.

    # Observe que é possivel chamar o atributo altura diretamente fora da Classe Retangulo nas proximas linhas
    retangulo.altura = 20
    print('Altura do Retangulo: {}'.format(retangulo.altura))

    # Utilização com Getter e Setter do atributo altura
    retangulo.setAltura(15)
    print('Altura do Retangulo: {}'.format(retangulo.getAltura()))


    # Não é possivel chamar um atributo privado (__largura) fora da sua classe e é necessario utilizar o seu Getter ou Setter
    # As Proximas linhas estão comentadas, especificamente por que elas não funcionam!

#    retangulo.__largura = 15
#    print('Largura do Retangulo: {}'.format(retangulo.__largura))

    # Utilização com Getter e Setter do atributo Largura
    retangulo.setLargura(40)
    print('Largura do Retangulo: {}'.format(retangulo.getLargura()))







