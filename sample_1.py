# a simple attendance

def attendance():
    names = []
    total_students = int(input("Enter the total number of students: "))
    absent = int(input("Enter the number of absentees: "))
    if absent > 0 and absent > 4 and absent != 0:
        for i in range(0,total_students):
            name = input("Enter the absentees name and type 'ok' to print: ")
            names.append(name)
            if name == 'ok':
                break
            else:
                continue
    present = total_students - absent
    if present == total_students:
        print("Good! All are present today.!")
    elif absent == 1:
        print("Ask" + names[0], " to meet me tomorrow.")
    elif absent == 2:
        print("Tell " + names[0]+ ' and'+ names[1]+ " to meet me tomorrow.")
    elif absent == 3:
        print("Tell "+ names[0]+ ", "+ names[1]+ " and "+ names[2]+ " to come with their parents.")
    else:
        print("Inform all the", absent, "absentees to meet the principal.")

attendance()