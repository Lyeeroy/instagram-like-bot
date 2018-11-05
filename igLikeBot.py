from selenium import webdriver
from selenium.common.exceptions import *
import time

varusername = "username" #USERNAME
varpassw = "password" #PASSWORD

#----- CHANGE THOSE IF ERROR -----
#in background is 1 sec ideal
#under 0.6 sec it doesnt work well
#depends on your internet/computer performance!
#---------------------------------
sleepPerPicture = 1 #sec
sleepForPic = 1 #sec
#---------------------------------

class ig(object):
    def core(self):
        self.likes = 0
        print("*----------------------*")
        print('| via Facebook:    [1] |')
        print('| via Instagram:   [2] |')
        print("*----------------------*")
        self.via = input('log in via: ')
        print("*----------------------*")
        print('| likeforlikes:    [1] |')
        print('| likeforlikesback [2] |')
        print("*----------------------*")
        print('| Custom:          [3] |')
        print("*----------------------*")
        #Hashtags for inspiration: #likeforlike #likeforfollow #likeforalike #likeforlikes #likeforashoutout #likefortags #likeforlikeback #likeforafollow #likeforlikealways #likeforfollowers #likeforme #likeforcomment #likefortag #likeforashououtback #likeforfollows #likeforliketeam #likeforelike #like4like #likeforlikefromme #likeforfun #likeforlikesback #likeforshare #likeforlikeandfollow #likeforspam #likeforsshoutouts #like4follow #like4likes #like4shoutout #like4comment
        self.qht = input('hashtag: ')

        if self.qht == "1":
            self.ht = "likeforlikes"
        elif self.qht == "2":
            self.ht = "likeforlikesback"
        elif self.qht == "3":
            self.ht = input('#')
        else:
            quit()

        self.reloads = input('Reloads: ')
        self.likelimit = input('Likes per reload: ')
        time.sleep(0.2)
        print("*---------------------------*")
        print('| Reload * Likes =', int(self.reloads)*int(self.likelimit), 'likes |')
        print('| Remain: ', (int(self.reloads)*int(self.likelimit))*sleepPerPicture/60/60, ' Hours           |')
        print("*---------------------------*")
        self.driver = webdriver.Chrome()
        igmain.login()

    def login(self):
        if self.via == '1': #FB LOGIN
            self.driver.get("https://www.instagram.com/accounts/login")
            self.fblogin = self.driver.find_element_by_xpath("//span[@class='KPnG0']")
            self.fblogin.click()
            self.username = self.driver.find_element_by_id('email')
            self.passw = self.driver.find_element_by_id('pass')
            self.logbtn = self.driver.find_element_by_id('loginbutton')
            self.username.send_keys(varusername)
            self.passw.send_keys(varpassw)
            self.logbtn.click()
            time.sleep(1)
            try:
                self.continueas = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div/section/div/div/span[2]/a[1]/span/button') #DK why but ig asks you if you want to continue with your logged account..?
                self.continueas.click()
            except NoSuchElementException:
                pass
        elif self.via == '2': #IG LOGIN
            self.driver.get("https://www.instagram.com/accounts/login/")
            time.sleep(1)
            self.username = self.driver.find_element_by_name("username")
            self.passw = self.driver.find_element_by_name("password")
            self.logbtn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/button')
            self.username.send_keys(varusername)
            self.passw.send_keys(varpassw)
            self.logbtn.click()
            time.sleep(1)
            try:
                self.continueas = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div/section/div/div/span[2]/a[1]/span/button')
                self.continueas.click()
            except NoSuchElementException:
                pass
        else:
            quit()
    def main(self):
        try:
            self.driver.get("https://www.instagram.com/explore/tags/" + self.ht)
            self.clickphoto = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div')

            self.clickphoto.click()
            time.sleep(sleepForPic)
            for self.i in range(0, int(self.likelimit)):
                try:
                    self.like = self.driver.find_element_by_xpath("//span[@class='glyphsSpriteHeart__outline__24__grey_9 u-__7']") #LIKE BTN
                    self.next = self.driver.find_element_by_xpath("//a[@class='HBoOv coreSpriteRightPaginationArrow']") #NEXT BTN
                    self.likes = self.likes + 1
                    self.like.click()
                    if int((self.i) + 1) != int(self.likelimit): #MAKE SURE TO NOT CLICK 'NEXT' IF LAST PHOTO
                        self.next.click()
                    print('    - LIKES:', self.i + 1, '/', self.likelimit, '        RELOADS: ', self.l + 1, ' / ', self.reloads, '        TOTAL:', self.likes, '-')
                except NoSuchElementException:
                    self.i = self.i + 1
                time.sleep(sleepPerPicture)
        except NoSuchElementException:
            print('! Something is wrong !') #IF HE CANT FIND THE POHOTO, LIKE BUTTON OR NEXT BUTTON HE SAYS THIS
            pass
    def counts(self):
        for self.l in range(0, int(self.reloads)):
            print('                             ----- RE -----')
            igmain.main()
        print('----- COMPLETED -----')

if __name__ == "__main__":
    igmain = ig()
    igmain.core()
    igmain.counts()
