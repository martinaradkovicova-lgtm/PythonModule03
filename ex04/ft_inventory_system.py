import sys

print("=== Inventory System Analysis ===")

inventory = {}
for arg in sys.argv[1:]:
    # Zjištění pozice dvojtečky ručně bez .find()
    colon_idx = -1
    for i in range(len(arg)):
        if arg[i] == ":":
            colon_idx = i
            break

    if colon_idx == -1:
        print(f"Error - invalid parameter '{arg}'")
        continue

    item_name = arg[:colon_idx]
    quantity_str = arg[colon_idx + 1:]

    if item_name in inventory:
        print(f"Redundant item '{item_name}' - discarding")
        continue

    try:
        quantity = int(quantity_str)
    except ValueError:
        print(
          f"Quantity error for '{item_name}': "
          f"invalid literal for int() with base"
          f" 10: '{quantity_str}'")
        continue

    inventory[item_name] = quantity

print(f"Got inventory: {inventory}")

items_list = list(inventory.keys())
print(f"Item list: {items_list}")

if inventory:
    total_qty = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")

    for name, qty in inventory.items():
        percentage = round((qty / total_qty) * 100, 1)
        print(f"Item {name} represents {percentage}%")

    items_keys = list(inventory.keys())
    most_abundant = items_keys[0]
    least_abundant = items_keys[0]

    for name in inventory:
        if inventory[name] > inventory[most_abundant]:
            most_abundant = name
        if inventory[name] < inventory[least_abundant]:
            least_abundant = name

    print(
      f"Item most abundant: {most_abundant} with quantity"
      f" {inventory[most_abundant]}")
    print(
      f"Item least abundant: {least_abundant} with quantity"
      f" {inventory[least_abundant]}")

    inventory["magic_item"] = 1
    print(f"Updated inventory: {inventory}")
