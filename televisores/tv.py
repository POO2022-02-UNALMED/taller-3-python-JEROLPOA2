class TV:

    numTV = 0

    def __init__(self, marca, estado):

        self.marca = marca
        self.estado = estado
        self.control = None
        self.canal = 1
        self.volumen = 1
        self.precio = 500
        TV.numTV += 1
    
    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca

    def setControl(self, control):
        self.control = control
    
    def getControl(self):
        return self.control

    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca

    def setPrecio(self, precio):
        self.precio = precio
    
    def getPrecio(self):
        return self.precio
    
    def setNumTV(numTV):
        TV.numTV = numTV
    
    def getNumTV():
        return TV.numTV

    def setVolumen(self, volumen):
        if volumen <= 7 and volumen >= 0 and self.estado == True:
            self.volumen = volumen
        else:
            pass
    
    def getVolumen(self):
        return self.volumen

    def setCanal(self, canal):
        if canal <= 120 and canal >= 0 and self.estado == True:
            self.canal = canal
        else:
            pass
    
    def getCanal(self):
        return self.canal
    
    def volumenUp(self):
        if self.volumen < 7 and self.volumen > 0 and self.estado == True:
            self.volumen += 1
        else:
            pass
    
    def volumenDown(self):
        if self.volumen < 7 and self.volumen > 0 and self.estado == True:
            self.volumen -= 1
        else:
            pass
    
    def canalUp(self):
        if self.canal < 120 and self.canal > 0 and self.estado == True:
            self.canal += 1
        else:
            pass

    def canalDown(self):
        if self.canal < 120 and self.canal > 0 and self.estado == True:
            self.canal -= 1
        else:
            pass
    
    def turnOn(self):
        self.estado = True
    
    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado

    
    
