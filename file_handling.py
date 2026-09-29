"""File handling"""
# file =open("ds.py")
# print(file.read())
# file.close 

"""Modes
w- write mode #1.create file if not created 2.and  overwritten the value  if allready present in the file
a- append mode
r- read mode
x-create mode
"""
# w->mode
# f=open('a_man','w')
# #f.write("HII")
# f.write("the content is overwritten")
# f.close()

#a->mode
# f=open('a_man','a')
# f.write("HII")
# f.close()

#r->mode
# f=open('a_man','r')
# print(f.read())
# f.close()

#with statement -> auto-closed the files
# with open('a_man','r') as file:
#     print(file.read())

# with open('a_man','w') as files:
#     files.write("Hii how are you!")
#     print("Done")

#paths
# C:\Users\muska\OneDrive\Desktop\python.coaching\a_man
from pathlib import Path
p = Path('a_man')
if p.exists():
    print("file exists")
else:
    print("Not exists")