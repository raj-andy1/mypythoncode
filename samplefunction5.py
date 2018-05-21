"""
samplefunction2 class3
use if/else within a function

"""

def createHeader(fullName, gender):
    if gender == 'M':
        title = 'Mr.'
    elif gender == "F":
        title = 'Ms.'
    else:
        title = 'Mr. or Ms.'

    header = 'Dear' + ' ' + title + ' ' + fullName + ','
    return header

print(createHeader("Joe Smith","M"))
print(createHeader("Susie Jones","F"))
print(createHeader("Andy Raja","?"))
print(createHeader("Gowri Rao","F"))
