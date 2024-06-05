ids = [1, 2, 3]
titles = ['Harry Potter', 'The Lord of the Rings', 'The Alchemist']
authors = ['J.K. Rowling', 'J.R.R. Tolkien', 'Paulo Coelho']
statuses = [True, False, True]

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
        elif choice == 6:   borrow()
        elif choice == 0:   running = False
        else:               print('Invalid choice!')
    
    print('Prgram stops.')

def print_menu():
    print('LIBRARY MANAGEMENT SYSTEM')
    print('1. Show all books')
    print('2. Add book')
    print('3. Edit book')
    print('4. Delete book')
    print('5. Search book')
    print('6. Borrow book')
    print('0. Quit')

def show_all():
    if len(titles) == 0:
        print('No books in store')
        return
    
    for i in range(len(titles)):
        print(f'Book ID {ids[i]}, title: {titles[i]}, author: {authors[i]}, status: {statuses[i]}')

def add():
    # enter book id
    id = int(input('Enter book id: '))
    # check id exist => error
    pos = check_id_exist(id)
    if pos != -1:
        print(f'ID {id} existed. Please choose other id.')
        return
    # enter other information
    title = input('Enter book title: ')
    author = input('Enter book author: ')
    status = True
    # add book information into 3 lists
    ids.append(id)
    titles.append(title)
    authors.append(author)
    statuses.append(status)
    print('Add new book success.')

def check_id_exist(id):
    for i in range(len(ids)):
        if ids[i] == id:
            return i
    return -1

def edit():
    # enter book id
    id = int(input('Enter book id to edit: '))
    # check id not exist => error
    pos = check_id_exist(id)
    if pos == -1:
        print(f'ID {id} not found.')
        return
    # enter other information
    title = input('Enter new book title: ')
    author = input('Enter new book author: ')
    # update book information
    titles[pos] = title
    authors[pos] = author
    print('Edit book success.')

def delete():
    # enter book id
    id = int(input('Enter book id to delete: '))
    # check id not exist => error
    pos = check_id_exist(id)
    if pos == -1:
        print(f'ID {id} not found.')
        return
    # delete book information
    ids.pop(pos)
    titles.pop(pos)
    authors.pop(pos)
    statuses.pop(pos)
    print('Delete book success.')

def search():
    # enter author to search
    author = input('Enter author to search: ')
    # search by for loop, if found print book information
    count = 0
    for i in range(len(authors)):
        if authors[i].lower() == author.lower():
            print(f'Book ID {ids[i]}, title: {titles[i]}, author: {authors[i]}, status: {statuses[i]}')
            count += 1
    if count == 0:
        print(f'No book found for author {author}.')
    else:
        print(f'Total {count} books found for author {author}.')

def borrow():
    # enter book id
    id = int(input('Enter book id to borrow: '))
    # check id not exist => error
    pos = check_id_exist(id)
    if pos == -1:
        print(f'ID {id} not found.')
        return
    # check status
    if statuses[pos] == False:
        print(f'Book ID {id} is not available.')
        return
    # update status
    statuses[pos] = False
    print(f'Borrow book ID {id} success.')

#### MAIN ####
main()
