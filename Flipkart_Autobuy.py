#Tulsipada Das
#Dr. android Guruji
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, winsound
from configparser import RawConfigParser
from colorama import Fore, init, deinit
init()
CONFIG = RawConfigParser()
CONFIG.read('config.ini')
driver_path = CONFIG.get('MAIN', 'DRIVER_LOCATION')
email_inp = CONFIG.get('CREDENTIALS', 'USERNAME')
pass_inp = CONFIG.get('CREDENTIALS', 'PASSWORD')
order_link = CONFIG.get('ORDER', 'LINK')
cvv_inp = CONFIG.get('ORDER', 'CVV')
addr_input = CONFIG.get('ORDER', 'ADDRESS')
pay_opt_input = CONFIG.get('ORDER', 'PAYMENT')
bankname_input = CONFIG.get('EMIOPTIONS', 'BANK')
tenure_input = CONFIG.get('EMIOPTIONS', 'TENURE')
frequency = 2500
duration = 2000

def prCyan(skk):
    print(Fore.CYAN + skk)


def prRed(skk):
    print(Fore.RED + skk)


def prGreen(skk):
    print(Fore.GREEN + skk)


def prYellow(skk):
    print(Fore.YELLOW + skk)


url = order_link
prRed('Opening Link in chrome..........')
prCyan('\n')
print('\nLogging in with username:', email_inp)
prYellow('\n')
if pay_opt_input == 'EMI_OPTIONS':
    print('\nEMI Option Selected. \nBANK:', bankname_input, '\nTENURE:', tenure_input, '\n')
else:
    if pay_opt_input == 'PHONEPE':
        print('\nPayment with Phonepe\n')
    else:
        if pay_opt_input == 'NET_OPTIONS':
            print('\nNet Banking Payment Selected\n')
        else:
            if pay_opt_input == 'COD':
                prGreen('COD selected\n')
            else:
                print('\nFull Payment Selected\n')
driver = webdriver.Chrome(driver_path)
driver.maximize_window()
driver.get(url)
prCyan('\n')
input('Confirm Payment Details above, Product Details on Browser & Press Enter to proceed.')

def login():
    try:
        prYellow('Logging In..\n')
        try:
            login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '._3Ep39l')))
            prYellow('Login Button Clickable\n')
        except:
            prYellow('Login Button Not Clickable\n')
        login.click()
        prYellow('Login Button Clicked Successfully\n')
    except:
        prRed('login Failed. Retrying.')
        time.sleep(0.5)
        login()


def login_submit():
    try:
        if 'Enter Password' in driver.page_source:
            print('Trying Usual method of Login.')
            email = driver.find_element_by_css_selector('.Km0IJL ._2zrpKA')
            passd = driver.find_element_by_css_selector('.Km0IJL ._3v41xv')
            email.clear()
            passd.clear()
            email.send_keys(email_inp)
            passd.send_keys(pass_inp)
            try:
                form = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.Km0IJL ._7UHT_c')))
                prCyan('Submit Button Clickable')
            except:
                prRed('Submit Button Not Clickable')
            else:
                form.click()
                prYellow('\nPress any key when login is done and your name appeares in menu bar.')
                input()
                prGreen('\nLogged in successully.')
    except:
        if 'Login &amp; Signup' not in driver.page_source and 'Login & Signup' not in driver.page_source:
            print('Logged in Manually.')
        else:
            prRed('login_submit Failed. Please login manually.')
            time.sleep(1)
            login_submit()


def buy_check():
    try:
        nobuyoption = True
        while nobuyoption:
            try:
                driver.refresh()
                time.sleep(0.2)
                buyprod = driver.find_element_by_css_selector('._1k1QCg ._7UHT_c')
                prYellow('Buy Button Clickable')
                nobuyoption = False
            except:
                nobuyoption = True
                prRed('Buy Button Not Clickable')

        buyprod.click()
        prYellow('Buy Button Clicked Successfully')
        buy_recheck()
    except:
        prRed('buy_check Failed. Retrying.')
        time.sleep(0.5)
        buy_check()


def buy_recheck():
    try:
        WebDriverWait(driver, 4).until(EC.title_contains('Secure Payment'))
        prYellow('Redirected to Payment')
    except:
        prRed('Error in Redirecting to Payment')
        time.sleep(0.5)
        buy_recheck()


def deliver_option():
    try:
        addr_input_final = "//label[@for='" + addr_input + "']"
        try:
            sel_addr = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, addr_input_final)))
            prYellow('Address Selection Button Clickable')
        except:
            prRed('Address Selection Button Not Clickable')
        else:
            sel_addr.click()
            prYellow('Address Selection Button Clicked Successfully')
    except:
        prRed('deliver_option Failed. Retrying.')


def deliver_continue():
    try:
        addr_sal_avl = True
        while addr_sal_avl:
            try:
                address_sel = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '._3K1hJZ ._7UHT_c')))
                address_sel.click()
                addr_sal_avl = False
                print('Address Delivery Button Clickable')
            except:
                addr_sal_avl = True
                winsound.Beep(frequency, duration)
                print('Address Delivery Button Not Clickable')

        print('Address Delivery Button Clicked Successfully')
    except:
        print('deliver_continue Failed. Retrying.')


def order_summary_continue():
    try:
        press_continue = driver.find_element_by_css_selector('._2Q4i61')
        press_continue.click()
        prYellow('Continue Button Clicked Successfully')
    except:
        prRed('order_summary_continue Failed. Retrying.')


def choose_payment():
    try:
        pay_opt_input_final = "//label[@for='" + pay_opt_input + "']"
        pay_method_sel = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, pay_opt_input_final)))
        pay_method_sel.click()
        if pay_opt_input == 'COD':
            cod_captcha()
        else:
            if pay_opt_input == 'PHONEPE':
                phonepe()
            else:
                prGreen('\nCard selected...')
                payment_cvv()
                payment_continue()
                otp_submit()
        prGreen('Payment Method Selected Successfully')
        winsound.Beep(frequency, duration)
    except:
        prRed('choose_payment Failed. Retrying.')
        time.sleep(0.5)
        choose_payment()


def cod_captcha():
    try:
        payment_sel = None
        payment_sel = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._16qL6K')))
        payment_sel.clear()
        prYellow('Type the captcha here:')
        capText = input()
        payment_sel.send_keys(capText)
        prGreen('\nCaptcha entered successfully.')
        prYellow('\nClicking Confirm Button order:')
        confirm_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._7UHT_c')))
        confirm_btn.click()
        prGreen('\nOrder confirmed successfully')
    except:
        prRed('\nCaptcha could not be entered. Plese type manually on webpage.')


def phonepe():
    try:
        upi = 'amitsaxena098@paytm'
        prYellow('Continuing with phonepe...')
        phonepe_con = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._7UHT_c')))
        phonepe_con.click()
        prYellow('Choose QR code mode for quicker payment')
    except:
        prRed('Could not enter number')


def payment_cvv():
    try:
        payment_sel = None
        payment_sel = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._16qL6K')))
        payment_sel.clear()
        payment_sel.send_keys(cvv_inp)
        print('CVV Entered:' + cvv_inp)
    except:
        print('payment_cvv Failed. Retrying.')


def payment_continue():
    try:
        pay = None
        try:
            pay = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._3K1hJZ ._7UHT_c')))
            print('Pay Button Clickable')
        except:
            print('Pay Button Not Clickable')
        else:
            pay.click()
            print('Pay Button Clicked Successfully')
    except:
        print('payment_continue Failed. Retrying.')


def otp_submit():
    try:
        otp = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._3K1hJZ .l5dwor')))
        otp.clear()
        print('Please enter OTP here:')
        otp_input = input()
        otp.send_keys(otp_input)
        submit_otp = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._3K1hJZ ._7UHT_c')))
        submit_otp.click()
        print('OTP Submitted Successfully')
    except:
        print('otp_submit Failed. Retrying.')
        time.sleep(0.5)
        otp_submit()


def try_till_otp():
    login()
    login_submit()
    buy_check()
    order_summary_continue()
    choose_payment()


if __name__ == '__main__':
    try_till_otp()