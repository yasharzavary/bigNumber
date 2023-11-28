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
    def __init__(self, num=0, s = None):
        """_summary_
            make one big number depend of the num's type...
        Args:
            num (, optional): value of the big number
            s(bool,optional): sign of the number
        """
        # default it is True, in init we check it
        self.__sign = s
        # our list of digits
        self.__bigNumber = []
        if isinstance(num, int):
            # if it is int, it will change to the string
            num = str(num)
        # fill the list depend on the type of the num
        if isinstance(num, str):
            # filter numbers that have problem
            if not search(r'^[+-]?\d+$', num[1:]):
                raise BNError('you can\'t use any characters in your number, just number please')
   
            # change sign flag and adding to the list
            if num[0] == '-':
                self.__sign = False
                #  ignore sign of the number
                self.__bigNumber = [number for number in num[1:]]
            elif num[0] == '+':
                self.__sign = True
                self.__bigNumber = [number for number in num[1:]]
            else:
                # if big number it isn't non-type, it default make positive
                self.__sign = True
                self.__bigNumber = [number for number in num]
                

        elif isinstance(num, list):
            temp = [str(number) for number in num]
            if not search(r'^[+-]?\d+$', ''.join(temp)):
                raise BNError('you can\'t use any characters in your number, just number please')
            self.bigNumber = temp
    def __len__(self):
        """_summary_
            return number of number's digits
        Returns:
            int: ...
        """
        return len(self.__bigNumber)
    def insertNum(self, num, were):
        """_summary_
            this function will ad one number in specific part of the number list
        Args:
            num (optional): number that we want to add to the number list
            were (int): place that we want to add it to the list
        """
        self.__bigNumber.insert(were, num)  
    def itemGetter(self, index):
        """_summary_
            it will return number of one postion that we get it to the function
        Args:
            index (int): position of the number that user want

        Returns:
            int: send back num of that position
        """
        return int(self.__bigNumber[index])       
    @property
    def Nsign(self):
        """_summary_
            one getter for get sign of the number
        Returns:
            bool: one bool depend on the sign
        """
        return self.__sign  
    @property
    def Ndigits(self):
        """_summary_
            one getter for return the list of the numbers
        Returns:
            list: return list of the numbers
        """
        return self.__bigNumber
    def __add__(self, other):
        """_summary_
            this will sum two big number
            
        Args:
            other (BN): number that we want to add to this number
        """
        # if two number have one similar sign, it will simply add them togheter and return
        if self.Nsign == other.Nsign:
            # one empty list for the new number
            result = []
            # our carry for the next step
            carry = 0
            
            # i get len of the numbers for use it in the adding part
            lself = len(self)
            lother = len(other)
            
            # if len of them is similar, we have simple way...
            # add them and send them with one of the signs
            if lself == lother:
                # i loop and sum one by one and add them to the result list
                for i in range(-1, lself*-1 - 1, -1):
                    temp = self.itemGetter(i) + other.itemGetter(i) + carry
                    # carry update
                    carry = temp // 10
                    # adding to the result
                    result.insert(0, temp%10)
                # check for extra digit(if we have...)
                if carry > 0:
                    result.insert(0, carry)
                    
            # if one of the numbers have longer len than other
            elif lself > lother:
                # add two number's similar len part
                for i in range(-1, lother*-1 - 1, -1):
                    # make one temp and add two index
                    temp = self.itemGetter(i) + other.itemGetter(i) + carry
                    # update carry
                    carry = temp // 10
                    result.insert(0, temp%10)
                # add part that it isn't similar in these two big number
                for i in range(lother*-1 - 1, lself*-1 - 1,-1):
                    # if carry is zero, we just add numbers of the self to result
                    if carry == 0:
                        result.insert(0, self.itemGetter(i))
                    temp = self.itemGetter(i) + carry
                    carry = temp // 10
                    result.insert(0, temp%10)
                # if we have one carry in last part, we must add it to the result
                if carry > 0:
                    result.insert(0, carry)
            else:
                # similar to the second condition, just we do it or other big number
                for i in range(-1, lself*-1 - 1, -1):
                    temp = self.itemGetter(i) + other.itemGetter(i) + carry
                    carry = temp // 10
                    result.insert(0, temp % 10)
                for i in range(lself*-1 - 1, lother*-1 - 1, -1 ):
                    if carry == 0:
                        result.insert(0, other.itemGetter(i))
                    temp = other.itemGetter(i) + carry
                    carry = temp // 10 
                    result.insert(0, temp % 10)
                if carry > 0:
                    result.insert(0, carry)
                
            # return new BN that is sum result
            return BN(result, self.Nsign)
            
        elif self.Nsign == True:
            return self - BN(other.Ndigits)
        else:
            return other - BN(self.Ndigits)        
        
            
             
        
    def __sub__(self, other):
        """_summary_
            this will subtract two big number
        Args:
            other (BN): big number that we want to use int he sub function
        """
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
    