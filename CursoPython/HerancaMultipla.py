class A:
    def falar(self):
        print("Falando... Estou em A")


class B(A):
    def falar(self):
        print("Falando... Estou em B")


class C(A):
    def falar(self):
        print("Falando... Estou em C")


class D(B, C):# Herda de B primeiro so depois vai no C caso nao exista em B
    pass


d = D()
super.falar()