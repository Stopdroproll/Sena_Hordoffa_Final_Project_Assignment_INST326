

import re 
import csv 
import pandas as pd 
import sqlite3 
import requests 







class FindingIngredients:  

    def list_of_ingredients(self, specific_recipe_name):  

        data_frame = pd.read_csv("Sena_Hordoffa_Finding_Ingredients_Final_Project_INST326.csv") 

        recipe_name = data_frame[data_frame["Recipe Name"] == specific_recipe_name] 

        if len(recipe_name) == 0: 
            raise ValueError("\nError: this recipe wasn't found.")


        ingredients_needed = recipe_name["List of Ingredients Needed"].iloc[0].strip() 

        recipe_title = recipe_name["Recipe Name"].iloc[0].strip() 

        return ingredients_needed, recipe_title 





class FindingInstructions:  

    def __init__(self): 
        self.conn = sqlite3.connect(':memory:') 
        self.read("Sena_Hordoffa_Recipe_Instructions_Final_Project_INST326.csv") 
    

    def __del__(self): 
        try:
            self.conn.close()
        except:
            pass 



    def read(self, filename): 

        cursor = self.conn.cursor() 

        instructions_table = ''' CREATE TABLE instructions 
        (id integer, "recipe name" text, "step 1" text, "step 2" text, "step 3" text) ''' 

        cursor.execute(instructions_table) 

        with open(filename, "r") as specified_file: 
            file = csv.reader(specified_file) 
            next(specified_file) 

            for i in file: 

                id_number = int(i[0]) 
                recipe_name = i[1] 
                step_one = i[2] 
                step_two = i[3] 
                step_three = i[4] 

                inserting_instructions_values = ''' INSERT INTO instructions VALUES (?,?,?,?,?) ''' 
                cursor.execute(inserting_instructions_values, (id_number, recipe_name, step_one, step_two, step_three)) 
            
            self.conn.commit() 
    


    def instructions_by_recipe(self, recipe_name): 

        another_cursor = self.conn.cursor() 

        finding_recipe_name_and_steps = ''' SELECT "step 1", "step 2", "step 3" FROM instructions WHERE "recipe name" =? ''' 
        
        information_about_recipe_instructions = another_cursor.execute(finding_recipe_name_and_steps, (recipe_name, )).fetchall() 
 

        return information_about_recipe_instructions, recipe_name



 







class FindingARecipeRecommendation: 

    def __init__(self): 
        self.section_two_recipes = {
            "pancakes": ["flour", "all-purpose flour", "sugar", "white sugar", "egg", "eggs", "milk", "non-dairy milk", "almond milk", "oat milk", "butter", "baking powder", "vanilla extract"],  
            "waffles": ["flour", "all-purpose flour", "sugar", "white sugar", "egg", "eggs", "milk", "non-dairy milk", "almond milk", "oat milk", "butter", "baking powder", "vanilla extract"],  
            "french toast": ["bread", "sugar", "white sugar", "egg", "eggs", "milk", "non-dairy milk", "almond milk", "oat milk", "butter", "cinnamon", "cinnamon powder", "vanilla extract", "berries", "maple syrup", "syrup", "honey"],  
            "peanut butter and jelly sandwich": ["bread", "white bread", "wheat bread", "whole wheat bread", "whole grain bread", "jam", "strawberry jam", "jelly", "strawberry jelly", "blueberry jam", "blueberry jelly", "peanut butter"], 
            "salad": ["lettuce", "arugula", "spinach", "tomato", "tomatoes", "cucumber", "cucumbers", "onion", "onions", "red onions", "olive oil", "oil", "pepper", "peppers", "bell pepper", "bell peppers", "cilantro", "salt"],  
            "hamburgers": ["beef", "bread", "hamburger buns", "burger buns", "lettuce", "tomato", "tomatoes", "ketchup", "mayo", "barbecue", "bbq suace", "barbecue sauce", "cheese", "cheddar cheese", "mayonnaise", "pickle", "pickles"], 
            "pasta": ["pasta noodles", "oil", "olive oil", "water", "dry pasta", "dry pasta noodles", "pasta dough", "pasta", "penne pasta", "pasta penne", "noodles", "dry noodles", "tomatoes", "tomato", "pasta sauce", "tomato sauce", "basil", "oregano", "salt", "parmesan", "parmesan cheese", "garlic powder", "garlic", "fresh garlic"], 
            "ice cream": ["heavy cream", "half and half", "cream", "whole milk", "milk", "sugar", "white sugar", "vanilla extract", "condensed milk", "sweetened condensed milk"], 
            "chocolate ice cream": ["heavy cream", "half and half", "cream", "whole milk", "milk", "sugar", "white sugar", "vanilla extract", "condensed milk", "sweetened condensed milk", "chocolate", "cocoa powder", "chocolate syrup"], 
            "strawberry ice cream": ["heavy cream", "half and half", "cream", "whole milk", "milk", "sugar", "white sugar", "vanilla extract", "condensed milk", "sweetened condensed milk", "strawberry", "strawberries", "strawberry syrup"],  
            "chocolate chip cookies": ["flour", "all-purpose flour", "butter", "chocolate chips", "chocolate chip", "sugar", "brown sugar", "white sugar", "baking soda", "egg", "eggs", "vanilla extract"], 
            "banana bread": ["flour", "all-purpose flour", "butter", "oil", "chocolate chips", "chocolate chip", "sugar", "brown sugar", "light brown sugar", "white sugar", "baking soda", "egg", "eggs", "vanilla extract", "walnuts", "bananas", "banana", "ripe banana", "ripe bananas"], 
            "blueberry muffins": ["flour", "all-purpose flour", "sugar", "white sugar", "egg", "eggs", "milk", "non-dairy milk", "almond milk", "oat milk", "baking powder", "vanilla extract", "oil", "blueberry", "blueberries", "frozen blueberry", "frozen blueberries"], 
            "chocolate chip chip muffins": ["flour", "all-purpose flour", "sugar", "white sugar", "egg", "eggs", "milk", "non-dairy milk", "almond milk", "oat milk", "baking powder", "vanilla extract", "butter", "chocolate chip", "chocolate chips"] 

            } 
    
    
    
    
    def using_ingredients_to_find_recipes(self, the_users_ingredients): 
        while True: 
            try: 
                for i in the_users_ingredients: 
                    if re.search(r"\d", i): 
                        raise ValueError("You can't include any numbers when writing your list of ingredients. ") 
                
                matching_ingredients = {} 
                
                for name_of_recipe, the_ingredients in self.section_two_recipes.items(): 
                    one_recipe_matches = [i for i in the_ingredients if i in the_users_ingredients] 
                    if one_recipe_matches: 
                        matching_ingredients[name_of_recipe] = one_recipe_matches 
                
                
                if matching_ingredients: 
                    number_one_recipe = max(matching_ingredients, key = lambda i: len(matching_ingredients[i])) 
                    number_one_match = matching_ingredients[number_one_recipe] 
                    
                    print(f"\nHere's one recipe that you can try to make: {number_one_recipe.title()}") 
                    
                    print(f"You have {len(number_one_match)} matching ingredients: ") 
                    
                    count = 1 
                    
                    for i in number_one_match: 
                        print(f"{count}. {i}") 
                        count += 1 
                
                
                else: 
                    print("No matching recipes were found. ") 
                

                break 



            except ValueError as error_statement: 
                print(f"Error: {error_statement}") 
                
                the_users_ingredients = input("Enter in the ingredients you currently have (and seperate them by commas OR type 'stop' to exit): ").strip().lower() 
                
                the_users_ingredients = [i.strip().lower() for i in the_users_ingredients.split(',')] 
            



            if "stop" in the_users_ingredients: 
                print("You've exited the program. Bye! ") 
                break 











class SpecificCuisines: 

    def get_meals_or_recipes(self, country): 

        url = f"https://www.themealdb.com/api/json/v1/1/filter.php?a={country}" 

        the_response = requests.get(url) 

        the_recipes = the_response.json() 
        
        count = 1 
        
        
        for i in the_recipes["meals"]: 
            print(f"{count}. {i ['strMeal']}") 
            count += 1






















def main(): 
    print("Hi! This is a recipe finder. You can either: \n" 
          "1. Search based on ingredients: and then get a recipe recomendation based on what you currently have \n" 
          "2. Search based on specific recipes: and then get a list of ingredients and instructions \n" 
          "3. Search up some meals or recipes you can make from a specific area or cuisine" ) 




    first_question = input("\nAre you looking for something? (yes or no): ").strip().lower()

    if first_question == "no": 
        print("Bye!") 
        return

    second_question = input("Are you looking for specific recipes with ingredients and instructions? (yes or no): ").strip().lower() 


    if second_question == "yes":  

        second_question_part_two = input("Enter in a specific recipe: ").strip().lower() 

        finder = FindingIngredients() 

        try: 
            ingredients_needed, recipe_name = finder.list_of_ingredients(second_question_part_two) 
            
            print(f"\nHere are the ingredients for {recipe_name}: ") 
            
            numbered_ingredients_list = ingredients_needed.split(",") 
            
            count = 1 
            
            for i in numbered_ingredients_list: 
                print(f"{count}. {i.strip()}") 
                count += 1 
            
            
            
            instructions_finder = FindingInstructions() 


            instructions, recipe_name = instructions_finder.instructions_by_recipe(second_question_part_two) 


            print(f"\nHere are the step-by-step instructions for {recipe_name}: ") 
            
            
            
            for i in instructions: 
                if i[0].strip().lower(): 
                    print("Step 1: ", i[0].strip()) 
                if i[1].strip().lower(): 
                    print("Step 2: ", i[1].strip()) 
                if i[2].strip().lower(): 
                    print("Step 3: ", i[2].strip()) 
        
        
        
        except ValueError as e: 
            print(e) 




    third_question = input("\nDo you want to be provided with recipe recommendations based on specific ingredients you currently have? (yes or no): ").strip().lower() 

    if third_question == "yes": 
        third_question_part_two = input("Enter in the ingredients you currently have (and seperate them by commas): ").strip().lower() 
        
        the_users_ingredients = [i.strip().lower() for i in third_question_part_two.split(',')] 

        specific_recipe_recommendation_finder = FindingARecipeRecommendation() 

        specific_recipe_recommendation_finder.using_ingredients_to_find_recipes(the_users_ingredients) 
    





    # import requests question four below: 

    question_four_input = input("\nDo you want to find some current recipes from a specific area or cuisines? (yes or no): ").strip().lower() 





    if question_four_input == "yes": 

        question_four_finder = SpecificCuisines() 



        areas_or_cuisines = ["British", "American", "Jamaican", "French", "Canadian", "Chinese", "Dutch", "Egyptian", "Greek", "Indian", 
                         "Irish", "Italian", "Japanese", "Kenyan", "Malaysian", "Mexican", "Moroccan", "Croatian", "Portuguese", 
                         "Russian", "Spanish", "Thai", "Vietnamese", "Turkish", "Tunisian", "Polish", "Filipino", "Ukrainian", "Uruguayan"] 
        

        print("Here are all the areas or cuisines you can search for: ") 




        sorting_the_areas_or_cuisines = sorted(areas_or_cuisines) 


        count = 1 

        for i in sorting_the_areas_or_cuisines: 
            print(f"{count}. {i}")
            count += 1 
        

        while True: 
            
            specific_country = input("\nEnter in a country to find some recipes (or type 'stop' to exit): ").strip().lower() 

            if specific_country.lower() == "stop": 
                print("Bye!") 
                return 
            


            if specific_country.title() not in areas_or_cuisines: 
                print("\nError: You can only choose areas or cuisines that are currently available in the list given to you! ") 
                
            else: 
                
                question_four_finder.get_meals_or_recipes(specific_country.title()) 
 
                break 


    
    else: 
        print("Bye!") 










if __name__ == "__main__": 
    main() 

























