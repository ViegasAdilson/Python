from threading import Thread
from time import sleep
from threading import Lock


# class MeuThread(Thread):
#
#     def __init__(self, texto, tempo):
#         self.texto = texto
#         self.tempo= tempo
#
#         super().__init__()
#
#
#     def run(self):
#         sleep(self.tempo)
#         print(self.texto)
#
# t1 = MeuThread("Thread1", 5)
# t1.start()
# t2 = MeuThread("Thread2", 2)
# t2.start()
# t3 = MeuThread("Thread3", 1)
# t3.start()
# t4 = MeuThread("Thread4", 5)
# t4.start()
# for i in range(10):
#     print(i)
#     sleep(1)


# def vai_demorar(texto, tempo):
#     sleep(tempo)
#     print(texto)
#
# t = Thread(target=vai_demorar, args=("Ola Mundo!", 10))
# t.start()
# # t1 = Thread(target=vai_demorar, args=("Ola Mundo!", 1))
# # t1.start()
# # t2 = Thread(target=vai_demorar, args=("Ola Mundo!", 2))
# # t2.start()
# # for i in range(10):
# #     print(i)
# #     sleep(.5)
#
# while t.is_alive():
#     print("esperando a thread")
#     sleep(2)
# print("thread acabou")

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()


    def comprar(self, quantidade):
        self.lock.acquire()

        if self.estoque < quantidade:
            print("Nao temos ingresso suficiente.")
            self.lock.release()
            return
        sleep(1)
        self.estoque -=quantidade
        print(f"Voce comprou {quantidade} de ingresso(s) ainda temos {self.estoque} em estoque.")
        self.lock.release()



if __name__== "__main__":
    ingresso = Ingressos(10)

    threads = []
    for i in range(1, 20):
        t = Thread(target=ingresso.comprar, args=(i,))
        threads.append(t)

    for t in threads:
        t.start()

    executando = True

    while executando:
        executando = False

        for t in threads:
            if t.is_alive():
                executando = True
                break

    print(ingresso.estoque)