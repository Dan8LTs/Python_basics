import webbrowser

def validator(func):
    def wrapper(url):
        print("Это текст до функции")
        func(url)
        print("Это текст после функции")

    return wrapper

@validator
def open_url(url):
    webbrowser.open(url)

login = input("Введите ник в гитхаб: ")
open_url("https://github.com/" + login)