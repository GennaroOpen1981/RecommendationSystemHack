import math


data = {
	'Gennaro Marrazzo': { 
		'L1D1': 3, 
		'L2D1': 5, 
		'L3D1': 5, 
		'L1D2': 2,
	},

	'Paolo Elefante': { 
		'L1D1': 1, 
		'L2D1': 2, 
		'L3D1': 12, 
		'L1D2': 20,
		'L3D4': 21, 
		'L1D4': 2,
	},

	'Vincenzo Paparo': { 
		'L1D1': 1, 
		'L2D1': 5, 
	},

	'Alfonso Attanasio': { 
		'L1D1': 7, 
		'L3D1': 6, 
		'L1D2': 9,
	},

	'Stefano Volpe': { 
		'L3D1': 2, 
		'L1D2': 5,
	},
	
	'Enzo Gentile': { 
		'L3D1': 5, 
	},

}

def euclidean_similarity(person1, person2):

	common_ranked_items = [itm for itm in data[person1] if itm in data[person2]]
	rankings = [(data[person1][itm], data[person2][itm]) for itm in common_ranked_items]
	distance = [pow(rank[0] - rank[1], 2) for rank in rankings]

	return 1 / (1 + sum(distance))

def pearson_similarity(person1, person2):

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
	scores = [(similarity(person, other), other) for other in data if other != person]

	scores.sort()
	scores.reverse()
	scores = scores[0:bound]

	print (scores)

	recomms = {}

	for sim, other in scores:
		ranked = data[other]

		for itm in ranked:
			if itm not in data[person]:
				weight = sim * ranked[itm]

				if itm in recomms:
					s, weights = recomms[itm]
					recomms[itm] = (s + sim, weights + [weight])
				else:
					recomms[itm] = (sim, [weight])

	for r in recomms:
		sim, item = recomms[r]
		recomms[r] = sum(item) / sim

	return recomms
def main():
	
    print recommend("Gennaro Marrazzo", 5, pearson_similarity)
    #print euclidean_similarity('Gennaro Marrazzo', 'Vincenzo Paparo')	

if __name__ == '__main__':
    main()

