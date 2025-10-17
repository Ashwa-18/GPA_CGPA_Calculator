import streamlit as st

st.title("GPA & CGPA Calculator")
st.write(

"""
**Name** : **Ashwa Asghar**

**Roll No**: **FA23-BST-018**

**Section** : **BST-B**

**Instructor**: **Dr.Noman**

**Title**: **GPA Calculator**
"""
)
st.info("PLZ First Enter Your Marks in Each Subject")
Tcc = 0
CCGPA = 0
a = st.number_input("How many semester do you want to calculate GPA or CGPA : ",min_value= 1 , step= 1)
for j in range(1,a+1):
   b =  st.number_input(f"How many subject do you have in {j} semester? : ",min_value= 1 , step= 1, key= f"subject{j}")
   d = 0
   Tgc = 0
   for i in range(1,b+1):
       c = st.number_input(f"Enter Marks in {i} subject: ",min_value= 1 ,max_value= 100, step= 1,key= f"marks{i}_{j}")
       c2 = st.number_input("Enter Credit Hours of that subject: ",min_value= 1 , step= 1,key= f"credit{i}_{j}")
       d = d + c2 


       if c >= 85:
          g = 4
          st.write(f"Your Grade point in {i} subject is {g}")
       elif c >= 80:
          g = 3.7
          st.write(f"Your Grade point in {i} subject is {g}")
       elif c >= 75:
          g = 3.3
          st.write(f"Your Grade point in {i} subject is {g}")
       elif c >= 70:
          g = 3.0
          st.write(f"Your Grade point in {i} subject is {g}")
       elif c >= 65:
          g = 2.7
          st.write(f"Your Grade point in {i} subject is {g}")
       elif c >= 60:
          g = 2.3
          st.write(f"Your Grade point in {i} subject is {g}")
       elif c >= 55:
          g = 2.0
          st.write(f"Your Grade point in {i} subject is {g}")
       else:
           g = 0
           st.write(f"Your Grade point in {i} subject is {g}")
     
       gc = g*c2
       Tgc =Tgc + gc
   GPA = Tgc/d
   st.write(f"Your Total GPA of Semester {j} is " , round(GPA,2))
   CCGPA = CCGPA +(GPA * d) 
   Tcc = Tcc + d
   CGPA =  CCGPA / Tcc
   st.write(f"Your Total CGPA of Semester " , round(CGPA,2))





 


