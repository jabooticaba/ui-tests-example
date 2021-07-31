import pytest
from pages.mypets_page import MyPetsPage


def test_exit_from(web_browser):

    page = MyPetsPage(web_browser)
    page.my_pets.click()

    assert page.get_current_url() == 'http://petfriends1.herokuapp.com/my_pets'
    assert page.title.get_attribute("innerText") == 'PetFriends: My Pets'
    web_browser.delete_all_cookies()
    page.exit_btn.click()
    assert page.get_current_url() == 'http://petfriends1.herokuapp.com/login'