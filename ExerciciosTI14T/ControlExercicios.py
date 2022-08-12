from modelExercicios import modelExercicios

class ControlExercicios:
    def __init__(self):
        self.opcao = -1
        self.modelo = modelExercicios() #Conectando com a classe model
        self.num1 = 0
        self.num2 = 0
        self.anos = 0
        self.meses = 0
        self.dias = 0
        self.eleitores = 0
        self.vbrancos = 0
        self.vnulos = 0
        self.vvalidos = 0
        self.salario = 0
        self.reajuste = 0

 #------------------------------------------------------------------------------------------------------------------------------
    def getOpcao(self):
            return self.opcao

    def getNum1(self):
        return self.num1

    def getNum2(self):
        return self.num2

    def getAnos(self):
        return self.anos

    def getMeses(self):
        return self.meses

    def getDias(self):
        return self.dias

    def getEleitores(self):
        return self.eleitores

    def getVbrancos(self):
        return self.vbrancos

    def getVnulos(self):
        return self.vnulos

    def getValidos(self):
        return self.vvalidos

    def getSalario(self):
        return self.salario

    def getReajuste(self):
        return self.reajuste
#----------------------------------------------------------------------------------------------------------------------------

    def setOpcao(self,opcao):
            self.opcao = opcao

    def setNum1(self, num1):
        self.num1 = num1

    def setNum2(self, num2):
        self.num2 = num2

    def setAnos(self, anos):
        self.anos = anos

    def setMeses(self, meses):
        self.meses = meses

    def setDias(self, dias):
        self.dias = dias

    def setEleitores(self, eleitores):
        self.eleitores = eleitores

    def setVbrancos(self, vbrancos):
        self.vbrancos = vbrancos

    def setVnulos(self, vnulos):
        self.vnulos = vnulos

    def setVvalidos(self, vvalidos):
        self.vvalidos = vvalidos


    def setSalario(self, salario):
        self.salario = salario

    def setReajuste(self, reajuste):
        self.reajuste =reajuste

 #---------------------------------------------------------------------------------------------------------------------

    def coletar1(self):
        print("Informe um número: ")
        self.setNum1(float(input()))

        print("Informe outro número: ")
        self.setNum2(float(input()))

    def coletar2(self):
        print("Informe um número: ")
        self.setNum1(float(input()))

    def coletar3(self):
        print("Informe a base: ")
        self.setNum1(float(input()))

        print("Informe a altura: ")
        self.setNum2(float(input()))

    def coletar4(self):

        print("Informe os anos: ")
        self.setAnos(float(input()))

        print("Informe os meses : ")
        self.setMeses(float(input()))

        print("Informe os dias : ")
        self.setDias(float(input()))

    def coletar5(self):

        print("Informe o total de eleitores : ")
        self.setEleitores(float(input()))

        print("Informe o total  votos brancos : ")
        self.setVbrancos(float(input()))

        print("Informe o total de votos nulos : ")
        self.setVnulos(float(input()))

        print("Informe o total de votos válidos : ")
        self.setVvalidos(float(input()))

    def coletar6(self):
        print("Informe o salário: ")
        self.setSalario(float(input()))

        print("Informe o reajuste: ")
        self.setReajuste(float(input()))





    def menu(self):
            print("\nEscolha uma das opções abaixo: " +
                  "\n0. Sair" +
                  "\n1. Exercício1" +
                  "\n2. Exercício2 " +
                  "\n3. Exercício3" +
                  "\n4. Exercício4" +
                  "\n5. Exercício5" +
                  "\n6. Exercício6" +
                  "\n7. Exercício7" +
                  "\n8. Exercício8" +
                  "\n9. Exercício9" )

            self.setOpcao(int(input()))  # Coletando a escolha do usuário

    def operacao(self):
        while (self.getOpcao != 0):
            self.menu()  # Mostrar a lista de dados na tela
            if self.getOpcao() == 0:
                print("Obrigado!")
                break
            elif self.getOpcao() == 1:
                self.coletar1()
                print(" A: {}  B: {} ".format(self.modelo.exercicio1(self.getNum1(), self.getNum2())))
            elif self.getOpcao() == 2:
                self.coletar2()
                print("O antecessor do número  é: {}".format(self.modelo.exercicio2(self.getNum1())))

            elif self.getOpcao() == 3:
                 self.coletar3()
                 print("A área é : {}".format(self.modelo.exercicio3(self.getNum1(), self.getNum2())))

            elif self.getOpcao() == 3:
                 self.coletar3()
                 print("A área é : {}".format(self.modelo.exercicio3(self.getNum1(), self.getNum2())))

            elif self.getOpcao() == 4:
                self.coletar4()
                print("O total de Dias é : {}".format(self.modelo.exercicio4(self.getAnos(), self.getMeses(), self.getDias())))

            elif self.getOpcao() == 5:
               self.coletar5()
               print("Porcentagem de votos brancos: {} % \nPorcentagem de votos nulos: {} %  \nPorcentagem de votos validos: {} %".format(self.modelo.exercicio5( self.getEleitores(),self.getVbrancos(), self.getVnulos(), self.getValidos())))


            elif self.getOpcao() == 6:
                 self.coletar6()
                 print("o novo sálario é : {}R$ ".format(self.modelo.exercicio6(self.getSalario(), self.getReajuste())))



