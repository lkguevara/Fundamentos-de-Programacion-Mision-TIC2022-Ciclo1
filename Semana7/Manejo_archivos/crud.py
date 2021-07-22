import pandas as pd

def get_data_Frame():
    return pd.read_csv("io_pandas.csv")

def list_devs():
    print(get_data_Frame())

def edit_devs():
    list_devs()
    id= int(input('ID desarrollador a editar: '))
    print("""Menu
                1 - Editar cedula
                2 - Editar Nombre
                3 - Editar salario
                4 - Editar años""")
    option = input("Escriba su opcion: ")
    data = get_data_Frame()
    if option == '1':
        data.loc[id, 'cc'] = input('cédula')
    elif option == '2':
        data.loc[id, 'nombre'] = input('nombre')
    elif option == '3':
        data.loc[id, 'salario'] = input('salario')
    elif option == '4':
        data.loc[id, 'years'] = input('years')
    data.to_csv('io_pandas.csv', index=False)

def remove_devs():
    list_devs()
    id = int(input('ID desarrollador a eliminar: '))
    data = get_data_Frame()
    data.drop([id], inplace=True, axis=0)
    data.to_csv('io_pandas.csv', index=False)

def create_dev():
    cc =input('cedula: ')
    name=input('nombre: ')
    salary=input('salario: ')
    years=input('experiencia: ')
    file_r=open('io_pandas.csv','a')
    file_r.write(f'\n{cc},{name},{salary},{years}')
    file_r.close()

def show_menu():
    print("""Menu
            1 - Crear Dev
            2 - Listar Devs
            3 - Editar Devs
            4 - Eliminar Devs
            9 - Salir""")
    option=input("Escriba su opcion: ")
    if option == '1':
        create_dev()
    if option == '2':
        list_devs()
    if option == '3':
        edit_devs()
    if option == '4':
        remove_devs()
    elif option == '9':
        exit()

def run():
    show_menu() #muestra un menú
    run() #Ciclo infinito

if __name__ == '__main__': #Entry point
    run()