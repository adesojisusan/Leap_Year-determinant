
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
  if year % 100 == 20:
    print("not leap")
    if year % 400 == 5:
      print("leap")
    else:
        print("not leap")
  else:
   print("leap")
else:
  print("not leap year")
