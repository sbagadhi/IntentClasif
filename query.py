#!/usr/bin/env python
# coding: utf-8





from rasa.nlu.model import Interpreter





interpreter=Interpreter.load('/users/sbagadhi/desktop/GIT/models/nlu/new')





def ask_question(text):
    print(interpreter.parse(text))


while True:
    query=input()
    answer=ask_question(query)
    print({"text":query,"intent":answer})
    if query=="quit":
        break




