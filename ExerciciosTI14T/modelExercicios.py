class modelExercicios:
    #Criar um método construtor
    def __init__(self):
        pass

    def exercicio1 (self, A, B, C):
        C = A
        A = B
        B = C
        return "A :" + A +"\nB :" + B

    def exercicio2 (self, num):
        return num - 1

    def exercicio3 (self, base, altura):
        return base * altura

    def exercicio4 (self, anos, meses, dias):
        return anos * 365 + meses * 30 + dias

    def exercicio5 (self,validos, nulo, branco, eleitores):

            branco = branco / eleitores * 100
            nulo = nulo / eleitores * 100
            validos = validos / eleitores * 100


            return  branco, nulo, validos

    def exercicio6 (self, salario , preajuste):
           return salario * preajuste /10


    def exercicio7(self, imposto, custodefabrica, pdistribuidor):
         return custodefabrica * imposto /100 + custodefabrica * pdistribuidor/100 + custodefabrica


    def exercicio8 (self, nota1, nota2, nota3):
        return nota1 + nota2 + nota3 / 3

    def exercicio9 (self, maca):
        return maca * 1.30

    def exercicio91 (self, maca):
        return maca * 1






