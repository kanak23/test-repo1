#!/usr/bin/python
f = open('content.txt')
totalA= 0
totalB= 0
totalC= 0
totalE= 0
totalG= 0
happy=[0,0,0,0,0]
sad=[0,0,0,0,0]
Sarcastic=[0,0,0,0,0]
Surprised=[0,0,0,0,0]
Crook=[0,0,0,0,0]
Neutral=[0,0,0,0,0]
angry=[0,0,0,0,0]
#label:loop 
for line in f:
	if "A :" in line:
		totalA+=1   
		if ":)" in line:
			happy [0]+=1
		
		if ":D"  in line:
			happy [0]+=1
		if ":("  in line:
			sad [0]+=1
		if ":'("  in line:
			sad [0]+=1
		if ":P"  in line:
			Sarcastic [0]+=1
		if ":'("  in line:
			Sarcastic [0]+=1
	        if "O_O"  in line:
			Surprised [0]+=1
		if ":-o"  in line:
			Surprised [0]+=1
	        if "B-)"  in line:
			Crook [0]+=1
		if ";)"  in line:
			Crook [0]+=1
	        if ":-/"  in line:
			Neutral [0]+=1
		if "=_="  in line:
			Neutral [0]+=1
	        if "x-("  in line:
			angry [0]+=1
		if ">_<"  in line:
			angry [0]+=1

	if "B :" in line:
		totalB+=1   
		if ":)"  in line:
			happy [1]+=1
		if ":D"  in line:
			happy [1]+=1
		if ":("  in line:
			sad [1]+=1
		if ":'("  in line:
			sad [1]+=1
		if ":P"  in line:
			Sarcastic [1]+=1
		if ":'("  in line:
			Sarcastic [1]+=1
	        if "O_O"  in line:
			Surprised [1]+=1
		if ":-o"  in line:
			Surprised [1]+=1
	        if "B-)"  in line:
			Crook [1]+=1
		if ";)"  in line:
			Crook [1]+=1
	        if ":-/"  in line:
			Neutral [1]+=1
		if "=_="  in line:
			Neutral [1]+=1
	        if "x-("  in line:
			angry [1]+=1
		if ">_<"  in line:
			angry [1]+=1
	if "C :" in line:
		totalC+=1   
		if ":)"  in line:
			happy [2]+=1
		if ":D"  in line:
			happy [2]+=1
		if ":("  in line:
			sad [2]+=1
		if ":'("  in line:
			sad [2]+=1
		if ":P"  in line:
			Sarcastic [2]+=1
		if ":'("  in line:
			Sarcastic [2]+=1
	        if "O_O"  in line:
			Surprised [2]+=1
		if ":-o"  in line:
			Surprised [2]+=1
	        if "B-)"  in line:
			Crook [2]+=1
		if ";)"  in line:
			Crook [2]+=1
	        if ":-/"  in line:
			Neutral [2]+=1
		if "=_="  in line:
			Neutral [2]+=1
	        if "x-("  in line:
			angry [2]+=1
		if ">_<"  in line:
			angry [2]+=1
	if "E :" in line:
		totalE+=1   
		if ":)"  in line:
			happy [3]+=1
		if ":D"  in line:
			happy [3]+=1
		if ":("  in line:
			sad [3]+=1
		if ":'("  in line:
			sad [3]+=1
		if ":P"  in line:
			Sarcastic [3]+=1
		if ":'("  in line:
			Sarcastic [3]+=1
	        if "O_O"  in line:
			Surprised [3]+=1
		if ":-o"  in line:
			Surprised [3]+=1
	        if "B-)"  in line:
			Crook [3]+=1
		if ";)"  in line:
			Crook [3]+=1
	        if ":-/"  in line:
			Neutral [3]+=1
		if "=_="  in line:
			Neutral [3]+=1
	        if "x-("  in line:
			angry [3]+=1
		if ">_<"  in line:
			angry [3]+=1
	if "G :" in line:
		totalG+=1   
		if ":)"  in line:
			happy [4]+=1
		if ":D"  in line:
			happy [4]+=1
		if ":("  in line:
			sad [4]+=1
		if ":'("  in line:
			sad [4]+=1
		if ":P"  in line:
			Sarcastic [4]+=1
		if ":'("  in line:
			Sarcastic [4]+=1
	        if "O_O"  in line:
			Surprised [4]+=1
		if ":-o"  in line:
			Surprised [4]+=1
	        if "B-)"  in line:
			Crook [4]+=1
		if ";)"  in line:
			Crook [4]+=1
	        if ":-/"  in line:
			Neutral [4]+=1
		if "=_="  in line:
			Neutral [4]+=1
	        if "x-("  in line:
			angry [4]+=1
		if ">_<"  in line:
			angry [4]+=1

            
f.close()
A=[happy[0],sad[0],Sarcastic [0],Surprised [0],Crook [0],Neutral [0],angry [0]]
B=[happy[1],sad[1],Sarcastic [1],Surprised [1],Crook [1],Neutral [1],angry [1]]
C=[happy[2],sad[2],Sarcastic [2],Surprised [2],Crook [2],Neutral [2],angry [2]]
E=[happy[3],sad[3],Sarcastic [3],Surprised [3],Crook [3],Neutral [3],angry [3]]
G=[happy[4],sad[4],Sarcastic [4],Surprised [4],Crook [4],Neutral [4],angry [4]]
print Neutral [3]
total=float (sum(happy)+sum(sad)+sum(Sarcastic)+sum(Surprised)+sum(Crook)+sum(Neutral)+sum(angry))
print total
print sum(sad)
print "happy :",(sum(happy)*100)/total,"%tage"
print "sad :",(sum(sad)*100)/total,"%tage"
print "Sarcastic :",(sum(Sarcastic)*100)/total,"%tage"
print "Surprised :",(sum(Surprised)*100)/total,"%tage"
print "Crook :",(sum(Crook)*100)/total,"%tage"
print "Neutral :",(sum(Neutral)*100)/total,"%tage"
print "angry :",(sum(angry)*100)/total,"%tage"
mx=A[0]
j=0
for i in range (1, len(A)):
	if A[i]>mx:
	 mx=A[i]
 	 j=i
print A[i]
#print A[A[i]

