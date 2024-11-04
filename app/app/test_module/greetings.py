"""This module define the greetings according to age of people."""
def define_greeting(age, name):
    if age > 18:
        return f'Namaste {name}'
    else:
        return f'Oi {name} ! k garya xas ?'
