import sys


def analyze_and_read_shelter_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        cat_visits = 0
        other_cat_visits = 0
        total_time_in_house = 0
        cat_visit_durations = []

        for record_lines in lines:
            if record_lines.strip() == 'END':
                break

            cat_type, entry_time, exit_time = record_lines.strip().split(',')
            entry_time, exit_time = int(entry_time), int(exit_time)

            # Calculate visit duration and update total time in the house
            visit_duration = exit_time - entry_time

            # Update cat visit durations for 'OURS' cat only
            if cat_type == 'OURS':
                cat_visits += 1
                cat_visit_durations.append(visit_duration)
                total_time_in_house += visit_duration
            elif cat_type == 'THEIRS':
                other_cat_visits += 1

        # Calculate statistical overview
        if cat_visits == 0:
            average_visit_length = longest_visit = shortest_visit = 0
        else:
            average_visit_length = sum(cat_visit_durations) / cat_visits
            longest_visit = max(cat_visit_durations)
            shortest_visit = min(cat_visit_durations)

        # Print the final analysis results
        total_hours, remaining_minutes = divmod(total_time_in_house, 60)
        total_minutes = int(remaining_minutes)
        print("\nLog File Analysis")
        print("==================\n")
        print(f"Cat Visits: {cat_visits}")
        print(f"Other Cats: {other_cat_visits}\n")
        print(f"Total Time in House: {int(total_hours)} Hours, {total_minutes} Minutes\n")
        print(f"Average Visit Length: {int(average_visit_length)} Minutes")
        print(f"Longest Visit:        {longest_visit} Minutes")
        print(f"Shortest Visit:       {shortest_visit} Minutes")

    except FileNotFoundError:
        print(f'Cannot open "{file_path}"!')
    except Exception as e:
        print(f'An error occurred: {e}')


# calling the function
if len(sys.argv) != 2:
    print("Missing command line argument!")
else:
    data_in_file_path = sys.argv[1]
    analyze_and_read_shelter_file(data_in_file_path)
