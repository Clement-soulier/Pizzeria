import unittest
from src.carte_pizzeria import CartePizzeria
from src.pizza import Pizza
from src.boisson import Boisson
from src.dessert import Dessert


class TestCartePizzeria(unittest.TestCase):
    def test_carte_vide(self):
        carte_pizerria = CartePizzeria([])

        self.assertTrue(carte_pizerria.is_empty())

    def test_nombre_elements(self):
        pizza1 = Pizza("margarita", 10, "", ["sauce tomate", "mozarella"], "tomate")
        pizza2 = Pizza("reine", 15, "", ["sauce tomate", "mozarella", "olive", "jambon"], "tomate")
        pizza3 = Pizza("carnivore", 15, "", ["sauce tomate", "mozarella", "boeuf haché", "jambon"], "tomate")
        carte_pizerria = CartePizzeria([pizza1, pizza2, pizza3])

        self.assertEqual(carte_pizerria.nb_elements(), 3)

    def test_nb_drink(self):
        pizza = Pizza("margarita", 10, "", ["sauce tomate", "mozarella"], "tomate")
        dessert = Dessert("gateau chocolat", 8, ["chocolat", "farine", "oeuf"], True)
        boisson = Boisson("jus d'orange", 3, ["jus"], False)
        carte_pizzeria = CartePizzeria([pizza, dessert, boisson])

        self.assertEqual(carte_pizzeria.nb_drinks(), 1)

    def test_nb_dessert(self):
        pizza = Pizza("margarita", 10, "", ["sauce tomate", "mozarella"], "tomate")
        dessert = Dessert("gateau chocolat", 8, ["chocolat", "farine", "oeuf"], True)
        boisson = Boisson("jus d'orange", 3, ["jus"], False)
        carte_pizzeria = CartePizzeria([pizza, dessert, boisson])

        self.assertEqual(carte_pizzeria.nb_desserts(), 1)

    def test_nb_pizza(self):
        pizza = Pizza("margarita", 10, "", ["sauce tomate", "mozarella"], "tomate")
        dessert = Dessert("gateau chocolat", 8, ["chocolat", "farine", "oeuf"], True)
        boisson = Boisson("jus d'orange", 3, ["jus"], False)
        carte_pizzeria = CartePizzeria([pizza, dessert, boisson])

        self.assertEqual(carte_pizzeria.nb_pizza(), 1)

    def test_ajout_element(self):
        carte_pizerria = CartePizzeria([])
        pizza = Pizza("margarita", 10, "", ["sauce tomate", "mozarella"], "tomate")
        carte_pizerria.add(pizza)

        self.assertEqual(carte_pizerria.nb_elements(), 1)

    def test_remove_pizzas(self):
        pizza1 = Pizza("margarita", 10, "", ["sauce tomate", "mozarella"], "tomate")
        pizza2 = Pizza("reine", 15, "", ["sauce tomate", "mozarella", "olive", "jambon"], "tomate")
        pizza3 = Pizza("carnivore", 15, "", ["sauce tomate", "mozarella", "boeuf haché", "jambon"], "tomate")
        carte_pizerria = CartePizzeria([pizza1, pizza2, pizza3])
        carte_pizerria.remove("reine")

        self.assertEqual(carte_pizerria.nb_elements(), 2)


if __name__ == "__main__":
    unittest.main()
