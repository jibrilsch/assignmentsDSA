def TowerOfHanoi(n, source, destination_rod, auxiliary_rod):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination_rod}")
        return
    TowerOfHanoi(n - 1, source, auxiliary_rod, destination_rod)
    print(f"Move disk {n} from {source} to {destination_rod}")
    TowerOfHanoi(n - 1, auxiliary_rod, destination_rod, source)

n = 3
TowerOfHanoi(n, 'A', 'C', 'B')
