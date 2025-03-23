import sqlite3

database = sqlite3.connect("words.db")
database_cursor = database.cursor()
database_cursor.execute("""CREATE TABLE Words (
                              WordID INTEGER PRIMARY KEY AUTOINCREMENT,
                              GermanWord TEXT NOT NULL UNIQUE,
                              EnglishTranslation TEXT NOT NULL,
                              WordTense TEXT NOT NULL,
                              Grammar TEXT NOT NULL,  
                              TimesCorrectlyGuessed INTEGER NOT NULL,
                              Notes TEXT
                              )
                              """)

database.commit()
database.close()
