author = 'Hemingway'

#indexing
print(author[0])
print(author[1])
print(author[2])
#negative indexing
print(author[-1])
print(author[-2])
print(author[-3])
#slicing string
#selecting a range of indexes
print(author[2:5])
print(author[2:-4])
#concatenation
print(author[0:2]) + (author[5:])
x = 'John'
greeting = input('Hello'+x+'how are you?')
#formating
#.lower
#.upper
#.capatilize
#especially valuable in inputs
#FORMATING
author2 = 'Jane Austen'
year_born = '1775'

print('{} was born in {}'.format(author2,year_born))

#works well for user input
n1=input('ENter a noun:')
v = input ('Enter a verb')
adj = input('Enter an adjective')
n2 = input('please enter another noun')

print ('The {}'' {} ''the {}''{}'.format(n1,v,adj,n2))

#splitting strings
grocery = input('Enter items to place in grocery bag, separated by commas')
print(grocery)
grocery2 = grocery.split(',') #split will seprarate items into a list
#parammeter - what character to look for split items

print(grocery2)
#join items in to make sting
words = ['cow','jumped','over','the','moon']
sentence = ' '.join(words)
print(sentence)

#replace characters in a string
sentence2 = 'Hello my name is Mr.Petrella'.replace('e','3')
print(sentence2)

#finding index
#return the positional index
# of the FIRST occurence of the character (Note: works with lists)
name = 'Joshua'
print(name.index('s'))
#newline
print('Roses are red,\n violets are blue,\n I like coding,\n how about you?')
#in method
x = 'cat'in'cat in the hat'
y='bat'in'cat in the hat'
print(x,y)
