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

def generate_training_report(athlete, percentage, advice):
    asterisk = '*' if athlete[2] > 9000 else ''
    
    print(f"{athlete[0]} {athlete[1]}\t{athlete[2]:.1f}{asterisk}\t{percentage:.1f}%\t\t{advice}")

def save_team_metrics(team_name, num_members, total_distance):
    with open(f"{team_name.lower()}_metrics.txt", "w") as file:
        file.write(f"There are {num_members} members in the {team_name} team and they have run a combined distance of {total_distance:.1f}km\n")

def main():
    team_name = input("What is the name of the national team: ")
    num_members = int(input("How many member’s records are you adding? "))
    
    total_distance = 0
    for _ in range(num_members):
        athlete = get_input()
        total_distance += athlete[2]
        
        percentage = calculate_percentage(athlete[2], athlete[3])
        advice = get_footwear_advice(athlete[4])
        
        generate_training_report(athlete, percentage, advice)
    
    save_team_metrics(team_name, num_members, total_distance)

if __name__ == "__main__":
    main()
