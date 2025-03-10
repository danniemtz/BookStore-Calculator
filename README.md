# BookStore-Calculator
Data Structures focused, Python Based Project

Installation

Install Python 3.8 or higher and numpy. A highly recommended IDE is PyCharm 
https://www.jetbrains.com/pycharm/.

Calculator 

The calculator exemplifies the use of Stacks, HashTables and BinaryTrees. It allows defining mathematical expression with variables, assigning values to the variables and evaluate it.

BookStore

BookStore uses a fraction of the Amazon database to exemplify the use of several data structures
such as Queues, Lists, HashTables, BinarySearch Trees, Heaps, Graphs and sorting. The program
allows adding books to a shopping cart. 

The entry point (main program) is the file main.py. That is done using the 
following lines: 

if __name__ == "__main__":
    main()

To run the program in command line use:

% python3.8 main.py

In Pycharm you can use the otions in the "run" tab.

The program will present the main menu with three options: 
        1 Calculator
        2 Bookstore System
        0 Exit/Quit
Pressing 1 or 2 and the enter will take you to a second menu with different 
options. The python function that allows to accept an input from the keyboard 
is input(). Use the same pattern to add new options accordingly.

The project is organized in different files (modules):
1. main.py: The main entry point of the program. It will present the menu that executes the assignments
2. Calculator.py: The calculator system to be done
3. BookStore.py: The book store system to be done during the semester
4. Book.py: Data class that holds the attributes of a book. The class allows to compare ranks using the operator < or >
5. SortableBook.py: Data class that holds the attributes of a book. The class allows to compare by alphabetical order   using the operator < or >
6. Interfaces.py: The interfaces to be implemented during the semeter: Stack, Queue, Deque, List, Set, Graph
7. ArrayStack.py: It will implement the interface Stack
8. ArrayQueue.py: It will implement the interface Queue
9. ArrayList.py: It will implement the interface List
10. ArrayDeque.py: It implements the interface Deque. It is a specialization (Inheritance) of ArrayList
11. RandomQueue.py: It will implement the interface Queue. It is a specialization (Inheritance) of ArrayQueue
12. SLLStack.py: It will implement the interface Stack
13. SLLQueue.py: It will implement the interface Queue
14. DLList.py: It will implement the interface List
15. DLLDeque.py: It implements the interface Deque. It is a specialization (Inheritance) of DLLList.
16. ChainedHashTable.py: It will implement the interface Set
17. BinarySearchTree.py: It will implement the interface Set
18. BinaryHeap.py: It will implement the interface Queue. It removes the element with highest priority
18. algorithms.py: It will implement the sorting algorithms
20. AdjacencyList.py: It will implement the Graph interface using the adjencency list
21. AdjacencyMatrix.py: It will implement the Graph interface using the adjacency matrix
22. RedBlackTree.py: It will implement the interface Set a balance tree.  This will be given as an extra-credit assignment, if time permits discussion of the relevant topics.


<img width="271" alt="Screenshot 2025-02-21 at 11 43 40 AM" src="https://github.com/user-attachments/assets/73c3a281-3a02-499c-a198-797b30186da7" />


