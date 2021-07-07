import os,json,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# =================================================================
# ==customize this==：
chromedriver = 'chromedriver.exe'
# =================================================================

def prepare_for_printing():
     chrome_options = webdriver.ChromeOptions()

     settings = {
         "recentDestinations": [{
             "id": "Save as PDF",
             "origin": "local",
             "account": ""
         }],
         "selectedDestinationId": "Save as PDF",
         "version": 2,
         "isHeaderFooterEnabled": False,

         # "customMargins": {},
         # "marginsType": 2,
         # "scaling": 100,
         # "scalingType": 3,
         # "scalingTypePdf": 3,
         "isLandscapeEnabled":False,#landscape横向，portrait 纵向，若不设置该参数，默认纵向
         "isCssBackgroundEnabled": True,
         "mediaSize": {
             "height_microns": 297000,
             "name": "ISO_A4",
             "width_microns": 210000,
             "custom_display_name": "A4 210 x 297 mm"
         },
     }

     chrome_options.add_argument('--enable-print-browser')
     #chrome_options.add_argument('--headless') #headless模式下，浏览器窗口不可见，可提高效率
     # =================================================================
     chrome_options.add_argument("load-extension=C:/Users/admin/AppData/Local/Google/Chrome/User Data/Default/Extensions/blablabla/1.1.1");
     # ==You need customize this too==
     # =================================================================


     prefs = {
         'printing.print_preview_sticky_settings.appState': json.dumps(settings),
         'savefile.default_directory': 'C:\\pdf' #此处填写你希望文件保存的路径
     }
     # and this again(Where you want to store your pdf files)
     # ================================================================
     chrome_options.add_argument('--kiosk-printing') #静默打印，无需用户点击打印页面的确定按钮
     chrome_options.add_experimental_option('prefs', prefs)


     driver = webdriver.Chrome(chromedriver, options=chrome_options)
     return driver

def load_urls(filename):
     url_prefix = 'https://plato.stanford.edu/'
     urls = []
     with open(filename,'r',encoding='utf8') as f:
          lines = f.readlines()
          for line in lines:
               url = {}
               k,v = line.split('\t')
               url[k] = url_prefix + v
               urls.append(url)
     return urls


def load_user_css():
     driver.maximize_window()
     # css = 'https://cdn.jsdelivr.net/gh/AlainAlan/SEP-style@main/index.user.css'
     css = 'https://raw.githubusercontent.com/AlainAlan/SEP-style/main/index.user.css'
     # 先应用用户css
     driver.get(css)
     time.sleep(8)


def print_it(url,number):
     driver.get(url)
     time.sleep(2)
     driver.find_element_by_xpath('//body').send_keys(Keys.END)
     time.sleep(1)
     driver.find_element_by_xpath('//body').send_keys(Keys.END)
     time.sleep(1)
     driver.find_element_by_xpath('//body').send_keys(Keys.HOME)
     time.sleep(1)
# https://stackoverflow.com/questions/30937153/selenium-send-keys-what-element-should-i-use
#      head = driver.find_element_by_xpath('//*[@id="aueditable"]/h1')
     head = driver.find_element_by_xpath('//*/h1')
     pdfname = str(number) + ' ' + head.text + '.pdf'
     print(pdfname)
     script_here = "document.title='" + pdfname + "';window.print();"
     driver.execute_script(script_here) #利用js修改网页的title，该title最终就是PDF文件名，利用js的window.print可以快速调出浏览器打印窗口，避免使用热键ctrl+P


def get_last():
     last = 1110

     path = 'C:\\pdf'
     # and here again
     # =================================================================

     for file in os.listdir(path):
          if os.path.isfile(os.path.join(path,file))==True:
               if file.endswith('.pdf'):
                    num_of_this_file = file[0:4]
                    if int(num_of_this_file) > last:
                         last = int(num_of_this_file)
     return(last)


driver = prepare_for_printing()
urls = load_urls('sum2021urls.txt')
load_user_css()

number = get_last() + 1

# from 1st entry to 1000th (e.g.)
for u in urls[0:1000]:
     for k,v in u.items():
          print_it(v,number)
          number += 1
          time.sleep(20)

## For single entry, use this:
# for k,v in urls[4].items():
#      print_it(v,number)


driver.close()

# References:
# https://www.cnblogs.com/new-june/p/14509601.html
# https://blog.csdn.net/zbj18314469395/article/details/89227986
# https://stackoverflow.com/questions/56897041/how-to-save-opened-page-as-pdf-in-selenium-python
# https://www.programmersought.com/article/32776623042/

