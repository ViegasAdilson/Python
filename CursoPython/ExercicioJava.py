frase = "O meu nome é adilson viegas".lower()

for l in frase:
    conta = frase.count(l)
    print("{} {} ".format(l,conta*"*"))

