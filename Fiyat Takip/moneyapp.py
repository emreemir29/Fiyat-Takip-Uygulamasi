from types import BuiltinMethodType
import requests
import smtplib
import time
from bs4 import BeautifulSoup


url = 'https://www.hepsiburada.com/hous-mobilya-tokyo-acik-ceviz-renk-raf-tasarim-ahsap-kitaplik-p-HBCV000003BHF4'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

def check_price():
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='product-name').get_text().strip()
    print(f'Ürünün Adı: {title}')
    span = soup.find(id='offering-price')
    content = span.attrs.get('content')
    price = float(content)
    print(f'Ürünün Fiyatı: {price}')   
    if price < 2079:
        send_mail(title)
        


def send_mail(title):
    sender = 'emreemir352935@gmail.com'
    receiver = 'emreemir353529@gmail.com'
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(sender, 'cdzaqxrqawzokbgy')
        subject = title + 'istedigin fiyata dustu'
        body = 'Bu linkten gidebilirsin ->' + url
        mailContent = f'To:{receiver}\n From:{sender}\nSubject:{subject}\n\n{body}'
        server.sendmail(sender,receiver,mailContent)
        print('Mail Gönderildi.')
    except smtplib.SMTPException as e:
        print(e)
    finally:
        server.quit()
while(1):
     check_price()
     time.sleep(60*60)