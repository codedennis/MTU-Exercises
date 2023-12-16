def get_input():
    first_name = input("Enter first name: ")
    last_name = input("Enter surname: ")
    distance_covered = float(input("How far did you run today (km): "))
    race_distance = float(input("What distance race are you training for (km): "))
    rainfall_amount = float(input("What is the hourly rainfall amount (mm): "))
    
    return first_name, last_name, distance_covered, race_distance, rainfall_amount

def calculate_percentage(distance_covered, race_distance):
    return (distance_covered / race_distance) * 100

def get_footwear_advice(rainfall_amount):
    if rainfall_amount > 50:
        return "Wear Long Spikes"
    elif 10 <= rainfall_amount <= 50:
        return "Wear Short Spikes"
    else:
        return "Spikes are not necessary"

def generate_training_report(first_name, last_name, distance_covered, race_distance, percentage, advice):
    asterisk = '*' if distance_covered > 9000 else ''
    
    print("\nTraining report")
    print("-" * 50)
    print(f"Name\t\tDistance\tRace percent\tAdvice")
    print(f"{first_name} {last_name}\t{distance_covered:.1f}{asterisk}\t{percentage:.1f}%\t\t{advice}")

def main():
    first_name, last_name, distance_covered, race_distance, rainfall_amount = get_input()
    
    percentage = calculate_percentage(distance_covered, race_distance)
    advice = get_footwear_advice(rainfall_amount)
    
    generate_training_report(first_name, last_name, distance_covered, race_distance, percentage, advice)

if __name__ == "__main__":
    main()
