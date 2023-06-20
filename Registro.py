class Registro:
    def __init__ (self, nroRegistro, tipoNormativa, nroNormativa, fecha, descripcion, categoria, jurisdiccion, organoLegislativo, palabrasClaves):
        self.nroRegistro = nroRegistro
        self.tipoNormativa = tipoNormativa
        self.nroNormativa = nroNormativa
        self.fecha = fecha
        self.descripcion = descripcion
        self.categoria = categoria
        self.jurisdiccion = jurisdiccion
        self.organoLegislativo = organoLegislativo
        self.palabrasClaves = palabrasClaves

    def imprimir(self):
        pares = []
        pares.append(('nroRegistro', self.nroRegistro))
        pares.append(('tipoNormativa', self.tipoNormativa))
        pares.append(('nroNormativa', self.nroNormativa))
        pares.append(('fecha', self.fecha))
        pares.append(('descripcion', self.descripcion))
        pares.append(('categoría', self.categoria))
        pares.append(('jurisdiccion', self.jurisdiccion))
        pares.append(('organoLegislativo', self.organoLegislativo))
        pares.append(('palabrasClave', self.palabrasClaves))
        return pares
