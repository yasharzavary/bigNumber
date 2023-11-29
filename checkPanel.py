from BigNumber import BN

print(True * -1)

print(BN(-989662) + BN(-5236598))
print(989662 + 5236598)

print(BN(563) - BN(123456))
print(563 - 123456)
# print(abs(BN('-549563289')))

# print(BN(1423) == BN(1423))

print(BN(-563) + BN(123456))
print(-563 + 123456)

x = BN(1234567895123145693215621556214856215)
x+=1
print(x)
