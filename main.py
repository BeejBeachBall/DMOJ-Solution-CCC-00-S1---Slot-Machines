money = int(input())
slot1 = int(input())
slot2 = int(input())
slot3 = int(input())
plays = 0

while money >= 1:
    slot1 += 1
    money -= 1
    plays += 1
    if slot1 == 35:
      money += 30
      slot1 = 0
    if money == 0:
      break
    slot2 += 1
    money -= 1
    plays += 1
    if slot2 == 100:
      money += 60
      slot2 = 0
    if money == 0:
      break
    slot3 += 1
    money -= 1
    plays += 1
    if slot3 == 10:
      money += 9
      slot3 = 0
    if money == 0:
      break

print ("Martha plays "+str(plays)+" times before going broke.")
