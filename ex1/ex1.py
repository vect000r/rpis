import random
import math
import matplotlib.pyplot as plt

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

print("Wyniki obliczeń liczby π:")
print("-" * 50)
print(f"{'N':>10} | {'Oszacowane π':>15} | {'Błąd bezwzględny':>15}")
print("-" * 50)

estimates = []
errors = []

for N in N_values:
    pi_estimate = estimate_pi(N)
    absolute_error = abs(math.pi - pi_estimate)
    estimates.append(pi_estimate)
    errors.append(absolute_error)
    print(f"{N:>10} | {pi_estimate:>15.10f} | {absolute_error:>15.10f}")

print("-" * 50)
print(f"Rzeczywista wartość π = {math.pi}")


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
fig.suptitle('Monte Carlo Pi Estimation Analysis', fontsize=14)


ax1.semilogx(N_values, estimates, 'ro-', label='Estimated π', markersize=8)
ax1.axhline(math.pi, color='blue', linestyle='--', label='Actual π')
ax1.fill_between(N_values, [math.pi - 0.01]*len(N_values), 
                 [math.pi + 0.01]*len(N_values), color='blue', alpha=0.1,
                 label='±0.01 range')
ax1.grid(True, which="both", ls="-", alpha=0.2)
ax1.set_xlabel('Number of Points (N)', fontsize=10)
ax1.set_ylabel('Estimated Value of π', fontsize=10)
ax1.legend()
ax1.set_title('Convergence to π')

ax2.loglog(N_values, errors, 'go-', label='Absolute Error', markersize=8)
ax2.grid(True, which="both", ls="-", alpha=0.2)
ax2.set_xlabel('Number of Points (N)', fontsize=10)
ax2.set_ylabel('Absolute Error', fontsize=10)
ax2.legend()
ax2.set_title('Error Analysis')


plt.tight_layout()
plt.show()