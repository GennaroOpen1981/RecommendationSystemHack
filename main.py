import math
import sys

'''
Input Data. See slide 6
'''
data = {
	'troc': { 
		'f1': 11,
	#	'f10': 0,
        'f2': 11,
        'f3': 10,
        'f4': 10,
        'f5': 10,
        'f6': 6,
        'f7': 5,
        'f8': 11#,
    #    'f9': 0
	},
	'ferrari': {
		'f1': 4,
		#'f10': 0,
        'f2': 4,
        #'f3': 0,
        'f4': 1,
        'f5': 3,
        'f6': 4,
        #'f7': 0,
        'f8': 4
        #'f9': 0
	
	},
	'panda': {
       'f1': 3,
       #'f10': 0,
       'f2': 3,
       'f3': 2,
       'f4': 3,
       #'f5': 0,
       'f6': 3,
       #'f7': 0,
       'f8': 3,
       #'f9': 0

     },
    'giulietta': {
       'f1': 12,
       #'f10': 0,
       'f2': 12,
       'f3': 12,
       'f4': 12,
       'f5': 10,
       'f6': 5,
       'f7': 7,
       'f8': 5,
       'f9': 7

  }


    
}


def euclidean_similarity(person1, person2):

	common_ranked_items = [itm for itm in data[person1] if itm in data[person2]]
	rankings = [(data[person1][itm], data[person2][itm]) for itm in common_ranked_items]
	distance = [pow(rank[0] - rank[1], 2) for rank in rankings]

	return 1 / (1 + sum(distance))

def pearson_similarity(person1, person2):

#	print "Person1", person1,"\n"
#	print "Person2", person2,"\n"
#	print "data[person1]", data[person1],"\n"
#	print "data[person2]", data[person2],"\n"

	common_ranked_items = [itm for itm in data[person1] if itm in data[person2]]

	n = len(common_ranked_items)

	s1 = sum([data[person1][item] for item in common_ranked_items])
	s2 = sum([data[person2][item] for item in common_ranked_items])

	ss1 = sum([pow(data[person1][item], 2) for item in common_ranked_items])
	ss2 = sum([pow(data[person2][item], 2) for item in common_ranked_items])

	ps = sum([data[person1][item] * data[person2][item] for item in common_ranked_items])

	num = n * ps - (s1 * s2)

	den = math.sqrt((n * ss1 - math.pow(s1, 2)) * (n * ss2 - math.pow(s2, 2)))

	return (num / den) if den != 0 else 0



def recommend(person, bound, similarity=pearson_similarity):
	
	'''
	Calculating the scores the score in included into the range [-1,1]. 
	See slide Pearson Correlaction Coefficient
	
	'''
	scores = [(similarity(person, other), other) for other in data if other != person]

	scores.sort()
	scores.reverse()
	
	scores = scores[0:bound]

	#print ("Printing scores: ",scores)

	recomms = {}

	for sim, other in scores:
		ranked = data[other]

		for itm in ranked:
			if itm not in data[person]:
				weight = sim * ranked[itm]

				if itm in recomms:
					s, weights = recomms[itm]
					recomms[itm] = (s + sim, weights + [weight])
					#print "else primo for recomms = ",recomms,"\n"
				else:
					recomms[itm] = (sim, [weight])
					#print "else primo for recomms = ",recomms,"\n"

	for r in recomms:
		#print "secondo for recomms = ",recomms,"\n"
		sim, item = recomms[r]
		#print "sim = ",sim,"\n"
		#print "item = ",item,"\n"
		#print "SIM = ",sim
		if sim != 0: 
		   recomms[r] = sum(item) / sim

	return recomms

def main():
	#print "Data: ",data,"\n"
	#print "Data Gennaro : ",data.get('Gennaro Marrazzo'),"\n"
	#print "Similarity", pearson_similarity("Gennaro Marrazzo", "Paolo Elefante")
	print "Raccomandation for the user :", recommend("panda", 3 , pearson_similarity)

if __name__ == '__main__':
    main()

