grade = float(input("grade : "))

score = ""

if grade >= 86:
    score = "A"
elif grade >= 76 and grade < 86:
    score = "AB"
elif grade >= 66 and grade < 76:
    score = "B"
elif grade >= 61 and grade < 66:
    score = "BC"
elif grade >= 56 and grade < 61:
    score = "C"
elif grade >= 41 and grade < 56:
    score = "D"
elif grade < 41:
    score = "E"

def grade_calc(score):
    grade = {
        "A": "It’s 4.0 of 4.0 Scale Grade",
        "AB": "It’s 3.5 of 4.0 Scale Grade",
        "B": "It’s 3.0 of 4.0 Scale Grade",
        "BC": "It’s 2.5 of 4.0 Scale Grade",
        "C": "It’s 2.0 of 4.0 Scale Grade",
        "D": "It’s 1.0 of 4.0 Scale Grade",
        "E": "It’s 0.0 of 4.0 Scale Grade",
    }
    return grade.get(score)

print(score)
print(grade_calc(score))
