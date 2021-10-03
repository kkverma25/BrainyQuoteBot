import requests
from bs4 import BeautifulSoup
from pyrogram.types import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


async def quote_of_the_day():
    URL = "https://www.brainyquote.com/quote_of_the_day"
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'lxml')
    result_divs = soup.find_all("div", attrs={"class": "qotd-q-cntr"})
    quotes = {}
    for result_div in result_divs:
        id = result_div.h2.text
        soup = BeautifulSoup(str(result_div), 'lxml')
        contents = soup.find_all("a")
        quote = contents[0].text.replace("\n", "")
        author = contents[1].text
        quotes[id] = [quote, author]
    articles = []
    for item in quotes.items():
        title = item[0]
        author = item[1][1]
        quote = item[1][0]
        result = InlineQueryResultArticle(
            title=title,
            input_message_content=InputTextMessageContent(f"**ıllıllı★ {title} ★ıllıllı**\n\n{quote} \n\n~ {author}"),
            url="https://t.me/ABOUT_DEVIL_DAD/4",
            description=quote,
            thumb_url="https://telegra.ph/file/f6dd497221ff913d3b3d2.png",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("✨ Search More Quotes ✨", switch_inline_query_current_chat="")],
                    [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/ABOUT_DEVIL_DAD/4")]
                ]
            ),
        )
        articles.append(result)
    return articles
