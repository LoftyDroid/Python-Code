'''
Write a program to fill in a letter template given
below with name and date

letter = Dear</Name>
         you are selected!
         </DATE>

'''
letter = '''Dear <|Name|>
Greeting from abc coding house. I am happy to tell you about your selection,
You are selected!
Date: <|Date|>
'''
name = input("Enter your name:\n")
date = input("Enter date:\n")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)
print(letter)