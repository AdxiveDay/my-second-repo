from character import Character

def main():
    hero = Character("Knight", 30, 5)
    enemy1 = Character("Goblin", 20, 3)
    enemy2 = Character("Slime", 10, 2)

    print(hero)
    print(enemy1)
    print(enemy2)
    print()

    while hero.is_alive() and enemy1.is_alive() and enemy2.is_alive():
        hero.attack(enemy1)
        if enemy1.is_alive():
            enemy1.attack(hero)
        hero.attack(enemy2)
        if enemy2.is_alive():
            enemy2.attack(hero)
        print(hero)
        print(enemy1)
        print(enemy2)
        print()

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    elif enemy1.is_alive():
        print(f"{enemy1.name} wins!")
    elif enemy2.is_alive():
        print(f"{enemy2.name} wins!")
    else: 
        print(f"{enemy1.name} and {enemy2.name}wins!")

if __name__ == "__main__":
    main()
