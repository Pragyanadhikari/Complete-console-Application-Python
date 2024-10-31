# 8. Recipe Manager
# • Description: Build a console-based recipe management application. Implement classes for Recipe, Ingredient, and Category. Include features for adding, searching, and managing recipes and ingredients.

# • OOP Concepts: Composition (recipes consist of ingredients), Inheritance (recipe categories), and Encapsulation (managing recipe details).

from abc import ABC, abstractmethod

class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.name}"
class Category(ABC):
    @abstractmethod
    def get_category_name(self):
        pass
class MainCourse(Category):
    def get_category_name(self):
        return "Main Course"
class Dessert(Category):
    def get_category_name(self):
        return "Dessert"
class Recipe:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.ingredients = []
        self.instructions = ""
    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
    def set_instructions(self, instructions):
        self.instructions = instructions
    def show_recipe(self):
        print(f"Recipe: {self.name}")
        print(f"Category: {self.category.get_category_name()}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        print("Instructions:")
        print(self.instructions)

class RecipeManager:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self, recipe):
        self.recipes[recipe.name] = recipe

    def search_recipe(self, name):
        if name in self.recipes:
            self.recipes[name].show_recipe()
        else:
            print(f"Recipe '{name}' not found.")

    def show_all_recipes(self):
        print("All Recipes:")
        for recipe in self.recipes.values():
            print(f"- {recipe.name}")

r=RecipeManager()
dessert=Dessert()
main_course=MainCourse()

ingredient1=Ingredient("Milk",1,"cup")
ingredient2=Ingredient("Sugar",1,"spoon")
ingredient3=Ingredient("Tea Leaves",1,"spoon")
tea_recipe=Recipe("Tea",dessert)
tea_recipe.add_ingredient(ingredient1)
tea_recipe.add_ingredient(ingredient2)
tea_recipe.add_ingredient(ingredient3)
tea_recipe.set_instructions("Boil milk then add sugar and tea leaves then serve when color changes to Orange/Yellow type.")

pulau_recipe=Recipe("Pulau",main_course)
ingredient4=Ingredient("Rice Grain",2,"cup")
ingredient5=Ingredient("Ghee",2,"spoon")
pulau_recipe.add_ingredient(ingredient4)
pulau_recipe.add_ingredient(ingredient5)
pulau_recipe.set_instructions("Properly wash rice grain and then put water 2cups and then ghee and then leave it to cook.")
r.add_recipe(tea_recipe)
r.add_recipe(pulau_recipe)
r.show_all_recipes()

r.search_recipe("Curd Rice")