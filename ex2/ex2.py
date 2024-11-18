import random
import numpy as np
from collections import Counter

def simulate_card_draw():
    # Tworzymy talie kart (0-12: trefle, 13-25: karo, 26-38: kier, 39-51: piki)
    deck = list(range(52))
    # Wyciagamy 3 karty
    drawn_cards = random.sample(deck, 3)
    # Sprawdź czy którakolwiek z kart jest treflem
    return not any(card < 13 for card in drawn_cards)

def estimate_probability(num_trials):
    successes = sum(simulate_card_draw() for _ in range(num_trials))
    return successes / num_trials

def find_required_trials():
    target_accuracy = 0.001 
    trials = 1000
    prev_prob = 0
    curr_prob = estimate_probability(trials)
    
    while True:
        trials *= 2
        prev_prob = curr_prob
        curr_prob = estimate_probability(trials)
        
        if abs(curr_prob - prev_prob) < target_accuracy:
            return trials, curr_prob

# Liczymy prawdopodobienstwo teoretyczne
total_cards = 52
club_cards = 13
theoretical_prob = (
    (39/52) * (38/51) * (37/50) 
)

# Uruchamiamy symulacje
required_trials, estimated_prob = find_required_trials()

print(f"Liczba przeprowadzonych prób: {required_trials}")
print(f"Oszacowane prawdopodobieństwo: {estimated_prob:.4f}")
print(f"Teoretyczne prawdopodobieństwo: {theoretical_prob:.4f}")
print(f"Różnica: {abs(estimated_prob - theoretical_prob):.4f}")

# Pojedyncze losowanie
single_draw_result = simulate_card_draw()
print(f"\nPrzykładowe pojedyncze losowanie:")
print("Wynik: " + ("brak trefli" if single_draw_result else "znaleziono trefla"))