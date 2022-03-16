import random
#272 de 137 ihtimalle a4ten sonra kart çekmeyen bilgisayar kazanır

risk_1 = int(input("'computer 1' elindeki sayı kaç olduğunda kart çekmesin?: "))
risk_2 = int(input("'computer 2' elindeki sayı kaç olduğunda kart çekmesin?: "))
oyun_sayısı = int(input("oyun kaç kere oynansın?: "))

cards = [1,2,3,4,5,6,7,8,9,10,10,10]

computer_1_score = []
computer_2_score = []
for play in range(oyun_sayısı):
    computer_1 = []
    computer_2 = []

    #game begins
    computer_1.append(random.choice(cards))
    computer_1.append(random.choice(cards))

    computer_2.append(random.choice(cards))
    computer_2.append(random.choice(cards))

    # print ("first 2 cards ------")
    # print(computer_1)
    # print(computer_2)

    if computer_1[0] + computer_1[1] < risk_1:
        computer_1.append(random.choice(cards))
    if computer_2[0] + computer_2[1] < risk_2:
        computer_2.append(random.choice(cards))

    # print ("adding cards to hand ------")
    # print(computer_1)
    # print(computer_2)

    if (len(computer_1)) == 3:
        if computer_1[0] + computer_1[1] + computer_1[2] < risk_1:
            computer_1.append(random.choice(cards))
    if (len(computer_2)) == 3:
        if computer_2[0] + computer_2[1] + computer_2[2] < risk_2:
            computer_2.append(random.choice(cards))

    # print ("adding cards to hand ------")
    # print(computer_1)
    # print(computer_2)

    if (len(computer_1)) == 4:
        if computer_1[0] + computer_1[1] + computer_1[2] + computer_1[3] < risk_1:
            computer_1.append(random.choice(cards))
    if (len(computer_2)) == 4:
        if computer_2[0] + computer_2[1] + computer_2[2] + computer_2[3] < risk_2:
            computer_2.append(random.choice(cards))

    computer_1_result = 0
    for x in computer_1:
        computer_1_result += x
    # print(f"computer 1 = {computer_1_result}")

    computer_2_result = 0
    for x in computer_2:
        computer_2_result += x
    # print(f"computer 2 = {computer_2_result}\n")

    ##### burada oyunun kuralları var

    if computer_1_result <= 21 and computer_2_result > 21:
        computer_1_score.append("win")
    if computer_2_result <= 21 and computer_1_result > 21:
        computer_2_score.append("win")
    if computer_1_result <= 21 and computer_2_result <= 21:
        if 21 - computer_1_result < 21 - computer_2_result:
            computer_1_score.append("win")
        if 21 - computer_2_result < 21 - computer_1_result:
            computer_2_score.append("win")





print(f"\nbilgisayar 1 = {len(computer_1_score)}")
print(f"bilgisayar 2 = {len(computer_2_score)}")

if len(computer_1_score) > len(computer_2_score):
    print("computer 1 kazandı")
if len(computer_2_score) > len(computer_1_score):
    print("computer 2 kazandı")








