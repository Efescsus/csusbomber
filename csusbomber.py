import concurrent.futures
import requests

# Kullanıcıdan telefon numarasını al
phone_number = input("Lütfen telefon numarasını girin: ")

# Hedef URL'ler
urls = ['https://www.kahvedunyasi.com/kayit-ol', 'https://www.jumbo.com.tr/users/register/', 'https://www.tiklagelsin.com/a/']

# POST işlemini yapan işlev
def post_form(url):
    form_data = {
        'phone_number': phone_number,
        # 'password': 'parola'  # Parolayı uygun şekilde güncelleyin
    }
    response = requests.post(url, data=form_data)
    return (url, response.status_code)

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(post_form, urls)

for url, status_code in results:
    if status_code == 200:
        print(f'Form gönderimi başarılı: {url}')
    else:
        print(f'Form gönderimi başarısız: {url}')
