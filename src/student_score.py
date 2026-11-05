PASS_THRESHOLD = 5


def calculate_average(scores):
    if not scores:
        raise ValueError("scores must not be empty")
    return sum(scores) / len(scores)


def get_student_result(scores):
    average = calculate_average(scores)
    result = "PASS" if average >= PASS_THRESHOLD else "FAIL"
    return average, result


def print_student_result(name, scores):
    average, result = get_student_result(scores)
    print("Student:", name)
    print("Average:", average)
    print("Result:", result)


if __name__ == "__main__":
    scores = [8, 7, 9, 6]
    print_student_result("Student A", scores)
