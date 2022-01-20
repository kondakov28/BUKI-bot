from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import telebot


bot = telebot.TeleBot('your_key')


def buki_bot():
    personal_orders = []
    potential_orders = []
    general_orders = []
    online_orders = []
    options = webdriver.ChromeOptions()
    options.add_argument(
        f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36')
    driver = webdriver.Chrome(executable_path='your_path',
                              options=options)
    try:
        driver.get(url='https://buki.com.ua/login/')
        time.sleep(4)

        login = driver.find_element_by_name('login')
        login.clear()
        time.sleep(2)
        login.send_keys('your_email')

        password = driver.find_element_by_name('password')
        password.clear()
        time.sleep(2)
        password.send_keys('your_password')
        time.sleep(1)

        password.send_keys(Keys.ENTER)
        time.sleep(20)
        driver.find_element_by_id('user-avatar').click()
        time.sleep(1)
        driver.find_element_by_link_text('Нові замовлення').click()

        while True:
            personal_count = 0
            # driver.find_element_by_link_text('Нові замовлення').click()
            time.sleep(3)
            personal = driver.find_element_by_id('personal_orders')
            if personal.text != 'Персональні заявки (0)':
                driver.find_element_by_partial_link_text('Всі персональні заявки').click()
                orders = driver.find_elements_by_class_name('order-title')
                for order in orders:
                    if order.text not in personal_orders:
                        print(order.text)
                        personal_orders.append(order.text)
                        personal_count += 1
                if personal_count > 0:
                    bot.send_message('user_key', f'New {personal_count} personal!')

                time.sleep(2)
                driver.back()

            potential_count = 0
            potential = driver.find_element_by_id('potentials_orders')
            if potential.text != 'Потенційні заявки (0)':
                driver.find_element_by_partial_link_text('Всі потенційні заявки').click()
                orders = driver.find_elements_by_class_name('order-title')
                for order in orders:
                    if order.text not in potential_orders:
                        print(order.text)
                        potential_orders.append(order.text)
                        potential_count += 1
                if potential_count > 0:
                    bot.send_message('user_key', f'New {potential_count} potentional!')

                time.sleep(2)
                driver.back()

            time.sleep(2)

            general_count = 0
            general = driver.find_element_by_id('general_orders')
            if general.text != 'Заявки мого міста (0)':
                driver.find_element_by_partial_link_text('Всі заявки мого міста').click()
                orders = driver.find_elements_by_class_name('order-title')
                for order in orders:
                    if order.text not in general_orders:
                        print(order.text)
                        general_orders.append(order.text)
                        general_count += 1
                if general_count > 0:
                    bot.send_message('user_key', f'New {general_count} general!')

                time.sleep(2)
                driver.back()

            time.sleep(2)

            online_count = 0
            online = driver.find_element_by_id('skype_orders')
            if online.text != 'Заявки на онлайн-заняття (0)':
                driver.find_element_by_partial_link_text('Всі онлайн заявки').click()
                orders = driver.find_elements_by_class_name('order-title')
                for order in orders:
                    if order.text not in online_orders:
                        print(order.text)
                        online_orders.append(order.text)
                        online_count += 1
                if online_count > 0:
                    bot.send_message('user_key', f'New {online_count} online!')

                time.sleep(2)
                driver.back()

            time.sleep(60)
            driver.refresh()
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    buki_bot()
    bot.infinity_polling()
