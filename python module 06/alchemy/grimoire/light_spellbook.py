from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validate = validate_ingredients(ingredients)
    if validate.count("VALID") > 0:
        return f"Spell recorded '{spell_name}' ({validate})"
    else:
        return f"Spell rejected '{spell_name}' ({validate})"
    # valiadation from validation funtion
