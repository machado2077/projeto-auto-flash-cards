import os
import re

from selenium.webdriver import Firefox, Chrome, Opera
#from selenium.webdriver.opera.options import Options
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.firefox.options import Options

from src.clss.assistants import AnkiEditPageHandler
from src.clss.autoFlashCards import AutoFlashCards
from src.clss.cardDeliverers import SeleniumAnkiBot
from src.clss.sourceAdmins import (
                MyCardShelveAdmin, TextSourceAdmin, 
                DictBasedCardWriter
    )

phrases_file = 'frases.txt'
file_path = os.path.join(os.getcwd(), phrases_file)

user_data_file = 'data.json'
user_data = os.path.join(os.getcwd(), user_data_file)

writer = DictBasedCardWriter()
sourceAdmin = TextSourceAdmin(file_path, writer)
dbAdmin = MyCardShelveAdmin('db', 'cards')



driver = Chrome
#driver = Firefox
#driver = Opera
#wdm = GeckoDriverManager()
#wdm = OperaDriverManager()
options = Options()
options.headless = False
web_driver_args = {
    'options': options
}
web_edit_page_handler = AnkiEditPageHandler(re)
selenium_anki_bot_args = {
    'web_driver': driver, 
    'user_data': user_data,
    'web_edit_page_handler': web_edit_page_handler,
}
deliver = SeleniumAnkiBot(**selenium_anki_bot_args, **web_driver_args)

automaton = AutoFlashCards(deliver, sourceAdmin, dbAdmin)

if __name__ == "__main__":
    automaton.run_task()
    if len(automaton.card_list) == 0:
        print('No cards to create.')
