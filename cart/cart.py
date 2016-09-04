from decimal import Decimal
from django.conf import settings
from tienda.models import Producto

class Cart(object):
    def __init__(self,request):
        """Inicializamos el carro de compras"""
        self.session = request.session
        self.cart = self.session.get(settings.CART_SESSIONS_ID)
        if not self.cart:
            #Guardar el carro vacio en la session
            self.cart =self.session[settings.CART_SESSIONS_ID] = {}

    def add(self, producto, quantity=1, update_quantity=False):
        """Agregamos un producto nuevo al carro o lo actualizamos"""
        producto_id = str(producto.id)
        if producto_id not in self.cart:
            self.cart[producto_id] = {
                'quantity':0,
                'precio':str(producto.precio)
            }
        if update_quantity:
            self.cart[producto_id]['quantity'] = quantity
        else:
            self.cart[producto_id]['quantity'] += quantity
        self.save()

    def save(self):
        #Actualizamos el carrito en la sessions
        self.session[settings.CART_SESSIONS_ID] = self.cart
        #marcamos la sesions como modificada para asegurarnos que si guardamos
        self.session.modified = True

    def remove(self, producto):
        """Eliminamos un producto del carrito"""
        producto_id = str(producto.id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()

    def __iter__(self):
        """iterar en los elementos del carrito y traer de la base de datos los productos"""
        producto_ids = self.cart.keys()
        #traer el producto y agregarlo
        productos = Producto.objects.filter(id__in=producto_ids)
        for producto in productos:
            self.cart[str(producto.id)]['producto'] = producto

        for item in self.cart.values():
            item['precio'] = Decimal(item['precio'])
            item['precio_total'] = item['precio'] * item['quantity']
            yield item

    def __len__(self):
        """cuanta todos los items en el carrito"""
        return sum(item['quantity'] for item in self.cart.values())
        """
        suma = 0
        for item in self.cart.values():
            suma = sum(item['quantity'])
        return suma
        """

    def get_precio_total(self):
        return sum(Decimal(item['precio']) * item['quantity'] for item in self.cart.values())

    def clear(sef):
        #borrar el carrito de la sesion de Usuario
        del self.session[settings.CART_SESSIONS_ID]
        self.session.modified = True
