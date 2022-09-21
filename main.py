from funciones import Punto

if __name__=='__main__':
    punto = Punto()
    punto.setter(2, 3)
    A = punto.get()
    punto.setter(5, 5)
    B = punto.get()
    punto.setter(-3, -1)
    C = punto.get()
    punto.setter(0,0)
    D = punto.get()
    print('Los puntos son: ' + str(A) + ', ' + str(B) + ', ' + str(C) + ' y ' + str(D) )
    #punto.cuadrante()