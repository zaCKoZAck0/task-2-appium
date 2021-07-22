from appium import webdriver
from time import sleep
desired_cap = {
  "deviceName": "emulator-5554",
  "platformName": "android",
  "appPackage": "com.ATG.World",
  "appActivity": "com.atg.world.activity.SplashActivity",
  "noReset": True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

def test_LoginWithRightCredential():
       getStartedTv = driver.find_element_by_id("com.ATG.World:id/getStartedTv")
       getStartedTv.click()
       sleep(2)
       login_email = driver.find_element_by_id("com.ATG.World:id/login_email")
       login_email.click()
       sleep(2)
       email = driver.find_element_by_id("com.ATG.World:id/email")
       email.send_keys('wiz_saurabh@rediffmail.com')
       password = driver.find_element_by_id("com.ATG.World:id/password")
       password.send_keys('Pass@123')
       signin = driver.find_element_by_id("com.ATG.World:id/email_sign_in_button")
       signin.click()
       print("test_LoginWithRightCredential passed")
'''
test_LoginWithRightCredential()
sleep(2)'''

def goto_image_fab_clicked():
    fab = driver.find_element_by_id("com.ATG.World:id/fab")
    fab.click()
    sleep(2)
    image_fab_clicked = driver.find_element_by_id("com.ATG.World:id/image_fab_clicked")
    image_fab_clicked.click()
    print("goto_image_fab_clicked passed")

goto_image_fab_clicked()

#TC#1
def camera_upload_test():
    camera_upload = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]")
    camera_upload.click()
    sleep(2)

    options = driver.find_element_by_id("com.android.camera2:id/mode_options_toggle")
    options.click()
    sleep(2)

    toggle_button = driver.find_element_by_id("com.android.camera2:id/camera_toggle_button")
    toggle_button.click()
    sleep(2)

    shutter = driver.find_element_by_id("com.android.camera2:id/shutter_button")
    shutter.click()
    sleep(2)

    done_button = driver.find_element_by_id("com.android.camera2:id/done_button")
    done_button.click()
    sleep(2)

    postCaption = driver.find_element_by_id("com.ATG.World:id/postCaption")
    postCaption.send_keys("Test Caption")
    sleep(2)

    post_action = driver.find_element_by_id("com.ATG.World:id/toolbar_post_action")
    post_action.click()

camera_upload_test()
print("TC#1 Sucessfull")

#TC#2
'''
photo_xcode = '//android.view.ViewGroup[@content-desc="Photo taken on Jul 22, 2021 9:18:07 AM"]'
camera_upload = driver.find_element_by_id("android:id/text1")
camera_upload.click()
gallery = driver.find_elements_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout")
gallery[1].click()
photo = driver.find_element_by_xpath(photo_xcode)
photo.click()
postCaption = driver.find_element_by_id("com.ATG.World:id/postCaption")
postCaption.send_keys("Test Caption")
post_action = driver.find_element_by_id("com.ATG.World:id/toolbar_post_action")
post_action.click()'''
