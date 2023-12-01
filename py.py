#File:Personal-Timetable-Weifeng-Zhou.py
#Athor: WEIFENG ZHOU
#UniSA Email: zhowy022@mymail.unisa.edu.au
# This is my own work as defined by the University's Academic Misconduct Policy

# Function to check if two events overlap
def is_overlapping(event1, event2):
    return not (event1[1] <= event2[0] or event1[0] >= event2[1])

# Function to validate time format (HH:MM)
def validate_time_format(time_str):
    if len(time_str) != 5:
        return False

    try:
        hours, minutes = map(int, time_str.split(':'))
        if 0 <= hours <= 23 and 0 <= minutes <= 59:
            return True
    except ValueError:
        pass

    return False

# Function to validate the day of the week
def validate_day_of_week(day_str):
    valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if day_str in valid_days:
        return True
    else:
        print("Error: Invalid day of the week. Please use full day names (e.g., Monday)")
        return False

# Function to add a new event to the schedule
def add_event(schedule):
    start_time = input("Enter event start time (in 24-hour format, e.g., 08:00): ")
    end_time = input("Enter event end time (in 24-hour format, e.g., 10:00): ")

    if not (validate_time_format(start_time) and validate_time_format(end_time)):
        print("Error: Invalid time format. Please use HH:MM format (e.g., 08:00)")
        return
    
    if start_time >= end_time:
        print("Error: Start time must be earlier than end time.")
        return
    
    event_name = input("Enter event name: ")
    event_location = input("Enter event location: ")
    day_of_week = input("Enter day of the week (e.g., Monday): ")

    if not validate_day_of_week(day_of_week):
        return
    
    new_event = (day_of_week, start_time, end_time, event_name, event_location)

    overlapping = False
    index = 0
    while index < len(schedule):
        event = schedule[index]
        if event[0] == new_event[0] and is_overlapping((event[1], event[2]), (new_event[1], new_event[2])):
            overlapping = True
            print(f"Error: The new event overlaps with an existing event on {day_of_week}.")
        index += 1
    
    if not overlapping:
        schedule.append(new_event)
        print("Event added successfully.")

# Function to display the schedule
def display_schedule(schedule):
    if not schedule:
        print("Current schedule is empty")
    else:
        days = {
            "Monday": [],
            "Tuesday": [],
            "Wednesday": [],
            "Thursday": [],
            "Friday": [],
            "Saturday": [],
            "Sunday": []
        }
        for event in schedule:
            days[event[0]].append((event[1], event[2], event[3], event[4]))

        # Display events in sorted order by day and time
        for day in days:
            events = sorted(days[day], key=lambda x: (x[0], x[1]))
            if events:
                print(f"\n{day}:")
                for i, event in enumerate(events, 1):
                    print(f"{i}. Start time: {event[0]}, End time: {event[1]}, Event: {event[2]}, Location: {event[3]}")
                    
# Function to search events for a specific day
def search_events_by_day(schedule):
    day = input("Enter the day to search (e.g., Monday): ")

    if not validate_day_of_week(day):
        return

    matching_events = [event for event in schedule if event[0] == day]

    if not matching_events:
        print(f"No events found for {day}.")
        return

    matching_events = sorted(matching_events, key=lambda x: (x[1], x[2]))

    print(f"\nEvents for {day}:")
    for i, event in enumerate(matching_events, 1):
        print(f"{i}. Start time: {event[1]}, End time: {event[2]}, Event: {event[3]}, Location: {event[4]}")


# Function to update an event by search or index select 
def update_event(schedule):
    if not schedule:
        print("Current schedule is empty. There are no events to update.")
        return

    print("\nCurrent Schedule:")
    display_schedule(schedule)

    option = input("\nEnter '1' to update by index, '2' to update by keyword: ")

    if option == '1':
        event_index = int(input("\nEnter the index of the event you want to update: ")) - 1

        if event_index < 0 or event_index >= len(schedule):
            print("Error: Invalid event index.")
            return

        event = schedule[event_index]

        print(f"\nUpdating Event: {event[3]} on {event[0]}")
        start_time = input(f"Enter new start time (current: {event[1]}): ")
        end_time = input(f"Enter new end time (current: {event[2]}): ")
        event_name = input(f"Enter new event name (current: {event[3]}): ")
        event_location = input(f"Enter new event location (current: {event[4]}): ")

        if start_time and not validate_time_format(start_time):
            print("Error: Invalid time format. Please use HH:MM format (e.g., 08:00)")
            return

        if end_time and not validate_time_format(end_time):
            print("Error: Invalid time format. Please use HH:MM format (e.g., 08:00)")
            return

        if start_time and end_time and start_time >= end_time:
            print("Error: Start time must be earlier than end time.")
            return

        if start_time or end_time:
            for other_event in schedule:
                if other_event != event and other_event[0] == event[0] and is_overlapping((other_event[1], other_event[2]), (start_time, end_time)):
                    print(f"Error: The new event overlaps with an existing event on {event[0]}.")
                    return

        if start_time:
            event = (event[0], start_time, event[2], event[3], event[4])

        if end_time:
            event = (event[0], event[1], end_time, event[3], event[4])

        if event_name:
            event = (event[0], event[1], event[2], event_name, event[4])

        if event_location:
            event = (event[0], event[1], event[2], event[3], event_location)

        schedule[event_index] = event
        print("Event updated successfully.")

    elif option == '2':
        keyword = input("Enter keyword to search for events: ")
        matching_events = search_events_by_keyword(schedule, keyword)

        if not matching_events:
            print(f"No events found matching the keyword '{keyword}'.")
            return

        print(f"\nSearch results for keyword '{keyword}':")
        for i, event in enumerate(matching_events, 1):
            print(f"{i}. Day: {event[0]}, Start time: {event[1]}, End time: {event[2]}, Event: {event[3]}, Location: {event[4]}")

        event_index = int(input("\nEnter the index of the event you want to update: ")) - 1

        if event_index < 0 or event_index >= len(matching_events):
            print("Error: Invalid event index.")
            return

        event = matching_events[event_index]

        print(f"\nUpdating Event: {event[3]} on {event[0]}")

    else:
        print("Invalid option, please try again")

# Function to delete an event by search or index select 
def delete_event(schedule):
    if not schedule:
        print("Current schedule is empty. There are no events to delete.")
        return

    print("\nCurrent Schedule:")
    display_schedule(schedule)

    option = input("\nEnter '1' to delete by index, '2' to delete by keyword: ")

    if option == '1':
        event_index = int(input("\nEnter the index of the event you want to delete: ")) - 1

        if event_index < 0 or event_index >= len(schedule):
            print("Error: Invalid event index.")
            return

        event = schedule[event_index]


    elif option == '2':
        keyword = input("Enter keyword to search for events: ")
        matching_events = search_events_by_keyword(schedule, keyword)

        if not matching_events:
            print(f"No events found matching the keyword '{keyword}'.")
            return

        print(f"\nSearch results for keyword '{keyword}':")
        for i, event in enumerate(matching_events, 1):
            print(f"{i}. Day: {event[0]}, Start time: {event[1]}, End time: {event[2]}, Event: {event[3]}, Location: {event[4]}")

        event_index = int(input("\nEnter the index of the event you want to delete: ")) - 1

        if event_index < 0 or event_index >= len(matching_events):
            print("Error: Invalid event index.")
            return

        event = matching_events[event_index]

    else:
        print("Invalid option, please try again")



def main():
    schedule = []
    while True:
        print("\nSelect an operation:")
        print("1. Add event")
        print("2. Update event")
        print("3. Delete event")
        print("4. Display current schedule")
        print("5. Display a certain day schedule")
        print("6. Search your events")
        print("7. Export your current schedule to txt file")
        print("8. Import txt schedule file")
        print("9. End")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_event(schedule)

        elif choice == '2':
           update_event(schedule)
        elif choice == '3':
            delete_event(schedule)
        elif choice == '4':
            display_schedule(schedule)
        elif choice =="5":
            search_events_by_day(schedule)
        elif choice == '6':
            search_results = search_events(schedule)
            if search_results:
             display_schedule(search_results)
       
        else:
            print("Invalid option, please try again")


if _name_ == "_main_":
    main()