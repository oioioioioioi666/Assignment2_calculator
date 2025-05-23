def calculate_cookout_supplies():
    people = int(input("Enter the number of people attending the cookout: "))
    hot_dogs_per_person = int(input("Enter the number of hot dogs each person will be given: "))
   
    total_hot_dogs = people * hot_dogs_per_person
    
    hot_dog_packages = (total_hot_dogs + 9) // 10 
    hot_dog_leftovers = (hot_dog_packages * 10) - total_hot_dogs
    
    bun_packages = (total_hot_dogs + 7) // 8 
    bun_leftovers = (bun_packages * 8) - total_hot_dogs
   
    print("\nResults:")
    print(f"Minimum number of hot dog packages needed: {hot_dog_packages}")
    print(f"Minimum number of hot dog bun packages needed: {bun_packages}")
    print(f"Hot dogs left over: {hot_dog_leftovers}")
    print(f"Hot dog buns left over: {bun_leftovers}")

calculate_cookout_supplies()


# balalaa