from booklover import BookLover
import unittest

class BookLoverTestSuite(unittest.TestCase): 
    
    def test_01_add_book(self):
        # Add a book and test if it is in book_list.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book('Persona', 4)
        self.assertTrue(test_object.has_read('Persona'))
        
    def test_02_add_book(self):
        #Add the same book twice. Test if it's in
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Uzumaki", 5)
        test_object.add_book("Uzumaki", 5)
        expected = 1
        self.assertEqual(test_object.num_books_read(), expected)

    def test_03_has_read(self):
        #Pass a book in the list and test the answer is True.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("The Hobbit", 5)
        self.assertTrue(test_object.has_read("The Hobbit"))
            
    def test_04_has_read(self):
        #Pass a book NOT in the list and use assert False to test if the answer is True
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Iliad", 4)
        self.assertFalse(test_object.has_read('Cat in the Hat'))
        
    def test_05_num_books_read(self):
        # Add some books to the list, and test num_books matches expected.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Gilgamesh", 4)
        test_object.add_book("The Witcher", 5)
        test_object.add_book("Pandemonium", 2)
        expected = 3
        self.assertEqual(test_object.num_books_read(), expected)
        
    def test_06_fav_books(self):
        #Add some books with ratings to the list, making sure some of them have rating > 3. 
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Inuyasha", 4)
        test_object.add_book("Japanese tattooing", 5)
        test_object.add_book("Gods and Monsters", 1)
        expected =  2
        actual = len(test_object.fav_books()['book_rating'] > 3)
        self.assertEqual(actual, expected)
            
        
if __name__ == '__main__':

    unittest.main(verbosity=3)