bio=(int(input("Enter your biology marks ")))
eng=(int(input("Enter your english marks  ")))
kisw=(int(input("Enter your kiswahili marks ")))
maths=(int(input("Enter your maths marks ")))
hist=(int(input("Enter your history marks ")))
x=bio+eng+kisw+maths+hist
print(("your total marks are"),x)
if (x>=400): {
    print("pass","grade A")
}
elif(x>=300):{
    print("average")
}
elif(x>=290):{
    print("below average")
}   
else:{
    print("fail","grade E")
}