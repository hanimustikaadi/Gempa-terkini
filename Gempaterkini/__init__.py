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

    hasil = dict()
    hasil['tanggal'] = '14 Mei 2023'
    hasil['waktu'] = '22:32:21 WIB'
    hasil['magnitudo'] = 4.0
    hasil['lokasi'] = {'LS': 1.48, 'BT': 134.01}
    hasil['pusat'] = 'pusat gempa berada di darat 18 km barat laut '
    hasil['dirasakan'] = 'dirasakan skala MMI'
    return hasil


def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"tanggal {result['tanggal']}")
    print(f"waktu {result['waktu']}")
    print(f"magnitudo {result['magnitudo']}")
    print(f"lokasi: LS= {result['lokasi']['LS']},BT= {result['lokasi']['BT']}")
    print(f"pusat {result['pusat']}")
    print(f"dirasakan {result['dirasakan']}")