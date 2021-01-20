import time
from creds import *
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

opt = Options()
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
})


def markPresent(caption, driver):
    # WHEN THESE WORDS ARE TRIGGERED A MESSAGE WILL BE SENT
    alertWords = ['46', '48', '49', '51']
    for word in caption:
        if word.text in alertWords:
            textArea = driver.find_element_by_xpath(
                '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea')
            textArea.send_keys('47')
            textArea.send_keys(Keys.ENTER)
            return True
    return False


def joinClass(url):
    try:
        driver = webdriver.Chrome(
            options=opt, executable_path='./chrome-driver/chromedriver.exe')
        driver.get('https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&_ga=2.231960408.632926866.1609170216-2046473962.1609170216&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

        # Logs you in
        username = driver.find_element_by_id('identifierId')
        username.click()
        username.send_keys(email)

        next = driver.find_element_by_xpath(
            '//*[@id="identifierNext"]/div/button/div[2]')
        next.click()
        time.sleep(4)
        password = driver.find_element_by_xpath(
            '//*[@id="password"]/div[1]/div/div[1]/input')
        password.click()
        password.send_keys(pword)
        next = driver.find_element_by_xpath(
            '//*[@id="passwordNext"]/div/button/div[2]')
        next.click()
        time.sleep(4)
        driver.get(url)
        time.sleep(4)

        # turn off mic and camera
        turn_off_mic_action = ActionChains(driver)
        turn_off_mic_action.key_down(Keys.CONTROL).send_keys(
            "d").key_up(Keys.CONTROL).perform()
        turn_off_camera_action = ActionChains(driver)
        turn_off_camera_action.key_down(Keys.CONTROL).send_keys(
            "e").key_up(Keys.CONTROL).perform()

        # clicks join button
        join = driver.find_element_by_xpath(
            '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]')
        join.click()
        time.sleep(3)

        # turn on captions
        # driver.find_element_by_xpath(
        #     '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[3]/div[2]/div/span/span/div').click()

        # turn on chat sidebar
        driver.find_element_by_xpath(
            '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]').click()
        time.sleep(4)

        marked = False

        # Reads the text from chat sidebar
        while True:
            try:
                now = datetime.now()
                if now.minute >= 55:
                    driver.quit()
                    return
                else:
                    caption = driver.find_elements_by_class_name("oIy2qc")
                    if not marked:
                        marked = markPresent(caption, driver)
                    time.sleep(1)
            except:
                time.sleep(1)
    except:
        time.sleep(3)


meetMap = [
    {
        9: 'https://meet.google.com/poj-yjpp-yis',
        10: 'https://meet.google.com/xrx-mkiy-mgv',
        11: 'https://meet.google.com/xit-ywwq-vts',
        13: 'https://meet.google.com/vio-btth-vav',
        14: 'https://meet.google.com/xrx-mkiy-mgv',
        15: 'https://meet.google.com/pva-cygj-mzb',
        16: 'https://meet.google.com/qwd-qofp-pas'
    },
    {
        9: 'https://meet.google.com/teh-sqyn-uer',
        10: 'https://meet.google.com/hsu-jywi-wkr',
        11: 'https://meet.google.com/xrx-mkiy-mgv',
        13: 'https://meet.google.com/ond-ehxu-wdj',
        14: 'https://meet.google.com/xrx-mkiy-mgv',
        15: 'https://meet.google.com/ugp-wdwr-miu',
        16: 'https://meet.google.com/wbe-bvzg-jff'
    },
    {
        9: 'https://meet.google.com/xrx-mkiy-mgv',
        10: 'https://meet.google.com/xig-eaic-sqn',
        11: 'https://meet.google.com/xit-ywwq-vts',
        14: 'https://meet.google.com/tzw-bxif-zci',
        15: 'https://meet.google.com/pva-cygj-mzb',
        16: 'https://meet.google.com/xrx-mkiy-mgv'
    },
    {
        9: 'https://meet.google.com/xrx-mkiy-mgv',
        10: 'https://meet.google.com/yik-xwss-vjo',
        11: 'https://meet.google.com/xit-ywwq-vts',
        14: 'https://meet.google.com/whq-kczg-tek',
        15: 'https://meet.google.com/pva-cygj-mzb',
        16: 'https://meet.google.com/xrx-mkiy-mgv'
    },
    {
        9: 'https://meet.google.com/owq-ixnj-bjd',
        10: 'https://meet.google.com/xrx-mkiy-mgv',
        11: 'https://meet.google.com/pag-nruq-aws',
        13: 'https://meet.google.com/ygk-iytx-pqi',
        14: 'https://meet.google.com/xrx-mkiy-mgv',
        15: 'https://meet.google.com/zrk-uahj-ctn',
        16: 'https://meet.google.com/srd-ubqc-rwp'
    },
    {
        9: 'https://meet.google.com/owq-ixnj-bjd',
        10: 'https://meet.google.com/pon-whfz-tck',
        11: 'https://meet.google.com/xrx-mkiy-mgv',
        13: 'https://meet.google.com/mqc-zbcj-smt',
        14: 'https://meet.google.com/xrx-mkiy-mgv',
        15: 'https://meet.google.com/dun-nxzb-pmb',
        16: 'https://meet.google.com/fip-ygmk-snq'
    }
]


def currentClass():
    now = datetime.now()
    weekday = datetime.today().weekday()
    if weekday == 6 or now.hour not in meetMap[weekday]:
        return None
    return meetMap[weekday][now.hour]


while True:
    now = datetime.now()
    if now.hour >= 17:
        quit()
    elif currentClass() != None and now.minute > 5 and now.minute < 55:
        joinClass(currentClass())
    else:
        time.sleep(60)
