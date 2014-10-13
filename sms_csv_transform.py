import os

android_file = 'android.csv'
trans_file = 'itools_trans_android.csv'

f_trans_file = open(trans_file,'w')
f_android = open(android_file)

c_android = f_android.readlines()
f_android.close()

def time_trans(android_time):
    items = android_time.split('.')
    year=items[0].strip()
    month = items[1].strip()
    if len(month) == 1:
        month = '0'+month
        
    items2 = items[2].strip()
    items3 = items2.split(':')
    part1 = items3[0].strip()
    part2 = items3[1].strip()
    part11 = part1.split(' ')

    date = part11[0].strip()
    if len(date) == 1:
        date = '0'+date
    if len(part11) == 3:
        hours = part11[2].strip()
    else:
        hours = part11[1].strip()
        
    if len(hours) == 1:
        hours = '0'+hours


    minitues =  part2
    if len(minitues) == 1:
        minitues = '0'+minitues

    seconds = '18'
    
    itools_date = year+'-'+month+'-'+date
    itools_time = hours+':'+minitues+':'+seconds
    itools_date_time = itools_date+' '+itools_time
    return itools_date_time
    


for line in c_android:
        line = line.strip()
        items = line.split(',')
        if len(items) == 8:
            sms_token = items[0].strip()
            send_received = items[1].strip()

            if send_received == 'deliver':
                io_state = 'recv'
                received_num = items[2].strip()
                received_name = items[3].strip()
            elif send_received == 'submit':
                io_state = 'send'
                received_name = items[2].strip()
                received_num = items[3].strip()
                
            blank1 = items[4].strip()
            time = items[5].strip()
            unknown = items[6].strip()
            sms_content = items[7].strip()

            itools_time_output = time_trans(time)

            #write transfered file
            f_trans_file.write(received_num+' ('+received_name+'),'+itools_time_output+','+sms_content+','+io_state+','+'read\n')
        
f_trans_file.close()


        
