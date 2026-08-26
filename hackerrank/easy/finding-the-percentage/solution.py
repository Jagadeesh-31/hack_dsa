if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_scores = student_marks[query_name]
    
    # Calculate the average dynamically based on the number of scores
    avg = sum(query_scores) / len(query_scores)
    
    # Print formatted to exactly 2 decimal places
    print(f"{avg:.2f}")
