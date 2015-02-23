#!/usr/bin/python

import random
import webapp

class aleat(webapp.webApp):
    def parse(self, request):
        return None

    def process(self, parsedRequest):
        random_number = str(random.randrange(9999999))
        return("HTTP/1.1 200 OK\r\n\r\n",
               "<html><body><h1><center>Tu URL aleatoria:</h1>" +
               "<center><b><a href='" + random_number + "'>Dame otra</a>" +
               "</body></html>" +
               "\r\n")

if __name__ == "__main__":
    servidor = aleat("localhost", 1234)
