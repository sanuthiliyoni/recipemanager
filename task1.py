allowed_units = ["g", "kg", "ml", "l", "cup", "tbsp", "tsp", "piece"]
catogeries = ["breakfast", "lunch", "dinner", "dessert", "snack", "beverage"]

def validate_name():
    """This is to validate the recipe inputs"""
    while True:
        
        recipe_name = input("Enter the recipe name: ")
        name_check = recipe_name.strip()#remove spaces

        #check for all spaces
        if name_check == "":
            print("Name cannot be empty or all spaces.")
            continue

        #Check the length
        if len(name_check) < 3 or len(name_check) > 50:
            print("Name must be between 3 and 50 characters.")
            continue

        #One letter validation
        has_letter = False
        for i in name_check:
            if i.isalpha():
                has_letter = True
                break
        
        #check whether name has a letter
        if not has_letter:
            print("Name should contain at least one letter.")
            continue
        
        #characters validation
        allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -'"
        for i in name_check:
            if i not in allowed_characters:
                print("Only letters, spaces, (-), (') are allowed.")
                break
        else:
            return recipe_name
        
def validate_ingredient_input():
    """This is to validate the ingredients"""
    ingredients = []   
    ingredients_count = 0

    print("\nEnter minimum 3 ingredients maximum 20.")
    while True:
        try:
            ingredients_count = int(input("How many ingredents do you want to add?: "))
        except:
            print("Please enter a valid number (3 - 20).")
        
        if ingredients_count < 3:
            print("You must add minimum 3 ingredients")
            continue
        elif ingredients_count > 20:
            print("You can only add maximum 20 ingredients")
            continue

        print(" ")
        for i in range(ingredients_count):

            while True:
                ingredient_input = input(f"Enter ingredient {i+1} (name,quantity,unit): ")
                try:
                    parts = ingredient_input.split(",")#to seperate ingredient name, qty and unit
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
                        print("Invalid unit.")#check validity of the unit
                        continue
                    
                    if any(ingredient_name.lower() == i[0].lower() for i in ingredients):#To check whether that ingredient is previously added
                        add_duplicate = False
                        while True:
                            confirm = input("Ingredient already added. Add anyway? (yes/no): ")
                            if confirm.lower() == "yes":
                                ingredients.append((ingredient_name, ingredient_qty, ingredient_unit))
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
                        ingredients.append((ingredient_name, ingredient_qty, ingredient_unit))
                        break

                except:
                    print("Invalid format. Use : (name, quantity, unit).")

        return ingredients

def validate_time():
    """This is to validate the time"""
    while True:
        time = input("\nEnter the cooking time (HH:MM): ")

        try:
            #Validate the format
            check_time = time.split(":")
            if len(check_time) != 2:
                raise ValueError
            
            hours = int(check_time[0])
            mins = int(check_time[1])

            if hours < 0 or hours > 12:#validate the hours
                print("Hours must be betwenn 0 and 12.")
                continue

            if mins < 0 or mins > 59:#validate the minutes
                print("Minutes must be between 0 and 59.")
                continue

            total_time = hours*60 + mins

            if total_time < 5 or total_time > 720:
                print("Time must be between 00:05 and 12:00.")
                continue

            return time
        
        except:
            print("Invalid format. Use HH:MM (example :- 01:30).")

def select_category():
    """This is to get the category of the recipe"""
    print("\nAvailable categories:\n")
    for category in catogeries:#print the categories
        print("-",category)
    while True:
        choice = input("\nEnter category: ").lower()

        if choice in catogeries:
            return choice
        else:
            print("Invalid category. Please choose from the list.")

def validate_recipe_inputs():
    print("\n---- Enter Recipe Detaials ---\n")
    
    #Run each funtion to get the output
    name = validate_name()
    ingredients = validate_ingredient_input()
    time = validate_time()
    category = select_category()
    tags = input("Enter tags (comma separated): ")
    tags = set(tags.split(","))

    #print the added recipe details
    print("\nRecipe added successfully\n")
    print("Name:",name)
    print("Ingredients:",len(ingredients))  
    print("Category:",category)
    print("Cooking time:",time)

    #return the values
    return{"name": name,
           "ingredients": ingredients,
           "category": category,
           "time": time,
           "tags": tags}


                    



            
