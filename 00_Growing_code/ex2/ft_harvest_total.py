def ft_harvest_total() -> None:
    weight_d1: int = int(input("Day 1 harvest: "))
    weight_d2: int = int(input("Day 2 harvest: "))
    weight_d3: int = int(input("Day 3 harvest: "))
    total: int = weight_d1 + weight_d2 + weight_d3
    print("Total harvest:", total)
