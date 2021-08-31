class Animal:
    def __init__(self):
        pass
    
    def som(self):
        pass
    
class Gato(Animal):
    def __init__(self):
      pass

    def som(self):
      return "miau"

class Cachorro(Animal):
  def __init__(self):
        pass

  def som(self):
      return "auau"

ccachorro = 1
gato = 2
hist = []

choice = input('selecione 1 ou 2:')
while(choice != "-1"):
  if (choice == "1"):
     doguinho = Cachorro()
     hist.append("1 auau")
     print(doguinho.som())
  elif (choice == "2"):
    gatinho = Gato()
    hist.append("2 miau")
    print(gatinho.som())
  else:
    print("historico: ", hist)

  choice = input('selecione 1 ou 2:')
