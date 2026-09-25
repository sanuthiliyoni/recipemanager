from Tasks.task1 import validate_recipe_inputs
from Tasks.task2 import *
from Tasks.task3 import *
from Tasks.task4 import *

def print_menu():
    """This is to print the main menu"""
    print("""
==========================
    Digtal Recipe Book
==========================
1. Add Recipe
2. View Menu
3. Search Recipes
4. Save to File
5. Load from File
6. Export Recipes
7. Manage Recipes
8. View Statistics
9. Exit
==========================""")

def main_menu():  
    program = True
    recipes = {}
    print("""\n=====================================
    WELCOME - DIGITAL RECIPE BOOK 
=====================================""")
    load_file(recipes) #load previous recipes

    while program == True:
        print_menu()
        
        choice = input("Enter choice (1 - 7): ")

        if choice == "1":
            a = True
            while a == True:
                recipe = validate_recipe_inputs()
                add_recipe(recipes, recipe)#add recipes to the dictionary
                a = False
                ask = input("\nAdd another recipe? (yes/no): ")
                if ask.lower() == "yes":
                    a = True

        elif choice == "2":
            display_recipes(recipes)
        elif choice == "3":
            search_recipe(recipes)
        elif choice == "4":
            save_file(recipes)
        elif choice == "5":
            load_file(recipes)
        elif choice == "6":
            export_recipe(recipes)
        elif choice == "7":
            manage_recipe(recipes)
        elif choice == "8":
            statistics(recipes)
        elif choice == "9":
            program = exit_menu(recipes) #ask to save and exit
            
main_menu()
