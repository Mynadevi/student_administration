import csv
def write_into_csvfile(info):
    with open("student_info.csv","a",newline='') as csv_file:
        write=csv.writer(csv_file)
        if csv_file.tell()==0:
            write.writerow(["Name","Age","Contact Number","E-Mail ID"])
        write .writerow(info)
if __name__=='__main__':
    stu_no=1
    condition=True
    while(condition):
   
      student_info=input("Enter the student information #{} in the format(NAME AGE CONTACT_NUMBER E-MAIL_ID ".format(stu_no))
      student_info_list=student_info.split(' ')
    
      print("Entered student information is:\n NAME:{}\n AGE:{}\n CONTACT_NUMBER:{}\n E-MAIL_ID:{} ".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
      check=input("Is the entered student infromation correct?(yes/no) ")
      if check=='yes':
         write_into_csvfile(student_info_list) 
         value=input("Do you want to enter student information (yes/no)? ")
         if value=="yes":
            condition=True
            stu_no=stu_no+1
         else:
            condition=False
      else:
            print("Renter the values :")
