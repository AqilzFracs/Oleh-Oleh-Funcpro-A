sequenceGenerator = lambda start, stop : [i for i in range(start, stop+1)]
print(sequenceGenerator(1, 10))

fizzBuzzlist = lambda a, b: ["FizzBuzz" if num % 3 == 0 and num % 5 == 0 else "Fizz" if num % 3 == 0 else "Buzz" if num % 5 == 0 else num for num in range(a, b)]
print(fizzBuzzlist(1, 10))

twoNumber = lambda l : list(filter(lambda l : True if l != None else None,list(map(lambda i : None if l.index(i) == len(l)-1 else i + l[l.index(i) + 1], l))))
print(twoNumber([1,2,3,4,5,6,7])) 

