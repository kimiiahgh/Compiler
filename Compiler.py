#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:20:52 2019

@author: apple
"""

rs_table= [("while","WHILE"),("int","INTEGER"),("flt","FLOAT"),("if","IF"),("ar","Array"),("str","STRING"),("ch","CHAR"),
     ("in","INPUT"),("out","OUTPUT")]
rs =["while","int","flt","if","ar","str","ch","in","out"]

dl_op=[("::","ASSIGN"),("+","PLUS"),("-","MINUS"),("*","MULTIPLY"),("/","DIVIDED"),("&&","AND"),("||","OR"),("$","KH_Q"),
("%","PERCENTAGE"),("^","POWER"),("=","EQUALITY"),("!=","NOTSAME"),("<","LOWER"),(">","HIGHER"),
(">=","ELOWER"),("=<","EHIGHER"),("(","STARTIF"),(")","FINISHIF"),("{","START"),("}","FINISH"),("~","ELINE") , ("`" , "S_STRING_F")]
dlopt=["::","+","-","*","/","&&","||","$","%","^","=","!=","<",">",">=","=<","(",")","{","}","~" , "`"]
symbol = []
token=[]#return khorooji
x = input( "ENTER YOUR CODE" )
def tokenize(x):
    t = iter(x)
    n = len(x)
    flgcm = True
    flgnum=True
    temp_=10
    for i in range(0,n):
        symbol.append((0,0))
    count=0
    #print("length:"+str(l))
    while count<n:
        temp_=10
        a=next(t)
        count+=1
        asci=ord(a)
        if asci>=48 and asci<=57:
            num = int(a) #adad
            if(count<n):
                d=next(t)
                count = count +1
                if ord(d)==46:
                        flgnum=False
                        if count<n:
                            d= next(t)
                            count=count+1
                        else:
                         print("error")   
                        while 48<=ord(d)<=57:
                            num=num+(int(d)/temp_)
                            print(num)
                            temp_=temp_*10
                            if count<n:
                                d=next(t)
                                count=count+1
                            else:
                                break
                                flgnum=False
            else:
                if num==int(num):
                    symbol.append((num ,"INT"))
                    token.append((num ,"INT"))
                    flgnum=False
                else:
                    symbol.append((num ,"FLOAT"))
                    token.append((num ,"FLOAT"))
                    flgnum=False
                    
                continue
            while 48<=ord(d)<=57 and flgnum==True: #flgnum ezafi
                num= num*10+int(d)
                if count<n:
                    d = next(t)
                    count = count +1
                    #float
                    if ord(d)==46:
                        if count<n:
                            d= next(t)
                            count=count+1
                        else:
                         print("error")   
                        while 48<=ord(d)<=57:
                            num=num+(1/temp_)*int(d)
                            temp_=temp_*10
                            if count<n:
                                d=next(t)
                                count=count+1
                            else:
                                flgnum=False
                                break    
                else:
                    break
            if num==int(num):
                symbol.append((num ,"INT"))
                token.append((num ,"INT"))
            else:
                symbol.append((num ,"FLOAT"))
                token.append((num ,"FLOAT"))
        elif  90>=asci>=65 or 122>=asci>=97:
            word = a
            if(count<n):
                l=next(t)
                count = count +1
            else:
                #print(letter)
                if word in rs:
                    
                   indx=rs.index(word)
                   token.append((rs_table[indx][1],'RS'))
                else:
                    if word in symbol[:][1]:
                        token.append((symbol.index((word,'ID'))-n),'ID')
                    else:
                        symbol.append((word,'ID'))
                        token.append((symbol.index((word,'ID')),'ID'))
                continue
            while 48<=ord(l)<=57 or 65<= ord(l)<=90 or 97<= ord(l)<= 122:
                word = word+l
                if(count<n):
                    l=next(t)
                    count = count +1
                else:
                    break
            if word in rs:
                   indx=rs.index(word)
                   token.append(('RS',rs_table[indx][1]))
            else:
                    if word in symbol[:][1]:
                        token.append((symbol.index((word,'ID'))-n,'RS'))
                    else:
                        symbol.append((word,'ID'))
                        token.append((symbol.index((word,'ID'))-n,'ID'))
        elif 33<=asci<=47 or 58<=asci<=64 or 123<= asci <=126 or 91<=asci<=96 :
            dlop =a
            # #( , )# be manaye comment 
            if count<n:
                d=next(t)
                count = count +1
                if 33<=ord(d)<=47 or  58<=ord(d)<=64 or 123 <= ord(d)<=126 or  91<=ord(d) <= 96 :
                    dlop = dlop + d
                    if dlop in dlopt:
                        
                        indx=dlopt.index(dlop)
                        token.append(("DL_OP",dl_op[indx][1]))
                    elif dlop == "#(" :
                        while flgcm == True:
                            d=next(t)
                            count = count +1
                            if d== ")" :
                                d= next(t)
                                count = count + 1
                                if d=="#" :
                                    flgcm=False
                else :
                    if dlop in dlopt:
                        indx=dlopt.index(dlop)
                        token.append(("DL_OP",dl_op[indx][1])) 
            else:
                if dlop in dlopt:
                   indx=dlopt.index(dlop)
                   token.append(("DL_OP",dl_op[indx][1]))
tokenize(x)  
print(token)

