from pages.base import WebPage
from pages.elements import WebElement
import pickle


class MyPetsPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'http://petfriends1.herokuapp.com/my_pets'
        super().__init__(web_driver, url)


        with open('cookies.txt', 'rb') as cookiesfile:
           cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            web_driver.add_cookie(cookie)
        web_driver.refresh()

    my_pets = WebElement(css_selector='a[href="/my_pets"]')

    all_pets = WebElement(css_selector='a[href="/all_pets"]')

    # exit_btn = WebElement(class_name='btn.btn-outline-secondary')
    exit_btn = WebElement(xpath="//*[contains(text(),'Выйти')]")
    title = WebElement(css_selector='head title')