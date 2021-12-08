agenda = [{'nombre':'Ian','telefono':3794355858},{'nombre':'Dana','telefono':3624101021},{'nombre':'China','telefono':3624158495},{'nombre':'Wanda','telefono':36244981561},{'nombre':'Hannah','telefono':3624123456}]

nombre = input('Ingrese un nombre a buscar en la agenda: ')
encontrado = False
for i in agenda:
    if nombre == i['nombre']:
        print(f'El telefono de {nombre} es:')
        print(i['telefono'])
        encontrado = True
if not encontrado:
    print(f'{nombre} no se encuentra en la agenda.')