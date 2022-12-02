import random

random_list=[]
repeat = True
while repeat:
    random_num = random.randint(1,100)
    contain = False
    if len(random_list)>0:
        for item in random_list: 
            if item == random_num:
                contain = False
            else:
                contain = True
        if contain:
            random_list.append(random_num)
    else:
        random_list.append(random_num)
    if len(random_list) == 5:
        repeat = False

rep = True
while rep:
    print("Try to guess the number between 1-100!")
    num1 =input("1: ")
    num2 =input("2: ")
    num3 =input("3: ")
    num4 =input("4: ")
    num5 =input("5: ")
    numbers = []
    hits = []
    hit = False
    same_num = False

    if num1.isnumeric() and num2.isnumeric() and num3.isnumeric() and num4.isnumeric() and num5.isnumeric():
        rep=False
        Rnum1=int(num1) 
        if Rnum1 in numbers:
                same_num = True
        else:
            numbers.append(Rnum1)   
            if Rnum1 in random_list: 
                hits.append(Rnum1)
                hit = True
                same_num = False
        
        Rnum2=int(num2)
        if Rnum2 in numbers:
                same_num = True
        else:
            numbers.append(Rnum2)   
            if Rnum2 in random_list: 
                hits.append(Rnum2)
                hit = True
                same_num = False

        Rnum3=int(num3)
        if Rnum3 in numbers:
                same_num = True
        else:
            numbers.append(Rnum3)   
            if Rnum3 in random_list: 
                hits.append(Rnum3)
                hit = True
                same_num = False

        Rnum4=int(num4)
        if Rnum4 in numbers:
                same_num = True
        else:
            numbers.append(Rnum4)   
            if Rnum4 in random_list: 
                hits.append(Rnum4)
                hit = True
                same_num = False

        Rnum5=int(num5)
        if Rnum5 in numbers:
                same_num = True
        else:
            numbers.append(Rnum5)   
            if Rnum5 in random_list: 
                hits.append(Rnum5)
                hit = True
                same_num = False
        
        if Rnum1 > 100 or Rnum2 > 100 or Rnum3 > 100 or Rnum4 > 100 or Rnum5 > 100:
            rep=True
            print("The numbers must be under 100!")

        elif Rnum1 < 1 or Rnum2 < 1 or Rnum3 < 1 or Rnum4 < 1 or Rnum5 < 1:
            rep=True
            print("The numbers must be above 1!")

        elif len(numbers) < 5:
           print("The numbers can't be identical!")
           rep=True   
      
        elif hit == False:
            print("You had 0 hits! :(")
            rep = True
        else:
            print(f"You had {len(hits)} hits!\nThese numbers were:{hits} ")
            rep = False
         
        
    else:
        rep=True
        print("It must be a number!")