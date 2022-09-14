# Write a decorator that takes a list of 'stop words' and replaces them with '*' inside the decorated function

def stop_words(words: list):

    pass

@stop_words(['pepsi', 'BMW'])

def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

################################################################################################################################

def stop_words(words: list):
    def a_few_words(words):
        return 

    few_words = ["pause", "stop", "break"]


def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

print(greet_bob(say_hello))
