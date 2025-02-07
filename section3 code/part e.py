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
    
    return steps

def compute_statistics():
    size = 30  # Limit for a and b
    results = np.zeros((size - 1, size - 1))
    
    for L_a in range(2, size + 1):
        for L_b in range(2, size + 1):
            step_counts = []
            for _ in range(10):  # Test 10 random binary pairs of the same length
                a = ''.join(random.choice('01') for _ in range(L_a))
                b = ''.join(random.choice('01') for _ in range(L_b))
                steps = turing_machine_multiplication(a, b)
                step_counts.append(steps)
            
            avg_steps = sum(step_counts) / len(step_counts)
            results[L_a - 2, L_b - 2] = avg_steps
    
    # Save heatmap
    plt.figure(figsize=(10, 8))
    plt.imshow(results, cmap='hot', interpolation='nearest', origin='lower')
    plt.colorbar(label='Average Steps ⟨n⟩')
    plt.xlabel('b (Length of second binary number)')
    plt.ylabel('a (Length of first binary number)')
    plt.xticks(np.arange(size - 1), np.arange(2, size + 1))
    plt.yticks(np.arange(size - 1), np.arange(2, size + 1))
    plt.title('2D Heatmap of Average Computation Complexity ⟨n⟩')
    plt.savefig("complexity_heatmap.png")
    plt.show()

if __name__ == "__main__":
    compute_statistics()
