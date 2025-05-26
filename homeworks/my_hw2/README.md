# Homework 2: Recipe Bot Error Analysys

## Part 1: Define Dimensions ^Generate Initial Queries

1. Identify the dimensions of the problem:
    
    I use ChatGPT to review my initial lists of dimensions and see if it can suggest any additional ones.

Here is the prompt I used:

```markdown
You are an expert Python programmer and chef.
I am making a recipe bot.
I have identified Key Dimensions, which are key aspects or variables of user inputs: 
- cuisine_type
- dietary_restriction
- meal_type
- food_allergies

Do you include or change any of them?
```

Here is the response I got:

```markdown
You're off to a solid start. Your current **Key Dimensions** cover many important axes for tailoring recipes. That said, depending on the scope of your recipe bot, I’d recommend **refining and potentially expanding** them to improve specificity and flexibility.

---

### 🔑 Your Current Dimensions (Reviewed)

1. **`cuisine_type`** – ✅

   * Good. Covers cultural/ethnic styles (e.g., Thai, Mexican). Consider normalizing with an ontology or list.

2. **`dietary_restriction`** – ✅/🔄

   * Valid, but ambiguous. It might be better to break this into:

     * **`diet_type`** (e.g., keto, vegan, paleo)
     * **`ethical_or_religious_restriction`** (e.g., halal, kosher)

3. **`meal_type`** – ✅

   * Great. Useful for context (e.g., breakfast, snack, dinner, dessert).

4. **`food_allergies`** – ✅

   * Essential for personalization and safety.

---

### 🧠 Additional Dimensions to Consider

Here are others worth including depending on how robust you want your bot:

5. **`main_ingredient`** or **`ingredient_focus`**

   * User wants to use up “chicken” or “zucchini” or “lentils.”
   * Helps drive relevance and reduce waste.

6. **`cooking_time`** / **`difficulty_level`**

   * Users often want quick, easy recipes (e.g., under 30 mins) or advanced ones.

7. **`available_equipment`**

   * E.g., air fryer, blender, sous-vide. Great for tailoring instructions and suggestions.

8. **`serving_size`** or **`number_of_servings`**

   * Impacts ingredient scaling and recipe recommendations.

9. **`flavor_profile`**

   * Optional but useful. E.g., spicy, umami, sweet, tangy — especially when matching cuisines or mood.

10. **`budget_level`**

* Users may want a budget-friendly meal or a splurge recipe.

---

### 📦 Recommended Final Set (Modular)

| Dimension                          | Description                            |
| ---------------------------------- | -------------------------------------- |
| `cuisine_type`                     | Cultural/geographical food style       |
| `diet_type`                        | Vegan, keto, gluten-free, etc.         |
| `ethical_or_religious_restriction` | Halal, kosher, etc.                    |
| `meal_type`                        | Breakfast, lunch, snack, dessert, etc. |
| `food_allergies`                   | Specific allergens to avoid            |
| `main_ingredient`                  | Ingredients to use or feature          |
| `cooking_time`                     | Time limit in minutes                  |
| `difficulty_level`                 | Easy, medium, hard                     |
| `available_equipment`              | Tools user has on hand                 |
| `serving_size`                     | How many people to cook for            |
| `flavor_profile`                   | Desired flavor(s): spicy, savory, etc. |
| `budget_level`                     | Low, medium, high                      |

This list gives you maximum flexibility without assuming every user will specify all values. A good bot can infer, ask follow-ups, or apply defaults.

Would you like help defining a schema or API structure around this?

```

2. Generate Unique Combinations (Tuples):

I use ChatGPT to generate unique combinations of the dimensions. Here is the prompt I used:

```markdown
I will use:
- cuisine_type
- diet_type
- ethical_or_religious_restriction
- meal_type
- food_allergies

Could you please generate 15-20 unique combinations (tuples and triples) of these dimension values?
```

Here is the response I got:

```markdown
Certainly! Below are **20 unique combinations** of 2 or 3 dimensions (tuples and triples) using your selected dimensions:

**Dimensions Used:**

* `cuisine_type`
* `diet_type`
* `ethical_or_religious_restriction`
* `meal_type`
* `food_allergies`

---

### 🧾 20 Unique Combinations

1. `(cuisine_type="Italian", diet_type="vegetarian")`
2. `(meal_type="breakfast", diet_type="keto")`
3. `(cuisine_type="Indian", ethical_or_religious_restriction="halal", food_allergies="dairy")`
4. `(diet_type="vegan", meal_type="dinner")`
5. `(cuisine_type="Japanese", food_allergies="shellfish")`
6. `(meal_type="lunch", diet_type="low-carb", food_allergies="gluten")`
7. `(cuisine_type="Mexican", diet_type="paleo")`
8. `(meal_type="snack", food_allergies="peanuts")`
9. `(cuisine_type="Middle Eastern", ethical_or_religious_restriction="kosher")`
10. `(diet_type="gluten-free", food_allergies="soy")`
11. `(cuisine_type="Thai", meal_type="dinner", food_allergies="tree nuts")`
12. `(diet_type="Mediterranean", ethical_or_religious_restriction="halal")`
13. `(meal_type="dessert", food_allergies="eggs")`
14. `(cuisine_type="Korean", meal_type="lunch")`
15. `(cuisine_type="French", diet_type="vegetarian", ethical_or_religious_restriction="kosher")`
16. `(diet_type="vegan", food_allergies="gluten")`
17. `(meal_type="breakfast", ethical_or_religious_restriction="halal")`
18. `(cuisine_type="Ethiopian", diet_type="whole30")`
19. `(cuisine_type="Chinese", food_allergies="MSG", diet_type="low-sodium")`
20. `(meal_type="dinner", diet_type="high-protein", food_allergies="dairy")`

---

These combinations cover a wide range of possible user intents and can serve as test cases or scenario prompts for recipe generation. Would you like a Python data structure (e.g. list of dicts) for these?
```

3. Generate Natural Language User Queries:

I use ChatGPT to generate natural language user queries based on the unique combinations. Here is the prompt I used:

```markdown
Please use the next combinations you give me:
`(meal_type="breakfast", diet_type="keto")`
`(cuisine_type="Indian", ethical_or_religious_restriction="halal", food_allergies="dairy")`
`(meal_type="lunch", diet_type="low-carb", food_allergies="gluten")`
`(diet_type="gluten-free", food_allergies="soy")`
`(diet_type="Mediterranean", ethical_or_religious_restriction="halal")`
`(meal_type="dessert", food_allergies="eggs")`
`(cuisine_type="Chinese", food_allergies="MSG", diet_type="low-sodium")`

Create natural language user queries with them that I can use to test my Recipe Bot for each selected tuple. Your output has to be in the CSV format:
id,query,dimension_tuple_json,is_realistic_and_kept,notes_for_filtering

The ID should be correlated.

Example:
SYN001,need easy dairy free curry recipes,"{""DietaryNeedsOrRestrictions"":""dairy-free"",""AvailableIngredientsFocus"":""no_specific_ingredients"",""CuisinePreference"":""specific_cuisine: indian"",""SkillLevelEffort"":""beginner_easy_low_effort"",""TimeAvailability"":""moderate_30_to_60_mins"",""QueryStyleAndDetail"":""short_keywords_minimal_detail""}",1,
SYN002,whats a simple indian dish no dairy,"{""DietaryNeedsOrRestrictions"":""dairy-free"",""AvailableIngredientsFocus"":""no_specific_ingredients"",""CuisinePreference"":""specific_cuisine: indian"",""SkillLevelEffort"":""beginner_easy_low_effort"",""TimeAvailability"":""moderate_30_to_60_mins"",""QueryStyleAndDetail"":""short_keywords_minimal_detail""}",1,
```

Here is the response I got:

```markdown
Here is a CSV-formatted output with synthetic user queries based on your specified combinations:


id,query,dimension_tuple_json,is_realistic_and_kept,notes_for_filtering
SYN001,what's a quick keto breakfast option,"{""meal_type"":""breakfast"",""diet_type"":""keto""}",1,
SYN002,any keto-friendly ideas for breakfast that aren't eggs,"{""meal_type"":""breakfast"",""diet_type"":""keto""}",1,
SYN003,halal indian recipes that don’t use any dairy,"{""cuisine_type"":""Indian"",""ethical_or_religious_restriction"":""halal"",""food_allergies"":""dairy""}",1,
SYN004,can you suggest dairy-free halal indian food?,"{""cuisine_type"":""Indian"",""ethical_or_religious_restriction"":""halal"",""food_allergies"":""dairy""}",1,
SYN005,need a low-carb lunch that’s also gluten free,"{""meal_type"":""lunch"",""diet_type"":""low-carb"",""food_allergies"":""gluten""}",1,
SYN006,any gluten-free low carb meals for lunch?,"{""meal_type"":""lunch"",""diet_type"":""low-carb"",""food_allergies"":""gluten""}",1,
SYN007,lunch ideas for someone eating low carb with gluten intolerance,"{""meal_type"":""lunch"",""diet_type"":""low-carb"",""food_allergies"":""gluten""}",1,
SYN008,what can I eat if I’m gluten free and allergic to soy?,"{""diet_type"":""gluten-free"",""food_allergies"":""soy""}",1,
SYN009,gluten free recipes without soy please,"{""diet_type"":""gluten-free"",""food_allergies"":""soy""}",1,
SYN010,looking for Mediterranean halal dishes,"{""diet_type"":""Mediterranean"",""ethical_or_religious_restriction"":""halal""}",1,
SYN011,halal Mediterranean meal ideas for dinner?,"{""diet_type"":""Mediterranean"",""ethical_or_religious_restriction"":""halal""}",1,
SYN012,I want a dessert that doesn’t use eggs,"{""meal_type"":""dessert"",""food_allergies"":""eggs""}",1,
SYN013,dessert recipes without eggs please,"{""meal_type"":""dessert"",""food_allergies"":""eggs""}",1,
SYN014,egg-free sweets or desserts for a party,"{""meal_type"":""dessert"",""food_allergies"":""eggs""}",1,
SYN015,low-sodium Chinese food without MSG?,"{""cuisine_type"":""Chinese"",""food_allergies"":""MSG"",""diet_type"":""low-sodium""}",1,
SYN016,I need a Chinese dish with no MSG and less salt,"{""cuisine_type"":""Chinese"",""food_allergies"":""MSG"",""diet_type"":""low-sodium""}",1,


Each query is phrased naturally and varies in tone and detail to simulate real user input. Let me know if you'd like a version with misspellings, informal phrasing, or voice-to-text-style queries.
```

I included new queries in other language, Spanish, to test the bot's multilingual capabilities. Here is the prompt I used:

```markdown
Generate another group of queries, but in Spanish, following the same rules, please. They do not have to be the translation of the previous ones. You can even include, sometimes, the number of people. Start the ID from SYN001.
```
Here is the response I got:

```markdown
Here is a new set of **Spanish-language synthetic user queries**, formatted in CSV as requested, using the same dimension tuples (not direct translations of the previous ones). IDs start again from `SYN001`.


id,query,dimension_tuple_json,is_realistic_and_kept,notes_for_filtering
SYN001,¿Qué puedo desayunar si sigo una dieta keto?,"{""meal_type"":""breakfast"",""diet_type"":""keto""}",1,
SYN002,Ideas de desayuno keto rápido para dos personas,"{""meal_type"":""breakfast"",""diet_type"":""keto""}",1,
SYN003,Busco recetas indias halal sin productos lácteos,"{""cuisine_type"":""Indian"",""ethical_or_religious_restriction"":""halal"",""food_allergies"":""dairy""}",1,
SYN004,¿Tienes platos indios halal sin leche ni queso?,"{""cuisine_type"":""Indian"",""ethical_or_religious_restriction"":""halal"",""food_allergies"":""dairy""}",1,
SYN005,Comida baja en carbohidratos para el almuerzo sin gluten,"{""meal_type"":""lunch"",""diet_type"":""low-carb"",""food_allergies"":""gluten""}",1,
SYN006,Recetas sin gluten y bajas en carbohidratos para almorzar con amigos,"{""meal_type"":""lunch"",""diet_type"":""low-carb"",""food_allergies"":""gluten""}",1,
SYN007,Soy intolerante al gluten y busco ideas bajas en carbohidratos para el almuerzo,"{""meal_type"":""lunch"",""diet_type"":""low-carb"",""food_allergies"":""gluten""}",1,
SYN008,¿Qué puedo comer si no puedo consumir gluten ni soya?,"{""diet_type"":""gluten-free"",""food_allergies"":""soy""}",1,
SYN009,Recetas fáciles sin gluten ni soya,"{""diet_type"":""gluten-free"",""food_allergies"":""soy""}",1,
SYN010,Platos mediterráneos que sean halal, por favor,"{""diet_type"":""Mediterranean"",""ethical_or_religious_restriction"":""halal""}",1,
SYN011,¿Tienes recetas halal con estilo mediterráneo para cuatro personas?,"{""diet_type"":""Mediterranean"",""ethical_or_religious_restriction"":""halal""}",1,
SYN012,Busco postres que no lleven huevo,"{""meal_type"":""dessert"",""food_allergies"":""eggs""}",1,
SYN013,¿Me das ideas de postres sin huevo para una fiesta?,"{""meal_type"":""dessert"",""food_allergies"":""eggs""}",1,
SYN014,Quiero hacer un dulce sin usar huevos,"{""meal_type"":""dessert"",""food_allergies"":""eggs""}",1,
SYN015,¿Qué comida china puedo hacer sin sal y sin glutamato?,"{""cuisine_type"":""Chinese"",""food_allergies"":""MSG"",""diet_type"":""low-sodium""}",1,
SYN016,Receta china sin MSG y baja en sodio para tres personas,"{""cuisine_type"":""Chinese"",""food_allergies"":""MSG"",""diet_type"":""low-sodium""}",1,


Let me know if you’d like a batch with voice-to-text patterns, slang, or mixed language (e.g., Spanglish) for more realism.
```

## Part 2: Initial Error Analysis (Ref Sec 3.2, 3.3, 3.4 of relevant course material)

1.  **Run Bot on Synthetic Queries:**
    *   Execute your Recipe Bot using the synthetic queries generated in Part 1.
    *   Record the full interaction traces for each query.

2.  **Open Coding:** (an initial analysis step where you review interaction traces, assigning descriptive labels/notes to identify patterns and potential errors without preconceived categories, as detailed in Sec 3.2 of the provided chapter)
    *   Review the recorded traces.
    *   Perform open coding to identify initial themes, patterns, and potential errors or areas for improvement in the bot's responses.

3.  **Axial Coding & Taxonomy Definition:** (a follow-up step where you group the initial open codes into broader, structured categories or 'failure modes' to build an error taxonomy, as described in Sec 3.3 of the provided chapter)
    *   Group the observations from open coding into broader categories or failure modes.
    *   For each identified failure mode, create a clear and concise taxonomy. This should include:
        *   **A clear Title** for the failure mode.
        *   **A concise one-sentence Definition** explaining the failure mode.
        *   **1-2 Illustrative Examples** taken directly from your bot's behavior during the tests. If a failure mode is plausible but not directly observed, you can provide a well-reasoned hypothetical example.

Using ChatGPT, I created a failure mode taxonomy based on the open coding I did. Here is the prompt I used:

```markdown
Below is a list of open-ended annotations describing failures
in an LLM-driven real estate CRM assistant. Please group
them into a small set of coherent failure categories, where
each category captures similar types of mistakes. Each group
should have a short descriptive title and a brief one-line
definition. Do not invent new failure types; only cluster
based on what is present in the notes.

id,query,dimension_tuple_json,is_realistic_and_kept,notes_for_filtering
SYN001,¿Qué puedo desayunar si sigo una dieta keto?,"{""meal_type"":""breakfast"",""diet_type"":""keto""}",1,"Los títulos de las secciones aparecen en inglés en lugar del idioma de la consulta. Da la receta para dos personas aunque la consulta no lo especifica directamente, aunque da a entender que es una una sóla."
SYN002,Ideas de desayuno paleto rápido para dos personas,"{""meal_type"":""breakfast"",""diet_type"":""paleto""}",1,"Los títulos de las secciones aparecen en inglés en lugar del idioma de la consulta."
SYN003,Busco recetas indias halal sin productos lácteos,"{""cuisine_type"":""Indian"",""ethical_or_religious_restriction"":""halal"",""food_allergies"":""dairy""}",1,""
SYN004,¿Tienes platos del Mediterráneo que sean kosher pero sin leche ni queso?,"{""cuisine_type"":""Mediterranean"",""ethical_or_religious_restriction"":""kosher"",""food_allergies"":""dairy""}",1,"Los títulos de las secciones aparecen en inglés en lugar del idioma de la consulta."
SYN005,Comida baja en carbohidratos para el almuerzo sin gluten,"{""meal_type"":""lunch"",""diet_type"":""low-carb"",""food_allergies"":""gluten""}",1,"Da la receta para dos personas aunque la consulta no lo especifica directamente, aunque da a entender que es una una sóla."
SYN006,Recetas sin gluten y bajas en carbohidratos para almorzar con amigos,"{""meal_type"":""lunch"",""diet_type"":""low-carb"",""food_allergies"":""gluten""}",1,"Los títulos de las secciones aparecen en inglés en lugar del idioma de la consulta."
SYN007,Soy intolerante al gluten y busco ideas bajas en carbohidratos para el almuerzo,"{""meal_type"":""lunch"",""diet_type"":""low-carb"",""food_allergies"":""gluten""}",1,"Los títulos de las secciones aparecen en inglés en lugar del idioma de la consulta. Da la receta para cuatro personas aunque la consulta no lo especifica el número de comensales."
SYN008,¿Qué puedo comer si no puedo consumir gluten ni soya porque soy alérgico a esta?,"{""diet_type"":""gluten-free"",""food_allergies"":""soy""}",1,"Los títulos de las secciones aparecen en inglés en lugar del idioma de la consulta."
SYN009,Recetas fáciles sin gluten ni soya,"{""diet_type"":""gluten-free"",""food_allergies"":""soy""}",1,"Los títulos de las secciones aparecen en inglés en lugar del idioma de la consulta."
SYN010,"Platos mediterráneos que sean halal, por favor","{""diet_type"":""Mediterranean"",""ethical_or_religious_restriction"":""halal""}",1,"Los títulos de las secciones aparecen en inglés en lugar del idioma de la consulta. Da la receta para dos personas aunque la consulta no lo especifica directamente, aunque da a entender que es una una sóla."
SYN011,¿Tienes recetas halal con estilo mediterráneo para cuatro personas?,"{""diet_type"":""Mediterranean"",""ethical_or_religious_restriction"":""halal""}",1,""
SYN012,Busco postres que no lleven huevo,"{""meal_type"":""dessert"",""food_allergies"":""eggs""}",1,""
SYN013,¿Me das ideas de postres sin huevo para una fiesta?,"{""meal_type"":""dessert"",""food_allergies"":""eggs""}",1,"Los títulos de las secciones aparecen en inglés en lugar del idioma de la consulta."
SYN014,Quiero hacer un dulce sin usar huevos,"{""meal_type"":""dessert"",""food_allergies"":""eggs""}",1,""
SYN015,¿Qué comida china puedo hacer sin sal y sin glutamato?,"{""cuisine_type"":""Chinese"",""food_allergies"":""MSG"",""diet_type"":""low-sodium""}",1,""
SYN016,Receta china sin MSG y baja en sodio para tres personas,"{""cuisine_type"":""Chinese"",""food_allergies"":""MSG"",""diet_type"":""low-sodium""}",1,"Los títulos de las secciones aparecen en inglés en lugar del idioma de la consulta."
```
The response I got:

```markdown
Here’s a structured grouping of the annotation notes into coherent **failure categories**, based only on the types of issues explicitly present in your dataset:

---

### **1. Localization Errors**

**Definition**: Interface elements or outputs (e.g., section titles) are not correctly translated to the user's language.

**Examples:**

* "Los títulos de las secciones aparecen en inglés en lugar del idioma de la consulta."

  * SYN001
  * SYN002
  * SYN004
  * SYN006
  * SYN007
  * SYN008
  * SYN009
  * SYN010
  * SYN013
  * SYN016

---

### **2. Incorrect Assumption of Number of People**

**Definition**: The assistant assumes a serving size or number of diners that wasn't explicitly mentioned and doesn't logically follow from the query.

**Examples:**

* "Da la receta para dos personas aunque la consulta no lo especifica directamente, aunque da a entender que es una una sóla."

  * SYN001
  * SYN005
  * SYN010

* "Da la receta para cuatro personas aunque la consulta no lo especifica el número de comensales."

  * SYN007

---

### **3. No Failure Noted**

**Definition**: Entries where no error or issue was annotated in the `notes_for_filtering` field.

**Examples:**

* SYN003
* SYN011
* SYN012
* SYN014
* SYN015

---

Let me know if you'd like a visual or tabular summary of this categorization, or a version ready to feed into an error classification model.
```


4.  **[Optional] Spreadsheet for Analysis:**
    *   Create a spreadsheet to systematically track your error analysis.
    *   Include the following columns:
        *   `Trace_ID` (a unique identifier for each interaction)
        *   `User_Query` (the query given to the bot)
        *   `Full_Bot_Trace_Summary` (a summary of the bot's full response and behavior)
        *   `Open_Code_Notes` (your notes and observations from the open coding process)
        *   A column for each of your 3-5 defined `Failure_Mode_Title`s (use 0 or 1 to indicate the presence or absence of that failure mode in the trace).


I complete the spreadsheet using GH Copilot - Claude 3.7 Sonnet - with the following prompt:

```markdown
Completa los valores de las columnas: Localization_Errors,Incorrect_Assumption_Number_People,
Para cada registro, basándote en el valor de la columna: Open_Code_Notes.
```
The resulting spreadsheet should look like this:
```markdown
id,query,dimension_tuple_json,is_realistic_and_kept,Open_Code_Notes,Localization_Errors,Incorrect_Assumption_Number_People,
SYN001,¿Qué puedo desayunar si sigo una dieta keto?,"{""meal_type"":""breakfast"",""diet_type"":""keto""}",1,"Los títulos de las secciones aparecen en inglés en lugar del idioma de la consulta. Da la receta para dos personas aunque la consulta no lo especifica directamente, aunque da a entender que es una una sóla.",1,1
SYN002,Ideas de desayuno paleto rápido para dos personas,"{""meal_type"":""breakfast"",""diet_type"":""paleto""}",1,"Los títulos de las secciones aparecen en inglés en lugar del idioma de la consulta.",1,0
SYN003,Busco recetas indias halal sin productos lácteos,"{""cuisine_type"":""Indian"",""ethical_or_religious_restriction"":""halal"",""food_allergies"":""dairy""}",1,"",0,0
SYN004,¿Tienes platos del Mediterráneo que sean kosher pero sin leche ni queso?,"{""cuisine_type"":""Mediterranean"",""ethical_or_religious_restriction"":""kosher"",""food_allergies"":""dairy""}",1,"Los títulos de las secciones aparecen en inglés en lugar del idioma de la consulta.",1,0
SYN005,Comida baja en carbohidratos para el almuerzo sin gluten,"{""meal_type"":""lunch"",""diet_type"":""low-carb"",""food_allergies"":""gluten""}",1,"Da la receta para dos personas aunque la consulta no lo especifica directamente, aunque da a entender que es una una sóla.",0,1
SYN006,Recetas sin gluten y bajas en carbohidratos para almorzar con amigos,"{""meal_type"":""lunch"",""diet_type"":""low-carb"",""food_allergies"":""gluten""}",1,"Los títulos de las secciones aparecen en inglés en lugar del idioma de la consulta.",1,0
SYN007,Soy intolerante al gluten y busco ideas bajas en carbohidratos para el almuerzo,"{""meal_type"":""lunch"",""diet_type"":""low-carb"",""food_allergies"":""gluten""}",1,"Los títulos de las secciones aparecen en inglés en lugar del idioma de la consulta. Da la receta para cuatro personas aunque la consulta no lo especifica el número de comensales.",1,1
SYN008,¿Qué puedo comer si no puedo consumir gluten ni soya porque soy alérgico a esta?,"{""diet_type"":""gluten-free"",""food_allergies"":""soy""}",1,"Los títulos de las secciones aparecen en inglés en lugar del idioma de la consulta.",1,0
SYN009,Recetas fáciles sin gluten ni soya,"{""diet_type"":""gluten-free"",""food_allergies"":""soy""}",1,"Los títulos de las secciones aparecen en inglés en lugar del idioma de la consulta.",1,0
SYN010,"Platos mediterráneos que sean halal, por favor","{""diet_type"":""Mediterranean"",""ethical_or_religious_restriction"":""halal""}",1,"Los títulos de las secciones aparecen en inglés en lugar del idioma de la consulta. Da la receta para dos personas aunque la consulta no lo especifica directamente, aunque da a entender que es una una sóla.",1,1
SYN011,¿Tienes recetas halal con estilo mediterráneo para cuatro personas?,"{""diet_type"":""Mediterranean"",""ethical_or_religious_restriction"":""halal""}",1,"",0,0
SYN012,Busco postres que no lleven huevo,"{""meal_type"":""dessert"",""food_allergies"":""eggs""}",1,"",0,0
SYN013,¿Me das ideas de postres sin huevo para una fiesta?,"{""meal_type"":""dessert"",""food_allergies"":""eggs""}",1,"Los títulos de las secciones aparecen en inglés en lugar del idioma de la consulta.",1,0
SYN014,Quiero hacer un dulce sin usar huevos,"{""meal_type"":""dessert"",""food_allergies"":""eggs""}",1,"",0,0
SYN015,¿Qué comida china puedo hacer sin sal y sin glutamato?,"{""cuisine_type"":""Chinese"",""food_allergies"":""MSG"",""diet_type"":""low-sodium""}",1,"",0,0
SYN016,Receta china sin MSG y baja en sodio para tres personas,"{""cuisine_type"":""Chinese"",""food_allergies"":""MSG"",""diet_type"":""low-sodium""}",1,"Los títulos de las secciones aparecen en inglés en lugar del idioma de la consulta.",1,0
```

---