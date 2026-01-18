class Vehicle:
    def __init__(self, vtype, capacity):
        self.vtype = vtype
        self.capacity = capacity
        self.loaded_products = []

    def remain_capacity(self):
        return self.capacity - sum(float(p['size']) for p in self.loaded_products)
    
    def can_transport(self, product):
        return float(product['size']) <= self.capacity
    
    def add_product(self, product):
        self.loaded_products.append(product)
        self.capacity -= float(product['size'])