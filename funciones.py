# mis funciones
from tabulate import tabulate


def read_file(filename):
    my_file = open(filename)
    return my_file.readlines()


def store_data_component(data, c_id, name, price):
    data.append({
        "Id": c_id,
        "Name": name,
        "Price": price
    })
    return data


def print_table(data):
    print(tabulate(data, headers="keys", tablefmt="grid"))
