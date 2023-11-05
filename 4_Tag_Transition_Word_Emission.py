def unigram_work(lines, f4):
	new = '\n'
	for i in range(0, len(lines)):
		for char in new:
			lines[i]=lines[i].replace(char,"")
		prob = 0
		count = 0
		splitted = lines[i].split(" ")
		numerator = int(splitted[1])
		kk = splitted[0].split("_")
		word = kk[0]
		tag = "_".join(kk[1:len(kk)])
		for j in range(0, len(lines)):
			if tag in lines[j]:
				splitted2 = lines[j].split(" ")
				count = count+int(splitted2[1])
		prob = numerator/count
		f4.write((tag+","+word+","+str(prob)+"\n").encode('utf-8'))
		
def bigram_work(lines, f3):
	new = '\n'
	wrt=[]
	for i in range(0, len(lines)):
		for char in new:
			lines[i]=lines[i].replace(char,"")
		count = count2 = prob = 0
		splitted = lines[i].split(" ")
		kk = splitted[0].split("_")
		tag = "_".join(kk[1:len(kk)])
		kk2 = splitted[1].split("_")
		tag2 = "_".join(kk2[1:len(kk2)])
		
		#check tag1 as tag1 
		for j in range(0, len(lines)):
			splitted2 = lines[j].split(" ")
			kk = splitted2[0].split("_")
			tag1 = "_".join(kk[1:len(kk)])
			if tag == tag1:
				count = count+int(splitted2[2])
		denominator = count 
		
		#check tag1 as tag1 and tag2 as tag2
		for j in range(0, len(lines)):
			splitted3 = lines[j].split(" ")
			kk = splitted3[0].split("_")
			tag3 = "_".join(kk[1:len(kk)])
			kk2 = splitted3[1].split("_")
			tag4 = "_".join(kk2[1:len(kk2)])
			if tag == tag3 and tag2 == tag4:
				count2 = count2 + int(splitted3[2])
		numerator = count2 
		prob = numerator / denominator
		sent = (tag+","+tag2+","+str(prob)+"\n").encode('utf-8') 
		if sent not in wrt:
			wrt.append(sent)
	for k in wrt:	
		f3.write(k)
		
def main():
	f1 = open("111603009-bigram-with-frequency.txt","r+")
	f2 = open("111603009-unigram-with-frequency.txt","r+")
	f3 = open("111603009-bigram-tag-prob.txt","wb")
	f4 = open("111603009-word-tag-prob.txt","wb")

	lines = f2.readlines() 
	unigram_work(lines, f4)			
	
	lines2 = f1.readlines() 
	bigram_work(lines2, f3)			
	
	f1.close()
	f2.close()
	f3.close()
	f4.close()
main()
