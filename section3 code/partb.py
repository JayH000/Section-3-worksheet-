import itertools

def binary_multiply(a: str, b: str) -> str:
    # Performs binary multiplication using integer conversion.
    return bin(int(a, 2) * int(b, 2))[2:]

def turing_machine_multiplication(a: str, b: str):
    # Simulates a Turing Machine that performs binary multiplication.
    # Define tape as a list to allow modifications
    result = binary_multiply(a, b)
    tape = list(f'{a}*{b}={result}')
    tape_length = len(tape)
    head_position = 0
    
    filename = f"multiplication_{a}_x_{b}.dat"
    with open(filename, 'w') as f:
        for step in itertools.count():
            # Write the current state of the tape
            f.write("".join(tape) + "\n")
            
            # Simulate the Turing Machine's movement (basic right shift here)
            if head_position < tape_length - 1:
                head_position += 1
            else:
                break  # Stop when reaching the end
    
    print(f"Simulation complete. Output saved in {filename}")

if __name__ == "__main__":
    test_cases = [("101001010111", "101000101"), ("101111", "101001")]
    for a, b in test_cases:
        turing_machine_multiplication(a, b)
