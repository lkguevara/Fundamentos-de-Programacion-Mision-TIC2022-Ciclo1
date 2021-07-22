import easygui as eg
import classes as cl
# eg.msgbox('Hola')

biblioteca = cl.Biblioteca('Alejandria')


def menu():
    msg= "Menu Biblioteca" #Mensaje de inicio
    title= f'Biblioteca {biblioteca.nombre}' #Nombre principal de la interfaz
    choices2= ['Agregar salas', 'Listar salas'] #Opciones de menu
    option= eg.buttonbox(msg, title, choices=choices2) 
    if option == None:
        eg.msgbox('Gracias, vuelva pronto') #Cuando uno le de en X
    elif option == choices2[0]:
        add_room() #función para agregar las salas
    elif option == choices2[1]:
        list_room() #Funcion para listar salas

def menu_room(index):
    msg='Menu sala'
    title=f'Biblioteca {biblioteca.nombre}-> sala {biblioteca.rooms[index].nombre}'
    choices=['Agregar libro', 'Listar libro']
    option= eg.buttonbox(msg,title,choices)


def add_room():
    msg = 'Agregar sala'
    title = f'Biblioteca {biblioteca.nombre} -> Agregar sala'
    field_names =['Nombre', 'Capacidad']
    field_values =[]
    field_values = eg.multenterbox(msg, title, field_names)
    #print(field_values)
    if field_values == None:
        menu()
    elif field_values[0] == '' or field_values[1] == '':
        eg.msgbox('Debe llenar los campos')
        add_room
    else:
        biblioteca.add_room(field_values[0], field_values[1])
        menu() 


def list_room():
    msg= 'Listado de salas'
    title = f'Biblioteca {biblioteca.nombre}-> Salas'
    choices = biblioteca.show_rooms()
    option=eg.indexbox(msg, title, choices=choices)
    if option == None:
        menu()
    else:
        menu_room(option)

def run():
    menu()

if __name__ == '__main__':
    run()