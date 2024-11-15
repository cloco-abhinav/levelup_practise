class Pizza:
    def __init__(self):
        self.crust = None
        self.size = None
        self.toppings = []
        self.sauce = None

    def __str__(self):
        return f"Pizza [Crust: {self.crust}, Size: {self.size}, Toppings: {', '.join(self.toppings)}, Sauce: {self.sauce}]"


class PizzaBuilder:
    def set_crust(self, crust: str):
        raise NotImplementedError

    def set_size(self, size: str):
        raise NotImplementedError

    def add_topping(self, topping: str):
        raise NotImplementedError

    def set_sauce(self, sauce: str):
        raise NotImplementedError

    def build(self):
        raise NotImplementedError


class CustomPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def set_crust(self, crust: str):
        self.pizza.crust = crust

    def set_size(self, size: str):
        self.pizza.size = size

    def add_topping(self, topping: str):
        self.pizza.toppings.append(topping)

    def set_sauce(self, sauce: str):
        self.pizza.sauce = sauce

    def build(self):
        return self.pizza


class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def make_margherita_pizza(self):
        self.builder.set_crust("Thin")
        self.builder.set_size("Medium")
        self.builder.add_topping("Mozzarella")
        self.builder.set_sauce("Tomato")

    def make_pepperoni_pizza(self):
        self.builder.set_crust("Thick")
        self.builder.set_size("Large")
        self.builder.add_topping("Mozzarella")
        self.builder.add_topping("Pepperoni")
        self.builder.set_sauce("Tomato")


def client_code():
    builder = CustomPizzaBuilder()

    director = PizzaDirector(builder)
    director.make_margherita_pizza()
    pizza1 = builder.build()
    print(f"Pizza 1: {pizza1}")

    director.make_pepperoni_pizza()
    pizza2 = builder.build()
    print(f"Pizza 2: {pizza2}")


client_code()
