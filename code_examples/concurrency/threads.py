import timeit
from urllib.request import Request, urlopen
import json
import threading
import os
import glob
from cleantext import clean


def write_genre():
    """
    Uses genrenator from binaryjazz.us to write a random genre to the
    name of the given file
    """

    req = Request(
        "https://binaryjazz.us/wp-json/genrenator/v1/genre/",
        headers={"User-Agent": "Mozilla/5.0"},
    )
    genre = json.load(urlopen(req))
    clean_genre = clean(
        genre.replace(" ", "_").replace("/", "-"),
        fix_unicode=True,  # fix various unicode errors
        to_ascii=True,  # transliterate to closest ASCII representation
        lower=True,  # lowercase text
        no_line_breaks=False,  # fully strip line breaks as opposed to only normalizing them
        no_urls=False,  # replace all URLs with a special token
        no_emails=False,  # replace all email addresses with a special token
        no_phone_numbers=False,  # replace all phone numbers with a special token
        no_numbers=False,  # replace all numbers with a special token
        no_digits=False,  # replace all digits with a special token
        no_currency_symbols=False,  # replace all currency symbols with a special token
        no_punct=False,  # remove punctuations
        replace_with_punct="",  # instead of removing punctuations you may replace them
        replace_with_url="<URL>",
        replace_with_email="<EMAIL>",
        replace_with_phone_number="<PHONE>",
        replace_with_number="<NUMBER>",
        replace_with_digit="0",
        replace_with_currency_symbol="<CUR>",
        lang="en",  # set to 'de' for German special handling
    )
    file_name = f"./sync/new_file_{clean_genre}.txt"
    with open(file_name, "w") as new_file:
        print(f'Writing "{genre}" to "{file_name}"...')
        new_file.write(genre)


def threaded_write_genre():
    threads = []
    n = 10

    for i in range(n):
        thread = threading.Thread(target=write_genre)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


print("Starting...")

R = 100

t = timeit.Timer(threaded_write_genre)
duration = t.repeat(repeat=R, number=1)

print(
    f"Time to complete threading read/writes (10 times repeated x{R} ): {round(min(duration), 2)} seconds"
)

files = glob.glob("./sync/*.txt")
for f in files:
    os.remove(f)
