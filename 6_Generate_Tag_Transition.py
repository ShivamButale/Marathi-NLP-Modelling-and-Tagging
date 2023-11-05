import pandas as pd
print("Pandas Loaded successfully")
tags = set("N_NNP N_NN PR_PRP N_NST PR PR_PRP PR_PRF PR_PRL PR_PRC PR_PRQ DM DM_DMD DM_DMR DM_DMQ V V_VM V_VAUX CC CC_CCD CC_CCS CC_CCS_UT RP RP_RPD RP_INJ RP_INTF RP_NEG QT QT_QTF QT_QTC RD RD_RDF RD_SYM RD_PUNC RD_UNK RD_ECH RB UNS UNE".split())
f1 = open("111603009-bigram-tag-prob.txt","r+")
lines = f1.readlines()
print(tags)

df = pd.DataFrame([[0 for i in range(len(tags))] for j in range(len(tags))],index = list(tags), columns=list(tags))
f1.seek(0)
for i in range(len(lines)) :
	k = lines[i].split(",")
	if k[0] not in tags:
		continue
	if k[1] not in tags:
		continue
	print(i,k[-1][:-2])
	df[k[0]][k[1]] = k[-1][:-2]
df.to_csv("viterbi_matrix.csv")
