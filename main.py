#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getRandomFortune():

    fortunes = [
"You will find a bushel of money",
"Your smile will tell you what makes you feel good.",
"The best year-round temperature is a warm heart and a cool head",]

    index = random.randint(0,2)

    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):

        header = "<h1>Fortune Cookie</h1>"

        fortune = "<strong>" + getRandomFortune() + "</strong>"
        fortuneSentence = "Your fortune: " + fortune
        fortuneParagraph = "<p>" + fortuneSentence + "</p>"

        luckyNumber = "<strong>" + str(random.randint(1,100)) + "</strong>"
        numberSentence = "Your lucky number: " + str(luckyNumber)
        numberParagraph = "<p>" + numberSentence + "</p>"

        cookieAgainButton = "<a href='.'><button>Another Cookie Please</button></a>"

        content = header + fortuneParagraph + numberParagraph + cookieAgainButton
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
