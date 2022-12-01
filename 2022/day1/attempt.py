
# Input is calories
# Each elves calories are separated by a blank line
# Need to find which elf carries the most calories and provide the total

# Read each line 
# IF there is a value, sum it the previous one
# IF there is a blank line compare the sum to the current max
# IF the current max is lower than the sum then replace it

def load_input():
    input_file = open('input.txt', 'r')
    lines = input_file.readlines()
    return lines


def traverse_input(lines):
    current_max = []
    current_sum = 0
    filled_max = False

    for line in lines:
        if len(line) > 2:
            calorie = int(line.strip())
            current_sum += calorie
            
        else:
            current_max.sort()

            if filled_max:
                for i, max in enumerate(current_max):
                    if current_sum > max:
                        current_max[i] = current_sum
                        break
            else:
                current_max.append(current_sum)

                if len(current_max) == 3:
                    filled_max = True


            current_sum = 0

    return sum(current_max)

if __name__ == "__main__":
    lines = load_input()
    result = traverse_input(lines)

    print(f"The most calories are {result}")
    
