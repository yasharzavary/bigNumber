"""_summary_
    big number class is maded for some very big numbers...
    like one number with 100 digits...
    
    this class made with list base calculation...
    it mean that all numbers add in one list amd do all functions on this list
    (i add other type of this class in my github that maded with string base calculation)\
    https://github.com/yasharzavary
    
    my linkedin:
    https://www.linkedin.com/in/yasharzavary360/
    
    you can do all math functions with this function and you can use for your codes
    it can be used in all fields like in astronomy, biotech and other fields
    
    writer:
        yashar zavary rezaie(student of KHU, Tehran_Iran)

"""

import string
from re import search

# exception class
class BNError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.__message = message
    
    def __str__(self):
        return f"Error happend : {self.__message}..."

class BN:
    def __init__(self, num=0):
        """_summary_
            make one big number depend of the num's type...
        Args:
            num (, optional): value of the big number
        """
        # our list of digits
        self.__bigNumber = []
        # fill the list depend on the type of the num
        if isinstance(num, str):
            if search(r'[^1-9]', num):
                raise BNError('you can\'t use any characters in your number, just number please')
            # adding to the list
            self.bigNumber = [number for number in num]
        elif isinstance(num, int):
            # change to the string and add it to the list
            self.bigNumber = [number for number in str(num)]
        elif isinstance(num, list):
            self.bigNumber = num
    
    def __len__(self):
        """_summary_
            return number of number's digits
        Returns:
            int: ...
        """
        return len(self.bigNumber)
    
    def insertNum(self, num, were):
        """_summary_
            this function will ad one number in specific part of the number list
        Args:
            num (optional): number that we want to add to the number list
            were (int): place that we want to add it to the list
        """
        self.bigNumber.insert(num, were)
         
    def __add__(self, other):
        lself = len(self)
        lother = len(other)
          
        if lself > lother:
            for _ in range(lself - lother):
                self.insertNum(0, 0)
        elif lother > lself:
            for _ in range(lother - lself):
                other.insertNum(0,0)
                
        result = []
        carry = 0
        for i in range(len(other)-1, -1, -1):
            numTemp = (self.bigNumber[i] + other.bigNumber[i] + carry) % 10
            carry = numTemp // 10
            result.insert(numTemp, 0)
        
        
            
             
        
    def __sub__(self, other):
        pass
    def __mul__(self, other):
        pass
    def __truediv__(self, other):
        pass
    def __floordiv__(self, other):
        pass
    def __mod__(self, other):
        pass
    def __pow__(self, other):
        pass
    def __rshift__(self, other):
        pass
    def __lshift__(self, other):
        pass
    def __lt__(self, other):
        pass
    def __gt__(self, other):
        pass
    def __le__(self, other):
        pass
    def __ge__(self, other):
        pass
    def __eq__(self, other):
        pass
    def __ne__(self, other):
        pass
    def __isub__(self, other):
        pass
    def __iadd__(self, other):
        pass
    def __imul__(self, other):
        pass
    def __ipow__(self, other):
        pass
    def __idiv__(self, other):
        pass
    def __ifloordiv__(self, other):
        pass
    
    def __repr__(self):
        pass
    def __str__(self):
        """_summary_
            str magic function of the class
        """
        return ''.join(self.bigNumber)
    def __del__(self):
        pass
    