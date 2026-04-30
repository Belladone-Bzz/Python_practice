def ft_water_reminder() -> None:
    last_water: int = int(input("Days since last watering: "))
    if last_water > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
