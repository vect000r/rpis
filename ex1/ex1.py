import random
import math

def estimate_pi(N:int)-> float:
    points_inside = 0
    
    for _ in range(N):
        # Generujemy losowe punkty w kwadracie [0,1] x [0,1]
        x = random.random()
        y = random.random()
        
        # Sprawdzamy czy punkt leży wewnątrz ćwiartki koła
        # poprzez obliczenie odległości od punktu (0,0)
        distance = math.sqrt(x**2 + y**2)
        
        if distance <= 1:
            points_inside += 1
    
    # Obliczamy pi na podstawie proporcji punktów
    pi_estimate = 4 * points_inside / N
    return pi_estimate

N_values = [10, 100, 1000, 100000, 1000000, 10000000, 100000000]

print("Wyniki obliczeń liczby pi:")
print("-" * 50)
print(f"{'N':>10} | {'Oszacowane pi':>15} | {'Błąd bezwzględny':>15}")
print("-" * 50)

for N in N_values:
    pi_estimate = estimate_pi(N)
    absolute_error = abs(math.pi - pi_estimate)
    
    print(f"{N:>10} | {pi_estimate:>15.10f} | {absolute_error:>15.10f}")

print("-" * 50)
print(f"Rzeczywista wartość pi = {math.pi}")