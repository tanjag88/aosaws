from time import sleep
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import aos_locators as locators



def set_up(driver):
    print(f'Launch {locators.website} Home Page')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.adv_url)
    sleep(2)
    if (driver.current_url == locators.adv_url and
            driver.title == locators.adv_title):
        print(f'{locators.website} Home Page Launched Successfully!')
        print(f'{locators.website} Home Page url:\nexpected result: {locators.adv_url} | '
              f'actual result: {driver.current_url}')
        print(f'{locators.website} Home Page title:\nexpected result: {locators.adv_title} | '
              f'actual result: {driver.title}')
        sleep(1)
    else:
        print(f'{locators.website} Home Page did not launch. Check your code and internet connection!')


def tear_down(driver):
    if driver is not None:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f'The test Completed at: {datetime.datetime.now()}')
        sleep(0.5)
        driver.close()
        driver.quit()


def create_new_user(driver):
    print('---------- Create New User ----------')
    sleep(2)
    driver.find_element(By.ID, "hrefUserIcon").click()
    sleep(2)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(2)
    for key, value in locators.account_dict.items():
        if key != 'countryListboxRegisterPage':
            driver.find_element(By.XPATH, f'//input[@name="{key}"]').send_keys(value)
            sleep(0.25)
        else:
            driver.find_element(By.XPATH,
                                f'//select[@name="{key}"]/option[@label="{locators.country}"]').click()
    driver.find_element(By.NAME, 'i_agree').click()
    sleep(0.25)
    driver.find_element(By.ID, 'register_btnundefined').click()
    print(f'New user with username: {locators.username}, and password: {locators.password} was created!')
    go_to_homepage(driver)


def validate_if_new_user_is_created(new_username, driver):
    print('---------- Validate New User is created ----------')
    sleep(0.25)
    driver.find_element(By.ID, 'menuUserLink')
    displayed_username = driver.find_element(By.CSS_SELECTOR,
                                             'span[data-ng-show="userCookie.response"]'
                                             '[class="hi-user containMiniTitle ng-binding"]').get_attribute('innerText')
    if new_username == displayed_username:
        print('New user is created and new username is displayed in the top menu!')
        print(
            f'New user with username: {new_username} was validate, new username: '
            f'{displayed_username} is displayed in the top menu: ')
    else:
        print('New user was not created!')
    go_to_homepage(driver)


def log_in(new_username, new_password, driver):
    print('----------- Log in with new User ----------')
    sleep(1)
    driver.find_element(By.ID, "hrefUserIcon").click()
    sleep(1)
    driver.find_element(By.NAME, 'username').send_keys(new_username)
    sleep(1)
    driver.find_element(By.NAME, 'password').send_keys(new_password)
    sleep(1)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    print('Successfully log in!')
    go_to_homepage(driver)


def validate_if_new_user_can_log_in(new_username, driver):
    print('---------- Validate New User can Sign in ----------')
    sleep(0.25)
    driver.find_element(By.ID, 'menuUserLink')
    displayed_username = driver.find_element(By.CSS_SELECTOR,
                                             'span[data-ng-show="userCookie.response"]'
                                             '[class="hi-user containMiniTitle ng-binding"]').get_attribute('innerText')
    if new_username == displayed_username:
        print('New user was successfully logged in!')
        print(f'New username: "{displayed_username}" is displayed in the top menu!')
    else:
        print('New user was not logged in!')
    go_to_homepage(driver)


def log_out(username, driver):
    print('---------- Log Out ----------')
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, username).click()
    sleep(1)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"Sign out")]').click()
    sleep(1)
    print('Successfully logged out!')
    go_to_homepage(driver)


def check_top_heading_menu_links_on_homepage(driver):
    print('---------- Check top heading menu links ----------')
    assert driver.find_element(By.XPATH, '//span[contains(text(),"dvantage")]').is_displayed()
    print('Main logo is displayed')
    for link_text in locators.links_text:
        assert driver.find_element(By.LINK_TEXT, link_text).is_displayed()
        sleep(1)
        driver.find_element(By.LINK_TEXT, link_text).click()
        sleep(1)
        print(f'Link "{link_text}", is displayed and clickable!')
        go_to_homepage(driver)


def check_all_texts_are_displayed_and_links_are_clickable_on_homepage(driver):
    print('---------- Check all texts are displayed and links are clickable on homepage ----------')
    for link in locators.links:
        assert driver.find_element(By.XPATH, f'//span[contains(.,"{link}")]').is_displayed()
        print(f'{link} link is displayed!')
        sleep(2)
        driver.find_element(By.XPATH, f'//span[contains(.,"{link}")]').click()
        print(f'{link} URL: {driver.current_url}')
        sleep(2)
        driver.back()
        # driver.find_element(By.XPATH, '//a[@href="#/"]').click()
    for text in locators.texts:
        assert driver.find_element(By.XPATH, f'//*[contains(.,"{text}")]').is_displayed()
        sleep(1)
        print(f"Text: '{text}' is displayed on homepage!")
    assert driver.find_element(By.ID, 'see_offer_btn').is_displayed()
    sleep(1)
    driver.find_element(By.ID, 'see_offer_btn').click()
    print(f'Button "SEE OFFER" is clickable, URL is: {driver.current_url}')
    sleep(1)
    # Go to homepage
    driver.back()
    driver.find_element(By.XPATH, '//button[@name="explore_now_btn"]').click()
    print(f'Button "EXPLORE NOW" is clickable, URL is: {driver.current_url}')
    sleep(1)
    driver.back()
    for key, value in locators.social_media.items():
        assert driver.find_element(By.XPATH, f'//img[@name="{value}"]').is_displayed()
        sleep(1)
        driver.find_element(By.XPATH, f'//img[@name="{value}"]').click()
        sleep(1)
        # close tab
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        print(f'{key} page URL: {driver.current_url}')
        driver.close()
        driver.switch_to.window(tabs[0])


def check_contact_us_form(driver, email):
    print('---------- Check CONTACT US form ----------')
    dropdown_category = Select(driver.find_element(By.NAME, 'categoryListboxContactUs'))
    dropdown_category.select_by_visible_text('Laptops')
    sleep(1)
    dropdown_product = Select(driver.find_element(By.NAME, 'productListboxContactUs'))
    dropdown_product.select_by_index(1)
    driver.find_element(By.NAME, 'emailContactUs').send_keys(email)
    sleep(1)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys("Enter something..")
    sleep(1)
    driver.find_element(By.ID, 'send_btnundefined').click()
    sleep(1)
    assert driver.find_element(By.XPATH,
                               '//p[contains(.,"Thank you for contacting Advantage support.")]').is_displayed()
    print(
        'CONTACT US form successfully populate. "Thank you for contacting Advantage support" message was displayed!')
    go_to_homepage(driver)


def delete_user(username, password, full_name, driver):
    print('---------- Delete Account ----------')
    driver.find_element(By.LINK_TEXT, username).click()
    sleep(1)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"My account")]').click()
    sleep(1)
    print('Check if full name is correct in account details!')
    sleep(1)
    full_name_displayed = driver.find_element(By.XPATH,
                                              '//div[@id="myAccountContainer"]//div[@class="borderBox"][1]//label[@class="ng-binding"]').text
    sleep(2)
    assert full_name_displayed == full_name
    print(f'Yes, full name "{full_name}" is correct. You can delete the account!')
    sleep(2)
    # delete_btn = driver.find_element(By.CLASS_NAME, 'deleteBtnText')
    driver.find_element(By.XPATH,
                        '//div[@id="myAccountContainer"]//button[@ class ="deleteMainBtnContainer a-button ng-scope"]/'
                        'div[@class ="deleteBtnText"]').click()
    sleep(2)
    # driver.execute_script("arguments[0].click();", delete_btn)
    # sleep(1)
    yes = driver.find_element(By.CLASS_NAME, 'deleteBtnContainer')
    sleep(3)
    yes.find_element(By.CLASS_NAME, 'deletePopupBtn').click()
    sleep(1)
    print(f'Try to log in with deleted account username: "{username}" and password: "{password}"!')
    sleep(2)
    driver.find_element(By.ID, "hrefUserIcon").click()
    sleep(2)
    driver.find_element(By.NAME, 'username').send_keys(username)
    sleep(1)
    driver.find_element(By.NAME, 'password').send_keys(password)
    sleep(3)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(1)
    signin_msg = driver.find_element(By.XPATH, '//div[@class="login ng-scope"]/label[@id="signInResultMessage"]').text
    sleep(1)
    assert signin_msg == 'Incorrect user name or password.'
    sleep(2)
    driver.find_element(By.XPATH,
                        '//div[@class="PopUp"]//div[@class="closeBtn loginPopUpCloseBtn"]').click()
    print('Message "Incorrect user name or password message" is displayed.')
    print('Account successfully deleted!')
    go_to_homepage(driver)


def checkout_shopping_cart(full_name, username, password, phone_number, driver):
    print('---------- Click on product and add the product to shopping cart ----------')
    print(f'Find the first product from the popular items section on home page and add it to the shopping cart ')
    driver.find_element(By.XPATH,
                        '//article[@id="popular_items"]//div[@class="ng-scope"][1]/a/label[contains(.,"View Details")]').click()
    sleep(1)
    selected_product_name = driver.find_element(By.XPATH, '//div[@id="Description"]/h1').text
    print(f'Your selected product is: "{selected_product_name}"!')
    driver.find_element(By.NAME, 'save_to_cart').click()
    sleep(1)
    driver.find_element(By.ID, 'shoppingCartLink').click()
    sleep(1)
    driver.find_element(By.ID, 'checkOutButton').click()
    sleep(1)
    print(f'Validate if full name: "{full_name}" and product: "{selected_product_name}" are correct in order payment')
    assert driver.find_element(By.XPATH, f'//div[@id="userDetails"]/div/label[contains(.,"{full_name}")]')
    sleep(1)
    displayed_product_text = driver.find_element(By.XPATH, '//div[@id="userCart"]//h3[@class="ng-binding"]').text
    sleep(1)
    assert displayed_product_text == selected_product_name
    print('Full name and product are correct, you can continue to payment method!')
    sleep(1)
    driver.find_element(By.ID, 'next_btn').click()
    sleep(1)
    driver.find_element(By.NAME, 'safepay_username').send_keys(username)
    sleep(1)
    driver.find_element(By.NAME, 'safepay_password').send_keys(password)
    sleep(1)
    driver.find_element(By.ID, 'pay_now_btn_SAFEPAY').click()
    sleep(1)
    print('Check the phone number!')
    sleep(1)
    order_phone_number = driver.find_element(By.XPATH, '//div[@id="orderPaymentSuccess"]//div[@class="innerSeccion"]'
                                                       '[3]/label[@class="ng-binding"]').text
    sleep(2)
    assert order_phone_number == phone_number
    print(f'Phone number is correct! Order phone number: {order_phone_number}, your number:{phone_number}')
    sleep(1)
    assert driver.find_element(By.XPATH, '//span[contains(.,"Thank you for buying with Advantage")]').is_displayed()
    sleep(1)
    assert driver.find_element(By.ID, 'trackingNumberLabel').is_displayed()
    t_number = driver.find_element(By.ID, 'trackingNumberLabel').text
    sleep(1)
    assert driver.find_element(By.ID, 'orderNumberLabel').is_displayed()
    sleep(1)
    o_number = driver.find_element(By.ID, 'orderNumberLabel').text
    print('Message: "Thank you for buying with Advantage" is displayed!')
    print(f'Thank you, {full_name}, your order is successful! Your order number is: {o_number} and '
          f'your tracking number is: {t_number}')
    go_to_homepage(driver)


def user_menu_validation(full_name, username, driver):
    print('---------- User Menu Validation ----------')
    driver.find_element(By.LINK_TEXT, username).click()
    sleep(1)
    print('Validate if there is no order in my orders!')
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"My orders")]').click()
    sleep(1)
    assert driver.find_element(By.XPATH, '//label[contains(.," - No orders - ")]')
    print('Yes, "no orders" text is displayed in your orders')
    print('Go to my account and validate the full name!')
    sleep(1)
    driver.find_element(By.LINK_TEXT, username).click()
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"My account")]').click()
    sleep(1)
    fullname_displayed = driver.find_element(By.XPATH,
                                             '//div[@id="myAccountContainer"]//div[1]/label[@class="ng-binding"]').text
    assert fullname_displayed == full_name
    print('Yes, full name is correct: "Jessica Arellano" is displayed in Account details!')
    go_to_homepage(driver)


def go_to_homepage(driver):
    driver.find_element(By.XPATH, '//a[@href="#/"]').click()
