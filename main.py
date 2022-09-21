from funciones import Punto

if __name__=='__main__':
    punto = Punto()
    punto.setter(2, 3)
    A1, A2 = punto.get()
    A = (A1, A2)
    punto.setter(5, 5)
    B1, B2 = punto.get()
    B = (B1, B2)
    punto.setter(-3, -1)
    C1, C2= punto.get()
    C = (C1, C2)
    punto.setter(0,0)
    D1, D2 = punto.get()
    D = (D1, D2)
    print('Los puntos son: ' + str(A) + ', ' + str(B) + ', ' + str(C) + ' y ' + str(D) )
    print('Cuadrantes de:')
    print('A')
    punto.setter(2, 3)
    punto.cuadrante()
    print('C')
    punto.setter(-3, -1)
    print('D')
    punto.setter(0,0)
    
    
    