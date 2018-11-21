from webdl import *

ourl = "https://pl.wikipedia.org/wiki/Alexander_Zverev"

alexander = Webpage(ourl)

alexander.count_uppercase()
alexander.count_numbers()
alexander.count_sentences()
alexander.count_telephone_numbers()
alexander.count_emails()