import bs4
import re
import urllib.request


def get_url():
    print("URL: ")
    return input()


def results(data):
    if data is None:
        print("Nothing found.")
    else:
        print("Found {} occurences.".format(len(data)))


class Webpage:

    def __init__(self, url):
        self.url = url
        print("Webpage with URL: '{}' created!".format(self.url))
        self.data = self.get_data()

    def get_data(self):
        webpage = str(urllib.request.urlopen(self.url).read())
        soup = bs4.BeautifulSoup(webpage, features="html.parser")

        return soup.get_text()

    def count_uppercase(self):
        print("Looking for uppercase letters in '{}'".format(self.url))
        data = re.findall("[A-Z]", self.data)
        results(data)

    def count_sentences(self):
        print("Looking for complete sentences in '{}'".format(self.url))
        data = re.findall("\s+[^.!?]*[.!?]", self.data)
        results(data)

    def count_numbers(self):
        print("Looking for numbers in '{}'".format(self.url))
        data = re.findall("[0-9]", self.data)
        results(data)

    def count_starting_with_a(self):
        print("Looking for words starting with A or a in '{}'".format(self.url))
        data = re.findall("[A,a]", self.data)
        results(data)

    def count_telephone_numbers(self):
        print("Looking for telephone numbers in '{}'".format(self.url))
        data = re.findall("[0-9]{3}-[0-9]{3}-[0-9]{3}", self.data)
        results(data)
        print("Printing telephone numbers from '{}' to a file".format(self.url))
        with open("telefony.txt", "w") as text_file:
            for number in data:
                print(number, file=text_file)

    def count_emails(self):
        print("Looking for email addresses in '{}'".format(self.url))
        data = re.findall(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", self.data)
        results(data)
        print("Printing emails from '{}' to a file".format(self.url))
        with open("adresyEmail.txt", "w") as text_file:
            for address in data:
                print(address, file=text_file)

    def count_unique_words(self):
        print("Looking for unique words '{}'".format(self.url))