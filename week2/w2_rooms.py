rooms = {100: ['Single', 2, 50, True],
         101: ['Double', 2, 75, True],
         102: ['Suite', 4, 100, True],
         200: ['Single', 2, 50, True]}

def main():
    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice: '))
        if choice   == 1:   show_all()
        elif choice == 2:   add()
        elif choice == 3:   edit()
        elif choice == 4:   delete()
        elif choice == 5:   check_in()
        elif choice == 6:   check_out()
        elif choice == 0:   running = False
        else:               print('Invalid choice!')
    
    print('Prgram stops.')

def print_menu():
    print('ROOM MANAGEMENT SYSTEM')
    print('1. Show all rooms')
    print('2. Add room')
    print('3. Edit room')
    print('4. Delete room')
    print('5. Check in')
    print('6. Check out')
    print('0. Quit')

def show_all():
    if len(rooms) == 0:
        print('No rooms in store')
        return
    
    for room, info in rooms.items():
        print('Room number:', room)
        print('Room type:', info[0])
        print('Max guests:', info[1])
        print(f'Price ${info[2]}')
        print('Status:', 'Available' if info[3] else 'Occupied')

def add():
    # enter room number
    room = int(input('Enter room number: '))
    # validate room unique
    if room in rooms:
        print(f'Room {room} existed. Please choose other room number.')
        return
    # enter other information
    room_type = input('Enter room type: ')
    max_guests = int(input('Enter max guests: '))
    price = int(input('Enter price: '))
    status = True
    # add room information into dictionary
    rooms[room] = [room_type, max_guests, price, status]
    print('Add new room success.')

def edit():
    # enter room number
    room = int(input('Enter room number to edit: '))
    # validate room unique
    if room not in rooms:
        print(f'Room {room} not existed. Please choose other room number.')
        return
    # check room status
    if rooms[room][3] == False:
        print(f'Room {room} is occupied. Cannot edit.')
        return

    # enter other information
    room_type = input('Enter room type: ')
    max_guests = int(input('Enter max guests: '))
    price = int(input('Enter price: '))
    status = True
    # add room information into dictionary
    rooms[room] = [room_type, max_guests, price, status]
    print('Edit room success.')

def delete():
    # enter room number
    room = int(input('Enter room number to delete: '))
    # validate room unique
    if room not in rooms:
        print(f'Room {room} not existed. Please choose other room number.')
        return
    # check room status
    if rooms[room][3] == False:
        print(f'Room {room} is occupied. Cannot delete.')
        return

    del rooms[room]
    print(f'Room {room} deleted.')

def check_in():
    # enter room number
    room = int(input('Enter room number to check in: '))
    # validate room unique
    if room not in rooms:
        print(f'Room {room} not existed. Please choose other room number.')
        return
    # check room status
    if rooms[room][3] == False:
        print(f'Room {room} is occupied. Cannot check in.')
        return

    room_info = rooms[room]
    room_info[3] = False

    print(f'Room {room} checked in.')

def check_out():
    # enter room number
    room = int(input('Enter room number to check out: '))
    # validate room unique
    if room not in rooms:
        print(f'Room {room} not existed. Please choose other room number.')
        return
    # check room status
    if rooms[room][3] == True:
        print(f'Room {room} is not occupied. Cannot check out.')
        return

    room_info = rooms[room]
    room_info[3] = True

    print(f'Room {room} checked out.')