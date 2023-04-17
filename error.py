class Error():
    listaErrores = []

    def agregarError(self, error):
        self.listaErrores.append(error)

    def mostrarErrores(self):
        if(self.existenErrores()):
            for error in self.listaErrores:
                print(error)
            exit()

    def existenErrores(self):
        return len(self.listaErrores) != 0