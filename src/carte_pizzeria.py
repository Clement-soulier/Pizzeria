from carte_pizzeria_exception import CartePizzeriaException


class CartePizzeria:
    def __init__(self, pizzas):
        self.pizzas = pizzas

    def is_empty(self):
        if (len(self.pizzas) == 0):
            return True
        else:
            return False

    def nb_pizzas(self):
        return len(self.pizzas)

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def remove_pizza(self, name):
        for pizza in self.pizzas:
            if pizza.name == name:
                self.pizzas.remove(pizza)
                return
        raise CartePizzeriaException
