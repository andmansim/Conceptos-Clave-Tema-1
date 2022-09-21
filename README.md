# Conceptos-Clave-Tema-1
Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/andmansim/Conceptos-Clave-Tema-1.git)

En este ejercicio he realizado una clase Punto, donde nos crea unos puntos mediante dos coordenadas. También hemos indicado el cuadrante, la distancia y los vectores de algunos puntos.

# Main
'''
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
    punto.setter(A1, A2)
    d3 = round(punto.distancia(D1, D2), 2)
    punto.cuadrante()
    print('C')
    punto.setter(C1, C2)
    d4 = round(punto.distancia(D1, D2), 2)
    punto.cuadrante()
    print('D')
    punto.setter(D1,D2)
    punto.cuadrante()
    
    print('El vector AB')
    punto.setter(A1, A2)
    vector1 = punto.vector(B1, B2)
    d = round(punto.distancia(B1, B2), 2)
    print(vector1)
    
    print('El vector BA')
    punto.setter(B1, B2)
    vector = punto.vector(A1, A2)
    d1 = round(punto.distancia(A1, A2), 2)
    print(vector)
    
    punto.setter(5, 5)
    d5 = round(punto.distancia(D1, D2), 2)
    
    print('La distancia de A a B es: ' + str(d))
    print('La distancia de B a A es: ' + str(d1))
    
    print(d3, d4, d5)
    lista = [d3, d4, d5]
    for i in range(len(lista)):
        if lista[i-1] > lista[i]:
            lista[i-1], lista[i] = lista[i], lista[i-1]
    print('La mayor distancia es ' + str(lista[-1]))
    print('El punto con mayor distancia es el B ' )
    
'''

# Clases

'''
import math

class Punto:
    def __init__(self):
        self.x = 0
        self.y = 0
       
    def get(self):
        return self.x, self.y
    def setter(self, x, y):
        self.x = x
        self.y = y
        
    def cuadrante(self):
        if self.x and self.y == 0:
            print('El punto está en el origen de coordenadas')
        elif self.x > 0:
            if self.y > 0:
                print('El punto está en el primer cuadrante')
            elif self.y < 0:
                print('El punto está en el cuarto cuadrante')
            else:
                print('El punto está sobre el eje X')
        elif self.x < 0:
            if self.y > 0:
                print('El punto está en el segundo cuadrante')
            elif self.y < 0:
                print('El punto está en el tercer cuadrante')
            else:
                print('El punto está sobre el eje X')
        elif self.y != 0 and self.x == 0:
            print('Estamos sobre el eje y')
        
    
    def vector(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
        v = (self.x - self.x1, self.y - self.y1)
        return v
        
    
    def distancia(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
        v1 = ((self.x - self.x1)**2 + (self.y - self.y1)**2)
        return math.sqrt(v1)
    

class Ractangulo(Punto):
    def __init__(self):
        Punto.__init__(self)
        
'''
