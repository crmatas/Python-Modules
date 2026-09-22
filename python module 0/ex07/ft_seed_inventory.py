def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if seed_type == "" or unit == "":
        return
    seed_type = seed_type.capitalize()
    print(seed_type + " seeds: ", end="")
    if unit == "packets":
        print(str(quantity) + " packets available")
    elif unit == "grams":
        print(str(quantity) + " grams total")
    elif unit == "area":
        print("covers " + str(quantity) + " square meters")
    else:
        print("Unknown unit type")
