from function import view_books,select_book,add_book,mark_book,delete

username=input('Please enter username.')
print(f'Wecome from Book Library- {username}')
print('1->View all the books in this library.')
print('2->Select the book want to read.')
print('3->Add book.')
print('4->Mark the book already read')
print('5->Delete the existing book.')
print('6->Exit')
loop=True
while loop==True:
    choose_number=int(input('Enter the number of the options above.'))
    if choose_number==1:
        view_books()    
    elif choose_number==2:
        select_book()
    elif choose_number==3:
        add_book()
    elif choose_number==4:
        mark_book()
    elif choose_number==5:
        delete()
    elif choose_number==6:
        print(f'See u next time! {username}')
        loop=False
