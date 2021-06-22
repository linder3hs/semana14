# Tienda de computadoras
# componenetes_id, componenetes_nombre, componenetes_precio
import funciones

c_id = funciones.read_file('componentes_id.txt')
c_names = funciones.read_file('componentes_nombre.txt')
c_prices = funciones.read_file('componentes_precio.txt')

# convertir la lista de txt a [{}]
table_components_data = []
for i in range(len(c_id)):
    component_id = c_id[i].strip()
    name = c_names[i].strip()
    price = c_prices[i].strip()
    table_components_data = funciones.store_data_component(
        table_components_data,
        component_id,
        name,
        price
    )

funciones.print_table(table_components_data)

input_name = input("Name of component: ")
input_price = input("Price of component: ")

table_components_data = funciones.store_data_component(
    table_components_data,
    len(c_id) + 1,
    input_name,
    input_price
)

funciones.print_table(table_components_data)

input_i = input("Put the number of element do you wish delete: ")
table_components_data.pop(int(input_i))

funciones.print_table(table_components_data)
