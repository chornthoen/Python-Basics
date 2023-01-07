count = 0
index = 0
student = int(input('Student : '))
print('------------------------------')
while count < student:
    index = count+1
    print('Student ', index)
    name = input('Name : ')
    subject = input('Subject : ')
    score = int(input('Score : '))
    print('------------------------')
    print('Name : ', name)
    print('Subject : ', subject)
    print('Score : ', score)
    if score < 0:
        print('Score can not be negative')
        break
    if score > 100:
        print('Score can not be over 100')
        break
    if score <= 49:
        print('Grade : F')
    elif score < 59:
        print('Grade : E')
    elif score < 69:
        print('Grade : D')
    elif score < 79:
        print('Grade : C')
    elif score < 89:
        print('Grade : B')
    else:
        print('Grade : A')
    print('------------------------')
    count +=1