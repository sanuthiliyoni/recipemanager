def save_file(recipes):
    """This is to save the recipes to a file"""
    try:    
        with open("w2212798_recipes.txt", "w") as fo: #open the file to write
            for id,i in recipes.items():
                file_ingredients = []

                fo.write("=====RECIPE=====\n")
                fo.write(f"Id: {id}\n")
                fo.write(f"Name: {i["name"]}\n")
                fo.write(f"Category: {i["category"]}\n")
                fo.write(f"Time: {i["time"]}\n")

                #get ingredients to a variable and save that
                for ingredient in i["ingredients"]:
                    file_ingredients.append(f"{ingredient[0]},{ingredient[1]},{ingredient[2]}")
                
                fo.write(f"Ingredients: {' | '.join(file_ingredients)}\n")

                tag_str = ",".join(i['tags'])
                fo.write(f"Tags: {tag_str}\n")
                fo.write("=====END=====\n\n")
        print(f"\nSuccessfully saved {len(recipes)} recipes.")
    except:
        print("File not found!")
        input("\nEnter any key to go to the main menu: ")

def load_file(recipes):
    """This is to load recipes"""
    try:
        with open("w2212798_recipes.txt", "r") as fo:
            lines = fo.readlines()#read all lines
        temp_id = ""
        temp_recipe = {}

        for line in lines: #get line by line
            line = line.strip()

            if line == "":
                continue #skip empty lines
            
            if line.startswith("Id:"):
                temp_id = line.split(":")[1].strip()
                temp_recipe = {}#new temp dict for the recipe

            elif line.startswith("Name:"):
                temp_recipe["name"] = line.split(":")[1].strip()

            elif line.startswith("Category:"):
                temp_recipe["category"] = line.split(":")[1].strip()
            
            elif line.startswith("Time:"):
                temp_recipe["time"] = line.split(":", 1)[1].strip()

            elif line.startswith("Ingredients:"):
                ingredient_string = line.split(":",1)[1].strip()
                temp_list = []

                if ingredient_string != "":
                    items = ingredient_string.split("|")
                    for item in items:
                        if item.strip() != "":
                            parts = item.split(",")
                            name = parts[0].strip()
                            qty = float(parts[1].strip())
                            unit = parts[2].strip()

                            temp_list.append((name, qty, unit))

                temp_recipe["ingredients"] = temp_list
            
            elif line.startswith("Tags:"):
                tag_string = line.split(":", 1)[1].strip()
                temp_set = set()

                if tag_string != "":
                    tags = tag_string.split(",")
                    for t in tags:
                        if t.strip() != "":
                            temp_set.add(t.strip())
                
                temp_recipe["tags"] = temp_set

            elif line == "=====END=====":
                if temp_id != "":
                    recipes[temp_id] = temp_recipe
                
        print(f"\nSuccessfully loaded {len(recipes)} recipe/s from file")
        input("Enter any key to go to the main menu: ")
    except FileNotFoundError:
        input("\nNo previous save file found. Press any key to start fresh")
    except:
        print("Error loading file")

def exit_menu(recipes):
    """This is to exit the program"""
    while True:
        print(f"""\n==========================
        Exit Menu
==========================
1. Save and exit
2. Exit without saving
3. Cancel
==========================""")
        
        #if program is false the main program will stop, if it is true main program keeps on running
        choice = input("Enter choice: ")
        if choice == "1":
            save_file(recipes)
            program = False
            print("Closing recipe book...")
            return program
        elif choice == "2":
            program = False
            print("Closing recipe book...")
            return program
        elif choice == "3":
            program = True
            return program
        else:
            print("Please enter valid (1-3)")
            continue

def export_recipe(recipes):
    """This is to export recipes"""
    id_list = []
    if not recipes:
        print("No recipes are added.")
        input("Enter any key to go to the main menu: ")
        return
    print(f"""\n==========================
    Export Menu
==========================
Available recipes:""")
    for id, i in recipes.items():
        print(f"    - {id}")
        id_list.append(id)#to get the input from the id and check if it exist
    while True:
        export_id = input("\nEnter recipe Id: ").upper().strip()
        if export_id in id_list:
            with open("Exported_Recipes/recipe_" + recipes[export_id]["name"] + ".txt", "w") as fo:
                fo.write(f"=======================\nRecipe: {recipes[export_id]["name"]}\n")
                fo.write("=======================\n")
                fo.write(f"Category: {recipes[export_id]["category"]}\n")
                fo.write(f"Cooking time: {recipes[export_id]["time"]}\n\n")
                fo.write("Ingredients:\n")
                for ingredient in recipes[export_id]["ingredients"]:
                    fo.write(f"- {ingredient[0]}: {ingredient[1]} {ingredient[2]}\n")
                if len(recipes[export_id]["tags"]) != 0:
                    fo.write(f"\nTags: {', '.join(recipes[export_id]["tags"])}\n=======================\n")
                else:
                    fo.write("\nTags:\n=======================\n")
            print("\nSuccessfully exported.")
            input("Enter any key to go to the main menu: ")
            break
        else:
            print("Invalid recipe.")
            