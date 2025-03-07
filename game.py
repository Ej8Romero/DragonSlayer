import random
import time

player_hp = 20
player_attack = 5
player_defense = 3
spider_hp = 10
spider_attack = 4
spider_defense = 2
dragon_hp = 60
dragon_attack=8
dragon_defense=2

def battledragon():
    global player_hp, dragon_hp, player_attack, player_defense  
    
    print("A wild monster has appeared!\n")
    
    while player_hp > 0 and dragon_hp > 0:
        print(f"Your HP: {player_hp} | Dragon's HP: {dragon_hp}")
        
       
        choice = input("What will you do? (Attack/Defend/Escape): ").lower()
        
        if choice == "attack":
            
            damage_dealt = random.randint(1, 6) * player_attack
            dragon_hp -= damage_dealt
            print(f"You attack! You roll a d6 and deal {damage_dealt} damage to the monster.")
        
        elif choice == "defend":
           
            defense_block = random.randint(1, 4) * player_defense
            damage_taken = max(0, dragon_attack - defense_block)  
            player_hp -= damage_taken
            print(f"You defend! You block {defense_block} damage. You take {damage_taken} damage from the dragon.")
        
        elif choice == "escape":
            print("You decide to escape the battle!")
            break
        
        else:
            print("Invalid choice! Please choose 'Attack', 'Defend', or 'Escape'.")
            continue
        
    
        if dragon_attack > 0:
            damage_taken = random.randint(1, 6) * dragon_attack 
            player_hp -= damage_taken
            print(f"The dragon spews flames! You take {damage_taken} damage.\n")
        
      
        if player_hp <= 0:
            print("You have been defeated! The dragon wins, your village will be lost to time.")
            break
        elif dragon_hp <= 0:
            print("You defeated the dragon! Congratulations! You have won the game!")
            break

def battle():
    global player_hp, spider_hp, player_attack, player_defense  
    
    print("A wild monster has appeared!\n")
    
    while player_hp > 0 and spider_hp > 0:
        print(f"Your HP: {player_hp} | Monster's HP: {spider_hp}")
        
       
        choice = input("What will you do? (Attack/Defend/Escape): ").lower()
        
        if choice == "attack":
           
            damage_dealt = random.randint(1, 6) * player_attack
            spider_hp -= damage_dealt
            print(f"You attack! You roll a d6 and deal {damage_dealt} damage to the monster.")
        
        elif choice == "defend":
           
            defense_block = random.randint(1, 4) * player_defense
            damage_taken = max(0, spider_attack - defense_block)  
            player_hp -= damage_taken
            print(f"You defend! You block {defense_block} damage. You take {damage_taken} damage from the monster.")
        
        elif choice == "escape":
            print("You decide to escape the battle!")
            break
        
        else:
            print("Invalid choice! Please choose 'Attack', 'Defend', or 'Escape'.")
            continue
        
     
        if spider_hp > 0:
            damage_taken = random.randint(1, 6) * spider_attack  
            player_hp -= damage_taken
            print(f"The monster attacks! You take {damage_taken} damage.\n")
        

        if player_hp <= 0:
            print("You have been defeated! The monster wins.")
            break
        elif spider_hp <= 0:
            print("You defeated the monster! Congratulations!")
            reward_choice()
            break


def reward_choice():
    print("\nYou have defeated the monster!")
    print("As a reward, you may choose between two items:")
    print("1. A Bow (+2 Attack)")
    print("2. A Helmet (+2 Defense)")

    choice = input("Which item do you choose? (1/2): ")

    if choice == "1":
        global player_attack
        player_attack += 2
        print("You chose the Bow! Your Attack has increased by 2.")
    elif choice == "2":
        global player_defense
        player_defense += 2
        print("You chose the Helmet! Your Defense has increased by 2.")
    else:
        print("Invalid choice! You didn't receive a reward.")

    print(f"Your final stats are: Attack: {player_attack}, Defense: {player_defense}")

print(r"""    ___                             __ _                       
   /   \_ __ __ _  __ _  ___  _ __ / _\ | __ _ _   _  ___ _ __ 
  / /\ / '__/ _` |/ _` |/ _ \| '_ \\ \| |/ _` | | | |/ _ \ '__|
 / /_//| | | (_| | (_| | (_) | | | |\ \ | (_| | |_| |  __/ |   
/___,' |_|  \__,_|\__, |\___/|_| |_\__/_|\__,_|\__, |\___|_|   
                  |___/                        |___/           """)
time.sleep(4)
print("")
print("")
print("")
print("")
print("")
print("")
print("You wake up from a deep sleep, in your home")
time.sleep(4)
print('You are able to select one object to take with you before you set out')
time.sleep(2)
choiceA = int(input("""
Choose your trusty item to begin:

1. The trusty sword
2. The reliable shield
3. A health potion

Enter the number of your choice: """))

time.sleep(2)
if choiceA == 1:
    print('You feel mightier as you take the family sword, you get +2 attack')
    time.sleep(2)
    player_attack += 2  
elif choiceA == 2:
    print('You feel safer with the leather grip of the family shield in your hands')
    time.sleep(2)
    player_defense += 2  
elif choiceA == 3:
    time.sleep(2)
    print('Supplies are as important as any weapon in an adventure')
    player_hp += 10  
elif choiceA == 69:
    time.sleep(2)
    print('You recall the existence of the family extendo, the mighty blicky. You take grip of the reliable 9mm and get +100 attack')
    player_attack += 100  
else:
    time.sleep(2)
    print('You end up just going back to bed. The End')
time.sleep(4)

print(f"Here are your stats so far: Your HP is {player_hp} / Your Attack is {player_attack} / And your Defense is {player_defense}")
time.sleep(2)
print('Just as you headout a spider appears!')
time.sleep(2)
battle()
time.sleep(2)
print('After such a scary encounter you press up to the task at hand, you got to fight the dragon')
time.sleep(2)
print('You go to the mountain when suddenly the dragon swoops in!')
battledragon()