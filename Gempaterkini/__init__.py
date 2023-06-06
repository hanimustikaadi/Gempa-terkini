import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    """
    Tanggal : 14 Mei 2023,
    Waktu 22:32:21 WIB
    Magnitudo 5.9
    kedalaman 109 km
    Lokasi 0.49 LU - 126.90 BT
    Pusat Gempa 60 km BaratDaya TERNATE-MALUT
    tidak berpotensi TSUNAMI
    """
    try:
      content = requests.get('https://www.bmkg.go.id/')
    except Exception:
          return  None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text,'html.parser')
        result = soup.find('span', {'class':'waktu'})
        result = result.text.split(', ')
        waktu = result[1]
        tanggal = result[0]
        result1 = soup.find('div',{'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result= result1.findChildren('li')
        i=0
        magnitudo = None
        Kedalaman = None
        ls = None
        bt = None
        lokasi =None
        dirasakan = None
        for res in result:
            print(i, res)
            if i == 1:
                magnitudo = res.text
            elif i == 2 :
                kedalaman = res.text
            elif i == 3 :
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4 :
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text

            i = i + 1




        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'LS': ls, 'BT': bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan
        return hasil


def tampilkan_data(result):
    if result is None:
        print('tidak bisa menemukan data gempa terkini')
        return

    print('Gempa terakhir berdasarkan BMKG')
    print(f"tanggal {result['tanggal']}")
    print(f"waktu {result['waktu']}")
    print(f"magnitudo {result['magnitudo']}")
    print(f"kedalaman {result['kedalaman']}")
    print(f"lokasi {result['lokasi']}")
    print(f"koordinat: LS= {result['koordinat']['LS']},BT= {result['koordinat']['BT']}")
    print(f"dirasakan {result['dirasakan']}")