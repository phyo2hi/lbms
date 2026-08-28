from book_database import data

def view_books():
    for i, book_data in enumerate(data):
     print(f'{i+1}.Book name->{book_data['book_name']},Writer->{book_data['writer']},Complete reading->{book_data['completed']}')


def select_book():
    for i, book_data in enumerate(data):
        print(f"{i+1}.Book name->{book_data['book_name']},Writer->{book_data['writer']},Complete reading->{book_data['completed']}")
        
    book_number = int(input('select the book number you want to read: '))     
    if 1 <= book_number <= len(data):
        selected_book = data[book_number - 1]
        
        print(f"\nBook name->{selected_book['book_name']},\nWriter->{selected_book['writer']},\nBook_summary->{selected_book['detail']},\nComplete reading->{selected_book['completed']}")
    else:
        print("Invalid book number!")


def add_book():
   name=(input('Enter the book name\n'))
   write=(input('Enter the book writer\n'))
   book_detail=(input('Enter the book summary\n'))
   new_book= {
         'id':len(data)+1,
         'book_name': name,
         'writer':write,
         'completed':False,  
         'detail': book_detail
                 }
   
   data.append(new_book)
   print('New book added successfully')

def mark_book():
   for i, book_data in enumerate(data):
     print(f'{i+1}.Book name->{book_data['book_name']},Writer->{book_data['writer']},Complete reading->{book_data['completed']}')
   mark=int(input('Select the book you already read: '))
   if 1<=  mark <= len(data):
      data[mark-1]['completed']=True
   print('Added that book to already read') 

def delete():
   for i, book_data in enumerate(data):
     print(f'{i+1}.Book name->{book_data['book_name']},Writer->{book_data['writer']},Complete reading->{book_data['completed']}')
   num =int(input('Select the book number you want to delete: '))
   if 1<=num<=len(data):
      data.pop(num-1)
   print('Deleted successfully!')




    

       
