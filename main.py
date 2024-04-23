import requests

def main():
    """Запрос на сайт"""
    return requests.get(url='https://www.google.com')

if __name__ == '__main__':
    print(main())

