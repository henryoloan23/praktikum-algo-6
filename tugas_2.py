hitung = 0
jawab = 'y'

while jawab == 'y':
    bulan = int(input('Bulan apa (1-12): '))
    jawab = str(input('confirm? '))
    
                       
    
    def hitung_bulan():
        if (bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12):
            print('Hari = 31')
        
        elif (bulan == 2):
            tahun = int(input('Tahun berapa: '))
            if (tahun % 4 == 0 and bulan == 2):
                print('Hari = 29')
                return
            else:
                print('Hari = 28')
        
        elif (bulan > 12):
            print('Invalid input')
            
        elif (bulan == 0):
            print('Terimakasih telah menggunakan program ini 😊')
            
        else:
            print('Hari = 30')
            
        print('Ketik 0 untuk menghentikan program')

    hitung_bulan()
        