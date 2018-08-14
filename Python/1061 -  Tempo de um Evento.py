first_day = str(input()).split()
first_times = str(input()).split()
last_day = str(input()).split()
last_times = str(input()).split()

first_hour = int(first_times[0])
first_minute = int(first_times[2])
first_second = int(first_times[4])

last_hour = int(last_times[0])
last_minute = int(last_times[2])
last_second = int(last_times[4])


first_seg_tot = first_hour *3600 +  first_minute * 60 + first_second
last_seg_tot = last_hour *3600 +  last_minute * 60 + last_second

tot_seg = ((int(last_day[1]) - int(first_day[1]))*86400)+ last_seg_tot - first_seg_tot

print('{} dia(s)'.format(tot_seg//86400))
print('{} hora(s)'.format((tot_seg%86400)//3600))
print('{} minuto(s)'.format(((tot_seg%86400)%3600)//60))
print('{} segundo(s)'.format(((tot_seg%86400)%3600)%60))

