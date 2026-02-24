import numpy as np
# Load data (skip header)
data=np.genfromtxt('student_data.txt',delimiter=',',dtype='int',skip_header=1)
Roll=data[:,0]
Marks=data[:,1:]
print("\n Student Analysis")
# Subject wise average
math_avg=np.mean(Marks[0],axis=0)
print("\n Math Average :",math_avg)
phy_avg=np.mean(Marks[1],axis=0)
print("\n Physics Average :",phy_avg)
eng_avg=np.mean(Marks[2],axis=0)
print("\n English Average :",eng_avg)
# Marks average
sub_avg=np.mean(Marks,axis=0)
print("\n Subject Average(Math,Physics,English) :",sub_avg)
# Student Average
stud_avg=np.mean(Marks,axis=1)
# Top 5 Students
top_students=np.argsort(stud_avg)[-5:][::-1]
print("\n Top 5 Students roll numbers :",Roll[top_students])
# Hardest Subject
Subjects=["Math","Physics","English"]
hardest=Subjects[np.argmin(sub_avg)]
print("\n Hardest Subject :",hardest)
# Easiest Subject
easiest=Subjects[np.argmax(sub_avg)]
print("\n Easiest Subject :",easiest)
# Students below class average
class_avg=np.mean(stud_avg)
below_avg=Roll[stud_avg<class_avg]
print("\n Below average students :",below_avg)
# Grade classification
grades=np.where(
    stud_avg>=90,"A", np.where(stud_avg>=70,"B",np.where(stud_avg>=40,"C","Fail"))
)
print("\n Grades:",grades)
# Column wise Normalization :  Rescaling numbers to a fixed range — usually 0 to 1.
# Math 
math_marks= Marks[:,0]
math_max=math_marks.max()
math_min=math_marks.min()
math_normalized=(math_marks-math_min)/(math_max-math_min)
print("\n Normalized Math marks:",math_normalized)
#Physics
phy_marks=Marks[:,1]
phy_max=phy_marks.max()
phy_min=phy_marks.min()
phy_normalized=(phy_marks-phy_min)/(phy_max-phy_min)
print("\n Normalized Physics marks:",phy_normalized)
# English
eng_marks=Marks[:,2]
eng_max=eng_marks.max()
eng_min=eng_marks.min()
eng_normalized=(eng_marks-eng_min)/(eng_max-eng_min)
print("\n Normalized English marks:",eng_normalized)
print("\n Analysis Completed Successfully")