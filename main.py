import Calculator
import BookStore
import ChainedHashTable
import DLList



def menu_calculator():
    calculator = Calculator.Calculator()
    option = ""
    while option != '0':
        print("""
        1 Check mathematical expression 
        2 Store variable values
        3 Print expression with values
        4 Evaluate expression
        0 Return to main menu
        """)
        option = input()
        if option == "1":
            expression = input("Introduce the mathematical expression: ")
            if calculator.matched_expression(expression) == True:
                print(f"{expression} is a valid expression")
            else:
                print(f"{expression} is an invalid expression")
        if option == "2":
            valid = False
            while not valid:
                variable = input("Enter a variable: ")
                value = float(input("Enter a value: "))
                calculator.set_variable(variable, value)
                yes_no = input("Enter another variable? Y/N ")
                if yes_no == "Y":
                    valid = False
                else:
                    valid = True
        if option == "3":
            expression = input("Introduce the mathematical expression: ")
            if calculator.matched_expression(expression) == False:
                print("Invalid Expression")
                continue
            calculator.print_expression(expression)
        if option == '4':
            expression = input("Enter the expression: ")
            exp = calculator.print_expression(expression)
            error = False
            for val in exp:
                if val.isalnum() == True:
                    error = True
                    print("Result: Error - Not all variable values are defined.")
                    break
            if error == False:
                print(f"Evaluating expression: {exp}")
                print(f"Result: {calculator.evaluate(expression)}")

        ''' 
        Add the menu options when needed
        '''


def menu_bookstore_system():
    bookStore = BookStore.BookStore()
    option = ""
    while option != '0':
        print("""
        s FIFO shopping cart
        r Random shopping cart
        1 Load book catalog
        2 Remove a book by index from catalog
        3 Add a book by index to shopping cart
        4 Remove from the shopping cart
        5 Search book by infix
        6 Get cart best-seller
        7 Add a book by key to shopping cart
        8 Add book by prefix
        9 Search best-sellers with infix
        0 Return to main menu
        """)
        option = input()
        if option == "r":
            bookStore.setRandomShoppingCart()
        elif option == "s":
            bookStore.setShoppingCart()
        elif option == "1":
            file_name = input("Introduce the name of the file: ")
            bookStore.loadCatalog(file_name)
            # bookStore.pathLength(0, 159811)
        elif option == "2":
            i = int(input("Introduce the index to remove from catalog: "))
            bookStore.removeFromCatalog(i)
        elif option == "3":
            i = int(input("Introduce the index to add to shopping cart: "))
            bookStore.addBookByIndex(i)
        elif option == "4":
            bookStore.removeFromShoppingCart()
        elif option == "5":
            infix = input("Introduce the query to search: ")
            cnt = int(input("Enter max number of results: "))
            bookStore.searchBookByInfix(infix, cnt)
        elif option == '6':
            bookStore.getCartBestSeller()
        elif option == '7':
            key = input("Enter book key: ")
            bookStore.addBookByKey(key)
        elif option == '8':
            pre = input("Introduce the prefix: ")
            book = bookStore.addBookByPrefix(pre)
            #print(f"Added first matched title: {book}")
        elif option == '9':
            bookStore.bestsellers_with(input('Enter infix: '),
                                       int(input('Enter structure (1 or 2): ')),
                                       int(input('Enter max number of titles: ')))

        ''' 
        Add the menu options when needed
        '''
def menu_palindrome():
    palindrom = DLList.DLList()
    user_input = input("Enter a word/phrase: ")
    user_pal = user_input.lower().replace(" ", "")
    string = []
    for y in user_pal:
        if y.isalpha() == True:
            string.append(y)
    for x in string:
        palindrom.append(x)

    if palindrom.isPalindrome() == True:
        print("Result: Palindrome")
    else:
        print("Result: Not a Palindrome")


# main: Create the main menu
def main():
    option = ""
    while option != '0':
        print("""
        1 Calculator
        2 Bookstore System
        3 Palindrome Test
        0 Exit/Quit
        """)
        option = input()

        if option == "1":
            menu_calculator()
        elif option == "2":
            menu_bookstore_system()
        elif option == "3":
            menu_palindrome()


if __name__ == "__main__":
    main()
