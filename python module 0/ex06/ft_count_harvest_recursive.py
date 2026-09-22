def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def recursive(days_num: int, day1: int = 1) -> None:
        print(f"Day {day1}")
        if day1 < days:
            recursive(days, day1 + 1)
    recursive(days)
    print("Harvest time!")
