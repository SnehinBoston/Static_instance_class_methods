from pizza import Pizza
a_pizza = Pizza(['cheese', 'tomatoes'])
print(a_pizza)
a_pizza.add_topping('garlic')
print(a_pizza)
a_pizza.remove_topping('cheese')
print(a_pizza)
print(Pizza(["mozzarella", "tomatoes"]))
print(Pizza(["mozzarella", "tomatoes", "ham", "mushrooms"]))
print(Pizza(["mozzarella" * 4]))
print(Pizza.margherita())
print(Pizza.prosciutto())
a_pizza = Pizza.prosciutto()
print(a_pizza)
a_pizza.add_topping("garlic")
print(a_pizza)
a_pizza = Pizza(["mozzarella", "tomatoes"])
print(a_pizza.get_size_in_inches("medium"))
print(Pizza.get_size_in_inches("small"))