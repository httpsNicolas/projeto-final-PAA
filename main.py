import csv
from Vehicle import Vehicle

products = []

with open('Produtos/produtos2.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        products.append(row)


def greedy_dispatch(products, dia=1):

    VEHICLE_DISPONIBLE = [
        Vehicle('Carro', 10),
        Vehicle('Caminhão', 25),
        Vehicle('Carreta', 40)
    ]

    products = sorted(products, key=lambda x: (float(x['dispatch_date']), float(x['size'])))
    product_rest = []

    print("Dia", dia)

    for v in VEHICLE_DISPONIBLE:
        for p in list(products):
            if v.can_transport(p):
                v.add_product(p)
                products.remove(p)
            else:
                product_rest.append(p)
        ids = [p['id'] for p in v.loaded_products]
        print("Veículo", v.vtype, "com produtos:", ids)
    
    product_rest = products

    if product_rest:
        greedy_dispatch(product_rest, dia=dia + 1)
    else:
        print("Todos os produtos foram despachados.")

greedy_dispatch(products)