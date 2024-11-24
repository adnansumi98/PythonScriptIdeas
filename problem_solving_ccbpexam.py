import itertools

def max_min_sum(input_string):
    # Convert the input string to a list of integers
    numbers = list(map(int, input_string.split()))

    # Total indices of the numbers
    indices = range(len(numbers))
    max_sum = float('-inf')  # Initialize max_sum to the smallest possible value

    # Generate all unique ways to split indices into pairs
    for pair_combination in itertools.combinations(itertools.combinations(indices, 2), len(numbers) // 2):
        # Ensure pairs are non-overlapping
        used_indices = set()
        valid = True
        for pair in pair_combination:
            if set(pair) & used_indices:  # Check for overlap
                valid = False
                break
            used_indices.update(pair)
        if not valid:
            continue

        # Calculate the sum of minimums of the pairs
        min_sum = sum(min(numbers[pair[0]], numbers[pair[1]]) for pair in pair_combination)
        # Update the maximum sum
        max_sum = max(max_sum, min_sum)

    return max_sum

# Example usage
input_string = "7 3 7 6 2 3"
result = max_min_sum(input_string)
print(result)


def print_k(n):
    rows = 2 * n - 1  # Total rows in the pattern
    mid = n - 1  # Middle row index (0-based)

    for i in range(rows):
        if i <= mid:
            # Upper part: left star and diagonal towards middle
            print("* " + "  " * (mid - i) + "*")
        else:
            # Lower part: left star and diagonal away from middle
            print("* " + "  " * (i - mid) + "*")

# Example usage
n = int(input("Enter the value of N: "))
print_k(n)


def convert_chemical_formula(input_formula):
    atom_count = {}

    for atom in input_formula:
        if atom in atom_count:
            atom_count[atom] += 1
        else:
            atom_count[atom] = 1

    output_formula = ""
    for atom, count in atom_count.items():
        output_formula += f"{atom}{count}+"

    return output_formula[:-1]  # Remove the extra plus sign at the end

# Input chemical formula
input_formula = "HHOOCHH"

# Convert and print the output
output_formula = convert_chemical_formula(input_formula)
print(output_formula)


def find_largest_group(M, N, B):
    # Remove numbers from M that appear in N
    updated_M = [num for num in M if num not in N]

    # Sort the updated list in descending order
    updated_M.sort(reverse=True)

    # Initialize variables
    current_sum = 0
    largest_group = []

    # Find the largest group whose sum is less than or equal to B
    for num in updated_M:
        if current_sum + num <= B:
            largest_group.append(num)
            current_sum += num

    # Print the sum of the numbers in the group
    print(sum(largest_group))

# Example usage
M = [1, 2, 3, 4, 5]
N = [2, 4]
B = 8

find_largest_group(M, N, B)
