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

import string, sys
from re import search

sys.set_int_max_str_digits(5000000)

# exception class
class BNError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.__message = message
    
    def __str__(self):
        return f"Error happend : {self.__message}..."

class BN:
    def __init__(self, num=0, s = None):
        self.__sign = s
        # our list of digits
        self.__bigNumber = []
        if isinstance(num, int):
            # if it is int, it will change to the string
            num = str(num)
            # change sign flag and adding to the list
            if num[0] == '-':
                # filter numbers that have problem
                if not search(r'^[+-]?\d+$', num[1:]):
                    raise BNError('you can\'t use any characters in your number, just number please')
                num = '-' + str(int(num[1:]))
                if not search(r'[^0]', num[1:]):
                    self.__sign = True
                    self.__bigNumber = ['0']
                    return                     

                self.__sign = False
                #  ignore sign of the number
                self.__bigNumber = [number for number in num[1:]]
            elif num[0] == '+':
                # filter numbers that have problem
                if not search(r'^[+-]?\d+$', num[1:]):
                    raise BNError('you can\'t use any characters in your number, just number please')
                num = '+' + str(int(num[1:]))
                # fill if number is zero
                if not search(r'[^0]', num[1:]):
                    self.__sign = True
                    self.__bigNumber = ['0']
                    return 
                self.__sign = True
                self.__bigNumber = [number for number in num[1:]]
            else:
                # filter numbers that have problem
                if not search(r'^[+-]?\d+$', num):
                    raise BNError('you can\'t use any characters in your number, just number please')
                num = str(int(num))
                if not search(r'[^0]', num):
                    self.__sign = True
                    self.__bigNumber = ['0']
                    return 

                # if big number it isn't non-type, it default make positive
                self.__sign = True
                self.__bigNumber = [number for number in num]
        elif isinstance(num, list):
            num = [x for x in str(int(''.join([str(x) for x in num])))]
            temp = [str(number) for number in num]
            if not search(r'^[+-]?\d+$', ''.join(temp)):
                raise BNError('you can\'t use any characters in your number, just number please')
            if not search(r'[^0]', ''.join(temp)):
                self.__sign = True
                self.__bigNumber = ['0']
                return
            self.__bigNumber = temp
            self.__sign = True
        else:
            raise BNError('you must use int type in big number, please correct it')
    def __len__(self):
        return len(self.__bigNumber)
    def insertNum(self, num, were):
        """_summary_
            this function will add one number in specific part of the number list
        Args:
            num (optional): number that we want to add to the number list
            were (int): place that we want to add it to the list
        """
        self.__bigNumber.insert(were, num)  
    def __getitem__(self, index):
        if isinstance(index, slice):
            temp = self.__bigNumber[index.start:index.stop:index.step]
            if not temp:
                return BN(0, True)
            return BN(temp, self.__sign)
        return int(self.__bigNumber[index])  
    def __setitem__(self, index, val):
        self.__bigNumber[index] = val
    @property
    def Nsign(self):
        """_summary_
            one getter for get sign of the number
        Returns:
            bool: one bool depend on the sign
        """
        return self.__sign
    @Nsign.setter
    def Nsign(self, sign):
        self.__sign = sign
    @property
    def Ndigits(self):
        """_summary_
            one getter for return the list of the numbers
        Returns:
            list: return list of the numbers
        """
        return self.__bigNumber
    @staticmethod
    def isBN(x):
        if not isinstance(x, BN):
            return True
    @property
    def getNum(self):
        temp = int(''.join(self.__bigNumber))
        if self.__sign == False:
            temp *= -1
        return temp
    def __add__(self, other):
        """_summary_
            add function: i write one carry and use it to do sum like on the paper...
            i control len of the self and other and write some section in this part
            if the sign is non-similart, i send it to the sub function to calculate.
        """
        # if other not BN, it will convert it
        if BN.isBN(other): other = BN(other)
        # if two number have one similar sign, it will simply add them togheter and return
        if self.__sign == other.Nsign:
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
                    temp = self[i] + other[i] + carry
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
                    temp = self[i] + other[i] + carry
                    # update carry
                    carry = temp // 10
                    result.insert(0, temp%10)
                # add part that it isn't similar in these two big number
                for i in range(lother*-1 - 1, lself*-1 - 1,-1):
                    # if carry is zero, we just add numbers of the self to result
                    if carry == 0:
                        result.insert(0, self[i])
                        continue
                    temp = self[i] + carry
                    carry = temp // 10
                    result.insert(0, temp%10)
                # if we have one carry in last part, we must add it to the result
                if carry > 0:
                    result.insert(0, carry)
            else:
                # similar to the second condition, just we do it or other big number
                for i in range(-1, lself*-1 - 1, -1):
                    temp = self[i] + other[i] + carry
                    carry = temp // 10
                    result.insert(0, temp % 10)
                for i in range(lself*-1 - 1, lother*-1 - 1, -1 ):
                    if carry == 0:
                        result.insert(0, other[i])
                        continue
                    temp = other[i] + carry
                    carry = temp // 10 
                    result.insert(0, temp % 10)
                if carry > 0:
                    result.insert(0, carry)
                
            # return new BN that is sum result
            return BN(result, self.__sign)
            
        elif self.__sign == True:
            return self - BN(other.Ndigits)
        else:
            return other - BN(self.Ndigits)        
    def __radd__(self, other):
        print(self)
        return self + BN(other)
    def __abs__(self):
        """_summary_
            this will abs our big number and return it for other usage
        Returns:
            BN: abs of the big number
        """
        self.__sign = True
        return self
    def __delitem__(self, index):
        # it will delete one index of the list of the big number
        del self.__bigNumber[index]             
    def __sub__(self, other):
        # if it isn't BN type, it will change it
        if BN.isBN(other): other = BN(other)
        # if sign's different, send to the sum
        if self.__sign != other.Nsign:
            return self + BN(other.Ndigits, self.__sign)
        
        # get len of both self and other
        lself = len(self)
        lother = len(other)
        
        result = []
        
        if self > other:
            BNTemp = self
            for i in range(-1, lother*-1 - 1, -1):
                a = BNTemp[i]
                b = other[i]
                if a >= b:
                    result.insert(0, a-b)
                else:
                    result.insert(0, a-b+10)
                    BNTemp[i-1] = BNTemp[i-1] - 1
            for i in range(lother*-1 - 1, lself*-1 - 1, -1):
                if BNTemp[i] < 0:
                    BNTemp[i-1] -= 1
                    result.insert(0, BNTemp[i] + 10)
                else:
                    result.insert(0, BNTemp[i]) 
            signTemp = self.__sign  
        elif self == other:
            return 0
        else:
            BNTemp = other
            for i in range(-1, lself*-1 - 1, -1):
                a = BNTemp[i]
                b = self[i]
                if a >= b:
                    result.insert(0, a-b)
                else:
                    result.insert(0, a-b+10)
                    BNTemp[i-1] = BNTemp[i-1] - 1
            for i in range(lself*-1 - 1, lother*-1 - 1, -1):
                if BNTemp[i] < 0:
                    BNTemp[i-1]-=1
                    result.insert(0, BNTemp[i] + 10)
                else:
                    result.insert(0, BNTemp[i])  
            signTemp = False if other.Nsign else True
        return BN(result, signTemp)
    def __rsub__(self, other):
        return self - BN(other)
    def __mul__(self, other):
        if BN.isBN(other):other=BN(other)
        resultSign = False if self.Nsign != other.Nsign else True
        self.__sign = True
        other.Nsign = True
        lself = len(self)
        lother = len(other)
        n = max(lself,  lother)
        if self.getNum == 0 or other.getNum == 0:
            return BN(0)
        elif n <= 4:
            return BN(self.getNum * other.getNum)

        m = n // 2
        if lself <= m:
            x = BN(0)
            y = self
        else:
            x = self[:lself - m]
            y = self[lself - m:]

        if lother <= m:
            w = BN(0)
            z = other
        else:
            w = other[:lother - m]
            z = other[lother - m:]

        # r1 = x+y

        r = (x+y)*(w+z)
        p = x * w
        q = y * z

        pH = BN(p.getNum, p.Nsign)
        result = (p<<(2*m)) + ((r - pH - q)<<m) + q

        return  BN(result.getNum, resultSign)
    def __truediv__(self, other):
        if BN.isBN(other): other = BN(other)
        if other.getNum == 0:
            raise ZeroDivisionError('divide bu zero is unsupported')

        result = []
        rem = BN(0)
        for i in range(len(self)):
            divideTemp = rem * 10 + self[i]
            rem = divideTemp % other
            result.append(divideTemp.getNum // (other.getNum))
        return BN(result)

    def __mod__(self, other):
        if BN.isBN(other):other = BN(other)
        rem = 0
        for i in range(len(self)):
            modeTemp = rem * 10 + self[i]
            rem = modeTemp % other.getNum
        return  BN(rem)

    def __rmod__(self, other):
        if BN.isBN(other):other = BN(other)
        rem = 0
        for i in range(len(self)):
            modeTemp = rem * 10 + self[i]
            rem = modeTemp % other.getNum
        return BN(rem)


    def __pow__(self, other):
        result = 1
        while other > 0:
            if other % 2 == 1:
                result *= self.getNum
            self *= self
            other //= 2
        return  result
    def __rshift__(self, time=1):
        for i in range(time):
            del self[-1]
        return self
    def __lshift__(self, time=1):
        for i in range(time):
            self.__bigNumber.append('0')
        return self
    def __lt__(self, other):
        # if other not BN, it will change it
        if BN.isBN(other): other = BN(other)
        # control sign of the numbers
        if self.Nsign==False and other.Nsign==True:
            return True 
        elif self.Nsign==True and other.Nsign==False:
            return False
        
        # now sign is important for next step
        if self.Nsign == True:
            # control len of the numbers
            if len(self) > len(other):
                return False
            elif len(other) > len(self):
                return True
            # two number with same len and sign...ok control one by one
            for i in range(len(self)):
                if self[i] < other[i]:
                    return True
            return False
        else:
            # control len of the numbers
            if len(self) > len(other):
                return True
            elif len(other) > len(self):
                return False
            
            for i in range(len(self)):
                if self[i]>other[i]:
                    return True
            return False
    def __gt__(self, other):
        if BN.isBN(other): other = BN(other)
        # control sign of the numbers
        if self.Nsign==False and other.Nsign==True:
            return False 
        elif self.Nsign==True and other.Nsign==False:
            return True
        
        # now sign is important for next step
        if self.Nsign == True:
            # control len of the numbers
            if len(self) > len(other):
                return True
            elif len(other) > len(self):
                return False
            # two number with same len and sign...ok control one by one
            for i in range(len(self)):
                if self[i]>other[i]:
                    return True
            return False
        else:
            # control len of the numbers
            if len(self) > len(other):
                return False
            elif len(other) > len(self):
                return True
            
            for i in range(len(self)):
                if self[i]<other[i]:
                    return True
            return False
    def __le__(self, other):
        if BN.isBN(other): other = BN(other)
        # control sign of the numbers
        if self.Nsign==False and other.Nsign==True:
            return True 
        elif self.Nsign==True and other.Nsign==False:
            return False
        
        # now sign is important for next step
        if self.Nsign == True:
            # control len of the numbers
            if len(self) > len(other):
                return False
            elif len(other) > len(self):
                return True
            # two number with same len and sign...ok control one by one
            # for equal, i set one flag!
            same = True
            for i in range(len(self)):
                if self[i]<other[i]:
                    return True
                if self[i]!=other[i]:
                    same=False
            if same:
                return True
            return False
        else:
            # control len of the numbers
            if len(self) > len(other):
                return True
            elif len(other) > len(self):
                return False
            
            same = True
            for i in range(len(self)):
                if self[i]>other[i]:
                    return True
                if self[i]!=other[i]:
                    same = False
            if same:
                return True
            return False
    def __ge__(self, other):
        if BN.isBN(other): other = BN(other)
        # control sign of the numbers
        if self.Nsign==False and other.Nsign==True:
            return False 
        elif self.Nsign==True and other.Nsign==False:
            return True
        
        # now sign is important for next step
        if self.Nsign == True:
            # control len of the numbers
            if len(self) > len(other):
                return True
            elif len(other) > len(self):
                return False
            # two number with same len and sign...ok control one by one
            # for control equal i use one flag
            same = True
            for i in range(len(self)):
                if self[i]>other[i]:
                    return True
                if self[i]!=other[i]:
                    same = False
            if same:
                return True
            return False
        else:
            # control len of the numbers
            if len(self) > len(other):
                return False
            elif len(other) > len(self):
                return True
            
            same = True
            for i in range(len(self)):
                if self[i]<other[i]:
                    return True
                if self[i]!=other[i]:
                    same = False
            if same:
                return True
            return False  
    def __eq__(self, other):
        if BN.isBN(other): other = BN(other)
        # if len or sign is different, it  will return false
        if self.Nsign != other.Nsign or len(self)!=len(other):
            return False

        # if len and sign is same, time for cheking number by number
        for i in range(len(self)):
            if self[i]!=other[i]:
                return False
        return True
    def __ne__(self, other):
        if BN.isBN(other): other = BN(other)
        # if len or sign is different, it  will return false
        if self.Nsign != other.Nsign or len(self)!=len(other):
            return True

        # if len and sign is same, time for cheking number by number
        for i in range(len(self)):
            if self[i]!=other[i]:
                return True
        return False
    def __isub__(self, other):
        if BN.isBN(other): other = BN(other)
        temp = self - other
        return temp
    def __iadd__(self, other):
        if BN.isBN(other): other = BN(other)
        # do the sum
        temp = self + other
        return temp
    def __imul__(self, other):
        if BN.isBN(other): other = BN(other)
        temp = self * other
        return temp
    def __ipow__(self, other):
        if isinstance(other, BN): other = other.getNum
        temp = self ** other
        return  self
    def __idiv__(self, other):
        if BN.isBN(other): other=BN(other)
        temp = self / other
        return temp
    def __repr__(self):
        # control the sign and send the output
        if self.__sign:   
            return ''.join(self.__bigNumber)
        else:
            return '-' + ''.join(self.__bigNumber)
    def __str__(self):
        if self.__sign:   
            return ''.join(self.__bigNumber)
        else:
            return '-' + ''.join(self.__bigNumber)
    def __del__(self):
        pass
    