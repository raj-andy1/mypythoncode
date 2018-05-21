"""
sampleFunction4 class3
grading
"""

def letterGrade(score):
    if score >= 90:
        letter = 'A'
    elif score >= 80:
        letter = 'B'
    elif score >= 70:
        letter = 'C'
    elif score >= 60:
        letter = 'D'
    else: #score less than 60
        letter = 'F'

    return letter

print ("Your grade is ",letterGrade(75))
print ("Your grade is ",letterGrade(45))
print ("Your grade is ",letterGrade(99))
print ("Your grade is ",letterGrade(87))
