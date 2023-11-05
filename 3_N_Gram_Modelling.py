stop_tokens = "</s>"
pos_tags = "_N_NNP _N_NN_ _PR_PRP _N_NST _PR _PR_PRP _PR_PRF _PR_PRL _PR_PRC _PR_PRQ _DM _DM_DMD _DM_DMR _DM_DMQ _V _V_VM _V_VAUX _CC _CC_CCD _CC_CCS _CC_CCS__UT _RP _RP_RPD _RP_INJ _RP_INTF _RP_NEG _QT _QT_QTF _QT_QTC _RD _RD_RDF _RD_SYM _RD_PUNC _RD_UNK _RD_ECH _RB"
gaps = " "
new = "\n"

def unigram_work(f1,f2,f3,lines):
	tempo = []
	done = []
	for i in range(0, len(lines)-1):
		#Writing into file 2 - with label
		q = lines[i].split(" ")
		if(q[0] != "<s>_UNS"):
			if(q[0] != "<s>"):	
				for ctr in range(0,3):
					q[0]=q[0].replace(q[0][0], "")
				q.insert(0,"<s>_UNS")
			else:
				q[0]=q[0].replace("<s>", "<s>_UNS")		
		if(q[-1] != "</s>_UNE"):
			q[-1]=q[-1].replace("</s>", "</s>_UNE")
		
		for k in range(0,len(q)):
			tempo.append(q[k])
			f2.write((q[k]+"\n").encode('utf-8'))
	
	#Handling \n for last token of last sentence
	i = len(lines)-1
	q = lines[i].split(" ")
	if(q[0] != "<s>_UNS"):
		if(q[0] != "<s>"):	
			for ctr in range(0,3):
				q[0]=q[0].replace(q[0][0], "")
			q.insert(0,"<s>_UNS")			
		else:
			q[0]=q[0].replace("<s>", "<s>_UNS")
	if(q[-1] != "</s>_UNE"):			
		q[-1]=q[-1].replace("</s>", "</s>_UNE")
	for k in range(0,len(q)-1):
		tempo.append(q[k])
		f2.write((q[k]+"\n").encode('utf-8'))
	
	k = len(q)-1
	tempo.append(q[k])
	f2.write((q[k]).encode('utf-8'))
		
	#Counting Frequnecy and writing into file 3 - With frequency
	for i in tempo:
		ct = tempo.count(i)
		if i not in done:
			done.append(i)
			done.append(ct)
	
	for i in range(0, len(done)-3, 2):
		string=str(done[i]) + " " + str(done[i+1]) + "\n"
		f3.write(string.encode('utf-8'))
	
	#Handling \n for last token of last sentence
	i=len(done)-2
	string=str(done[i]) + " " + str(done[i+1])
	f3.write(string.encode('utf-8'))
	
	#Removing POS tags and writing into file1 - Without label
	for k in range(0, len(tempo)-1):
		for char in pos_tags:
			tempo[k] = tempo[k].replace(char, "")
		f1.write((tempo[k]+"\n").encode('utf-8'))

	#Handling \n for last token of last sentence
	k = len(tempo)-1
	for char in pos_tags:
		tempo[k] = tempo[k].replace(char, "")
	f1.write((tempo[k]).encode('utf-8'))
	   	
def bigram_work(f1,f2,f3,lines):	
	tempo = []
	done = []
	for i in range(0, len(lines)-1):
		#Writing into file 2 - With label
		q = lines[i].split(" ")
		if(q[0] != "<s>_UNS"):
			if(q[0] != "<s>"):	
				for ctr in range(0,3):
					q[0]=q[0].replace(q[0][0], "")
				q.insert(0,"<s>_UNS")			
			else:
				q[0]=q[0].replace("<s>", "<s>_UNS")
		if(q[-1] != "</s>_UNE"):				
			q[-1]=q[-1].replace("</s>", "</s>_UNE")
		for k in range(0,len(q)-1):
			pair = [q[k],q[k+1]]
			tempo.append(pair)
			f2.write((q[k]+" "+q[k+1]+"\n").encode('utf-8'))
	
	#Handling \n for last token of last sentence
	i = len(lines)-1
	q = lines[i].split(" ")
	if(q[0] != "<s>_UNS"):
		if(q[0] != "<s>"):	
			for ctr in range(0,3):
				q[0]=q[0].replace(q[0][0], "")
			q.insert(0,"<s>_UNS")	
		else:
			q[0]=q[0].replace("<s>", "<s>_UNS")
	if(q[-1] != "</s>_UNE"):		
		q[-1]=q[-1].replace("</s>", "</s>_UNE")	
	
	for k in range(0,len(q)-2):
		pair = [q[k],q[k+1]]
		tempo.append(pair)
		f2.write((q[k]+" "+q[k+1]+"\n").encode('utf-8'))
		
	k = len(q)-2
	pair = [q[k],q[k+1]]
	tempo.append(pair)
	f2.write((q[k]+" "+q[k+1]).encode('utf-8'))

	#Counting Frequnecy and writing into file 3 - With frequency	
	for i in tempo:
		ct = tempo.count(i)
		if i not in done:
			done.append(i)
			done.append(ct)
	for i in range(0, len(done)-3, 2):
		string= str(done[i][0]) + " " + str(done[i][1])+ " " + str(done[i+1]) + "\n"
		f3.write(string.encode('utf-8'))
	
	i=len(done)-2
	string= str(done[i][0]) + " " + str(done[i][1])+ " " + str(done[i+1])
	f3.write(string.encode('utf-8'))

	#Removing POS tags and writing into file1 - Without label
	for k in range(0, len(tempo)-1):
		for char in pos_tags:
			tempo[k][0] = tempo[k][0].replace(char, "")
			tempo[k][1] = tempo[k][1].replace(char, "")
		f1.write((tempo[k][0]+" "+tempo[k][1]+"\n").encode('utf-8'))
	
	#Handling \n for last token of last sentence
	k = len(tempo)-1
	for char in pos_tags:
		tempo[k][0] = tempo[k][0].replace(char, "")
		tempo[k][1] = tempo[k][1].replace(char, "")
	f1.write((tempo[k][0]+" "+tempo[k][1]).encode('utf-8'))

def trigram_work(f1,f2,f3,lines):
	tempo = []
	done = []
	for i in range(0, len(lines)-1):
		#Writing into file 2 - With label
		q = lines[i].split(" ")
		if(q[0] != "<s>_UNS"):		
			if(q[0] != "<s>"):	
				for ctr in range(0,3):
					q[0]=q[0].replace(q[0][0], "")
				q.insert(0,"<s>_UNS")	
			else:
				q[0]=q[0].replace("<s>", "<s>_UNS")		
		if(q[-1] != "</s>_UNE"):
			q[-1]=q[-1].replace("</s>", "</s>_UNE")	

		
		
		for k in range(0,len(q)-2):
			pair = [q[k],q[k+1],q[k+2]]
			tempo.append(pair)
			f2.write((q[k]+" "+q[k+1]+" "+q[k+2]+"\n").encode('utf-8'))
	
	#Handling \n for last token of last sentence
	i = len(lines)-1
	q = lines[i].split(" ")
	if(q[0] != "<s>_UNS"):
		if(q[0] != "<s>"):	
			for ctr in range(0,3):
				q[0]=q[0].replace(q[0][0], "")
			q.insert(0,"<s>_UNS")	
		else:
			q[0]=q[0].replace("<s>", "<s>_UNS")		
	if(q[-1] != "</s>_UNE"):
		q[-1]=q[-1].replace("</s>", "</s>_UNE")	
		
	for k in range(0,len(q)-3):
		pair = [q[k],q[k+1],q[k+2]]
		tempo.append(pair)
		f2.write((q[k]+" "+q[k+1]+" "+q[k+2]+"\n").encode('utf-8'))
		
	k = len(q)-3
	pair = [q[k],q[k+1],q[k+2]]
	tempo.append(pair)
	f2.write((q[k]+" "+q[k+1]+" "+q[k+2]).encode('utf-8'))

	#Counting Frequency and writing into file 3 - With frequency	
	for i in tempo:
		ct = tempo.count(i)
		if i not in done:
			done.append(i)
			done.append(ct)
	for i in range(0, len(done)-3, 2):
		string= str(done[i][0]) + " " + str(done[i][1])+ " " +str(done[i][2])+ " " + str(done[i+1]) + "\n"
		f3.write(string.encode('utf-8'))

	#Handling \n for last token of last sentence
	i=len(done)-2
	string= str(done[i][0]) + " " + str(done[i][1])+ " " + str(done[i][2])+ " " +str(done[i+1])
	f3.write(string.encode('utf-8'))

	#Removing POS tags and writing into file1 - Without label
	for k in range(0, len(tempo)-1):
		for char in pos_tags:
			tempo[k][0] = tempo[k][0].replace(char, "")
			tempo[k][1] = tempo[k][1].replace(char, "")
			tempo[k][2] = tempo[k][2].replace(char, "")
		f1.write((tempo[k][0]+" "+tempo[k][1]+" "+tempo[k][2]+"\n").encode('utf-8'))
	
	#Handling \n for last token of last sentence	
	k = len(tempo)-1
	for char in pos_tags:
		tempo[k][0] = tempo[k][0].replace(char, "")
		tempo[k][1] = tempo[k][1].replace(char, "")
		tempo[k][2] = tempo[k][2].replace(char, "")
	f1.write((tempo[k][0]+" "+tempo[k][1]+" "+tempo[k][2]).encode('utf-8'))  
		
def _4gram_work(f1,f2,f3,lines):
	tempo = []
	done = []
	for i in range(0, len(lines)-1):
		#Writing into file 2 - With label
		q = lines[i].split(" ")
		if(q[0] != "<s>_UNS"):
			if(q[0] != "<s>"):	
				for ctr in range(0,3):
					q[0]=q[0].replace(q[0][0], "")
				q.insert(0,"<s>_UNS")	
			else:
				q[0]=q[0].replace("<s>", "<s>_UNS")		
		if(q[-1] != "</s>_UNE"):
			q[-1]=q[-1].replace("</s>", "</s>_UNE")	

		
		for k in range(0,len(q)-3):
			pair = [q[k],q[k+1],q[k+2],q[k+3]]
			tempo.append(pair)
			f2.write((q[k]+" "+q[k+1]+" "+q[k+2]+" "+q[k+3]+"\n").encode('utf-8'))
	
	#Handling \n for last token of last sentence
	i = len(lines)-1
	q = lines[i].split(" ")
	if(q[0] != "<s>_UNS"):
		if(q[0] != "<s>"):	
			for ctr in range(0,3):
				q[0]=q[0].replace(q[0][0], "")
			q.insert(0,"<s>_UNS")	
		else:
			q[0]=q[0].replace("<s>", "<s>_UNS")		
	if(q[-1] != "</s>_UNE"):
		q[-1]=q[-1].replace("</s>", "</s>_UNE")	
	
	for k in range(0,len(q)-4):
		pair = [q[k],q[k+1],q[k+2],q[k+3]]
		tempo.append(pair)
		f2.write((q[k]+" "+q[k+1]+" "+q[k+2]+" "+q[k+3]+" "+"\n").encode('utf-8'))
	
	k = len(q)-4
	pair = [q[k],q[k+1],q[k+2],q[k+3]]
	tempo.append(pair)
	f2.write((q[k]+" "+q[k+1]+" "+q[k+2]+" "+q[k+3]).encode('utf-8'))

	#Counting Frequency and writing into file 3 - With frequency	
	for i in tempo:
		ct = tempo.count(i)
		if i not in done:
			done.append(i)
			done.append(ct)	
	for i in range(0, len(done)-3, 2):
		string= str(done[i][0]) + " " + str(done[i][1])+ " " +str(done[i][2])+ " " + str(done[i][3])+ " "+str(done[i+1]) + "\n"
		f3.write(string.encode('utf-8'))

	#Handling \n for last token of last sentence
	i=len(done)-2
	string= str(done[i][0]) + " " + str(done[i][1])+ " " + str(done[i][2])+ " " + str(done[i][3])+ " "+str(done[i+1])
	f3.write(string.encode('utf-8'))
	
	#Removing POS tags and writing into file1 - Without label
	for k in range(0, len(tempo)-1):
		for char in pos_tags:
			tempo[k][0] = tempo[k][0].replace(char, "")
			tempo[k][1] = tempo[k][1].replace(char, "")
			tempo[k][2] = tempo[k][2].replace(char, "")
			tempo[k][3] = tempo[k][3].replace(char, "")
		f1.write((tempo[k][0]+" "+tempo[k][1]+" "+tempo[k][2]+" "+tempo[k][3]+"\n").encode('utf-8'))
	
	#Handling \n for last token of last sentence
	k = len(tempo)-1
	for char in pos_tags:
		tempo[k][0] = tempo[k][0].replace(char, "")
		tempo[k][1] = tempo[k][1].replace(char, "")
		tempo[k][2] = tempo[k][2].replace(char, "")
		tempo[k][3] = tempo[k][3].replace(char, "")
	f1.write((tempo[k][0]+" "+tempo[k][1]+" "+tempo[k][2]+" "+tempo[k][3]).encode('utf-8'))  

def _5gram_work(f1,f2,f3,lines):
	tempo = []
	done = []
	for i in range(0, len(lines)-1):
		#Writing into file 2 - With label
		q = lines[i].split(" ")
		if(q[0] != "<s>_UNS"):	
			if(q[0] != "<s>"):	
				for ctr in range(0,3):
					q[0]=q[0].replace(q[0][0], "")
				q.insert(0,"<s>_UNS")	
			else:
				q[0]=q[0].replace("<s>", "<s>_UNS")		
		if(q[-1] != "</s>_UNE"):
			q[-1]=q[-1].replace("</s>", "</s>_UNE")	

		for k in range(0,len(q)-4):
			pair = [q[k],q[k+1],q[k+2],q[k+3],q[k+4]]
			tempo.append(pair)
			f2.write((q[k]+" "+q[k+1]+" "+q[k+2]+" "+q[k+3]+" "+q[k+4]+"\n").encode('utf-8'))
	
	i = len(lines)-1
	q = lines[i].split(" ")
	if(q[0] != "<s>_UNS"):	
		if(q[0] != "<s>"):	
			for ctr in range(0,3):
				q[0]=q[0].replace(q[0][0], "")
			q.insert(0,"<s>_UNS")	
		else:
			q[0]=q[0].replace("<s>", "<s>_UNS")		
	if(q[-1] != "</s>_UNE"):
		q[-1]=q[-1].replace("</s>", "</s>_UNE")	

	for k in range(0,len(q)-5):
		pair = [q[k],q[k+1],q[k+2],q[k+3],q[k+4]]
		tempo.append(pair)
		f2.write((q[k]+" "+q[k+1]+" "+q[k+2]+" "+q[k+3]+" "+q[k+4]+" "+"\n").encode('utf-8'))
	
	#Handling \n for last token of last sentence	
	k = len(q)-5
	pair = [q[k],q[k+1],q[k+2],q[k+3],q[k+4]]
	tempo.append(pair)
	f2.write((q[k]+" "+q[k+1]+" "+q[k+2]+" "+q[k+3]+" "+q[k+4]).encode('utf-8'))

	#Counting Frequency and writing into file 3 - With frequency	
	for i in tempo:
		ct = tempo.count(i)
		if i not in done:
			done.append(i)
			done.append(ct)
	for i in range(0, len(done)-3, 2):
		string= str(done[i][0]) + " " + str(done[i][1])+ " " +str(done[i][2])+ " " + str(done[i][3])+ " "+str(done[i][4])+ " " + str(done[i+1]) + "\n"
		f3.write(string.encode('utf-8'))
	
	#Handling \n for last token of last sentence
	i=len(done)-2
	string= str(done[i][0]) + " " + str(done[i][1])+ " " + str(done[i][2])+ " " + str(done[i][3])+ " "+str(done[i][4])+ " "+str(done[i+1])
	f3.write(string.encode('utf-8'))
	
	#Removing POS tags and writing into file1 - Without label
	for k in range(0, len(tempo)-1):
		for char in pos_tags:
			tempo[k][0] = tempo[k][0].replace(char, "")
			tempo[k][1] = tempo[k][1].replace(char, "")
			tempo[k][2] = tempo[k][2].replace(char, "")
			tempo[k][3] = tempo[k][3].replace(char, "")
			tempo[k][4] = tempo[k][4].replace(char, "")
		f1.write((tempo[k][0]+" "+tempo[k][1]+" "+tempo[k][2]+" "+tempo[k][3]+" "+tempo[k][4]+"\n").encode('utf-8'))
		
	#Handling \n for last token of last sentence	
	k = len(tempo)-1
	for char in pos_tags:
		tempo[k][0] = tempo[k][0].replace(char, "")
		tempo[k][1] = tempo[k][1].replace(char, "")
		tempo[k][2] = tempo[k][2].replace(char, "")
		tempo[k][3] = tempo[k][3].replace(char, "")
		tempo[k][4] = tempo[k][4].replace(char, "")
	f1.write((tempo[k][0]+" "+tempo[k][1]+" "+tempo[k][2]+" "+tempo[k][3]+" "+tempo[k][4]).encode('utf-8'))

def main():
	file1 = open("Assignment2-111603009.txt","r+")
	
	f1 = open("111603009-unigram-without-label.txt","wb")
	f2 = open("111603009-unigram-with-label.txt","wb")
	f3 = open("111603009-unigram-with-frequency.txt","wb")
	
	f4 = open("111603009-bigram-without-label.txt","wb")
	f5 = open("111603009-bigram-with-label.txt","wb")
	f6 = open("111603009-bigram-with-frequency.txt","wb")
	
	f7 = open("111603009-trigram-without-label.txt","wb")
	f8 = open("111603009-trigram-with-label.txt","wb")
	f9 = open("111603009-trigram-with-frequency.txt","wb")

	f10 = open("111603009-4gram-without-label.txt","wb")
	f11 = open("111603009-4gram-with-label.txt","wb")
	f12 = open("111603009-4gram-with-frequency.txt","wb")

	f13 = open("111603009-5gram-without-label.txt","wb")
	f14 = open("111603009-5gram-with-label.txt","wb")
	f15 = open("111603009-5gram-with-frequency.txt","wb")

	lines = file1.readlines() 
	t = "</s>"
	index = 0
	while index < len(lines):
		for char in new:
			lines[index]=lines[index].replace(char,"")
		if t in lines[index]:
			for char in stop_tokens:
				lines[index]=lines[index].replace(char,"")
		lines[index] = lines[index] + " </s>"	
		lines2 = "<s>"
		lines2 = lines2 + lines[index]
		lines[index] = lines2
		index=index+1		
		
	unigram_work(f1,f2,f3,lines)
	bigram_work(f4,f5,f6,lines)
	trigram_work(f7,f8,f9,lines)
	_4gram_work(f10,f11,f12,lines)
	_5gram_work(f13,f14,f15,lines)
			
	file1.close()
	f1.close()
	f2.close()
	f3.close()
	f4.close()
	f5.close()
	f6.close()
	f7.close()
	f8.close()
	f9.close()
	f10.close()
	f11.close()
	f12.close()
	f13.close()
	f14.close()
	f15.close()
main()
