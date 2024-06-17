def multiplication_table(a):
    for i in range(1,15+1):
        print(f" {a} x{i:3} ={a*i:5}")

num=int(input("Which table you want? "))
multiplication_table(num)