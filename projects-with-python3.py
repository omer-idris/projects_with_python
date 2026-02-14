import random, time, os, string
from shapes import bank_note, HANGMANPICS, game_symbols, black_jack_logo

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')
clear()

# These are ten projects I've made with python throughout my learning journey.

  # project 1. Automation
  # project 2. Paper, Rock, Scissor Game
  # project 3.  Caesar Cipher
  # project 4. Password Generator
  # project 5. Hang Man Game
  # project 6. Library Catalog
  # project 7. Currency Converter
  # project 8. 
  # project 9. 
  # project 10. Black-Jack Game


# 1 ---------------------  (Automation)
# This is a simplified model of an automation program that allows you to send invitations to as many people as you want with one click.

TEMPLATE_FILE = "D:\Advanced Py\chapter 1\lesson 01\message.txt'"
RECIPIENTS_FILES = "D:\Advanced Py\chapter 1\lesson 01/names.txt"

def read_template():
    with open(TEMPLATE_FILE, 'r') as file:
        return file.read()

def read_names():
    with open(RECIPIENTS_FILES, 'r') as file:
        return [i.strip() for i in file.readlines()]

guests = read_names()
template = read_template()

def generate_invitations():
    for guest in guests:
        new_letter = template.replace('name', guest)
        output_file = f"D:\Advanced Py/chapter 1/lesson 02/letter_for_{guest.lower()}.txt"
        with open(output_file, 'w') as file:
            file.write(new_letter)

generate_invitations()

# 2 ------------------- (Paper, Rock, Scissor Game)
print('\nPaper, Rock, Scissor\n')

while True:
  clear()
  print(game_symbols)
  options = ['Paper', 'Rock', 'Scissor']
  print('Welcome to scissor rock paper game....')
  if input('Type "yes" to see the rules or press enter to skip: ').lower() == 'yes':
    print("""    ******* Rules *******
                 You choose and the computer choose and then...we check
                 1. Paper covers the rock.
                 2. Rock smashes the scissor.
                 3. Scissor cuts the paper. """)
  user_choice = input('Enter you choice (Paper, Rock, Scissor): ').title()
  computer_choice = random.choice(options)

  if user_choice in options:
    if computer_choice == user_choice:
      print(f'Neutral! The computer also chose {computer_choice}')
    elif (computer_choice == 'Rock' and user_choice == 'Paper' or
      computer_choice == 'Scissor' and user_choice == 'Rock' or
      computer_choice == 'Paper' and user_choice == 'Scissor'  ):
       print(f'You Win! {user_choice} beats {computer_choice}.')
    else:
      print(f'You loose! {computer_choice} beats {user_choice}')
  else:
    print('Invalid input. Try again')
  if input('Press any key to play again or type "break" to exit... ').lower() == 'break':
     break
    
# 3 ------------------- (Cryptography)
print('\nWelcome to the Caesar Cipher.....\n')
alphabet = string.ascii_lowercase

def caesar_cipher(to_encrypt, shift_key):
  message = ''
  
  for i in to_encrypt:
    if i.lower() in alphabet:
      postion_letter = alphabet.index(i.lower())
      new_postion = (postion_letter + shift_key) % 26
      
      if i.isupper():
        message += alphabet[new_postion].upper()
      else:
        message += alphabet[new_postion]
    else:
      message += i
  return message
while True:
    clear()
    choice = input('Choose an operation to start:\n1. Encryption\n2. Decryption\nChoice 1-2: ')
    if choice == '1':
        print('\nEncryption....')
        to_encrypt = input('Enter a word for encryption: ')
        shift_key = int(input('Enter the shift key: '))

        # التشفير
        print(f'ENCRYPTED MESSAGE: "{caesar_cipher(to_encrypt, shift_key)}"')
    elif choice == '2':
        print('\nDecryption....')
        to_decrypt = input('\nEnter a word for decryption: ')
        shift_key = int(input('Enter the shift key: '))

        #    فك التشفير بنفس الدالة ، ضرب المفتاح في سالب واحد لعكس الاتجاه 
        print(f'DECRYPTED MESSAGE: "{caesar_cipher(to_decrypt, shift_key * -1)}"')
    else:
       print('Wrong input! Try again.')
    if input('Do you want to decrypt or encrypt another message? y/n ').lower() != 'y':
      break


# 4 ----------------- (Password Generator)
print('Password Generator')
while True:
  clear()
  print('Welcome to the Strong Passwords Generator!\n')
  while True:
    length = int(input('Enter the length of the password you want: '))
    if length >= 8:
      clear()
      break
    else:
      print('Password length must be 8 or more. Try again.\n')
  letters_length = int(input('Enter the number of letters in the password: '))
  numbers_length = int(input('Enter the number of numbers in the password: '))
  symbols_length = int(input('Enter the number of symbols in the password: '))
  if letters_length + numbers_length + symbols_length != length:
    print('Invalid Error')
  else:
    password = []
    for i in random.choices(string.ascii_letters, k=letters_length):
      password.append(i)
    for i in random.choices(string.digits, k=numbers_length):
      password.append(i)
    for i in random.choices(string.punctuation, k=symbols_length):
      password.append(i)
    random.shuffle(password)
    print(f"\nGenerated password: {''.join(password)}")
  if input('Do you want to generate another password? y/n ').lower() != 'y':
     break


# 5 ------------- (Hangman Game)
print('Hangman project')
while True:
    words = ['home', 'egg', 'house', 'love', 'country']
    word = random.choice(words)
    display = ["_" for i in range(len(word))]
    display2 = ['_'] * len(word)

    tries = 6
    twice = []
    clear()
    print(HANGMANPICS[0])
    print(f"\n{' '.join(display)}\n")
    while '_' in display and tries > 0:
        enter_letter = input('Enter a letter: ')
        for position in range(len(word)):
            if word[position] == enter_letter:
                display[position] = enter_letter
        if enter_letter not in word:
            if enter_letter not in twice:
                twice += enter_letter
                tries -= 1
                print(HANGMANPICS[6-tries])
            else:
                print('Try again... you guessed this letter earlier.')
        print(f'You have {tries} tries remained...')
        print(f"\n{' '.join(display)}\n")
    if ''.join(display) == word:
        print('\n******* You Win! ********\n')
    else:
        print('\n------ You loose ------\n')
    if input('Do you want to play again? y/n ').lower() != 'y':
        break
# 6 ------------------------ (Library Catalog)
print('Library Catalog....')
time.sleep(4)
library = {}

def add():
  while True:
    clear()
    print('Adding a book.... \n')
    isbn = input("Enter the ISBN: ")
    title = input('Enter the title: ')
    author = input('Enter the author: ')
    library[isbn] = {
      'ISBN': isbn,
      'Title': title,
      'Author': author, }
    library[isbn]['available'] = True
    print(f'Book "{title}" by {author} add to library with ISBN {isbn}.')
    if input('Add another? y/n ').lower() != 'y':
      break

def checkout():
  while True:
    clear()
    print('Checking out a book.... \n')
    isbn = input("Enter the ISBN to check out: ")
    if isbn in library and library[isbn]['available'] == True:
      print(f'Book {library[isbn]["Title"]} checked out successfully....')
      library[isbn]['available'] = False
    elif isbn in library and library[isbn]['available'] == False:
      print('Sorry! this book has checked before you...')
    else:
      print('Book not found in the catalog.')
    if input('Check out another? y/n ').lower() != 'y':
      break

def checkin():
  while True:
    clear()
    print('Checking in a book.... \n')
    isbn = input('Enter ISBN to check in: ')
    if isbn in library and library[isbn]['available'] == True:
      print("Sorry this book is already in.")
    elif isbn in library and library[isbn]['available'] == False:
      print(f'Thanks! book {library[isbn]["Title"]} has checked in successfuly')
      library[isbn]['available'] = True
    else:
      print('Book not found in the catalog.')
    if input('Check in another? y/n ').lower() != 'y':
      break

while True:
  clear()
  entered = input('''
  Please enter from 1-5:
  1- add a book
  2- check out a book
  3- check in a book
  4- see catalog
  5- Exit \n ''')
  if entered == '1':
    add()

  elif entered == '2':
    checkout()

  elif entered == '3':
    checkin()

  elif entered == '4':
    clear()
    print('Library Catalog: \n')
    for i in library:
      print(f"ISBN: {i}  Title: {library[i]['Title']}  Author: {library[i]['Author']}  Available: {library[i]['available']}")
    print('-'*18)
    input('\npress enter to see the menu....')

  elif entered == '5':
    break

 # 7 ----------------- (Currency Converter)
print('Currency Converter')
currencies = {'USD': 1.0, 'EUR': 0.85, 'SDP': 598.35, 'SAR': 3.7,
             'GBP': 0.74, 'SHP': 0.32, 'RUB': 80.1, 'EGP': 47.66}

clear()
print('Welcome to currency converter....')
def currency_rates():
  print(bank_note)
  print('\n  ==== Our currencies and rates for today ===\n')
  for currency in sorted(currencies):
    print(f"    {currency}: {currencies[currency]}")
  print('_'*29)

while True:
  currency_rates()
  owned_currency = input('\nChoose a currency to convert from: ').upper()
  if owned_currency not in currencies:
    print('Oops! Currency not recognized to system. Try again.')
    time.sleep(3)
    continue
  amount = float(input('Enter the amount: '))

    # confirm the amount and currency
  while True:
    confirm = input(f'You entered {amount} {owned_currency} Confirm? y/n: ').lower()
    if confirm == 'y':
      break
    else:
      amount = float(input('Enter the amount: '))

    # take wanted currency
  clear()
  currency_rates()
  wanted_currency = input('\nChoose a currency to convert to: ').upper()
  if wanted_currency in currencies:
    clear()
    print('Analyzing your request... Please wait.')
    time.sleep(3)
    print(f"Checking for {wanted_currency}'s best rates available..... Please wait.")
    time.sleep(3)
    print(f"Getting a discount price for {owned_currency}.... Please wait.")
    time.sleep(3)
    print(f'Preparing the deal from {owned_currency} to {wanted_currency}....')
    time.sleep(3)
      
      # سعر التغيير يساوي سعر المحول اليه على سعر المحول منه (كليهما اما الدولار) ثم يُضرب في كمية المبلغ المراد تحويله
    print(f"\nExchange Rate:  1 {owned_currency} = {(currencies[wanted_currency]) / currencies[owned_currency]} {wanted_currency}")
    print(f"\n{amount:.2f} {owned_currency} equals {(amount/currencies[owned_currency]) * currencies[wanted_currency]: .2f} {wanted_currency}")
      
      # accept the deal
    print('\nSuccessful exchange... \n') if input('Do you accept this transaction? y/n: ').lower() == 'y' else print('Transaction Canceled.')
  else:
    print('Oops! Currency not recognized to system.')
    
     # another deal or exit
  if input('Do you want to perform another conversion? y/n: ').lower() != 'y':
    print('thank you for using Money Exchanger.')
    break

# 8 ------------------------ ()
# 9 ------------------------ ()
# 10 ----------------------- ()
print('Black Jack Game ')

def random_cardfunc1(number):
    for i in range(number):
        random_card1 = random.choice(mother_cards)
        if random_card1 == 'As':
            if sum(user_cards) <= 10:
                random_card1 = 11
            else:
                random_card1 = 1
        user_cards.append(random_card1)

def random_cardfunc2(number):
    for i in range(number):
        random_card2 = random.choice(mother_cards)
        if random_card2 == 'As':
            if sum(computer_cards) <= 10:
                random_card2 = 11
            else:
                random_card2 = 1
        computer_cards.append(random_card2)

while True:
    card = True
    on_game = True
    mother_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 'As']
    computer_cards = []
    user_cards = []
    while on_game:
        print('\nStarting the game...')
        time.sleep(2)
        print(black_jack_logo)
        random_cardfunc1(2)
        print(f'Your cards are {user_cards}, current score is {sum(user_cards)}')
        random_cardfunc2(2)
        print(f"Computer's first card is {computer_cards[0]}")

        while card == True and sum(user_cards) < 21:
                if input('Do you another card? yes or no ').lower() == 'yes':
                    random_cardfunc1(1)
                    print(f'Your cards are {user_cards}, current score is {sum(user_cards)}')

                else:
                    card = False

        if sum(user_cards) > 21:
            print(f'You loose! BUST!! score {sum(user_cards)}')
            on_game = False
        if sum(user_cards) == 21:
            print(f'You Win! Congra🌹🌹 score {sum(user_cards)}')
            on_game = False  

        while sum(computer_cards) < 17:
                random_cardfunc2(1)

        if sum(computer_cards) > 21:
            print(f"Computer looses! BUST!! score {sum(computer_cards)}")
            on_game = False

        if sum(computer_cards) == sum(user_cards):
            print(f'compter score {sum(computer_cards)} and yours {sum(user_cards)}')
            print('Draw 😐😐')
            on_game = False

        if sum(computer_cards) < sum(user_cards):
            print(f"You win, yours {sum(user_cards)} and computer's {sum(computer_cards)}")
            on_game = False
        if sum(computer_cards) > sum(user_cards):
            print(f"You loose, yours {sum(user_cards)} and computer's {sum(computer_cards)}")
            on_game = False
    if input('Do you want to play again? y/n ').lower() != 'y':
        break
