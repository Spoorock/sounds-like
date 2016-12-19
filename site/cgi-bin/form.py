#!/usr/bin/env python3


#last stuff
import pylast
from itertools import islice
last = pylast.LastFMNetwork(api_key="71deec92ca9ee71cf7b535f168d094cc", api_secret="d89ec00f808e558cf4bbdfaf46aa22b6")


import cgi
import html
form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "не задано")
text2 = form.getfirst("TEXT_2", "не задано")
text1 = html.escape(text1)
text2 = html.escape(text2)


track = last.get_track(text1, text2)
error = 0



print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Похожие композиции</title>
        </head>
        <body>""")

print("<h1>Похожие композиции</h1>")
try : 
	for sim in islice(track.get_similar(), 5):
		print("<p>{}</p>".format(sim.item))
except Exception:
	error = 1
if error == 1:
	print("<p>Ничего не найдено</p>")
#print("<p>TEXT_1: {}</p>".format(text1))
#print("<p>TEXT_2: {}</p>".format(text2))
print("<form action='../index.html'>")
print("<p><input type='submit' value='Новый поиск'></p>")
print("</form>") 
print("""</body>
        </html>""")
