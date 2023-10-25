import pandas as pd

class BookLover:
   
    # test function
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})): 
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.book_list = book_list
        self.num_books = len(self.book_list['book_name'])
        
#method 1
    def add_book(self, book_name, book_rating:int):
        if not any(self.book_list['book_name'] == book_name):
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [book_rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)

#method 2
    def has_read(self, book_name):
        return any(self.book_list['book_name'] == book_name)
            
        
#method 3
    def num_books_read(self):
        return len(self.book_list['book_name'])
    
#method 4
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]
