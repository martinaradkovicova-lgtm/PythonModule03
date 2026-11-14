import sys


def print_header() -> None:
    print("=== Command Quest ===")


def argc() -> int:
    return len(sys.argv)


def total_count() -> None:
    print(f"Total count: {argc()}")


def check_args_errors() -> bool:
    return (len(sys.argv) <= 1)


if __name__ == "__main__":
    print_header()
    if check_args_errors() is False:
        print(f"Program name: {sys.argv[0]}")
        print(f"Argument received: {argc() - 1}")
        i = 1
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i = i + 1
        total_count()
    else:
        print("No arguments provided!")
        total_count()
