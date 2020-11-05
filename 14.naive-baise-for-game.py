
weather_tbl=[] #for weather
play_tbl=[] #for play

n=int(input("Enter number of dataset:"))

for i in range(n):
    weather=input("Enter weather name:")
    weather_tbl.append(weather.lower())
    play=input("Enter paly or not:")
    play_tbl.append(play.lower())



t_rainy_y=t_rainy_n=0
t_y=t_n=0
t_rainy=0

for i in range(n):
    if play_tbl[i]=="yes":
        t_y +=1
    else:
        t_n +=1
    if weather_tbl[i]=="rainy":
        t_rainy +=1
        if play_tbl[i]=="yes":
            t_rainy_y +=1
        else:
            t_rainy_n +=1

p_rainy_y=(t_rainy_y/t_y)
p_y=(t_y/n)
p_rainy=(t_rainy/n)
p_rainy_n=(t_rainy_n/t_n)
p_n=(t_n/n)

p_y_rainy=(p_rainy_y*p_y)/p_rainy
p_n_rainy=(p_rainy_n*p_n)/p_rainy

if p_n_rainy>p_y_rainy:
    print("Player will play,if it not rainy")
else:
    print("player will not play if it rainy")
