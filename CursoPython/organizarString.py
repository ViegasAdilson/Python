string = "012345678901234567890123456789"
n = 10
nova_lista = [string[i: i+n] for i in range(0,len(string), n)]
retorno = ".".join(nova_lista)
print(nova_lista)
print(retorno)

