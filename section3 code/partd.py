import itertools
import random
import matplotlib.pyplot as plt
import numpy as np

def binary_multiply(a: str, b: str) -> str:
    # Performs binary multiplication using integer conversion.
    return bin(int(a, 2) * int(b, 2))[2:]

def turing_machine_multiplication(a: str, b: str):
    # Simulates a Turing Machine that performs binary multiplication.
    result = binary_multiply(a, b)
    tape = list(f'{a}*{b}={result}')
    tape_length = len(tape)
    head_position = 0
    steps = 0
    
    filename = f"multiplication_{a}_x_{b}.dat"
    with open(filename, 'w') as f:
        for step in itertools.count():
            f.write("".join(tape) + "\n")
            steps += 1
            if head_position < tape_length - 1:
                head_position += 1
            else:
                break  # Stop when reaching the end
    
    print(f"Simulation complete. Output saved in {filename}")
    return steps

def compute_statistics():
    test_lengths = [(2, 3), (3, 2), (3, 5), (5, 3), (3, 12), (12, 3)]
    results = {}
    
    for L_a, L_b in test_lengths:
        step_counts = []
        for _ in range(10):  # Test 10 random binary pairs of the same length
            a = ''.join(random.choice('01') for _ in range(L_a))
            b = ''.join(random.choice('01') for _ in range(L_b))
            steps = turing_machine_multiplication(a, b)
            step_counts.append(steps)
        
        results[(L_a, L_b)] = step_counts
        
        # Compute min, max, and average
        min_steps = min(step_counts)
        max_steps = max(step_counts)
        avg_steps = sum(step_counts) / len(step_counts)
        
        # Write statistics to file
        with open("complexity_results.txt", "a") as f:
            f.write(f"L({L_a},{L_b}): Min={min_steps}, Max={max_steps}, Avg={avg_steps}\n")
        
        # Plot histogram
        plt.hist(step_counts, bins=range(min_steps, max_steps+2), alpha=0.7, edgecolor='black')
        plt.xlabel("Number of Steps (n)")
        plt.ylabel("Frequency")
        plt.title(f"Histogram of Steps for L({L_a},{L_b})")
        plt.savefig(f"histogram_L{L_a}_{L_b}.png")
        plt.clf()

if __name__ == "__main__":
    compute_statistics()
