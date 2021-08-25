"""
This is a HEALTH MANAGEMENT SYSTEM project.
In this project:-
1. client_list is given {1:"SHREYANSHI",2:"ANURAG",3:"AYUSHI",4:"ABHINAV",5:"AWNI",6:"SHASHANK"} and when executed program  u
takes as input client name after input client name  u locked ur daily routine exercise and food and print the locked result with current locking time
"""
client_list={1:"SHREYANSHI",2:"ANURAG",3:"AYUSHI",4:"ABHINAV",5:"AWNI",6:"SHASHANK"}
log_list={1:"Exercise",2:"Diet"}
def getdate():
    import datetime
    return datetime.datetime.now()
try:
    print("Select Client Name:")
    for key, value in client_list.items():
        print("Press",key,"For",value,"\n",end="")
    client_name=int(input())
    print("Selected Client:",client_list[client_name],"\n",end="")
    print("Press 1 for log")
    print("Press 2 for retrieve")
    op=int(input())
    if op == 1:
        for key,value in log_list.items():
            print("Press",key,"to log ",value,"\n",end="")
        log_name=int(input())
        print("Selected Job:",log_list[log_name])
        f=open(client_list[client_name] +"_"+ log_list[log_name] + ".txt","a")
        k='y'
        while(k != "n"):
            print("Enter",log_list[log_name],"\n",end="")
            mytext=input()
            f.write("["+str(getdate())+"]:"+mytext+"\n")
            k=input("IF YOU WANT TO ADD MORE DETAIL PRESS y OTHERWISE PRESS n:")
            continue
        f.close()
    elif op == 2:
        for key,value in log_list.items():
            print("Press",key,"to retrieve",value,"\n",end="")
        log_name=int(input())
        print(client_list[client_name],"-",log_list[log_name],"Report:","\n",end="")
        f=open(client_list[client_name]+"_"+log_list[log_name]+".txt","rt")
        contents=f.readlines()
        for line in contents:
            print(line,end="")
        f.close()
    else:
        print("INNVALID INPUT!!!")
except Exception as e:
    print("Wrong Input !!!")
