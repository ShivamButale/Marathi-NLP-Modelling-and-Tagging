import math
def viterbi(dict1, dict2, C, words):
    T = len(words)
    N = len(C)
    seqscore = [[0 for i in range(T)] for j in range(N)]
    backptr = [[0 for i in range(T)] for j in range(N)]
    for i in range(0, N):
        for j in range(0, N):
            if((C[i] + "," + C[j]) not in dict2.keys()):
                dict2[C[i] + "," + C[j]] = 0
    for i in range(0, N) :
        if((C[i] + "," + words[0]) not in dict1.keys()):
            dict1[C[i] + "," + words[0]] = 0.0001
        seqscore[i][0] = dict1[C[i] + "," + words[0]] * dict2["UNS" + "," + C[i]]
        backptr[i][0] = 0

    for t in range(1, T):
        for i in range(0, N):
            max_value = -1
            max_index = -1
            for j in range(0, N):    
                if(max_value < (seqscore[j][t - 1] * dict2[C[j] + "," + C[i]])):
                    max_value = seqscore[j][t - 1] * dict2[C[j] + "," +C[i]]
                    max_index = j
            if((C[i] + "," + words[t]) not in dict1.keys()):
                dict1[C[i] + "," + words[t]] = 0.0001   
            seqscore[i][t] = max_value * dict1[C[i] + "," + words[t]]
            backptr[i][t] = max_index

    c = [0] * T
    max_value = -1
    for i in range(0, N) :
        if(max_value < seqscore[i][T - 1]):
            max_value = seqscore[i][T - 1]
            c[T - 1] = i
    for i in range(T - 2, -1, -1):
        c[i] = backptr[c[i + 1]][i + 1]
    tagged_output = ""    
    for i in range(0, T):
        tagged_output += words[i].strip() + "_" + C[c[i]] + " "
    return tagged_output

def main():
	f1 = open("111603009-bigram-tag-prob.txt", "r+")
	f2 = open("111603009-word-tag-prob.txt", "r+") 
	#f3 = open("Assignment1-111603009.txt", "r+")
	#f4 = open("Tagging_Corpus_Output.txt", "w")
	
	f3 = open("111603009-Assign3_Viterbi_Input.txt", "r+")
	f4 = open("111603009-Assign3_Viterbi_Output.txt", "w")
	
	#FORMING DICTIONARY TO STORE WORD EMISSION PROBABILITIES
	dict1 = {}
	lines = f2.readlines()
	for i in lines :
		try:
			tag, word, prob = i.split(",")
		except:
			pass
		try:
			dict1[tag + "," + word] = float(prob)
		except:
			pass
	
	#FORMING DICTIONARY TO STORE TAG TRANSITION PROBABILITIES
	dict2 = {}
	C = set()
	lines = f1.readlines()
	for i in lines :
		try:
			tag1, tag2, prob = i.split(",")
		except:
			pass
		try:	
   			dict2[tag1 + "," + tag2] = float(prob)    
		except:
			pass
		C.add(tag1)
		C.add(tag2)
	
	#ADDING UNKNOWN WORD TAG TO THE SET OF TAGS
	C.add('UNK')
	tag_list = sorted(list(C))
	
	#READ SENTENCES TO BE TAGGED FROM FILE
	lines = f3.readlines()
	for i in lines:
		words = i.split(" ")
		#CALLING VITERBI FUNCTION
		f4.write(viterbi(dict1, dict2, tag_list, words) +"\n")
main()
