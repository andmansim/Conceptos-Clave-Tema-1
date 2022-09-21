class Punto:
    def __init__(self):
        self.x = 0
        self.y = 0
       
    def get(self):
        return self.x and self.y
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
        print('El vector es' + str(v)) 
    
    def distancia(self):
        pass