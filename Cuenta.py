class cuenta:
  def __init__(self,titular,saldo=0):
     self.titular=titular
     self.saldo=saldo
     def mostrar(self,titutar,saldo):
        print('Nombre',titular, '$',saldo)
     def ingreso(self,num_1):
       self.saldo+=num_1
       print(saldo+num_1)
     def retiro(self,num_2):
       self.saldo-=num_2
       if num_2<saldo:
         print(saldo-num_2)
       else:
         print('imposible realizar la accion')





         

cuenta_1=cuenta('Roxana',35000)       
cuenta.mostrar()
cuenta.ingresar(7000)
cuenta.retirar(30000)