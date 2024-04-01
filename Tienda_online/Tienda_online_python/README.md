# tienda_online_python

Este proyecto consiste en la implementación de una clase en Python llamada TiendaOnline, que simula el funcionamiento de una tienda en línea. La clase cumple con una serie de requisitos específicos que se detallan a continuación.

## Instrucciones de Uso
Requisitos Previos
- Asegúrate de tener instalado Jupyter Notebook o algún otro entorno compatible con Python.
- Se requiere tener instalado Python en tu sistema. 

## Atributos de la clase
i- nventario: Una lista de diccionarios que almacena los productos en el inventario.
- clientes: Un diccionario que lleva un registro de los clientes de la tienda.
- ventas_totales: Un float para llevar un registro de las ventas totales de la tienda.

## Métodos
- agregar_producto(self, nombre, precio, cantidad): Agrega un producto al inventario o actualiza su cantidad si ya existe.
- ver_inventario(self): Muestra el inventario de productos con sus detalles.
- buscar_producto(self, nombre): Busca un producto en el inventario por nombre y muestra sus detalles si se encuentra.
- actualizar_stock(self, nombre, cantidad): Actualiza el stock de un producto en el inventario.
- eliminar_producto(self, nombre): Elimina un producto del inventario por nombre.
- calcular_valor_inventario(self): Calcula y muestra el valor total del inventario.
- buscar_producto_regex(self, patron): Busca productos en el inventario que coincidan con un patrón de búsqueda en formato regex en - el nombre y muestra los resultados.
- realizar_compra(self): Permite a un cliente realizar una compra seleccionando productos del inventario.
- procesar_pago(self): Procesa el pago de una compra, calcula el cambio y muestra un mensaje de confirmación.
- agregar_cliente(self, nombre, email): Agrega un nuevo cliente al registro de clientes.
- ver_clientes(self): Muestra la lista de clientes registrados con sus nombres y correos electrónicos.
- registrar_compra(self, nombre_cliente, carrito): Registra una compra para un cliente, actualiza las ventas totales y agrega la   compra al historial del cliente.
- ver_compras_cliente(self, nombre_cliente): Muestra el historial de compras de un cliente.
- calcular_ventas_totales(self): Muestra las ventas totales de la tienda.

## Autor

Este proyecto fue realizado por Ana González Gutiérrez
Linkedin:  www.linkedin.com/in/ana-gonzález-121979185