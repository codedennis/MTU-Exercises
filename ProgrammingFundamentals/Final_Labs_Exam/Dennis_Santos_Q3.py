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

def save_team_metrics(team_name, num_members, total_distance, longest_distance_athlete, achieved_target_athletes):
    with open(f"{team_name.lower()}_metrics.txt", "w") as file:
        file.write(f"There are {num_members} members in the {team_name} team and they have run a combined distance of {total_distance:.1f}km\n")
        
        file.write(f"{longest_distance_athlete[0]} {longest_distance_athlete[1]}. has qualified for a private coaching session with a high performance coach.\n")
        
        for athlete in achieved_target_athletes:
            file.write(f"{athlete[0]} {athlete[1]}. has reached their target distance, we advise increasing their target to {min(athlete[3] * 1.25, 35):.1f}km\n")

def main():
    team_name = input("What is the name of the national team: ")
    num_members = int(input("How many member’s records are you adding? "))
    
    total_distance = 0
    longest_distance_athlete = None
    achieved_target_athletes = []
    
    for _ in range(num_members):
        athlete = get_input()
        total_distance += athlete[2]
        
        percentage = calculate_percentage(athlete[2], athlete[3])
        advice = get_footwear_advice(athlete[4])
        
        generate_training_report(athlete, percentage, advice)
        
        # Track athlete with the longest distance race
        if longest_distance_athlete is None or athlete[3] > longest_distance_athlete[3]:
            longest_distance_athlete = athlete
        
        # Track athletes who achieved their desired race distance
        if athlete[2] >= athlete[3]:
            achieved_target_athletes.append(athlete)
    
    save_team_metrics(team_name, num_members, total_distance, longest_distance_athlete, achieved_target_athletes)

if __name__ == "__main__":
    main()
