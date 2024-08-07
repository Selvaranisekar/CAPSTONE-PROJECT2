    import os
    import time

    import pytest
    from selenium import webdriver
    from selenium.common import TimeoutException

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC

    from selenium.webdriver.support.wait import WebDriverWait

    from capstoneProject2.Test_Excel_Functions.excel_functions import Selva_Excel_Functions
    from capstoneProject2.Test_locators.locators import TestLocators


    class Test_capstone_orangehrm:

        @pytest.fixture
        def boot(self):
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
            excel_file = 'C:\\Users\\ssekar588\\PycharmProjects\\GUVI Selenium 2\\capstoneProject2\\Test_Datas\\test_data.xlsx'
            sheet_name = 'Sheet1'
            self.driver.get(TestLocators.url)
            self.driver.maximize_window()
            self.wait = WebDriverWait(self.driver, 5)
            self.s = Selva_Excel_Functions(excel_file, sheet_name)
            self.rows = self.s.Row_Count()

            self.username_element = self.wait.until(EC.visibility_of_element_located((By.NAME, TestLocators().Email)))

            self.password_element = self.wait.until(EC.visibility_of_element_located((By.NAME, TestLocators().Password)))
            self.forgot_password = self.wait.until(EC.element_to_be_clickable((By.XPATH, TestLocators().forgoten_password)))

            self.login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, TestLocators().Login_button)))

            yield

            self.driver.quit()

        def reset_password(self):
            WebDriverWait(self.driver, 10)
            try:
                self.password_rst = self.wait.until(EC.element_to_be_clickable((By.XPATH, TestLocators().password_reset)))
                self.password_rst.click()
                WebDriverWait(self.driver, 15)

                self.wait.until(
                    EC.url_matches('https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset'))
                WebDriverWait(self.driver, 5)
                if self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset':
                    print("Reset: SUCCESS")

                    WebDriverWait(self.driver, 10)
                    screenshot_dir = os.path.join(os.getcwd(), 'screenshot')
                    os.makedirs(screenshot_dir, exist_ok=True)
                    screenshot_path = os.path.join(screenshot_dir, f"reset_success.png")
                    self.driver.save_screenshot(screenshot_path)
                    print(f"screenshot saved at: {screenshot_path}")
                else:
                    print("Reset: FAIL")

            except Exception as e:
                print(f"Exception occurred: {str(e)}")
                # Save screenshot when exception occurs
                screenshot_dir = os.path.join(os.getcwd(), 'screenshot')
                os.makedirs(screenshot_dir, exist_ok=True)
                screenshot_path = os.path.join(screenshot_dir, f"reset_failure.png")
                self.driver.save_screenshot(screenshot_path)
                print(f"screenshot saved at: {screenshot_path}")

        def title_name(self):
            if self.driver.title == "OrangeHRM":
                print("Title is OrangeHRM")
            else:
                print(f"Title is not OrangeHRM, it is {self.driver.title}")

        def admin_page(self):
            WebDriverWait(self.driver, 25)
            try:

                self.admin_opt = self.wait.until(EC.element_to_be_clickable((By.XPATH, TestLocators().admin)))
                self.admin_opt.click()
                WebDriverWait(self.driver, 10)

                self.wait.until(
                    EC.url_matches('https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers'))
                time.sleep(10)
                if self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers':
                    print("Admin: SUCCESS")

                    # Save screenshot of admin page
                    screenshot_dir = os.path.join(os.getcwd(), 'screenshot')
                    os.makedirs(screenshot_dir, exist_ok=True)
                    screenshot_path = os.path.join(screenshot_dir, "admin_page_navigated.png")
                    self.driver.save_screenshot(screenshot_path)
                    print(f"Screenshot saved at: {screenshot_path}")
                else:
                    print("Admin navigation: FAIL")

            except Exception as e:
                print(f"Exception occurred: {str(e)}")
                # Save screenshot when exception occurs
                screenshot_dir = os.path.join(os.getcwd(), 'screenshot')
                os.makedirs(screenshot_dir, exist_ok=True)
                screenshot_path = os.path.join(screenshot_dir, f"failure.png")
                self.driver.save_screenshot(screenshot_path)
                print(f"screenshot saved at: {screenshot_path}")

        def admin_options(self):
            # Assuming self.wait is properly initialized elsewhere in your class
            # WebDriverWait instantiation should assign the created WebDriverWait object to self.wait
            self.wait = WebDriverWait(self.driver, 5)
            options = [
                (By.XPATH, TestLocators().usermanagement),
                (By.XPATH, TestLocators().job),
                (By.XPATH, TestLocators().org),
                (By.XPATH, TestLocators().qualification),
                (By.XPATH, TestLocators().Nationalities),
                (By.XPATH, TestLocators().Corporatebranding),
                (By.XPATH, TestLocators().config)]

            text = [('usermanagement'), ('job'), ('org'), ('qualification'), ('Nationalities'), ('Corporatebranding'),('config')]
            for i in range(len(options)):
                locator = options[i]
                category_text = text[i]

                # for locator in options:
                try:
                    element = self.wait.until(EC.visibility_of_element_located(locator))
                    if element.is_displayed():
                        # print(f"{locator[1]} is visible")
                        print(f"Element identified by '{category_text}' is visible")
                        # print(options.text, "is visible")

                    else:
                        print(f"Element identified by '{category_text}' is not visible")
                except Exception as e:
                    print(f"Exception occurred while checking '{category_text}': {str(e)}")

        def home_page(self):
            WebDriverWait(self.driver, 25)
            try:
                WebDriverWait(self.driver, 25)
                self.login_button = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
                self.login_button.click()
                self.wait.until(
                    EC.url_matches('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'))

                if self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index':
                    print("HOME PAGE: SUCCESS")

                    # Save screenshot of admin page
                    screenshot_dir = os.path.join(os.getcwd(), 'screenshot')
                    os.makedirs(screenshot_dir, exist_ok=True)
                    screenshot_path = os.path.join(screenshot_dir, "Home_page_navigated.png")
                    self.driver.save_screenshot(screenshot_path)
                    print(f"Screenshot saved at: {screenshot_path}")
                else:
                    print("HOME PAGE: FAIL")

            except Exception as e:
                print(f"Exception occurred: {str(e)}")
                # Save screenshot when exception occurs
                screenshot_dir = os.path.join(os.getcwd(), 'screenshot')
                os.makedirs(screenshot_dir, exist_ok=True)
                screenshot_path = os.path.join(screenshot_dir, f"failure.png")
                self.driver.save_screenshot(screenshot_path)
                print(f"screenshot saved at: {screenshot_path}")

        def home_options(self):
            self.wait = WebDriverWait(self.driver, 5)
            options = [
                (By.XPATH, TestLocators().admin),
                (By.XPATH, TestLocators().PIM),
                (By.XPATH, TestLocators().leave),
                (By.XPATH, TestLocators().time),
                (By.XPATH, TestLocators().requirement),
                (By.XPATH, TestLocators().Myinfo),
                (By.XPATH, TestLocators().Performance),
                (By.XPATH, TestLocators().Dashboard),
                (By.XPATH, TestLocators().Directory),
                (By.XPATH, TestLocators().Maintainance),
                (By.XPATH, TestLocators().Buzz)
            ]
            text = [('Admin'), ('PIM'), ('Leave'), ('Time'), ('Recuirement'), ('My Info'),
                    ('Performance'), ('Dashboard'), ('Directory'), ('Maintenance'), ('Buzz')]
            for i in range(len(options)):
                locator = options[i]
                category_text = text[i]

                # for locator in options:
                try:
                    element = self.wait.until(EC.visibility_of_element_located(locator))
                    if element.is_displayed():
                        # print(f"{locator[1]} is visible")
                        print(f"Element identified by '{category_text}' is visible")
                        # print(options.text, "is visible")

                    else:
                        print(f"Element identified by '{category_text}' is not visible")
                except Exception as e:
                    print(f"Exception occurred while checking '{category_text}': {str(e)}")

        def test_pim_01(self, boot):

            self.forgot_password.click()
            # No need for time.sleep(40) if using WebDriverWait correctly

            username = self.s.Read_Data(2, 6)
            # Re-locate the username element after clicking forgot_password
            username_element = self.wait.until(EC.visibility_of_element_located((By.NAME, TestLocators().Email)))
            username_element.send_keys(username)
            print(username)
            self.reset_password()

        def test_admin_02(self, boot):

            username = self.s.Read_Data(2, 6)
            password = self.s.Read_Data(2, 7)

            self.username_element.send_keys(username)
            self.password_element.send_keys(password)
            self.login_button.click()
            self.title_name()
            self.admin_page()
            self.admin_options()

        def test_home_page_03(self, boot):

            username = self.s.Read_Data(2, 6)
            password = self.s.Read_Data(2, 7)

            self.username_element.send_keys(username)
            self.password_element.send_keys(password)
            self.login_button.click()

            self.home_page()
            self.title_name()
            self.home_options()



