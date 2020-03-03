import time
from robobrowser import RoboBrowser

br = RoboBrowser()

while True:
    br.open("https://login.ufpi.br:6082/php/uid.php?vsys=1&rule=0&url=http://conecta.ufpi.br%2f")

    #print(str(br.parsed()))

    form = br.get_form("login_form")
    form['user'] = "sirwez"
    form['passwd'] = "weslley12"
    br.submit_form(form)
    #src = str(br.parsed())

    #start = src.find('id="notificationsCountValue"')
    #numberOfNotifications = src[start:start + 40]

    print(time.ctime() + ": autenticando...")

    time.sleep(1800)
