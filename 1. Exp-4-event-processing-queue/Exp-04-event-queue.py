from collections import deque

event_queue = deque()

def add_event():
    event_id = input("Enter Event ID: ")
    description = input("Enter Event Description: ")
    event = (event_id, description)
    event_queue.append(event)
    print("Event added successfully.")

def process_event():
    if event_queue:
        event = event_queue.popleft()
        print("Processing Event:", event)
    else:
        print("No events to process.")

def display_events():
    if event_queue:
        print("\nPending Events:")
        for event in event_queue:
            print(event)
    else:
        print("No pending events.")

def cancel_event():
    event_id = input("Enter Event ID to cancel: ")

    for event in event_queue:
        if event[0] == event_id:
            event_queue.remove(event)
            print("Event cancelled successfully.")
            return

    print("Event not found.")


while True:
    print("\n===== EVENT PROCESSING SYSTEM =====")
    print("1. Add Event")
    print("2. Process Event")
    print("3. Display Pending Events")
    print("4. Cancel Event")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_event()
    elif choice == '2':
        process_event()
    elif choice == '3':
        display_events()
    elif choice == '4':
        cancel_event()
    elif choice == '5':
        print("Exiting Program.")
        break
    else:
        print("Invalid choice.")
