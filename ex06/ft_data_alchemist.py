import random

print("=== Game Data Alchemist ===")

# Počáteční seznam hráčů podle zadání
initial_players = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam",
]
print(f"Initial list of players: {initial_players}")

# 1. Seznamová komprehenze: Všechna jména s velkým prvním písmenem
all_capitalized = [name.capitalize() for name in initial_players]
print(f"New list with all names capitalized: {all_capitalized}")

# 2. Seznamová komprehenze: Ponechat jen ty, které už začínaly velkým písmenem
only_capitalized = [name for name in initial_players if name[0].isupper()]
print(f"New list of capitalized names only: {only_capitalized}")

# 3. Slovníková komprehenze: Jméno jako klíč, náhodné skóre jako hodnota
score_dict = {name: random.randint(1, 1000) for name in all_capitalized}
print(f"Score dict: {score_dict}")

# 4. Výpočet průměrného skóre (pomocí povolených sum, len, round)
score_average = round(sum(score_dict.values()) / len(score_dict), 2)
print(f"Score average is {score_average}")

# 5. Slovníková komprehenze: Filtrování skóre vyšších než průměr
high_scores = {
    name: score for name, score in score_dict.items() if score > score_average
}
print(f"High scores: {high_scores}")
