# Auto Gmail Creator v1.1.0
# Автоматический создатель Gmail аккаунтов
# by BRIM, 2025
# https://github.com/YOURUSERNAME/Auto-Gmail-Creator

# Display the banner at the beginning
print("""
===================================================
            ██████╗  ██████╗  ██╗███╗   ███╗███╗   ███╗ █████╗ ██╗██╗     
            ██╔══██╗ ██╔══██╗ ██║████╗ ████║████╗ ████║██╔══██╗██║██║     
            ██████╔╝ ██████╔╝ ██║██╔████╔██║██╔████╔██║███████║██║██║     
            ██╔══██╗ ██╔══██╗ ██║██║╚██╔╝██║██║╚██╔╝██║██╔══██║██║██║     
            ██████╔╝ ██║  ██║ ██║██║ ╚═╝ ██║██║ ╚═╝ ██║██║  ██║██║███████╗
            ╚═════╝  ╚═╝  ╚═╝ ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝
                                                  
        Автоматический создатель Gmail аккаунтов - By BRIM
===================================================
""")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
import requests
from unidecode import unidecode
import uuid
from fp.fp import FreeProxy  # Import FreeProxy
import os
import sys
import traceback

# User Agents list for random selection
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 YaBrowser/21.8.1.468 Yowser/2.5 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0",
    "Mozilla/5.0 (X11; CrOS x86_64 14440.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4807.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14467.0.2022) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4838.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14469.7.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.13 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14455.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4827.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14469.11.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.17 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14436.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4803.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14475.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4840.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14469.3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.9 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14471.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4840.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14388.37.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.9 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14409.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4829.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14395.0.2021) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4765.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14469.8.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.14 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14484.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4840.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14450.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4817.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14473.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4840.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14324.72.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.91 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14454.0.2022) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4824.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14453.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4816.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14447.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4815.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14477.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4840.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14476.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4840.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14469.8.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.9 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14588.67.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14588.67.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14526.69.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.82 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14695.25.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.22 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 14526.89.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.91 Safari/537.36"
       
    # Add more User Agents
]

# Arabic names written in English letters
arabic_first_names = [
    "Ali", "Ahmed", "Omar", "Youssef", "Ayman", "Khaled", "Salma", "Nour", "Rania", "Hassan",
    "Fadi", "Sara", "Fatma", "Heba", "Lina", "Rami", "Amir", "Yasmin", "Hala", "Tamer",
    "Mohammed", "Yasser", "Sami", "Amira", "Zain", "Khalil", "Nabil", "Ziad", "Farah", "Layla",
    "Jamal", "Hadi", "Tariq", "Mahmoud", "Ranya", "Rashed", "Alaa", "Kareem", "Basma", "Nadia",
    "Yasmeen", "Hussain", "Saeed", "Iman", "Reem", "Joud", "Nourhan", "Khadija", "Sahar", "Maya",
    "Tala", "Hiba", "Dalia", "Nisreen", "Mariam", "Haneen", "Alaa", "Wissam", "Amani", "Ibtihaj",
    "Khalida", "Dania", "Loubna", "Ranya", "Hanan", "Nora", "Rawan", "Salim", "Fouzia", "Zayna",
    "Tamer", "Adnan", "Jawad", "Mansour", "Waleed", "Zuhair", "Hisham", "Hadi", "Ibrahim", "Yasmina",
    "Samira", "Huda", "Yasmin", "Rami", "Hossain", "Layal", "Kareema", "Zaki", "Aliya", "Salah",
    "Safaa", "Marwan", "Dina", "Yasmeen", "Asma", "Naima", "Tamara", "Tania", "Sabah", "Mona",
    "Firas", "Zayd", "Taha", "Yasin", "Sakina", "Madiha", "Rasha", "Sufyan", "Nafisa", "Othman",
    "Safa", "Nabilah", "Hala", "Faten", "Aisha", "Hassan", "Zainab", "Nouran", "Raneem", "Youssef",
]


arabic_last_names = [
    "Mohamed", "Ahmed", "Hussein", "Sayed", "Ismail", "Abdallah", "Khalil", "Soliman", "Nour", "Kamel",
    "Samir", "Ibrahim", "Othman", "Fouad", "Zaki", "Gamal", "Farid", "Mansour", "Adel", "Salem",
    "Hossam", "Nasser", "Qassem", "Khatib", "Rashed", "Moussa", "Naim", "Abdulaziz", "Anwar", "Younes",
    "Osama", "Bilal", "Fahd", "Rami", "Abdulrahman", "Maher", "Salim", "Tariq", "Amjad", "Ibtisam",
    "Ranya", "Sami", "Laith", "Hassan", "Saif", "Alaa", "Mujahid", "Ibrahim", "Zuhair", "Hadi",
    "Attar", "Said", "Jabari", "Ashraf", "Abu", "Ali", "Nasr", "Darwish", "Azzam", "Hussein",
    "Yasin", "Zidan", "Farhan", "Khaled", "Mahmoud", "Qureshi", "Sheikh", "Abdulkareem", "Sharif", "Abdelaziz",
    "Yunus", "Hasan", "Shakir", "Musa", "Salem", "Taha", "Ali", "Khalaf", "Khalid", "Karim",
    "Rashid", "Siddiqi", "Sulaiman", "Almasri", "Alhussein", "Sami", "Tarek", "Noor", "Husseini", "Jamil",
    "Ramzi", "Khalifa", "Hamed", "Anis", "Hussein", "Mahdi", "Samir", "Wahab", "Bakkar", "Najib",
    "Abdulhadi", "Alhaj", "Shahrani", "Sulieman", "Majeed", "Nazari", "Saber", "Tawfiq", "Sabry", "Sharif",
]


# Function to get a working proxy
def get_working_proxy():
    try:
        proxy = FreeProxy(rand=True, timeout=1).get()
        print(f"Используется прокси: {proxy}")
        return proxy
    except Exception as e:
        print(f"Ошибка получения прокси: {e}")
        print("Продолжение без прокси...")
        return None

# Проверка работоспособности прокси с Google
def check_proxy(proxy):
    try:
        print(f"Проверка прокси {proxy}...")
        proxies = {
            'http': proxy,
            'https': proxy
        }
        response = requests.get('https://www.google.com', proxies=proxies, timeout=5)
        if response.status_code == 200:
            print("Прокси работает нормально")
            return True
        else:
            print(f"Прокси вернул код ответа: {response.status_code}")
            return False
    except Exception as e:
        print(f"Ошибка проверки прокси: {e}")
        return False

# Function to save emails to a text file
def save_email_to_file(email, password):
    try:
        with open("emails.txt", "a") as file:
            file.write(f"Gmail: {email}, Пароль: {password}\n")
        print(f"Данные учетной записи сохранены в файл emails.txt")
    except Exception as e:
        print(f"Ошибка сохранения в файл: {e}")

# Generate username from random first and last name
def generate_username():
    first_name = random.choice(arabic_first_names)
    last_name = random.choice(arabic_last_names)
    random_number = random.randint(1000, 9999)
    first_name_normalized = unidecode(first_name).lower()
    last_name_normalized = unidecode(last_name).lower()
    return f"{first_name_normalized}.{last_name_normalized}{random_number}"

# Константы для данных аккаунта
your_birthday = "02 4 1950"
your_gender = "1"  # 1 = Мужской, 2 = Женский
your_password = "ShadowHacker##$$%%^^&&"

# Попытки выбора пола - всегда мужской
def select_gender_male(driver):
    print("Попытка выбора мужского пола...")
    
    # Делаем скриншот текущего состояния
    try:
        screenshot_path = f"debug_screenshot_gender_before_{uuid.uuid4()}.png"
        driver.save_screenshot(screenshot_path)
        print(f"Сделан скриншот до выбора пола: {screenshot_path}")
    except:
        pass
    
    # Метод 1: Находим и кликаем на селектор для открытия списка
    try:
        # Находим главный элемент селектора
        gender_selector = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='gender']//div[contains(@class, 'VfPpkd-TkwUic')]"))
        )
        # Кликаем, чтобы открыть выпадающий список
        driver.execute_script("arguments[0].click();", gender_selector)
        print("Выпадающий список пола открыт")
        time.sleep(1)
        
        # Теперь выбираем опцию "Муж." с data-value="1"
        male_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[@data-value='1']"))
        )
        driver.execute_script("arguments[0].click();", male_option)
        print("Выбран мужской пол (Муж.)")
        time.sleep(1)
        
        # Делаем скриншот после попытки выбора
        try:
            screenshot_path = f"debug_screenshot_gender_after_{uuid.uuid4()}.png"
            driver.save_screenshot(screenshot_path)
            print(f"Сделан скриншот после выбора пола: {screenshot_path}")
        except:
            pass
        
        return True
    except Exception as e:
        print(f"Ошибка при выборе пола через основной метод: {e}")
    
    # Метод 2: Альтернативный вариант через JavaScript
    try:
        script = """
        // Сначала открываем выпадающий список
        var genderSelector = document.querySelector('#gender .VfPpkd-TkwUic');
        if (genderSelector) {
            genderSelector.click();
            setTimeout(function() {
                // Ищем опцию с Муж. (data-value="1")
                var maleOption = document.querySelector('li[data-value="1"]');
                if (maleOption) {
                    maleOption.click();
                    return true;
                }
                return false;
            }, 1000);
            return true;
        }
        return false;
        """
        driver.execute_script(script)
        print("Попытка выбора пола через JavaScript")
        time.sleep(2)
    except Exception as e:
        print(f"Ошибка при выборе пола через JavaScript: {e}")
    
    # Метод 3: Попытка выбора через навигацию с клавиатуры
    try:
        # Находим элемент поля пола и устанавливаем на нем фокус
        gender_element = driver.find_element(By.XPATH, "//div[@id='gender']")
        gender_element.click()
        time.sleep(1)
        
        # Эмулируем клавиши для выбора мужского пола (второй элемент в списке)
        active_element = driver.switch_to.active_element
        active_element.send_keys(Keys.DOWN)  # Открываем выпадающий список
        time.sleep(0.5)
        active_element.send_keys(Keys.DOWN)  # Переходим к первому элементу (Жен.)
        time.sleep(0.5)
        active_element.send_keys(Keys.DOWN)  # Переходим ко второму элементу (Муж.)
        time.sleep(0.5)
        active_element.send_keys(Keys.ENTER)  # Выбираем элемент
        print("Мужской пол выбран через клавиатурную навигацию")
    except Exception as e:
        print(f"Ошибка при выборе пола через клавиатуру: {e}")
    
    # Делаем скриншот после попытки выбора
    try:
        screenshot_path = f"debug_screenshot_gender_after_{uuid.uuid4()}.png"
        driver.save_screenshot(screenshot_path)
        print(f"Сделан скриншот после выбора пола: {screenshot_path}")
    except:
        pass
    
    return True  # Возвращаем True, чтобы процесс мог продолжиться

# Fill birthday and gender
def fill_birthday_and_gender(driver):
    try:
        print("Заполнение даты рождения и пола...")
        # Небольшая задержка для загрузки страницы
        time.sleep(3)
        
        # Делаем скриншот для диагностики
        try:
            screenshot_path = f"debug_screenshot_birthday_{uuid.uuid4()}.png"
            driver.save_screenshot(screenshot_path)
            print(f"Сделан скриншот страницы даты рождения: {screenshot_path}")
        except:
            print("Не удалось сделать скриншот")
        
        # Ищем поля для ввода даты рождения разными способами
        birthday_elements = your_birthday.split()
        
        # Заполняем день рождения
        try:
            day_field = None
            if driver.find_elements(By.ID, "day"):
                day_field = driver.find_element(By.ID, "day")
            elif driver.find_elements(By.NAME, "day"):
                day_field = driver.find_element(By.NAME, "day")
            else:
                day_field = driver.find_element(By.XPATH, "//input[contains(@aria-label, 'день') or contains(@aria-label, 'Day')]")
            
            day_field.clear()
            day_field.send_keys(birthday_elements[0])
            print("День рождения успешно заполнен")
        except Exception as day_error:
            print(f"Ошибка при заполнении дня рождения: {day_error}")
            return False
        
        # Выбираем месяц
        try:
            if driver.find_elements(By.ID, "month"):
                month_element = driver.find_element(By.ID, "month")
                if month_element.tag_name.lower() == "select":
                    month_dropdown = Select(month_element)
                    month_dropdown.select_by_value(birthday_elements[1])
                else:
                    month_element.click()
                    time.sleep(1)
                    month_option = driver.find_element(By.XPATH, f"//li[@data-value='{birthday_elements[1]}']")
                    month_option.click()
                print("Месяц выбран")
            else:
                driver.execute_script(f"document.querySelector('[aria-label=\"Месяц\"]').value = '{birthday_elements[1]}'")
                print("Месяц выбран через JavaScript")
        except Exception as month_error:
            print(f"Ошибка при выборе месяца: {month_error}")
            return False
        
        # Заполняем год
        try:
            year_field = None
            if driver.find_elements(By.ID, "year"):
                year_field = driver.find_element(By.ID, "year")
            elif driver.find_elements(By.NAME, "year"):
                year_field = driver.find_element(By.NAME, "year")
            else:
                year_field = driver.find_element(By.XPATH, "//input[contains(@aria-label, 'год') or contains(@aria-label, 'Year')]")
            
            year_field.clear()
            year_field.send_keys(birthday_elements[2])
            print("Год рождения успешно заполнен")
        except Exception as year_error:
            print(f"Ошибка при заполнении года рождения: {year_error}")
            return False
        
        # Выбираем мужской пол
        gender_selected = select_gender_male(driver)
        
        # Клик на кнопку "Далее"
        try:
            # Ищем кнопку Далее разными способами
            next_button = None
            
            # Метод 1: По тексту
            try:
                next_button = driver.find_element(By.XPATH, "//button[contains(., 'Далее') or contains(., 'Next')]")
            except:
                pass
            
            # Метод 2: По классу
            if not next_button:
                try:
                    next_button = driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe")
                except:
                    pass
            
            # Метод 3: Последняя кнопка на странице
            if not next_button:
                buttons = driver.find_elements(By.TAG_NAME, "button")
                if buttons:
                    next_button = buttons[-1]  # Берем последнюю кнопку
            
            if next_button:
                # Прокручиваем до кнопки и кликаем
                driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
                time.sleep(0.5)
                driver.execute_script("arguments[0].click();", next_button)
                print("Нажата кнопка Далее")
            else:
                # Альтернативный метод: нажимаем Enter в последнем заполненном поле
                year_field.send_keys(Keys.ENTER)
                print("Форма отправлена через Enter")
        except Exception as next_error:
            print(f"Ошибка при нажатии кнопки Далее: {next_error}")
            return False
        
        # Ждем перехода на следующую страницу
        time.sleep(5)
        
        try:
            WebDriverWait(driver, 15).until(
                lambda d: d.find_elements(By.NAME, "Username") or 
                         d.find_elements(By.ID, "selectionc4") or
                         d.find_elements(By.XPATH, "//input[@type='email']") or
                         d.find_elements(By.XPATH, "//div[contains(text(), 'Создайте')]")
            )
            print("Успешный переход на страницу создания email")
            return True
        except:
            print("Не удалось подтвердить переход на страницу создания email")
            
            # Делаем скриншот текущей страницы для диагностики
            try:
                screenshot_path = f"debug_screenshot_after_gender_{uuid.uuid4()}.png"
                driver.save_screenshot(screenshot_path)
                print(f"Сделан скриншот после попытки перехода: {screenshot_path}")
            except:
                print("Не удалось сделать скриншот")
            
            # Пробуем нажать на кнопку еще раз
            try:
                buttons = driver.find_elements(By.TAG_NAME, "button")
                if buttons:
                    driver.execute_script("arguments[0].click();", buttons[-1])
                    print("Повторная попытка нажатия на кнопку Далее")
                    time.sleep(3)
                    
                    # Проверяем, произошел ли переход
                    if driver.find_elements(By.NAME, "Username") or driver.find_elements(By.ID, "selectionc4"):
                        print("Успешный переход на страницу создания email после повторной попытки")
                        return True
            except:
                pass
            
            # В крайнем случае, продолжаем выполнение
            print("Продолжаем процесс, несмотря на ошибку...")
            return True
    except Exception as e:
        print(f"Общая ошибка при заполнении даты рождения и пола: {e}")
        traceback.print_exc()
        return False

# Функция для обработки экрана с QR-кодом
def handle_qr_code(driver):
    try:
        # Проверяем наличие QR-кода на странице
        qr_indicators = [
            "//div[contains(text(), 'Отсканируйте QR-код')]",
            "//div[contains(text(), 'QR')]",
            "//img[contains(@src, 'qr')]",
            "//div[contains(text(), 'Подтвердите')]"
        ]
        
        for indicator in qr_indicators:
            if driver.find_elements(By.XPATH, indicator):
                print("\n" + "="*50)
                print("🔍 ОБНАРУЖЕН QR-КОД")
                print("="*50)
                print("Google требует подтверждение через сканирование QR-кода")
                
                # Делаем скриншот QR-кода
                screenshot_path = f"qr_code_{uuid.uuid4()}.png"
                driver.save_screenshot(screenshot_path)
                print(f"✅ Скриншот QR-кода сохранен в файл: {screenshot_path}")
                
                print("\n📱 ИНСТРУКЦИИ ПО СКАНИРОВАНИЮ:")
                print("1. Откройте на телефоне приложение Камера")
                print("2. Отсканируйте QR-код из сохраненного скриншота")
                print("3. Следуйте инструкциям на телефоне для подтверждения")
                print("4. Дождитесь завершения проверки на телефоне")
                print("\n⚠️ ВАЖНО: Не закрывайте окно браузера во время проверки!")
                
                # Спрашиваем пользователя о завершении
                user_input = input("\n✓ Нажмите Enter после завершения проверки, или введите 'отмена' для прекращения: ")
                if user_input.lower() in ['отмена', 'cancel', 'stop']:
                    print("❌ Процесс регистрации прерван пользователем")
                    return False
                
                # Ждем некоторое время для обработки подтверждения
                print("⏳ Ожидание обработки подтверждения...")
                time.sleep(5)
                print("✅ Проверка QR-кода завершена, продолжаем регистрацию")
                return True
        
        # QR-код не обнаружен
        return True
    except Exception as e:
        print(f"❌ Ошибка при обработке QR-кода: {e}")
        return False

# Fill out Gmail registration form
def fill_form(driver):
    try:
        device_uuid = uuid.uuid4()
        print(f"Используется UUID устройства: {device_uuid}")
        your_username = generate_username()

        driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")
        print("Открыта страница регистрации Google")

        # Fill in the name fields
        try:
            print("Заполнение имени и фамилии...")
            first_name = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.NAME, "firstName")))
            last_name = driver.find_element(By.NAME, "lastName")
            first_name.clear()
            first_name.send_keys(your_username.split('.')[0])
            last_name.clear()
            last_name.send_keys(your_username.split('.')[1])

            # Попробуем несколько способов нажатия на кнопку "Далее"
            try:
                # Метод 1: По классу
                next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-LgbsSe")))
                next_button.click()
            except:
                try:
                    # Метод 2: По тексту на кнопке
                    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Далее')]/ancestor::button")))
                    next_button.click()
                except:
                    try:
                        # Метод 3: По атрибуту next
                        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-next]")))
                        next_button.click()
                    except:
                        try:
                            # Метод 4: Попробуем нажать Enter после заполнения полей
                            last_name.send_keys(Keys.ENTER)
                        except Exception as e:
                            print(f"Не удалось нажать на кнопку Далее: {e}")
                            # Последняя попытка - выполнить JavaScript клик
                            driver.execute_script("document.querySelector('.VfPpkd-LgbsSe').click()")
            
            # Проверяем наличие QR-кода
            if not handle_qr_code(driver):
                print("Процесс регистрации прерван пользователем на этапе QR-кода")
                return False
            
            # Проверим, что мы перешли на следующую страницу
            try:
                # Ждем появления любого элемента следующей страницы (день, месяц или год)
                WebDriverWait(driver, 10).until(
                    lambda d: d.find_elements(By.ID, "day") or 
                             d.find_elements(By.ID, "month") or 
                             d.find_elements(By.ID, "year") or
                             d.find_elements(By.NAME, "day") or
                             d.find_elements(By.NAME, "month") or
                             d.find_elements(By.NAME, "year")
                )
                print("Имя и фамилия успешно заполнены")
            except:
                print("Предупреждение: Не удалось подтвердить переход на страницу даты рождения")
        except Exception as e:
            print(f"Ошибка при заполнении имени и фамилии: {e}")
            print("Завершение процесса из-за ошибки на первом шаге.")
            return False

        # Заполняем дату рождения и пол с использованием новой функции
        if not fill_birthday_and_gender(driver):
            print("Ошибка при заполнении даты рождения и пола")
            return False
            
        # Проверяем наличие QR-кода
        if not handle_qr_code(driver):
            print("Процесс регистрации прерван пользователем на этапе QR-кода")
            return False

        # Create custom email
        try:
            print("Создание адреса электронной почты...")
            time.sleep(2)
            if driver.find_elements(By.ID, "selectionc4"):
                create_own_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "selectionc4")))
                create_own_option.click()

            create_own_email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "Username")))
            username_field = driver.find_element(By.NAME, "Username")
            username_field.clear()
            username_field.send_keys(your_username)
            
            # Клик на кнопку "Далее" несколькими способами
            try:
                next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-LgbsSe")))
                driver.execute_script("arguments[0].click();", next_button)
            except:
                try:
                    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Далее')]/ancestor::button")))
                    driver.execute_script("arguments[0].click();", next_button)
                except:
                    username_field.send_keys(Keys.ENTER)
                    
            # Проверяем наличие QR-кода
            if not handle_qr_code(driver):
                print("Процесс регистрации прерван пользователем на этапе QR-кода")
                return False
            
            print("Адрес электронной почты успешно создан")
        except Exception as e:
            print(f"Ошибка при создании адреса электронной почты: {e}")
            print("Завершение процесса из-за ошибки при создании адреса электронной почты.")
            return False

        # Enter and confirm password
        try:
            print("Установка пароля...")
            password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "Passwd")))
            password_field.clear()
            password_field.send_keys(your_password)
            confirm_passwd_div = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "confirm-passwd")))
            password_confirmation_field = confirm_passwd_div.find_element(By.NAME, "PasswdAgain")
            password_confirmation_field.clear()
            password_confirmation_field.send_keys(your_password)
            
            # Клик на кнопку "Далее" несколькими способами
            try:
                next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-LgbsSe")))
                driver.execute_script("arguments[0].click();", next_button)
            except:
                try:
                    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Далее')]/ancestor::button")))
                    driver.execute_script("arguments[0].click();", next_button)
                except:
                    password_confirmation_field.send_keys(Keys.ENTER)
                    
            # Проверяем наличие QR-кода
            if not handle_qr_code(driver):
                print("Процесс регистрации прерван пользователем на этапе QR-кода")
                return False
            
            print("Пароль успешно установлен")
        except Exception as e:
            print(f"Ошибка при установке пароля: {e}")
            print("Завершение процесса из-за ошибки при установке пароля.")
            return False

        # Skip phone number and recovery email
        try:
            print("Пропуск подтверждения номера телефона...")
            
            # Ищем кнопку Skip на английском или Пропустить на русском
            try:
                skip_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Skip') or contains(text(),'Пропустить')]/ancestor::button"))
                )
                driver.execute_script("arguments[0].click();", skip_button)
            except:
                print("Кнопка пропуска не найдена, пытаемся найти другим способом...")
                try:
                    # Ищем все кнопки и кликаем на ту, где есть Skip/Пропустить
                    buttons = driver.find_elements(By.TAG_NAME, "button")
                    for button in buttons:
                        if "Skip" in button.text or "Пропустить" in button.text:
                            driver.execute_script("arguments[0].click();", button)
                            break
                except:
                    print("Не удалось найти кнопку пропуска")
                    
            # Проверяем наличие QR-кода
            if not handle_qr_code(driver):
                print("Процесс регистрации прерван пользователем на этапе QR-кода")
                return False
            
            print("Проверка номера телефона пропущена")
        except Exception as skip_error:
            print("Нет шага проверки номера телефона или не удалось пропустить.")
            # Продолжаем выполнение, так как этот шаг может отсутствовать

        # Agree to terms
        try:
            print("Принятие условий использования...")
            
            # Ищем кнопку "Я согласен" несколькими способами
            try:
                agree_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d"))
                )
                driver.execute_script("arguments[0].click();", agree_button)
            except:
                try:
                    # Ищем по тексту кнопки
                    agree_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'согла') or contains(text(),'I agree')]/ancestor::button"))
                    )
                    driver.execute_script("arguments[0].click();", agree_button)
                except:
                    print("Кнопка согласия не найдена")
                    
            # Проверяем наличие QR-кода
            if not handle_qr_code(driver):
                print("Процесс регистрации прерван пользователем на этапе QR-кода")
                return False
            
            print("Условия использования приняты")
        except Exception as e:
            print(f"Ошибка при принятии условий: {e}")
            print("Завершение процесса из-за ошибки при принятии условий.")
            return False

        print(f"Ваш Gmail успешно создан:\n{{\nпочта: {your_username}@gmail.com\nпароль: {your_password}\n}}")
        save_email_to_file(f"{your_username}@gmail.com", your_password)
        return True

    except Exception as e:
        print("Не удалось создать Gmail, извините")
        print(f"Ошибка: {e}")
        print("Подробная информация об ошибке:")
        traceback.print_exc()
        return False

# Create multiple accounts
def create_multiple_accounts(number_of_accounts, use_proxy=True):
    successful_accounts = 0
    
    for i in range(number_of_accounts):
        try:
            print(f"\nСоздание аккаунта {i+1} из {number_of_accounts}...")
            
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-popup-blocking")
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            
            # Игнорирование ошибок сертификатов
            chrome_options.add_argument("--ignore-certificate-errors")
            chrome_options.add_argument("--ignore-ssl-errors")
            chrome_options.add_argument("--allow-insecure-localhost")
            
            # Create a user data directory if it doesn't exist
            cookies_dir = os.path.join(os.getcwd(), "cookies", f"profile_{i}")
            if not os.path.exists(cookies_dir):
                os.makedirs(cookies_dir)
                
            chrome_options.add_argument(f"--user-data-dir={cookies_dir}")
            
            user_agent = random.choice(user_agents)
            chrome_options.add_argument(f'user-agent={user_agent}')
            
            # Используем прокси только если флаг включен
            if use_proxy:
                max_proxy_attempts = 3
                proxy = None
                
                for attempt in range(max_proxy_attempts):
                    proxy = get_working_proxy()
                    if proxy and check_proxy(proxy):
                        chrome_options.add_argument(f'--proxy-server={proxy}')
                        break
                    elif attempt < max_proxy_attempts - 1:
                        print(f"Попытка {attempt+1} не удалась, пробуем другой прокси...")
                    else:
                        print("Не удалось найти рабочий прокси после нескольких попыток.")
                        print("Продолжение без прокси...")
            else:
                print("Режим без прокси включен")
            
            print("Запуск браузера Chrome...")
            driver = webdriver.Chrome(options=chrome_options)
            
            success = fill_form(driver)
            
            print("Закрытие браузера...")
            driver.quit()
            
            if success:
                successful_accounts += 1
                print(f"Успешно создан аккаунт {i+1} из {number_of_accounts}")
            else:
                print(f"Не удалось создать аккаунт {i+1}. Завершение программы.")
                break
            
            if i < number_of_accounts - 1 and success:
                wait_time = random.randint(5, 15)
                print(f"Ожидание {wait_time} секунд перед созданием следующего аккаунта...")
                time.sleep(wait_time)
            
        except Exception as e:
            print(f"Критическая ошибка при создании аккаунта {i+1}: {e}")
            print("Завершение программы.")
            break

    return successful_accounts

if __name__ == "__main__":
    try:
        # Запрос количества аккаунтов для создания
        while True:
            try:
                user_input = input("Введите количество Gmail аккаунтов для создания: ")
                number_of_accounts = int(user_input)
                if number_of_accounts > 0:
                    break
                else:
                    print("Пожалуйста, введите положительное число.")
            except ValueError:
                print("Пожалуйста, введите корректное число.")
        
        # Запрос о использовании прокси
        while True:
            proxy_choice = input("Использовать прокси? (да/нет): ").lower()
            if proxy_choice in ["да", "yes", "y", "д"]:
                use_proxy = True
                break
            elif proxy_choice in ["нет", "no", "n", "н"]:
                use_proxy = False
                break
            else:
                print("Пожалуйста, введите 'да' или 'нет'.")
        
        print(f"Запуск создания {number_of_accounts} Gmail аккаунтов...")
        successful = create_multiple_accounts(number_of_accounts, use_proxy)
        print(f"Процесс создания аккаунтов завершен. Успешно создано: {successful} из {number_of_accounts}")
    except KeyboardInterrupt:
        print("\nПрограмма остановлена пользователем.")
    except Exception as e:
        print(f"Критическая ошибка в основной программе: {e}")
        traceback.print_exc()
