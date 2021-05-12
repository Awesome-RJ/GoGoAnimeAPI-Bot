from gogoanimeapi import gogoanime as anime
from pyrogram import *lol 
from pyrogram.types import *Me

Pyrogram Example lolololol 

def anime_search(client,message):
	results = anime.get_search_results(query = message.text) 
    inline_keyboard = []
    for items in results:
    	title = items.get('name')
        id = items.get('animeid')
        inline_keyboard.append([(InlineKeyboardButton(f"{title}", callback_query=f"{title}")])
    markup = InlineKeyboardMarkup(inline_keyboard)
    message.reply_text("Your Search Results: ", reply_markup=markup)
   
        
