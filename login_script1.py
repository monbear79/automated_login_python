from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import traceback
import schedule
import time

def login_to_website(username, password):
    print("Attempting to log in...")

    website_url = "https://regist.vlu.edu.vn/"
    chromedriver_path = 'path/to/chromedriver.exe'

    # Create ChromeOptions object
    options = Options()

    # Uncomment the line below if you want to run Chrome in headless mode
    # options.add_argument('--headless')

    # Set the path to the ChromeDriver executable
    options.add_argument(f'--webdriver-path={chromedriver_path}')

    # Initialize the WebDriver with ChromeOptions
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(website_url)

        # Wait for the username input to be present within the login form
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )

        # Send the provided username
        username_input.send_keys(username)

        # Locate the password input and send the provided password
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_input.send_keys(password)

        # Submit the login form
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='Đăng nhập']"))
        )

        login_button.click()

        print("Login successful!")

    except Exception as e:
        print(f"An error occurred: {e}")
        print(f"Stacktrace: {traceback.format_exc()}")

    # Keep the browser open after a successful login
    input("Press Enter to close the browser...")

    # Close the browser only if there was an exception
    # Comment out or remove the following line if you want to keep the browser open after a successful login
    driver.quit()

# Schedule the login function to run every day at a specific time
# Replace 'your_username' and 'your_password' with the actual credentials
schedule.every().day.at("06:55:58").do(login_to_website, username='2274801030174', password='22052004')

while True:
    schedule.run_pending()
    time.sleep(1)
