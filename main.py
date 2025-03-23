#mein deutsch lehrer
import sqlite3
import os #Used to wipe console text to help with program readability
import time

class Helper():
    def clear_console(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


class Main(Helper):    
    def __init__(self):
        #Inherits from the parent class Helper
        super().__init__()
        self.choice = ""

    def greet(self):
        print("Hallo.")

    def menu_choices(self):
        time.sleep(1)
        self.clear_console()

        while True:
            self.choice = input("Was möchten Sie tun? (What would you like to do?) \n1. See saved words\n2. Add a word\n3. Guess German to English translations\n4. Check grammar rules\n5. Quit the program\nEnter your choice: ") # What would you like to do?
            if self.choice not in ("1", "2", "3", "4", "5"):
                print("falsche Wahl (Wrong choice)") #Wrong choice
                continue
            else: 
                break

        
        #Matches it to a function
        program.choice_matcher()

class Choices(Main):
    #Inherits from the parent class Main
    def __init__(self):
        super().__init__()


    #See all saved words
    def see_all_saved_words(self) -> None:
            #Gets all data from the database and puts it in a variable called "data" for later use.
            database = sqlite3.connect("words.db")
            database_cursor = database.cursor()
            data = database_cursor.execute("SELECT * FROM Words").fetchall()

            display_string = ""
            longest_line_length = 0

            #Adds on an entry string for row in the database
            for entry in data:
                entry_string = f"Word ID - {entry[0]} | Word in German - {entry[1]} | English translation/word - {entry[2]} | Times correctly guessed - {entry[3]}\n"

                #Gets the longest entry_string for surrounding border
                if len(entry_string) > longest_line_length:
                    longest_line_length = len(entry_string)

                display_string += entry_string

            #Displays the final string for the user
            number_of_hyphens = "-" * longest_line_length

            print(number_of_hyphens + "\n" + display_string + number_of_hyphens)

            input("Click enter to continue.")

            print(number_of_hyphens)

            database.close()


    #Add a word to the database
    def add_a_word(self) -> None:
        while True:
            german_word = input("Enter a GERMAN word: ")
            if german_word != "":
                break
            else: 
                print("Try again")

        while True:
            english_word = input("Enter the English translation for that word: ")
            if english_word != "":
                break
            else: 
                print("Try again")

        database = sqlite3.connect("words.db")
        database_cursor = database.cursor()

        database_cursor.execute("INSERT INTO Words (GermanWord, EnglishTranslation, TimesCorrectlyGuessed) VALUES (?, ?, ?)", (german_word, english_word, 0))

        database.commit()
        database.close()


    #Guess words to help learn German
    def guess_words(self) -> None:
        for i in range(8):
            print("-----------------------------------------------")
            database = sqlite3.connect("words.db")
            database_cursor = database.cursor()

            random_german_word_array = database_cursor.execute("SELECT rowid, * FROM Words ORDER BY RANDOM() LIMIT 1").fetchall()[0]

            # print(random_german_word_array) # debug

            random_german_word_id = random_german_word_array[1]
            random_german_word = random_german_word_array[2]
            random_english_translation = random_german_word_array[3]
            random_german_word_times_correctly_guessed = random_german_word_array[4]
            # print(random_german_word_array) # debug

            # print(random_german_word_id, random_german_word, random_english_translation, random_german_word_times_correctly_guessed) # debug


            print("Your word is... " + random_german_word)
            entry = input("What is the english translation? - ")
            if entry != random_english_translation:
                print(f"❌ Wrong! The translation was '{random_english_translation}'.")
            else:
                random_german_word_times_correctly_guessed += 1
                print(f"✅ You got it correct! You have solved this word correctly {random_german_word_times_correctly_guessed} times!")


            database.execute("UPDATE Words SET TimesCorrectlyGuessed = (?) WHERE GermanWord = (?)", (random_german_word_times_correctly_guessed, random_german_word))


            database.commit()
            database.close()



    def check_grammar_rules(self):
        print("-----------------------------------------------")
        print("Present tense")
        print("-----------------------------------------------")
        print("ich Habe - I have")
        print("du hast - you have")
        print("er/sie/es Hat - he/she/it has")
        print("sie Haben - they have")
        print("wir haben - we have")
        print("-----------------------------------------------")
        input("Click enter to continue.")
        print("-----------------------------------------------")
        time.sleep(0.2)

    #Matches the choices with a function
    def choice_matcher(self):

        self.clear_console()

        if self.choice == "1":
            self.see_all_saved_words()

        elif self.choice == "2":
            self.add_a_word()

        elif self.choice == "3":
            self.guess_words()
        
        elif self.choice == "4":
            self.check_grammar_rules()

        elif self.choice == "5":
#             print("""
#      _____ 
#     /     | | | | | 
#    /  /_\ | | |_| |
#   /  /  | |  \___/
                  
# """)
            print("tschüss 👋")
            time.sleep(1.2)
            self.clear_console()
            quit()

        program.menu_choices()



program = Choices()
program.greet()
#Asks for user's choice
program.menu_choices()
