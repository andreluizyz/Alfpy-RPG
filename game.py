import random

player_hp = 30
player_attack = 5

while player_hp > 0:

    print("\nVocê entrou em uma sala...")
    
    event = random.choice(["enemy", "potion"])

    if event == "enemy":
        enemy_hp = 10
        
        print("👹 Um inimigo apareceu!")

        while enemy_hp > 0 and player_hp > 0:
            print(f"\nSua vida: {player_hp}")
            print(f"Vida do inimigo: {enemy_hp}")

            action = input("1- Atacar\n2- Fugir\n> ")

            if action == "1":
                damage = random.randint(3, player_attack)

                enemy_hp -= damage

                print(f"\nVocê deu {damage} de dano!")

                if enemy_hp > 0:
                    enemy_damage = random.randint(1, 4)

                    player_hp -= enemy_damage

                    print(f"O inimigo deu {enemy_damage} de dano!")

            elif action == "2":
                print("Você fugiu!")
                break

    elif event == "potion":
        heal = random.randint(5, 10)

        player_hp += heal

        print(f"\n🧪 Você encontrou uma poção e recuperou {heal} HP!")

print("\n💀 GAME OVER")