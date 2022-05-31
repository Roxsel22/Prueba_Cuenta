class Cuenta:
  def __init__(self,titular,saldo=0):
     self.titular=titular
     self.saldo=saldo
  def mostrar(self):
        print('Nombre',self.titular, '$',self.saldo)
       
  def ingreso(self, cantidad):
       self.saldo+=cantidad
       print(self.saldo)
       
  def retiro(self,cantidad):
    self.saldo-=cantidad
    print(self.saldo)


cuenta_1=Cuenta('Roxana',35000)      
cuenta_1.mostrar()
cuenta_1.ingreso(7000)
cuenta_1.retiro(30000)