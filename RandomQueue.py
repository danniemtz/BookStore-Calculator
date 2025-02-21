import numpy as np
import random
from ArrayQueue import ArrayQueue
import random


class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)

    def remove(self) -> object:
        """
            remove a random element
            You can call the method of the parent class using super(). e.g.
            super().remove()
        """
        if self.n <= 0:
            raise IndexError("List is empty")
        head_ele = self.a[self.j%len(self.a)]
        rand = random.randint(0, self.n - 1)
        random_element = self.a[(self.j + rand) % len(self.a)]
        self.a[(self.j + rand) % len(self.a)] = head_ele
        super().remove()
        return random_element



"""
IDK WHAT I DID: basically head is equal to the element j in array.
element j equal to whatever first element is (circular array thing) 
rand is a random integer in length of array.
now head is equal to array index rand ( whatever was chosen)
rand is now equal to j (head)
return the random element swapped with head
idk
"""


