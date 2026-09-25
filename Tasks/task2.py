def generate_id(recipes):
    """This is to generate the recipe ID"""
    #check whether there are no recipes
    if len(recipes) == 0:
        return "RCP001"
    
    highest_num = 0

    for id in recipes.keys():
        num = int(id[3:])
        #To get the highest valued recipe id
        if num > highest_num:
            highest_num = num
    return f"RCP{highest_num + 1:03}"

def add_recipe(recipes, recipe):
    """This is to add the recipe to all the recipe list"""
    id = generate_id(recipes)
    recipes[id] = recipe
    print(f"Id: {id}")
    return

def display_one(recipes):
    """This is to display a single recipe"""
    rec_id = input("Enter recipe ID: ").upper()
    if rec_id in recipes:           
        print(f"""\n==========================
\nRecipe ID: {rec_id}
Name: {recipes[rec_id]["name"]}
Category: {recipes[rec_id]["category"]}
Cooking time: {recipes[rec_id]["time"]}
--------------------------
Ingredients:""")
        #print all ingredients 
        for b in recipes[rec_id.upper()]["ingredients"]:
            print(f"{b[0]} - {b[1]}{b[2]}")
        print("--------------------------")
        print(f"""tags: {",".join(recipes[rec_id.upper()]["tags"])}
==========================\n""")
    else:
        print("\nNo recipe found.")
        
    input("Enter any key to go to the view menu: ")


def display_all(recipes):
    """This is to display all the recipes"""
    if not recipes:#if no recipes are added
        print("\nNo recipes are added.")
        input("Enter any key to go to the main menu: ")
        return
    print(" ")
    for id, i in recipes.items():
        print(f"{id} | {i["name"]} | {i["category"]} | {i["time"]}")
    
    input("\nEnter any key to go to the view menu: ")

def display_by_category(recipes):
    """This is to display by category"""
    cat = input("Enter the category: ").lower().strip() #remove spaces and make all lower case
    a = False
    print(" ")
    for id,i in recipes.items():
        if i["category"] == cat:
            print(f"{id} | {i["name"]} | {i["category"]} | {i["time"]}")
            a = True #to check whether any recipe was found
    if a == False:
        print("No recipes in that category")
    input("\nEnter any key to go to the view menu: ")

def display_id_and_name(recipes):
    """This is to display id and name"""
    if not recipes:
        print("\nNo recipes are added.")
        input("Enter any key to go to the view menu: ")
        return
    print(" ")
    for id, i in recipes.items():
        print(f"{id} | {i['name']}")

    input("\nEnter any key to go to the view menu: ")

def display_category_count(recipes):
    """This is to display count of a category"""
    cat = input("Enter the category: ").lower().strip()
    count = 0
    a = False
    print(" ")
    for id,i in recipes.items():
        if i["category"] == cat:
            count += 1
            a = True
    if a == False:
        print("No recipes in that category")
    print(f"found {count} recipe/s in {cat}")
    input("\nEnter any key to go to the view menu: ")

def view_recipe_menu():
    """This is to print the view menu and get the input"""
    print(f"""\n==========================
         View Menu
==========================
1. View single recipe
2. View all recipes
3. View by category
4. View Id with name
5. View recipe count per category
6. Exit view menu
==========================""")

def display_recipes(recipes):
    """Main function to display recipes"""
    while True:
        view_recipe_menu()
        choice = input("Enter choice (1 - 6): ")
        if choice == "1":
            display_one(recipes)
        elif choice == "2":
            display_all(recipes)
        elif choice == "3":
            display_by_category(recipes)
        elif choice == "4":
            display_id_and_name(recipes)
        elif choice == "5":
            display_category_count(recipes)
        elif choice == "6":
            break
        else:
            print("Enter valid number (1 - 6).")
