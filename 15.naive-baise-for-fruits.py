
typ_col=[]
lon_col=[]
n_lon_col=[]
swt_col=[]
n_swt_col=[]
yell_col=[]
n_yell_col=[]
total_col=[]

d_set=int(input("Enter number of data in dataset:"))
n=int(input("Eneter total fruits:"))

for i in range(n):
    typ=input("Enter fruits type:")
    typ_col.append(typ.lower())
    lon=int(input("Enter long fruits:"))
    lon_col.append(lon)
    n_lon=int(input("Enter not long fruits:"))
    n_lon_col.append(n_lon)
    swt=int(input("Enter sweet fruits:"))
    swt_col.append(swt)
    n_swt=int(input("Enter not sweet fruits:"))
    n_swt_col.append(n_swt)
    yell=int(input("Enter yellow fruits:"))
    yell_col.append(yell)
    n_yell=int(input("Enter not yellow fruits:"))
    n_yell_col.append(n_yell)
    total=int(input("Enter total fruits:"))
    total_col.append(total)

p_banana,p_orange,p_other=0,0,0

for i in range(n):
    if typ_col[i]=="banana":
        p_banana=total_col[i]/d_set
        p_long_b=lon_col[i]/total_col[i]
        p_sweet_b=swt_col[i]/total_col[i]
        p_yell_b=yell_col[i]/total_col[i]

    elif typ_col[i]=="orange":
        p_orange=total_col[i]/d_set
        p_long_o=lon_col[i]/total_col[i]
        p_sweet_o=swt_col[i]/total_col[i]
        p_yell_o=yell_col[i]/total_col[i]

    elif typ_col[i]=="other":
        p_other=total_col[i]/d_set
        p_long_other=lon_col[i]/total_col[i]
        p_sweet_other=swt_col[i]/total_col[i]
        p_yell_other=yell_col[i]/total_col[i]


p_fruits_b=p_long_b*p_sweet_b*p_yell_b
p_fruits_o=p_long_o*p_sweet_o*p_yell_o
p_fruits_other=p_long_other*p_sweet_other*p_yell_other

new_fruit=max(p_fruits_b,p_fruits_o,p_fruits_other)


if new_fruit==p_fruits_b:
    print("========New fruit will be banana==========")
elif new_fruit==p_fruits_o:
    print("=========New fruit will be orange=======")
else:
    print("======new fruits will be other fruits=======")




