@dajaxice_register
def additem(request, producto_nombre, producto_precio):
nuevoitem = Cart(item = producto_nombre, precio = producto_precio)
nuevoitem.save()
itemsstring = ''
itemslist = Cart.objects.all().order_by('item')
for i in itemslist:
itemsstring = itemsstring + '<p>' + i.item + ' Precio: ' + str(i.precio) + '</p>'
return json.dumps({'message': itemsstring})
@dajaxice_register
def search(request, param):
    bicis = Bici.objects.filter(Q(marca__icontains = param))
    libros = Libro.objects.filter(Q(titulo__icontains = param))
    canciones = Cancion.objects.filter(Q(titulo__icontains = param))
    context = {'bikes_founded' : bicis, 'libros_founded': libros, 'canciones_founded': canciones}
    return render(request, 'stock/found.html', context)
