#if თუ
#elif წინააღმდეგ შემთხვევაში
#else სხვა შემთხვევაში


surname1="ninikashvili"
surname2=input("enter your surname: ")
 
if surname1==surname2:
    print("our surnames are similar")
else:
    print("our surnames are not similar")

height1=180
height2=int(input("enter your height: "))
if height1>height2:
    print("i am taller than you")
elif height2>height1:
    print("you are taller than me")
else:
    print("we are same height")