from Sena_Hordoffa_Final_Project_Assignment_For_INST326 import FindingIngredients 
from Sena_Hordoffa_Final_Project_Assignment_For_INST326 import FindingInstructions 





def test_list_of_ingredients(): 
    # testing for the first class 


    finder = FindingIngredients()

    # Test for pancakes
    ingredients, recipe_name = finder.list_of_ingredients("pancakes")
    assert ingredients.strip().lower() == "flour, sugar, baking powder, milk or non-dairy milk, eggs, butter, vanilla extract"
    assert recipe_name.strip().lower() == "pancakes"

    # Test for PB&J sandwich
    ingredients, recipe_name = finder.list_of_ingredients("PB&J sandwich")
    assert ingredients.strip().lower() == "bread, peanut butter, jelly"
    assert recipe_name.strip().lower() == "pb&j sandwich"

    # Test for cookies
    ingredients, recipe_name = finder.list_of_ingredients("cookies")
    assert ingredients.strip().lower() == "flour, eggs, brown sugar, sugar, vanilla extract, baking soda, or baking powder, butter, milk, and chocolate chips"
    assert recipe_name.strip().lower() == "cookies"

    # Test for waffles
    ingredients, recipe_name = finder.list_of_ingredients("waffles")
    assert ingredients.strip().lower() == "flour, sugar, baking powder, milk or non-dairy milk, eggs, butter, vanilla extract"
    assert recipe_name.strip().lower() == "waffles" 

    # Test for bluberry muffins 
    ingredients, recipe_name = finder.list_of_ingredients("blueberry muffins")
    assert ingredients.strip().lower() == "flour, sugar, eggs, milk or non-dairy milk, baking powder, vanilla extract, butter or oil, and blueberries or frozen blueberries"
    assert recipe_name.strip().lower() == "blueberry muffins" 

    # Test for pasta  
    ingredients, recipe_name = finder.list_of_ingredients("pasta")
    assert ingredients.strip().lower() == "dry pasta noodles, water, oil, tomatoes or tomato sauce, basil, oregano, salt, garlic powder or fresh garlic, and parmesan cheese"
    assert recipe_name.strip().lower() == "pasta" 

    # Test for banana bread  
    ingredients, recipe_name = finder.list_of_ingredients("banana bread")
    assert ingredients.strip().lower() == "flour, butter or oil, chocolate chips (optional), sugar, brown sugar, baking soda, eggs, vanilla extract walnuts (optional), and some ripe bananas"
    assert recipe_name.strip().lower() == "banana bread" 

    # Test for chocolate chip muffins 
    ingredients, recipe_name = finder.list_of_ingredients("chocolate chip muffins")
    assert ingredients.strip().lower() == "flour, sugar, eggs, milk or non-dairy milk, baking powder, vanilla extract, butter, and chocolate chips"
    assert recipe_name.strip().lower() == "chocolate chip muffins" 

    # Test for vanilla ice cream 
    ingredients, recipe_name = finder.list_of_ingredients("vanilla ice cream")
    assert ingredients.strip().lower() == "heavy cream or whole milk or half and half, sugar (optional), vanilla extract, and sweetened condensed milk"
    assert recipe_name.strip().lower() == "vanilla ice cream" 

    # Test for strawberry ice cream 
    ingredients, recipe_name = finder.list_of_ingredients("strawberry ice cream")
    assert ingredients.strip().lower() == "heavy cream or whole milk or half and half, sugar (optional), vanilla extract, sweetened condensed milk, and strawberries or strawberry syrup"
    assert recipe_name.strip().lower() == "strawberry ice cream" 

    # Test for chocolate ice cream 
    ingredients, recipe_name = finder.list_of_ingredients("chocolate ice cream")
    assert ingredients.strip().lower() == "heavy cream or whole milk or half and half, sugar (optional), vanilla extract, sweetened condensed milk, and chocolate or cocoa powder or chocolate syrup"
    assert recipe_name.strip().lower() == "chocolate ice cream" 

    # Test for french toast 
    ingredients, recipe_name = finder.list_of_ingredients("french toast")
    assert ingredients.strip().lower() == "slices of bread, sugar, eggs, milk or non-dairy milk, butter, cinnamon powder, vanilla extract, maple syrup or honey, and berries (optional)"
    assert recipe_name.strip().lower() == "french toast" 










def test_instructions_by_recipe():
    # this is testing for the second class 


    instructions_finder = FindingInstructions()

    # Test for pancakes
    instructions, recipe_name = instructions_finder.instructions_by_recipe("pancakes")
    assert recipe_name.strip().lower() == "pancakes"
    assert instructions[0][0].strip() == "In a large bowl, whisk together the dry ingredients such as the flour, sugar, and baking powder."
    assert instructions[0][1].strip() == "In a separate bowl, whisk the wet ingredients together such as the milk, eggs, melted butter, and vanilla. Then, pour into the dry ingredients and stir it together."
    assert instructions[0][2].strip() == "Heat a lightly buttered skillet or griddle over medium heat. Pour a small amount of batter for each pancake. Cook until some bubbles form and then flip and cook until golden brown."

    # Test for PB&J sandwich
    instructions, recipe_name = instructions_finder.instructions_by_recipe("PB&J sandwich")
    assert recipe_name.strip().lower() == "pb&j sandwich"
    assert instructions[0][0].strip() == "Take one slice of bread and then spread a layer of peanut butter on one side of the bread."
    assert instructions[0][1].strip() == "Next, take the second slice of bread and spread jelly on the one side of the other piece of bread."
    assert instructions[0][2].strip() == "Press the two slices of bread  together, peanut butter and jelly sides facing each other. You can also slice the sandwich if you want."

    # Test for cookies
    instructions, recipe_name = instructions_finder.instructions_by_recipe("cookies")
    assert recipe_name.strip().lower() == "cookies"
    assert instructions[0][0].strip() == "In a large bowl, mix the butter, brown sugar, and white sugar together. Then, add the vanilla extract and eggs, and mix it together. In a separate bowl, combine the flour and baking soda or baking powder, and then mix it into the wet ingredients. Next, add a splash of milk if the dough is too dry. Then, stir in some chocolate chips or other optional toppings."
    assert instructions[0][1].strip() == "Preheat oven to 350 degrees fahrenheit. Then, scoop some spoonfuls of dough and place them on a baking sheet lined with parchment paper, leaving some space between each piece of cookie dough. Next, chill it in the fridge for a few hours."
    assert instructions[0][2].strip() == "Bake for 10 to 12 minutes or until edges are golden brown. Let it cool on the baking sheet for a few minutes or a few hours before eating it."

    # Test for waffles
    instructions, recipe_name = instructions_finder.instructions_by_recipe("waffles")
    assert recipe_name.strip().lower() == "waffles"
    assert instructions[0][0].strip() == "In a large bowl, whisk together the dry ingredients such as the flour, sugar, and baking powder. In another bowl, mix the milk, eggs, melted butter, and vanilla together. Next, pour the wet mixture into the dry and then mix it together."
    assert instructions[0][1].strip() == "Pour the batter into you waffle maker."
    assert instructions[0][2].strip() == "Add some optional toppings. Then, cook it in the waffle maker until the waffles are golden brown." 

    # Test for blueberry muffins 
    instructions, recipe_name = instructions_finder.instructions_by_recipe("blueberry muffins")
    assert recipe_name.strip().lower() == "blueberry muffins"
    assert instructions[0][0].strip() == "In a bowl, mix together the flour, sugar, and baking powder. In another bowl, whisk together the milk, eggs, melted butter or oil, and vanilla extract. Then, combine the wet and dry ingredients and mix it together. Then, add in the blueberries and mix it together."
    assert instructions[0][1].strip() == "Preheat the oven to about 350 degrees fahrenheit. Then, pour the muffin batter or the mixture into a muffin pan."
    assert instructions[0][2].strip() == "Bake it for about 18 to 20 minutes or until a toothpick inserted into the center of one of the muffins comes out clean. Let it cool down before eating it." 

    # Test for pasta 
    instructions, recipe_name = instructions_finder.instructions_by_recipe("pasta")
    assert recipe_name.strip().lower() == "pasta"
    assert instructions[0][0].strip() == "Boil some water and then add in a pinch of salt. Add the pasta noodles and cook the pasta for about 10 to 12 minutes or according to the package instructions. Then, drain the pasta water and set it aside for now."
    assert instructions[0][1].strip() == "In a pan, heat some oil over medium heat. Add in some fresh sliced garlic or some garlic powder and then stir in some sliced tomatoes or tomato sauce. Then, season it with some salt, basil, and oregano. Next, simmer it for about a few minutes."
    assert instructions[0][2].strip() == "Add the cooked pasta to the tomato sauce and then toss it or mix it all together. You can also add some parmesan cheese on top of it if you want to." 

    # Test for banana bread 
    instructions, recipe_name = instructions_finder.instructions_by_recipe("banana bread")
    assert recipe_name.strip().lower() == "banana bread"
    assert instructions[0][0].strip() == "In a large bowl, mash the bananas together. Add in some melted butter or oil, sugar, brown sugar, eggs, and also some vanilla extract and mix it all together. Then, add in some flour and baking soda and mix it all together. Next, add in some chocolate chips (optional) and/ or some walnuts (optional) and mix it all together."
    assert instructions[0][1].strip() == "Preheat the oven to 350 degrees fahrenheit and then pour the batter into a loaf pan."
    assert instructions[0][2].strip() == "Bake it for about sixty minutes or until a toothpick inserted into the center of the banana bread comes out clean. Let it cool down before slicing it and eating it." 

    # Test for chocolate chip muffins 
    instructions, recipe_name = instructions_finder.instructions_by_recipe("chocolate chip muffins")
    assert recipe_name.strip().lower() == "chocolate chip muffins"
    assert instructions[0][0].strip() == "In a bowl, mix together the flour, sugar, and baking powder. In another bowl, whisk together the milk, eggs, melted butter, and vanilla extract. Then, combine the wet and dry ingredients and mix it together. Then, add in the chocolate chips and mix it together."
    assert instructions[0][1].strip() == "Preheat the oven to about 350 degrees fahrenheit. Then, pour the muffin batter or the mixture into a muffin pan."
    assert instructions[0][2].strip() == "Bake it for about 18 to 20 minutes or until a toothpick inserted into the center of one of the muffins comes out clean. Let it cool down before eating it." 

    # Test for vanilla ice cream 
    instructions, recipe_name = instructions_finder.instructions_by_recipe("vanilla ice cream")
    assert recipe_name.strip().lower() == "vanilla ice cream"
    assert instructions[0][0].strip() == "In a large bowl, whisk together the sweetened condensed milk, vanilla extract, and sugar (optional)."
    assert instructions[0][1].strip() == "In another bowl, whip the heavy cream until some soft peaks form. Gently fold the whipped cream into the condensed milk mixture until it's smooth. If you're using milk or half and half, just mix it with the sweetened condensed milk."
    assert instructions[0][2].strip() == "Pour the mixture into a container, smooth the top, and then cover it. Freeze for a few hours or until it's firm. Then, scoop the ice cream and enjoy!" 

    # Test for strawberry ice cream 
    instructions, recipe_name = instructions_finder.instructions_by_recipe("strawberry ice cream")
    assert recipe_name.strip().lower() == "strawberry ice cream"
    assert instructions[0][0].strip() == "In a large bowl, whisk together the sweetened condensed milk, vanilla extract, and sugar (optional)."
    assert instructions[0][1].strip() == "In another bowl, whip the heavy cream until some soft peaks form. Gently fold the whipped cream into the condensed milk mixture until it's smooth. If you're using milk or half and half, just mix it with the sweetened condensed milk. Then, add in the strawberry syrup then mix it all together. Make sure the strawberry syrup is not hot before adding it into the mixture."
    assert instructions[0][2].strip() == "Pour the mixture into a container, smooth the top, and then cover it. Freeze for a few hours or until it's firm. Then, scoop the ice cream and enjoy!" 

    # Test for chocolate ice cream 
    instructions, recipe_name = instructions_finder.instructions_by_recipe("chocolate ice cream")
    assert recipe_name.strip().lower() == "chocolate ice cream"
    assert instructions[0][0].strip() == "In a large bowl, whisk together the sweetened condensed milk, vanilla extract, and sugar (optional)."
    assert instructions[0][1].strip() == "In another bowl, whip the heavy cream until some soft peaks form. Gently fold the whipped cream into the condensed milk mixture until it's smooth. If you're using milk or half and half, just mix it with the sweetened condensed milk. Then, add in the cocoa powder, melted chocolate, or chocolate syrup and then mix it all together. Make sure the metled chocolate is not hot before adding it into the mixture."
    assert instructions[0][2].strip() == "Pour the mixture into a container, smooth the top, and then cover it. Freeze for a few hours or until it's firm. Then, scoop the ice cream and enjoy!" 

    # Test for french toast 
    instructions, recipe_name = instructions_finder.instructions_by_recipe("french toast")
    assert recipe_name.strip().lower() == "french toast"
    assert instructions[0][0].strip() == "In a wide bowl, whisk together the wet ingredients such as the eggs, milk, sugar, cinnamon, and vanilla extract."
    assert instructions[0][1].strip() == "Heat a small amount of butter in a pan over medium heat. Dip each slice of bread and each side of the bread into the wet ingredients mixture, and then cook it in the pan for 2 to 3 minutes per side, or until it's golden brown."
    assert instructions[0][2].strip() == "Serve the french toast warm, topped with maple syrup or honey, or other optional toppings such as some berries." 






















