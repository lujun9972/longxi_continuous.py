import urllib2
import splinter
import time

def longxi_timeout_p (url):
    '''判断longxi认证是否已到期,到期了则返回认证的url地址,否则返回None'''
    response = urllib2.urlopen(url)
    if url != response.geturl():
        return response.geturl()
    else:
        return None

def longxi_continuous (passwd,interval=300):
    '''longxi到期后,自动重新认证'''
    browser = splinter.Browser("firefox")
    while True:
        longxi_login_url = longxi_timeout_p("http://www.baidu.com")
        if longxi_login_url:
            browser.visit(longxi_login_url)
            browser.fill()

        time.sleep(interval)
