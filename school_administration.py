import csv

def write_into_csvfile(student_info):
    with open("Student_info.txt",'a',newline='') as student_file:
        writer=csv.writer(student_file)

        if student_file.tell()==0:
            writer.writerow(["Name", "Age", "Contact_info", "E-mail_ID"])
        writer.writerow(student_info)


if __name__ == "__main__":
    condition= True
    student_no=1
    while(condition):
        student_info=input("enter the student #{} information in format [name age contact_info email]:\n".format(student_no))
        student_info_list=student_info.split()
        print("Details that you have entered: \n name: {}\n age: {}\n contact_info: {}\n email: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],
                                                                                                          student_info_list[3]))
        check_info=input("Please check what you have entered type (yes/no): ").lower()
        if check_info == "yes":
            write_into_csvfile(student_info_list)
            student_no+=1
            condition=eval(input("Do you want to enter more student details? type (true/false)").capitalize())
            
        elif check_info == "no":
            print("please re-enter the details of student #{}".format(student_no))
            
    
