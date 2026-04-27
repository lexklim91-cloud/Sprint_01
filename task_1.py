str_time = '1h 45m,360s,25m,30m 120s,2h 60s'

#str_time = str_time.replace('s', '/60').replace('h','*60').replace('m','').replace(' ', '+')
str_time = str_time.replace(' ', ',')
lst_time = str_time.split(',')
h = 0 # часы
m = 0 # минуты
s = 0 # секунды

for t in lst_time:
    if t[-1] =='m':
        m += int(t.replace('m', ''))  
    elif t[-1] =='s':
        s += int(t.replace('s', ''))     
    else :
        h += int(t.replace('h', ''))
        
sum_time = h*60 + m + s/60
        
print("Итого: "+str(sum_time) +" минут")
