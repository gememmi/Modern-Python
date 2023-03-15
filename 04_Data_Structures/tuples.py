
from typing import Tuple

subjects: Tuple[str,str,str] = ("Maths", "Science", "History")
print(subjects)
print(f"No. of Subjects {len(subjects)}")

# here we are using for in loop to print something for each element of the tuple
for subject in subjects:
    print(f"Louis is signing up for {subject}")

addl_subjects = ("English", "Python", "Phyics")
total_subjects = subjects + addl_subjects
print(total_subjects)

# checking if a certain object is in this tuple
if "English" in total_subjects:
    print("Yeah you can take this class, sure")
else:
    print("You didn't sign up for this class, sorry!")
