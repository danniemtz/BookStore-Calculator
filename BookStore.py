import Book
import ArrayList
import ArrayQueue
#import RandomQueue
import DLList
import SLLQueue
import ChainedHashTable
import BinarySearchTree
import BinaryHeap
# import AdjacencyList
import time
import MaxQueue


class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''

    def __init__(self):
        self.bookCatalog = DLList.DLList()
        self.shoppingCart = ArrayQueue.ArrayQueue() #SLLQueue.SLLQueue() #MaxQueue.MaxQueue()
        # adding attribute for chained hash tables
        self.bookIndicis = ChainedHashTable.ChainedHashTable()
        self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()

    def loadCatalog(self, fileName: str):
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = ArrayList.ArrayList() #DLList.DLList()
        with open(fileName, encoding="utf8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(s)
                #self.bookIndicis.add(key, self.bookCatalog.size() -1)
                self.sortedTitleIndices.add(title, self.bookCatalog.size() -1)

            # The following line is used to calculate the total time 
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def setShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def removeFromCatalog(self, i: int):
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i: int):
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def searchBookByInfix(self, infix: str, cnt : int):
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string    
        '''
        start_time = time.time()
        num = 0
        for book in self.bookCatalog:
            if infix in book.title:
                print(book)
                num += 1
            if num == cnt:
                break

        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self):
        '''
        removeFromShoppingCart: remove one book from the shoppung cart  
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")

    def getCartBestSeller(self):
        """returns the best-selling book (books already  stored in max order)"""
        start_time = time.time()
        i = self.shoppingCart.max().title
        elapsed_time = time.time() - start_time
        print(f"getCartBestseller returned")
        print(i)
        print(f"Completed in {elapsed_time:0.1f} seconds")

    def addBookByKey(self, key):
        """adds book with the given key to the shopping cart"""
        start_time = time.time()
        x = self.bookIndicis.find(key)
        if x is not None:
            b = self.bookCatalog.get(x)
            self.shoppingCart.add(b)
        elapsed_time = time.time() - start_time
        print(f"addBookByKey Completed in {elapsed_time} seconds")

    def addBookByPrefix(self, prefix):
        if prefix != "":
            book_ind = self.sortedTitleIndices.find_node(prefix).v
            if book_ind != None:
                b = self.bookCatalog.get(book_ind)
                if len(b.title) >= len(prefix):
                    if b.title[0:len(prefix)] == prefix:
                        self.shoppingCart.add(b)
                        return b.title
        return None

    def bestsellers_with(self, infix, structure, n=0):
        best_sellers = None
        if structure == '1':
            best_sellers = BinarySearchTree.BinarySearchTree()
        elif structure == '2':
            best_sellers = BinaryHeap.BinaryHeap()
        else:
            print("Invalid data structure.")
        if best_sellers is not None:
            if infix == "":
                print("Invalid infix.")
            else:
                start_time = time.time()
                if n < 0:
                    print('Invalid number of titles')
                elif n == 0:
                    for b in self.bookCatalog:
                        if infix in b.title:
                            best_sellers.add(b)
                elif n > 0:
                    n2 = 0
                    for b in self.bookCatalog:
                        if n2 < n:
                            if infix in b.title:
                                best_sellers.add(b)
                        else:
                            break
                if structure == 2:
                    for b in best_sellers.a:
                        print(b)
                if structure == 1:
                    for b in reversed(best_sellers.in_order()):
                        print(b)

                elapsed_time = time.time() - start_time

                print(f"Displayed bestsellers_with({infix}, {structure}, {n}) in {elapsed_time} seconds")
        #pass


