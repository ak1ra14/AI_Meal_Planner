string = """For an athlete aiming to aggressively bulk, it's important to focus on high-calorie, nutrient-dense meals that provide a good balance of protein, carbs, and fats. Here are two meal suggestions:

### Meal 1: Chicken and Sweet Potato Power Bowl

**Ingredients:**
- 2 large chicken breasts
- 2 large sweet potatoes
- 1 avocado
- 1 cup quinoa
- 1 cup cherry tomatoes, halved
- 1/2 cup black beans, drained and rinsed
- 1/2 cup corn kernels
- 2 tablespoons olive oil
- 1 teaspoon paprika
- 1 teaspoon garlic powder
- Salt and pepper to taste
- Fresh cilantro for garnish

**Instructions:**
1. **Prepare the Chicken:**
   - Preheat your oven to 375°F (190°C).
   - Season the chicken breasts with olive oil, paprika, garlic powder, salt, and pepper.
   - Place the chicken on a baking sheet and bake for 25-30 minutes, or until fully cooked. Let it rest for 5 minutes before slicing.

2. **Cook the Sweet Potatoes:**
   - While the chicken is baking, peel and dice the sweet potatoes into 1-inch cubes.
   - Toss the sweet potato cubes with a bit of olive oil, salt, and pepper.
   - Spread them out on a separate baking sheet and roast in the oven for 20-25 minutes, or until tender.

3. **Prepare the Quinoa:**
   - Rinse the quinoa under cold water.
   - In a medium saucepan, combine 1 cup of quinoa with 2 cups of water and bring to a boil.
   - Reduce the heat to low, cover, and simmer for about 15 minutes, or until the water is absorbed and the quinoa is fluffy.

4. **Assemble the Bowl:**
   - In a large bowl, combine the cooked quinoa, sliced chicken, roasted sweet potatoes, cherry tomatoes, black beans, and corn.
   - Slice the avocado and add it to the bowl.
   - Drizzle with a bit more olive oil if desired and garnish with fresh cilantro.

### Meal 2: Beef and Vegetable Stir-Fry with Brown Rice

**Ingredients:**
- 1 lb (450g) flank steak, thinly sliced
- 2 cups broccoli florets
- 1 red bell pepper, sliced
- 1 yellow bell pepper, sliced
- 1 cup snap peas
- 2 carrots, julienned
- 3 cloves garlic, minced
- 1 tablespoon fresh ginger, minced
- 3 tablespoons soy sauce
- 2 tablespoons hoisin sauce
- 1 tablespoon sesame oil
- 2 tablespoons olive oil
- 2 cups cooked brown rice
- Sesame seeds for garnish
- Green onions for garnish

**Instructions:**
1. **Prepare the Steak:**
   - In a bowl, combine the sliced flank steak with 1 tablespoon of soy sauce and 1 tablespoon of olive oil. Let it marinate for at least 15 minutes.

2. **Cook the Vegetables:**
   - In a large skillet or wok, heat 1 tablespoon of olive oil over medium-high heat.
   - Add the minced garlic and ginger, and sauté until fragrant, about 1 minute.
   - Add the broccoli, bell peppers, snap peas, and carrots. Stir-fry for about 5-7 minutes, or until the vegetables are tender but still crisp. Transfer the vegetables to a plate and set aside.

3. **Cook the Steak:**
   - In the same skillet, add the sesame oil and marinated steak. Stir-fry for about 3-5 minutes, or until the steak is cooked to your desired level of doneness.

4. **Combine and Serve:**
   - Return the cooked vegetables to the skillet with the steak.
   - Add the remaining soy sauce and hoisin sauce. Stir to combine and cook for another 2-3 minutes until everything is well-coated and heated through.
   - Serve the beef and vegetable stir-fry over cooked brown rice.
   - Garnish with sesame seeds and sliced green onions.

These meals are designed to be moderate in difficulty to prepare and will provide a substantial amount of calories and nutrients to support your aggressive bulking goals. Enjoy!
"""

from info_helper import InformationHelper

inf = InformationHelper()

splits = string.split("###")
meal1 = splits[1]
# data = inf.parse_recipe(meal1)
name = meal1.split(":")[1].split("**")[0]
ingredients = meal1.split("**Ingredients:**")[1].split("**Instructions:**")[0]
recipe = meal1.split("**Instructions:**")[1]

print(name)