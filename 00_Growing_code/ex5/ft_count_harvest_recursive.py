def ft_recursive(last_day: int) -> None:
    if last_day > 1:
        ft_recursive(last_day - 1)
    print("Day", last_day)


def ft_count_harvest_recursive() -> None:
    last_day: int = int(input("Days until harvest: "))
    ft_recursive(last_day)
    print("Harvest time!")
