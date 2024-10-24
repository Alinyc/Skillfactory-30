import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')

    yield driver

    driver.quit()


# def test_show_all_pets(driver):
#     # Вводим email
#     driver.find_element(By.ID, 'email').send_keys('alina.chikineva@yahoo.com')
#     # Вводим пароль
#     driver.find_element(By.ID, 'pass').send_keys('15131513')
#     # Нажимаем на кнопку входа в аккаунт
#     driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
#     # Проверяем, что мы оказались на главной странице пользователя
#     assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
#
#     # Устанавливаем явное ожидание
#     WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a')))
#     driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
#
#     images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
#     names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
#     descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')
#
#     for i in range(len(names)):
#         assert images[i].get_attribute('src') != ''
#         assert names[i].text != ''
#         assert descriptions[i].text != ''
#         assert ', ' in descriptions[i]
#         parts = descriptions[i].text.split(", ")
#         assert len(parts[0]) > 0
#         assert len(parts[1]) > 0
#
#
# def test_all_my_pets(driver):
#     driver.find_element(By.ID, 'email').send_keys('alina.chikineva@yahoo.com')
#     # Вводим пароль
#     driver.find_element(By.ID, 'pass').send_keys('15131513')
#     # Нажимаем на кнопку входа в аккаунт
#     driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
#     # Проверяем, что мы оказались на главной странице пользователя
#     assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
#     time.sleep(3)
#     # Устанавливаем явное ожидание
#     WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a')))
#     driver.find_element(By.XPATH, '//a[text()="Мои питомцы"]').click()
#
#     pets_number = driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1]
#     pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
#
#     assert int(pets_number) == len(pets_count)
#
#
# def test_my_pets_name_age_breed(driver):
#     driver.find_element(By.ID, 'email').send_keys('alina.chikineva@yahoo.com')
#     # Вводим пароль
#     driver.find_element(By.ID, 'pass').send_keys('15131513')
#     # Нажимаем на кнопку входа в аккаунт
#     driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
#     # Проверяем, что мы оказались на главной странице пользователя
#     assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
#     time.sleep(3)
#     driver.find_element(By.XPATH, '//a[text()="Мои питомцы"]').click()
#
#     pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
#
#     # Устанавливаем неявное ожидание
#     driver.implicitly_wait(10)
#     names = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
#     breeds = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[2]')
#     ages = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[3]')
#
#     for pet in pets_count:
#         assert len(names) > 0
#         assert len(breeds) > 0
#         assert len(ages) > 0
#
#
# def test_my_pets_photos(driver):
#     driver.find_element(By.ID, 'email').send_keys('alina.chikineva@yahoo.com')
#     # Вводим пароль
#     driver.find_element(By.ID, 'pass').send_keys('15131513')
#     # Нажимаем на кнопку входа в аккаунт
#     driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
#     # Проверяем, что мы оказались на главной странице пользователя
#     assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
#     time.sleep(1)
#     driver.find_element(By.XPATH, '//a[text()="Мои питомцы"]').click()
#
#     image_count = driver.find_elements(By.XPATH, '//img[starts-with(@src, "data:image/")]')
#     pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
#     pets_photos = 0
#
#     # Проверяем что фотографии имеются более чем у половины питомцев
#     assert len(image_count) >= len(pets_count) / 2, "Меньше половины питомцев с фото"
#
#     if len(pets_count) == 0:
#         print("Питомцев нет")
#
#
# def test_my_pets_no_same_names(driver):
#     driver.find_element(By.ID, 'email').send_keys('alina.chikineva@yahoo.com')
#     # Вводим пароль
#     driver.find_element(By.ID, 'pass').send_keys('15131513')
#     # Нажимаем на кнопку входа в аккаунт
#     driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
#     # Проверяем, что мы оказались на главной странице пользователя
#     assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
#     time.sleep(3)
#     driver.find_element(By.XPATH, '//a[text()="Мои питомцы"]').click()
#
#     all_rows = driver.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody > tr')
#
#     pet_names = []
#
#     for row in all_rows:
#         name_element = row.find_element(By.TAG_NAME, 'td')
#         pet_names.append(name_element.text)
#         unique_names = set(pet_names)
#         assert len(unique_names) == len(pet_names), "В списке есть повторяющиеся имена"


def test_my_pets_no_same_pets(driver):
    driver.find_element(By.ID, 'email').send_keys('alina.chikineva@yahoo.com')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('15131513')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    time.sleep(3)
    driver.find_element(By.XPATH, '//a[text()="Мои питомцы"]').click()

    names = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
    ages = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[3]')
    breeds = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[2]')
    pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')

    list_names = []
    list_ages = []
    list_breeds = []

    for i in range(len(pets_count)):
        if names[i].text != '':
            list_names.append(names[i].text)
        set_names = set(list_names)

        if len(set_names) != len(list_names):
            for i in range(len(pets_count)):
                if ages[i].text != '':
                    list_ages.append(ages[i].text)
        set_ages = set(list_ages)

        if len(set_ages) != len(list_ages):
            for i in range(len(pets_count)):
                if breeds[i].text != '':
                    list_breeds.append(breeds[i].text)
        set_breeds = set(list_breeds)

        assert (len(set_names) == len(list_names)) and (len(set_ages) == len(list_ages)) and (len(set_breeds) == len(list_breeds)), "Есть повторяющиеся питомцы"
