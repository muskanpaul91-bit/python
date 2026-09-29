# SPLIT FUNCTION
# convert message into list
msg = "hii everyone"
print(msg.split())
#to find length 
le = msg.split()
print(len(le))
# input function
msg=input("Enter msg. :")
l= msg.split()
print(l)
print(len(l))

file2 =" info.txt"
file3 ="details.pdf"
li=(file2.split(" ."))
print(li[-1])
# "-"SPLIT 
product_id ="xyz-1234-abc"
li= product_id.split("-")
print(len(li))
print(li[1])

msg = input("Enter your message:")
li = (msg.split())
l =(li[::-1])
op=" ".join(l)#join function
print(op)