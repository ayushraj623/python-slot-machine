import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 2

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns: list[list[str]], lines: int, bet: int, values: dict[str, int]) -> tuple[int, list[int]]:
    """Evaluate the slot machine grid to calculate winnings across active lines."""
    winnings = 0
    winning_lines = []
    
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows: int, cols: int, symbols: dict[str, int]) -> list[list[str]]:
    """Generates a randomized grid of symbols for the slot machine."""
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns: list[list[str]]) -> None:
    """Prints the slot machine columns in a clean, formatted grid."""
    for row in range(len(columns[0])):
        # Isolate the current row and join the symbols with a pipe
        current_row = [column[row] for column in columns]
        print(" | ".join(current_row))

def deposit() -> int:
    """Prompts the user to deposit a valid starting balance."""
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")
    return amount

def get_number_of_lines() -> int:
    """Prompts the user to select the number of lines to bet on."""
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Enter a valid number of lines (1-{MAX_LINES}).")
        else:
            print("Please enter a valid number.")
    return lines

def get_bet() -> int:
    """Prompts the user for their bet amount per line."""
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a valid number.")
    return amount

def spin(balance: int) -> int:
    """Executes a single spin, calculates bets, and determines the outcome."""
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print
