#global variabel
process = []
i = 1
test = 0
initiator = 0

# Mencari leader nilai value terbesar
def leaderElection(initiator):
    leader = 0
    j = 0
    test = initiator
    #Mengecek setiap value pada proses
    while 1:
        value = process[test-1][0]
        if(value >= leader): #jika ada yang lebih besar maka akan menjadi leader
            leader = value
        
        #Tahapan kondisi untuk menelusuri semua proses (Ring)
        test += 1
        if(test > temp):
            j = 1
            test = 1
        
        if(j == 1 and test == initiator):
            break
    
    return leader

#menulis ulang leader pada setiap proses
def overwriteMessage(initiator,leader):
    test = initiator
    j = 0
    while 1:
        #Overwrite proses leader
        process[test-1][1] = leader
        
        #Tahapan kondisi untuk menelusuri semua proses (Ring)
        test += 1
        if(test > temp):
            j = 1
            test = 1
        
        if(j == 1 and test == initiator):
            break

#Mulai program
print("Selamat Datang di Ring Election")
jumlah = int(input("Berapa proses yang ingin disimulasikan? "))
temp = jumlah

#Memasukkan value pada setiap proses
while temp > 0:
    print("Process "+str(i))
    value = int(input("Berapa value process? "))
    leader = 0
    process.append([value,leader])
    temp -= 1
    i += 1

#loop program
while 1:
    i = 1
    temp = jumlah
    print("Ring Election For "+ str(jumlah) +" Process")
    for data in process:
        print("Process "+ str(i) +" = Value ("+str(data[0])+") , Leader = ("+str(data[1])+")")
        i += 1
        
    #Pilih salah satu sebagai inisiator
    initiator = int(input("Pilih process sebagai initiator "))
    leader = leaderElection(initiator)
    overwriteMessage(initiator,leader)

    #Menampilkan hasil setiap proses sementara
    i = 1
    for data in process:
        print("Process "+ str(i) +" = Value ("+str(data[0])+") , Leader = ("+str(data[1])+")")
        i += 1

    #Memilih proses yang ingin failed
    failed = int(input("Pilih process yang ingin failed "))
    del process[failed-1]
    jumlah -= 1
    
    
