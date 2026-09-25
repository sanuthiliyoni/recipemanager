from Tasks.task1 import *
from Tasks.task2 import generate_id
import copy

def search_recipe(recipes):
    """This is to search recipes"""
    while True:
        print(f"""\n==========================
        Search Menu
==========================
1. Search with ingredient
2. Search with time
3. Exit search menu
==========================""")
        
        choice = input("Enter choice: ")
        if choice == "1":
            search_by_ingredient(recipes)
        elif choice == "2":
            search_by_time(recipes)
        elif choice == "3":
            return
        else:
            print("Invalid input enter (1 - 3)")

def search_by_ingredient(recipes):
    """This is to search by recipe"""
    keyword = input("\nEnter ingredient to search: ").lower()

    found_recipes = []

    for id, i in recipes.items():
        for ingredient in i["ingredients"]:
            ingredient_name = ingredient[0].lower()
            if keyword == ingredient_name:
                found_recipes.append((id, i["name"]))
                break #break the second for loop
            
    if len(found_recipes) > 0:
        print(f"\nFound {len(found_recipes)} recipe/s containing {keyword}")
        for id, name in found_recipes:
            print(f"{id} | {name}")
    else:
        print(f"\nNo recipes found containing {keyword}")
    input("\nEnter any key to go to the search menu: ")

def search_by_time(recipes):
    """This is to search by time"""
    found_recipes = []
    while True:
        try:
            #get the range of the time
            minimum = input("Enter minimum time (eg - 00:00): ").strip()
            maximum = input("Enter maximum time (eg - 00:00): ").strip()

            #check validity of the format
            if len(minimum.split(":")) != 2:
                raise ValueError
            if len(maximum.split(":")) != 2:
                raise ValueError
            
            min_hour = int(minimum.split(":")[0])
            min_minute = int(minimum.split(":")[1])
            max_hour = int(maximum.split(":")[0])
            max_minute = int(maximum.split(":")[1])

            min_time = (min_hour * 60) + min_minute
            max_time = (max_hour * 60) + max_minute

            for id,i in recipes.items():
                rec_time_str = i["time"]

                rec_time_hours = int(rec_time_str.split(":")[0])
                rec_time_minutes = int(rec_time_str.split(":")[1])

                rec_time = (rec_time_hours * 60) + rec_time_minutes

                if rec_time <= max_time and rec_time >= min_time:
                    found_recipes.append((id, i["name"], i["time"]))

            if len(found_recipes) > 0:
                print(f"\nFound {len(found_recipes)} between {minimum} and {maximum}.\n")
                for rec_id, name, time in found_recipes:
                    print(f"{rec_id} | {name} | {time}")
            else:
                print(f"\nNo recipes found between {minimum} and {maximum}.")
            
            input("\nEnter any key to go to the search menu: ")
            break
        except:
            print("Invalid input.")
            continue

def manage_recipe(recipes):
    """This is to manage recipes"""
    while True:
        print(f"""\n==========================
        Manage Menu
==========================
1. Delete recipe
2. Edit recipe
3. Duplicate recipe
4. Exit manage menu
==========================""")
        
        choice = input("Enter choice: ")
        if choice == "1":
            delete_recipe(recipes)
        elif choice == "2":
            edit_recipe(recipes)
        elif choice == "3":
            duplicate_recipe(recipes)
        elif choice == "4":
            return
        else:
            print("Invalid input enter (1 - 3)")

def delete_recipe(recipes):
    """This is to delete recipes"""
    if not recipes:
        print("No recipes found.")
        input("Enter any key to go to the manage menu: ")
        return
    
    print("\nAvailable recipes:")
    for id, i in recipes.items():
        print(f"    - {id}")
    
    while True: 
        rec_id = input("\nEnter recipe Id to delete: ").upper()
        if rec_id in recipes:
            while True:
                confirm = input(f"Are you sure you want to delete {rec_id}? (yes/no): ").lower()
                if confirm == "yes":
                    del recipes[rec_id]
                    print(f"\nSuccessfully deleted {rec_id}.")
                    break
                elif confirm == "no":
                    print("\nDeletion cancelled.")
                    break
                else:
                    print("Invalid input enter (yes/no).")
        else:
            print("\nPlease enter a valid Id.")
            continue

        input("\nEnter any key to go to the manage menu: ")
        break
                
def edit_recipe(recipes):
    """This is to edit recipes"""

    if not recipes:
        print("No recipes found.")
        input("Enter any key to go to the manage menu: ")
        return
    
    print("\nAvailable recipes:")
    for id, i in recipes.items():
        print(f"    - {id}")

    stop = False #Used to break the main while loop
    while True:
        if stop:
            break
        rec_id = input("\nEnter recipe Id to edit: ").strip().upper()
        if rec_id in recipes:
            while True:
                print(f"\n=== Editing {rec_id} ===")
                print("""1. Edit name
2. Edit category
3. Edit time
4. Edit tags
5. Edit ingredients
6. Exit editing
==========================""")
                choice = input("Enter choice (1 - 5): ")
                if choice == "1":
                    recipes[rec_id]["name"] = validate_name()
                    print("Name updated successfully.")
                    continue
                elif choice == "2":
                    recipes[rec_id]["category"] = select_category()
                    print("Category updated successfully.")
                    continue
                elif choice == "3":
                    recipes[rec_id]["time"] = validate_time()
                    print("Time updated successfully.")
                    continue
                elif choice == "4":
                    tags = input("Enter tags (comma separated): ")
                    tags = set(tags.split(","))
                    recipes[rec_id]["tags"] = tags
                    print("Tags updated successfully.")
                    continue
                elif choice == "5":
                    change_ingredients(recipes,rec_id)
                elif choice == "6":
                    print(f"\nFinished editing {rec_id}")
                    stop = True
                    break
                else:
                    print("Invalid choice. chose from 1 - 5")

        else:
            print("Please enter a valid Id.")


def statistics(recipes):
    """This is to print statistics of all recipes"""
    print(f"""\n==========================
         Statistics
==========================""")

    if not recipes:
        print("\nNo recipes added.")
        print("Enter any key to go to the main menu.")
    
    total_recipes = len(recipes)
    category_count = {}
    total_time = 0
    time_30 = 0
    time_30_60 = 0
    time_60 = 0
    total_ingredients = 0
    most_ingredients = 0
    least_ingredients = None #nothing is assigned to this at first
    most_ingre_id = "" 
    least_ingre_id = ""


    print(f"Total recipes: {total_recipes}")

    for id,i in recipes.items():
        cat = i["category"]
        if cat in category_count:
            category_count[cat] += 1
        else:
            category_count[cat] = 1
        
        time = i["time"]
        hours = int(time.split(":")[0])
        mins = int(time.split(":")[1])
        total_time = (hours * 60) + mins

        if total_time < 30:
            time_30 += 1
        elif total_time >= 30 and total_time <= 60:
            time_30_60 += 1
        else:
            time_60 += 1
        
        #to get the avarage ingredients count
        num_ingredients = len(i["ingredients"])
        total_ingredients += num_ingredients
        if num_ingredients > most_ingredients:
            most_ingredients = num_ingredients
            most_ingre_id = id
        
        if least_ingredients is None or num_ingredients < least_ingredients:
            least_ingredients = num_ingredients
            least_ingre_id = id
        
    print("\nRecipes by category:")
    for cat,count in category_count.items():
        print(f"  {cat} : {count}")
    
    print("\nCooking time distribution:")
    print(f"  Quick (<30 min): {time_30}")
    print(f"  Medium (30-60 min): {time_30_60}")
    print(f"  Long (>60 min): {time_60}")

    print(f"\nAvarage ingredients per recipe: {total_ingredients/len(recipes.keys())}")
    print(f"Largest recipe: {most_ingre_id} with {most_ingredients} ingredients.")
    print(f"Smallest recipe: {least_ingre_id} with {least_ingredients} ingredients.")
    input("\nEnter any key to go to the main menu: ")


def change_ingredients(recipes, rec_id):
    """This is to change the ingredients"""
    while True:
        print(f"==========================")
        print("""1. Add ingredients
2. Remove ingredients
3. Cancel
==========================""")
        
        choice = input("Enter choice: ")
        if choice == "1":
            new_ingredients(recipes, rec_id)
            print("Successfully added ingredient/s")
        elif choice == "2":
            del_ingredients(recipes, rec_id)
        elif choice == "3":
            break
        else:
            print("Invalid number. Enter(1 - 3).")


def new_ingredients(recipes, rec_id):
    """This is to validate the ingredients"""
    allowed_units = ["g", "kg", "ml", "l", "cup", "tbsp", "tsp", "piece"]
    ingredients_count = 0
    ingredients = ()

    #Used the previous function without asking for the number of ingredients that they want to add
    while True:
        try:
            ingredients_count = int(input("How many ingredents do you want to add?: "))
        except:
            print("Please enter a valid number.")
        print(" ")

        for i in range(ingredients_count):

            while True:
                ingredient_input = input(f"Enter ingredient {i+1} (name,quantity,unit): ")
                try:
                    parts = ingredient_input.split(",")
                    if len(parts) != 3:
                        raise ValueError

                    ingredient_name = parts[0]
                    ingredient_qty = parts[1]
                    ingredient_unit = parts[2].lower()

                    if len(ingredient_name) < 3 or len(ingredient_name) > 30:
                        print("Ingredient name must be 3-30 characters.")
                        continue

                    ingredient_qty = float(ingredient_qty)
                    if ingredient_qty <= 0:
                        print("Quantity must be positive.")
                        continue

                    if ingredient_unit not in allowed_units:
                        print("Invalid unit.")
                        continue
                    
                    if any(ingredient_name.lower() == i[0].lower() for i in ingredients):
                        add_duplicate = False
                        while True:
                            confirm = input("Ingredient already added. Add anyway? (yes/no): ")
                            if confirm.lower() == "yes":
                                ingredients = (ingredient_name, ingredient_qty, ingredient_unit)
                                recipes[rec_id]["ingredients"].append(ingredients)
                                add_duplicate = True
                                break
                            elif confirm.lower() == "no":
                                break
                            else:
                                print("Please enter a valid input.")
                                
                        if add_duplicate:
                            break
                        else:
                            continue

                    else:
                        ingredients = (ingredient_name, ingredient_qty, ingredient_unit)
                        recipes[rec_id]["ingredients"].append(ingredients)
                        break

                except:
                    print("Invalid format. Use : (name, quantity, unit).")
        break

def del_ingredients(recipes, rec_id):
    """This is to delete ingredients"""
    count = 1

    print("\nIngredients in recipe:")
    for i in recipes[rec_id]["ingredients"]:
        print(f"    {count} - {i[0]}, {i[1]}, {i[2]}")
        count += 1

    while True:
        try:
            del_index = int(input("\nEnter the number of the ingredient to delete: "))
            del_index -= 1

            if 0 <= del_index < len(recipes[rec_id]["ingredients"]):
                recipes[rec_id]["ingredients"].pop(del_index)
                print("Successfully removed ingredient")
                input("Enter any key to go back: ")
                break
            else:
                print("Invalid number. Select from the list.")

        except ValueError:
            print("Enter a valid number.")

def duplicate_recipe(recipes):
    """This is to duplicate a recipe"""
    if not recipes:
        print("No recipes found.")
        input("Enter any key to go to the manage menu: ")
        return
    
    print("\nAvailable recipes:")
    for id, i in recipes.items():
        print(f"    - {id}")
    
    while True: 
        rec_id = input("\nEnter recipe Id to duplicate: ").upper()
        if rec_id in recipes:
            new_name = validate_name()
            new_id = generate_id(recipes)
            clone_recipe = copy.deepcopy(recipes[rec_id])#used deepcopy to get everything from the recipe without dependency 
            clone_recipe["name"] = new_name
            recipes[new_id] = clone_recipe
            print(f"Successfully duplicated {rec_id} with new name '{new_name}'")
            input("Enter any key to go to the manage menu: ")
            break
        else:
            print("Enter a valid id.")



    
    


