from src.carte_pizzeria_exception import CartePizzeriaException
from src.pizza import Pizza
from src.dessert import Dessert


class CartePizzeria:
    def __init__(self, elements):
        if elements:
            self.elements = elements
        else:
            self.elements = []

    def is_empty(self):
        if (len(self.elements) == 0):
            return True
        else:
            return False

    def nb_drinks(self):
        count = 0
        for element in self.elements:
            if (isinstance(element, Pizza)):
                count += 1
        return count

    def nb_desserts(self):
        count = 0
        for element in self.elements:
            if (isinstance(element, Dessert)):
                count += 1
        return count

    def nb_elements(self):
        return len(self.elements)

    def add(self, element):
        for i in range(len(self.elements)):
            if (self.elements[i].name == element.name):
                raise CartePizzeriaException
            if (self.elements[i].base == element.base and element.ingredients == self.elements):
                raise CartePizzeriaException
        else:
            self.elements.append(element)

    def remove(self, name):
        for element in self.elements:
            if element.name == name:
                self.elements.remove(element)
                return
        raise CartePizzeriaException
