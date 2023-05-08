import random

#commands are case sensitive

print("Welcome, brave adventurer, to a dark underwolrd dungeon where only luck will decide whether you live or die! "
      "\nShall you succeed in slaying all the monsters you will be rewarded with nothing!"
      "\nDo you want to risk it all just for the glory? : Y/N? ")

decision = (input("Begin your journey:\n "))

if decision == "Y":
    opponents = ["Clay Golem", "Witch", "Warmonger", "Titan", "Deity"]
    print(f"The moment you set foot in the cave a fearsome monster appears out of thin air."
          f"\nYou reach for your pocket and take out the magical dice once belonging to your father.")
    slayed_opponents = []
    total_opponents = 0

    for _ in range(100):
        if total_opponents == len(opponents):
            print("But those sound familiar! An old wizard emerges from the shadows - your father!\n"
                  "He looks straight into your eyes and yells:'What in the tarnation! Why did you kill my pets!"
                  "\nAnd why did you steal my magic dice!Wait till your mother hears about this!'")
            break

        current_opponent = random.choice(opponents)
        if current_opponent not in slayed_opponents:
            slayed_opponents.append(current_opponent)
            total_opponents += 1
        else:
            continue

        if current_opponent == "Clay Golem":
            opponent_name = "Clay Golem"
            opponent_health = 20
        elif current_opponent == "Witch":
            opponent_name = "Witch"
            opponent_health = 30
        elif current_opponent == "Warmonger":
            opponent_name = "Warmonger"
            opponent_health = 40
        elif current_opponent == "Titan":
            opponent_name = "Titan"
            opponent_health = 50
        elif current_opponent == "Deity":
            opponent_name = "Deity"
            opponent_health = 60

        roll_counter = 0
        total_damage_dealt = 0

        start_the_fight = str(input("Are you ready for battle: Y/N\n"))
        game_end = False
        print(f"A ghastly {opponent_name} stands before you!")

        if start_the_fight != "Y":
            game_end = True
            print("And you decide to run away with fear!")

        while start_the_fight == "Y":
            roll_counter += 1
            if roll_counter > 2:
                print(f"But there is no time!You receive a mortal wound before your third try!"
                      f" The {opponent_name} mutters:'Pathetic!' and leaves!")
                game_end = True
                break
            dice_roll = str(input("Roll thy dice: "))
            if dice_roll != "Roll":
                game_end = True
                print("You have no idea how dice work and there is no one around to tell you. You died!")
                break
            else:
                dice_sum = random.randint(2, 12)
                if dice_sum <= 4:
                    damage_dealt = random.randint(1, 20)
                elif 4 < dice_sum <= 9:
                    damage_dealt = random.randint(21, 35)
                elif dice_sum >= 10:
                    damage_dealt = random.randint(36, 70)


                print(f"You roll {dice_sum}.")
                print(f"You deal {damage_dealt} points of damage to the {opponent_name}")

                total_damage_dealt += damage_dealt
                remaining_health = opponent_health - total_damage_dealt

                if total_damage_dealt < opponent_health:
                    print(f"Your enemy has {remaining_health} HP left.\nYou can taste the victory as you reach for your dice once more.")
                    continue
                elif total_damage_dealt >= opponent_health:
                    print("Congratulations adventurer , you slayed your enemy!\n"
                      "No time to rest as you hear more footsteps approaching!")
                    break

        if game_end:
            break
    print("Game over!")

elif decision == "N":
    print("You've made a wise decision to stay away from danger. May you live long and forgettable life!")

else:
    print("A simple queston was asked , mortal! How dare you disobey!?")