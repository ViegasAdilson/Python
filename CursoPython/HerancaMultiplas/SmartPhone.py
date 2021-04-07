from HerancaMultiplas.Eletronico import Electronico
from HerancaMultiplas.Log import LogMixing


class SmartPhone(Electronico, LogMixing):

    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False


    def conectar(self):
        if not self._ligado:
            info = f"{self._nome} nao esta ligado."
            print(info)
            self.log_inf(info)
            return
        if self._conectado:
            error = f"{self._nome} ja esta conectado."
            print(error)
            self.log_error(error)
            return
        info = f"{self._nome} esta conectado."
        self._conectado = True
        self.log_inf(info)
        print(info)

    def desconectar(self):
        if not self._conectado:
            error = f"{self._nome} Esta conectado"
            print(error)
            self.log_error(error)
            return

        info = f"{self._nome} foi desligado com sucesso"
        print(info)
        self._conectado = False
        self.log_inf(info)
