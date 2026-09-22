
def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allow_ingredients = light_spell_allowed_ingredients()
    for ingre in allow_ingredients:
        if ingredients.count(ingre) > 0:
            break
        else:
            return ingredients + " - INVALID"
    return ingredients + " - VALID"
    # string with the ingredients and valid or invalid
