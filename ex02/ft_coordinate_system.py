import math


def get_player_pos() -> tuple:
    while True:
        input_values = input("Enter new coordinates as "
                             "floats in format 'x,y,z': ")
        try:
            string_val = []
            current_string = ""

            for char in input_values:
                if char == ',':
                    string_val += [current_string]
                    current_string = ""
                else:
                    current_string += char
            string_val += [current_string]

            if len(string_val) != 3:
                print("Invalid syntax")
                continue

            x = float(string_val[0])
            y = float(string_val[1])
            z = float(string_val[2])
            return (x, y, z)

        except ValueError:
            bad_part = ""
            for p in string_val:
                try:
                    float(p)
                except ValueError:
                    bad_part = p
                    break
            print(f"Error on parameter '{bad_part}': "
                  f"could not convert string to float")


if __name__ == "__main__":
    player1 = get_player_pos()
    print(f"Got a first tuple: {player1}")
    print(f"It includes: X={player1[0]}, Y={player1[1]}, Z={player1[2]}")

    distance_to_center = round(math.sqrt(
        (player1[0] - 0) ** 2 +
        (player1[1] - 0) ** 2 +
        (player1[2] - 0) ** 2), 4)

    print(f"Distance to center: {distance_to_center}")
    print("\nGet a second set of coordinates")
    player2 = get_player_pos()

    distance_between = round(math.sqrt(
        (player2[0] - player1[0]) ** 2 +
        (player2[1] - player1[1]) ** 2 +
        (player2[2] - player1[2]) ** 2
    ), 4)
    print(f"Distance between the 2 sets of coordinates: {distance_between}")
