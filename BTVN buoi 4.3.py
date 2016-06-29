##bai 5.1
##from turtle import*
##def draw_square(n,a):
##    for i in range(n):
##        forward(100)
##        left(360/n)
##        color(a)
##n=int(input("So canh: "))
##a=str(input("Mau sac: "))
##draw_square(n,a)


##for i in range(30):
##    draw_square(i*5,'red')
##    left(17)
##    penup()
##    forward(i*2)
##    pendown()


def remove_dollar_sign(str):
    s = str(input("Nhap vao 1 day "))
    print (s.replace("$", ""))
remove_dollar_sign(str)
    
