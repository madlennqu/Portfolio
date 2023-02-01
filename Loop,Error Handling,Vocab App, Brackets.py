#Vocab builder
def vocab_builder():
    vocabs = {'programming': ['the act of writing computer program', 'p_________g'],
              'python': ['a kind of very large snake', 'p____n'],
              'fun': ['pleasure', 'f_n']}

    while True:
        print("This is vocab builder app")
        print("1. Test")
        print("2. Add a word")
        print("3. Remove a word")
        print("4. List all the words")
        print("5. exit")
        command = input("input the number")
        if command == "5":
            break
        elif command == "4":
            for key in vocabs.keys():
                print("{} ({})\n    - {}\n".format(key, vocabs[key][1], vocabs[key][0]))
            print()
        elif command == "2":
            new_word = input("Enter a new word")
            new_word_definition = input("Enter the definition of the new word")
            new_word_hint = input("Enter the hint of the new word")
            vocabs[new_word] = [new_word_definition, new_word_hint]
        elif command == "3":
            word = input("enter the word that you want to remove")
            try:
                del (vocabs[word])
            except KeyError:
                print("{} is not in the vocabs word list".format(word))
        elif command == "1":
            run_test(vocabs)


def run_test(vocabs):
    correct_count = 0

    for key in vocabs.keys():
        while True:
            answer = input("What's {}? [h]int, [p]ass".format(vocabs[key][0]))
            if answer == key:
                # correct_count = correct_count + 1
                correct_count += 1
                break
            elif answer == 'h':
                print("Here's the hint: {}".format(vocabs[key][1]))
            elif answer == 'p':
                break

    print()
    print("You have got {} vocabs correct".format(correct_count))
    print()


#Copy list, dictionary
# list

numbers = [1,2,3,4,5,6]

num_copy = numbers

numbers.append(7)

num_copy

num_real_copy = numbers.copy()

numbers.append(7)

num_copy

num_real_copy

#Supplementary Material - Name of Brackets {} [] ()
() - Bracket

[] - Square Bracket

{} - Curly Bracket

# An example of while loop.
# - Print the first 3 odd number of a list
# - We can use for loop to do the same thing

numbers = [1, 2, 4, 5, 6, 7, 8, 9, 10]

count_odd = 0

while count_odd < 3: # the following lines will be executed if the condition is True
    num = numbers.pop(0)  # pop get the first item from the list and remove it from the list
    if num % 2 == 1:
        print(num)
        count_odd += 1

    # after all line of codes under the while block is executed, the while condition will be
    #  evaluated again.



# An example of using while True loop to do control

while True:  # as the condition is always True, the loop will run forever.
    user_input = input("Enter user input")

    if user_input == "exit":
        break # except hitting a break that will exit the loop

    print("Do something")


Looping sample code (in class 2 Oct)
# simpliest form of looping 
fruits = ["apple", "melon", "orange", "banana"]
for fruit in fruits:
    print("I like {}".format(fruit))
    print("It's great")

# Looping with condition to apply different logic     
fruits_dislike = ["apple", "banana"]

for fruit in fruits:
    if fruit in fruits_dislike:
        print("I don't like {}".format(fruit))
    else:
        print("I like {}".format(fruit))
        print("It's great")
        
# high level skeleton of using looping and condition for analysis

stocks = ["AAPL", "MSFT", "TSLA", "GOOGL", "FB"]
stocks_adr = ["BABA"]
for stock in stocks:
    if stock not in stocks_adr:
        print("analysis result of {}".format(stock))
    else:
        print("ADR analysis result of {}".format(stock))
        

# looping with list of numbers        
   
numbers = [1,2,3,4,5,6,7,8,9,10]
for n in numbers:
    if n % 2 == 0:
        print("{} is even")
    else:
        print("{} is odd")
# side material - using range()
for n in range(1,11):
    if n % 2 == 0:
        print("{} is even".format(n))

# aggregating a list
# sum all even number of the list
numbers = [7, 9, 8, 67, 890, 76, 44, 67, 89, 90, 65, 43, 145, 5658, 890]
result = 0
for n in numbers:
    if n % 2 == 0:
        result = result + n
        print("n is {}. the result is {}".format(n, result))
        
# shorthand of result += n
result = 0
for n in numbers:
    if n % 2 == 0:
        result += n  # exactly the same as result = result + n
        print("n is {}. the result is {}".format(n, result))
        
# get the sum of first 5 even number in the list
result = 0
count = 0
for n in numbers:
    if n % 2 == 0:
        result += n  # exactly the same as result = result + n
        count += 1
        print("n is {}. the result is {}. count is {}".format(n, result, count))
        
# using break
result = 0
count = 0
for n in numbers:
    if n % 2 == 0:
        result += n  # exactly the same as result = result + n
        count += 1
        print("n is {}. the result is {}. count is {}".format(n, result, count))
    if count >= 5:
        break

# Error crash the app

def err_example():
    colors = ["red", "blue"]
    print(colors[0])
    print(colors[2]) # will get an error
    print(colors[1])
    
# Preventive

def err_example():
    colors = ["red", "blue"]
    print_item(colors,0)
    print_item(colors,2)
    print_item(colors,1)
    
def print_item(a_list, index):
    if len(a_list) > index:
        print(a_list[index])
    else:
        print("There is no such item")
        
# Reactive

def err_example():
    colors = ["red", "blue"]
    print_item(colors,0)
    print_item(colors,2)
    print_item(colors, 1)
    print_item(colors, "o")
   
def print_item(a_list, index):
    try:
        print(a_list[index])
    except IndexError:
        pass
    except TypeError:
        print("Index has to be integer")
    except:
        print("Something is wrong")
err_example()


#Vocab builder code 30 Oct
def vocab_app():
    vocabs = {'programming': ['the activity or job of writing computer programs', '_______ming'],
              'python': [
                  'a very large snake that kills animals for food by wrapping itself around them and crushing them',
                  '___hon'],
              'fun': ['pleasure, enjoyment, or entertainment', '__n']}

    while True:
        user_input = menu()
    
        if user_input == "1":
            vocab_test(vocabs)
        elif user_input == "2":
            add_vocab(vocabs)
        elif user_input == "3":
            remove_vocab(vocabs)
        elif user_input == "4":
            list_vocab(vocabs)
        elif user_input == "5":
            break
        
def menu():
    print("+++++++++++++++++++++")
    print("Welcome to vocab builder app")
    print("1. Test")
    print("2. Add a word")
    print("3. Remove a word")
    print("4. List all words")
    print("5. exit")
    user_input = input()
    return user_input

def list_vocab(vocabs):
    for vocab in vocabs:
        print("{}\n    - {}".format(vocab,vocabs[vocab][0]))
        
def remove_vocab(vocabs):
    word_to_remove = input("which word you want to remove?")
    try:
        del(vocabs[word_to_remove])
    except KeyError:
        pass
    
def add_vocab(vocabs):
    word = input("whats the word you want to add")
    
    if word in vocabs:
        print("It is already in vocabs")
    else:
        definition = input("whats the definition of {}".format(word))
        hint = input("whats the hint {}".format(word))
        vocabs[word] = [definition, hint]
    

def vocab_test(vocabs):
    score = 0
    incorrect_words = []
    
    for word in vocabs:
        while True:
            print()
            user_input = input("What is {}?\nor press [p]ass, [h]int, [q]uit".format(vocabs[word][0]))
            if user_input == "p":
                incorrect_words.append(word)
                break
            elif user_input == "h":
                print("Hint: {}".format(vocabs[word][1]))
            elif user_input == "q":
                incorrect_words.append(word)
                print_test_summary(vocabs, score, incorrect_words)
                return
            elif user_input == word:
                print("You are right")
                score += 1
                break
            else:
                print("You are wrong")
    
    print_test_summary(vocabs, score, incorrect_words)
            
def print_test_summary(vocabs, score, incorrect_words):
    print("================")
    print("Score: {}/{}".format(score, len(vocabs)))
    print()

    if len(incorrect_words) > 0:
        print("List of incorrect word")
        for incorrect_word in incorrect_words:
            print("{} - {}".format(incorrect_word, vocabs[incorrect
