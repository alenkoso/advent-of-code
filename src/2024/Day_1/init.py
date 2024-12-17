from collections import Counter

def parse_input(file_path):
    left_list = []
    right_list = []
    with open(file_path) as file:
        for line in file:
            if line.strip():
                left_value, right_value = map(int, line.split())
                left_list.append(left_value)
                right_list.append(right_value)
    return left_list, right_list

def compute_distance(left_list, right_list):
    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)
    total_distance = 0
    for left_value, right_value in zip(sorted_left, sorted_right):
        total_distance += abs(left_value - right_value)
    return total_distance

def compute_similarity(left_list, right_list):
    occurrence_count = Counter(right_list)
    similarity_score = 0
    for value in left_list:
        similarity_score += value * occurrence_count[value]
    return similarity_score

def main():
    left_list, right_list = parse_input("input.txt")
    
    total_distance = compute_distance(left_list, right_list)
    print(total_distance)
    
    similarity_score = compute_similarity(left_list, right_list)
    print(similarity_score)

if __name__ == "__main__":
    main()
