import unittest
from src.carte_pizzeria import CartePizzeria
from src.pizza import Pizza


class TestCartePizzeria(unittest.TestCase):
    def test_carte_vide(self):
        carte_pizerria = CartePizzeria([])

        self.assertTrue(carte_pizerria.is_empty())

    def test_nombre_pizzas(self):
        pizza1 = Pizza("margarita", ["sauce tomate", "mozarella"], 10)
        pizza2 = Pizza("reine", ["sauce tomate", "mozarella", "olive", "jambon"], 10)
        pizza3 = Pizza("carnivore", ["sauce tomate", "mozarella", "boeuf haché", "jambon"], 10)
        carte_pizerria = CartePizzeria([pizza1, pizza2, pizza3])

        self.assertEqual(carte_pizerria.nb_pizzas(), 3)

    def test_ajout_pizza(self):
        carte_pizerria = CartePizzeria([])
        pizza = Pizza("margarita", ["sauce tomate", "mozarella"], 10)
        carte_pizerria.add_pizza(pizza)

        self.assertEqual(carte_pizerria.nb_pizzas(), 1)

    def test_remove_pizzas(self):
        pizza1 = Pizza("margarita", ["sauce tomate", "mozarella"], 10)
        pizza2 = Pizza("reine", ["sauce tomate", "mozarella", "olive", "jambon"], 10)
        pizza3 = Pizza("carnivore", ["sauce tomate", "mozarella", "boeuf haché", "jambon"], 10)
        carte_pizerria = CartePizzeria([pizza1, pizza2, pizza3])
        carte_pizerria.remove_pizza("reine")

        self.assertEqual(carte_pizerria.nb_pizzas(), 2)


if __name__ == "__main__":
    unittest.main()
