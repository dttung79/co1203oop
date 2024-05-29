ids = [1, 2, 3]
names = ['Computer', 'Monitor', 'Keyboard']
prices = [1000, 300, 50]

def main():
    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice: '))
        if choice   == 1:   show_all()
        elif choice == 2:   add()
        elif choice == 3:   edit()
        elif choice == 4:   delete()
        elif choice == 5:   search()
        elif choice == 0:   running = False
        else:               print('Invalid choice!')
    
    print('Prgram stops.')

def print_menu():
    print('PRODCUT MANAGEMENT SYSTEM')
    print('1. Show all products')
    print('2. Add product')
    print('3. Edit price')
    print('4. Delete product')
    print('5. Search product')
    print('0. Quit')

def show_all():
    if len(ids) == 0:
        print('No products in store')
        return
    
    for i in range(len(ids)):
        print(f'Product ID {ids[i]}, name: {names[i]}, price: ${prices[i]}')
    
def add():
    # enter product id
    id = int(input('Enter product id: '))
    # check id exist => error
    pos = check_id_exist(id)
    if pos != -1:
        print(f'ID {id} existed. Please choose other id.')
        return
    # enter other information
    name = input('Enter product name: ')
    price = int(input('Enter product price: '))
    # add product information into 3 lists
    ids.append(id)
    names.append(name)
    prices.append(price)
    print('Add new product success.')

def check_id_exist(id):
    for i in range(len(ids)):
        if ids[i] == id:
            return i
    return -1

def edit():
    # enter product id
    id = int(input('Enter product id to edit: '))
    # check id not exist => error
    pos = check_id_exist(id)
    if pos == -1:
        print(f'No product for ID {id}')
        return
    # enter new price
    new_price = int(input('Enter new price: '))
    # edit price
    prices[pos] = new_price
    print(f'New price ${new_price} updated for product ID {id}.')

def delete():
    # enter product id
    id = int(input('Enter product id to delete: '))
    # check id not exist => error
    pos = check_id_exist(id)
    if pos == -1:
        print(f'No product for ID {id}')
        return
    # delete id, name, price in 3 lists at found position (ids.pop(pos))
    ids.pop(pos)
    names.pop(pos)
    prices.pop(pos)
    print(f'Delete product ID {id} success.')

def search():
    # enter product name
    name = input('Enter product name to search: ')
    # search by for loop, if found print product information
    count = 0
    for i in range(len(names)):
        if names[i] == name:
            print(f'Product ID: {ids[i]}, name: {names[i]}, price: ${prices[i]}')
            count += 1
    # if not found => print error
    if count == 0:
        print(f'No product found for name {name}')

    
#### MAIN ####
main()