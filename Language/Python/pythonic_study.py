# 1 - p03~05
def apply_discount(product, discount):  
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price

def test1():
    shoes = {'name': 'Fancy Shoes', 'price': 14900}
    print apply_discount(shoes, 0.25)
    
    # print apply_discount(shoes, 2.0)
    # print apply_discount(shoes, -0.3)

def delete_product(product_id, user):
    if not user.is_admin():
        raise AuthError('Must have ~')

# 1 - p10~
# Context Manageer
class ManagedFile:
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

from contextlib import contextmanager
@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()

class Indenter:
    def __init__(self):
        self.level = 0
    
    def __enter__(self):
        self.level += 1
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print('    ' * self.level + text)

def test2():
    with open('hello.txt', 'w') as f:
        f.write('hello, world!')

    with ManagedFile('hello.txt') as f:
        f.write('hello, world!')

    with managed_file('hello.txt') as f:
        f.write('hello, world!')

    with Indenter() as intent:
        indent.print('hi!')
        with indent:
            indent.print('hello')
            with indent:
                indent.print('bonjiur')
        indent.print('hey')


if __name__ == "__main__":
    # test1()



