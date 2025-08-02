class Carro:
    def __init__(self, request):
        self.request = request

        self.session = request.session

        # Busco el carro de la sesión
        carro = self.session.get("carro")

        if not carro:
            self.carro = self.session["carro"] = {}
        else:
            self.carro = carro
    
    def agregarProductos(self, producto):
        producto_id = str(producto.id)

        if producto_id not in self.carro:
            self.carro[producto_id] = {
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.url.url
            }
        else:
            self.carro[producto_id]["cantidad"] += 1
        self.guardar()
    
    def eliminarProducto(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro:
            del self.carro[producto_id]
            self.guardar()
            return 0
        return None

    def quitarProducto(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro:
            self.carro[producto_id]["cantidad"] -= 1
            if self.carro[producto_id]["cantidad"] <= 0:
                del self.carro[producto_id]
            self.guardar()
            return 0
        return 1
    
    def vaciar(self):
        self.carro = {}
        self.guardar()
        
    def guardar(self):
        self.session["carro"] = self.carro 
        self.session.modified = True