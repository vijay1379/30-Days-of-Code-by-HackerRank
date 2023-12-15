n=int(input())
dict_list={}

for i in range(n):
    name=input()
    x = name.split(" ")
    dict_list[x[0]]=x[1]
while True:
    try:
        check=input()
    except:
        break
            
    if check in dict_list:
        print(check +'='+ dict_list[check])
    else:
        print("Not found")        
