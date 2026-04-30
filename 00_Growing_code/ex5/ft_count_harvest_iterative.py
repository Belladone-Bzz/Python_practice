def ft_count_harvest_iterative() -> None:
    last_day: range = range(int(input("Days until harvest: ")))
    count: int = 0
    for count in last_day:
        print(f"Day {count + 1}")
        count += 1
    print("Harvest time!")
