'''
1 for snake
-1 for water 
0 for gun
In version 2 Handle scores'''
import random
invalid_inputs=0
round=0
userscore=0
computerscore=0
drawscore=0
a=0
print(f"======================\nSnake Water Gun Game\n======================")
while True:
 a=int(input("Set total_rounds 1,3,5 or 10:"))
 if(a in [1,3,5,10]):
   break
 else:
  print("Please set valid mode!")
while True:
 computer=random.choice([-1,0,1]) 
 if(round<a):
   round+=1
   print(f"Round-Num: {round}/{a}")
 youstr=input("Enter your choice:")
 choices={"w":-1,"s":1,"g":0}
 if(youstr in choices):
   invalid_inputs=0
 reverseDict={1:"🐍 snake",-1:"💧 water",0:"🔫 gun"}
 if(youstr not in choices):
      invalid_inputs+=1
      print("❌ Invalid choice!")
      if(invalid_inputs<3):
            continue
      print("🚫 Game Over")
      break
 you=choices[youstr]
 print(f"you choose {reverseDict[you]}\nComputer Choose {reverseDict[computer]}")
 if(computer==you):
    print("🤝 Its a draw!")
    drawscore+=1
 else:
   if(computer==-1 and you==1): 
    print("🎉Congratulations! You win!")
    userscore+=1
   elif(computer==-1 and you==0):#
    print("😌 You lose!")
    computerscore+=1
   elif(computer==1 and you==-1):
    print("😌 You lose!")
    computerscore+=1
   elif(computer==1 and you==0):
    print("🎉Congratulations! You win!")
    userscore+=1
   elif(computer==0 and you==-1):
     print("🎉Congratulations! You win!")
     userscore+=1
   elif(computer==0 and you==1):
     print("😌 You lose!")
     computerscore+=1
     #Handle here score---------------------------------------------------------------
 print("Score:--------\n")
 print(f"you: {userscore}\ncomputer: {computerscore}\nDraw: {drawscore}")
 if(round==a):
   print("==============\n🚫 Game Over \n==============")
   print(f"============Final Result==========")
   print(f"👨  Your score: {userscore}\n💻  Computer score: {computerscore}\n🖐  Draw score:{drawscore}\n")
   if(userscore>computerscore):
     print("🏆  Overall Winner: You")
   elif(computerscore>userscore):
     print("🏆  Overall Winner : Computer")
   else:
     print("Anyone no winner! match draw ")
   exit()
 while True:
  play=input("\nDo you want to play agian? (y/n):").lower()
  if(play=="y"):
   break
  elif(play=="n"):
      print("👋 Thanks for playing")
      exit()
  else:
     print("❌ Invalid input!Please enter only y or n.")