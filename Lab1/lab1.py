# C:\Users\rebli156>c:\Python25\python lab1.py
tosses = [
"11111111010011000101101100101000111010011110010100011001000001100110101001010110100111111100111011100111101010001110000001101001110111100000010101001001000100110100110011110101111110101000110101111011", 
"01110000100101101100011101111010010010100100100111011000100010011111010110100011000111100110100110010110111010010010011101000111000101110001011010100111100110001100011001100000011001011100101101001100", 
"10000101111110110101100000111000110001000101101001100011111110111100000001101001100110100111110001100110100110101100110000010010001110110110010111011100001101111101110001110110101100010101011000010010", 
"11010010001001010110010011110000001110101100110111100001010011101101101011010111100110101111001101001111100001110100011101111110101111011101101100110011100000101001100111000001011110010000101001100100", 
"00101000110111101001101001101011100111101110010100110110010110000110110001101000001000111000010110001011101111100110101010010110011001101011111010001100110011000100100011111010101011010111100100001001", 
"10110110111010011101010011000100011111111011001101010011001001001110100000011011011010101100011000101100100011001001101011010011011010001000100011101110111010001000010011101101111010101011100100101111", 
"00101111000001010110111100011001100111010100011011110011000011001110010011011101100100011001101001010000001010000110101001000011010000110011000101111100010111010100011011001101001101001111110000110110", 
"01110111100011101011010011110100101110110101001101110110111000001011011001000010110101110101000100001110100110010110111000101010101100001101110010100111011100001010001101110100010110100101001000110010", 
"01101100111010010011001011101110110100101101011001000111010101010000001001111010111011101101011110110101011010011101001101110110000101011011101110001101111010100010101000110100010101011001011001110011", 
"10011010110010010110001100001011100111110111111101110001001101010111010000010011111010010010110101010011001101101010000010111100001111100101010010111101100110101110111111010101111110000100110011010110", 
"10001000011001101010110001000110111110000111100101010010010100111000101101010110010010011100000001111110000011110010100111111101100110111101100000110011011111010000111011100010001111000010000001010111", 
"11010010111010001101001000100101101011001001101010101100110001010100001100100100110101011100101001000101001101010001001111010001110111110101101100001111001010001100001010110000111000100010101100000010", 
"11001001010011010011100010110101000010011100100011111101010111101111001011101111000010100110101001010101111101111001101101010010101100100111100010001111100000100100110110000111110011110101011010101100", 
"11111010100010100100010101111000111111000111110000100011011001101100011010101101010111001111001100111001010001101110000000101000101010101010001010011111110100111100000011101000010010001101001101101111", 
"11110010101010000011011010011110110111010010110010001100101111011111101111001010011101010101001001001000101101111000000010111001101101101001101111100010001010011111011100101001010100101000100101001011", 
"11110011011101101110111111110000100011011100100100100011011000010100001000001000000000110101010111111010000101011101001111000101101100110000100011100100001101010111101010111101101110101111011101001010", 
"11110100000000010101000001010100111010001100010100100001101010101110110100001010010100110011101001000101100000100111001010011111010101001000111001001001000000010010101010101111101011111101110110110001", 
"00110011010001000100011001000110001101101001011001100101100101111000000011100110010100010100101100000011101011001101101011010001010010001000000100101100101100111010010111110111110110010101001001000000", 
"01001100001010110000110110000001111110011111001011011011110110101001101100000001111101000110100110110101000010011010010001011111001101100000011011101010001111000111010101001110011011010110101000110001", 
"10000001000100010000010100100101001000010000000000111000000001000001010001000010010010001010000010000100100000101000110100001000010011100000100000110111011000001010101000000100010010001000000000000000", 
"00010100011101001001011010010111111000100100101000000011101100110110000100111010110010010001000111110011000100010011101111010000001010111100111100100011010001111010011011010110111111011001101110100111", 
"10110100010000101000001100111100000010011001000100110001111010111000010010011010111010010001011000100000110101000011100001000000010001101011010110100010000010001010100100000101011000111111100101001101", 
"00111010110000110111011010010100110111010010101101010001101001111101101101111011101010001011000101011011001101010110111010100101011100001011100011100110011110011100001010100011111110001100011000100110", 
"11010001010011100101100111101010001011101110011111111011000000001100100010000000011000001100100011001011110010000110010010000010011100100000101100011001110000001000101110111101000111001101010110001101", 
"10000010101100011011100000110111001110110001101101111010011000000100100000101111101101010000000111010101001101001011011101101111000011110000111100000100000110011000011110000010100000011000000110110100", 
"10010111001010001101110101011101001001011110010101000011111110100101000000000000000100001110110100001111111101000000111011110001110110111111100001110110111101101010001010101010010110111100011111000011", 
"01110110001111110010010100100100010000110110100110101101001110101100011001111000100101001000111100010101100000001100110010110110011010110011010101110110011100110111000010101101001110111010001100110000", 
"10110011111111011001001010010100101100110001101010011110011100010000110100111001111000001000111101100010001100110010100010010001011110111101101011010010011010010010001100100110111011010001000001011100", 
"11010110101110101111110011111111010000000010010100100101110011110010110100011000100111110011001100100001010110000010010101001101110110001111010101001010010100100101110011111111010011100011110100111010", 
"01100111101000010011101101001110111101000010011001110100110110000111111000001010111100001011100001100100001110101111100110111101001011000100010011111010101110101011110111011100101010101010110111100111", 
"01101111100001111100000001111101110111011010011100100010100100010111000110110000101110000010010000100001101110101011101100111110000100101101111101001111101100111000011001011111001000011101101100001100", 
"10110101011101111100110100001110010001110001000001100010010110111100110011000000101110110000011111000111000011110011011000011000000000000010001111110001011101100011001100000011000100001000000100101101", 
"01001111001000010100001101011110010000010110111011011001100100000010010100010110101000110001000010110001110110010011110100100100101111000001110111101010110001111010110010000110011000000100111101101110", 
"00100010000100110000000100101010100110010100001110100110100110100100100010111000100011001100010000100010000010010000010010100010100010001100100111000110010100000010100111010011100100000000100011110001", 
"11111110001110110011000111010111101110000010010000001111001111111010011010110001010101100101110111010000011110001110110111011111000110010001010001011001010100000001011011000001011110011110110001110011", 
"10100000000101000000000100010001110111010111100101001000010100111010101101101000001001011111000111101000010111000100111100111001110111000110111000101000101100000010000101000000001100110100100000001111", 
"11111101010011101101010011100011110111001001110100000111011001100110110011101000101111010000100011010101100100111001010101111000010001010110111111000000001100000000001101000000001111000001011000110101", 
"00101101110101000101000001101000100010111010000110100001010110001010110101110110001000000010101000011111001100011111101011000111000110100001000000110110110010100100101011001011001001101001101111111101", 
"01001111011101110001010011000011001011010100000001110111010011111101100001000010001110100010110001000000000100101111101001101101101111011100100011100011010111011011010100001101100100111100011011110111", 
"11100101111111111110000111000110111110011000100000101011101011010100001101001000101011000111000100001101101001111111100010001001001001011111100000001001101111010001011001100001101011010001101001110011", 
"10000110101110001000011101110110010011111000000000110011001001110111110000110000000000101010011111010111001010000100000011000100011010010110101010001101101101011011111001101000110011110110100010010011", 
"10001110011110100010001001101011111111100000001011110110111111010000011101101011101001001111110100000011001000111110100101110111001110011001101001100010101000010011100100101010001110110011111010000010", 
"00110110001011101001111011000111011011001110010011110110011101011001110101101001010011010001010111011010110111101111011000100011100101000001101101111101110111001011010110010011010000101101010101101000", 
"10111001101100111100111110010101001010111000011010010011000101110011010101011010101111010101100110101010110110100110110000001010111011101010110110011110110011100010101100101101110011000001110001110001", 
"10111101001001011111011111100101101101100111101010110001000001011011001000101110111110110000100011111000110101000000011111100000001101001000010001001011100100101001000000101000100101110011101110110001", 
"01101110011101010111110010011010010111111111000101011111010111010000111000000011101100001110101010111011111110000110100010110101000001110100001101111101011011110001000100011111111011011111100110010101", 
"01001111011011001011001110101111010110000011000111110110001001000110001101110000111100110100111010100101010010011010110011010100101001101100101101010101010010100101010011001001110111111001100010011111", 
"10111001011001100100110111000100111111101011010100011011101000001001100010000111101011010011101100100101001110111011010010101101101111101011000000111100010111101001111100111101011110100000000000100011", 
"00111111101111111111011100101111011011011100011110000000001100100000000001110001111110110011000100111010100010010011010000111001110110100100000111101100000001001000111010101011101100010010010100000110", 
"01010011011011011000101010101001010001011000010011001001001110110001001100100110100110010110001111000110111110010001101010111111001001110011100110101111001010111110101100010101111001101110001101100100", 
"10110100011010101110100110010001101110101010010001101101110010101101001110111110010101000110000101001010110001010101001110011110010100111001000110100010111011101101110011010101111000011010010100110101", 
"01111101110111010100001010110101001011111001101010000000011111011101111011001111100000000011001010010100110100010011111000011010000110011000000110010011101110000001110101110100001100110011110101100011", 
"11111000001001111100110100110011111100000010111101000010001010000011110000000011000001111110010100011001110011001101011111001100010010110110001010100110010101000000110011111101010111101110101001111111", 
"10101010001100100100000010001010101010100100100010101011001010111101010110111011011000100100010100100001010110101100100001101011010100101010100101100001010100101101100100100100101011010011100010010001", 
"01100110010000100001011100001100101011011011001110001111111000010011101100000010000001111010110111001111110001011000110001110000111111100100010000101101101001000100101101101011001111100010101110000000", 
"10110101101000011011110101000111111010110000010011001010010010010100000010011000111010101101111101001001011010110001001111011100001000111110000000000011001110011110000010001100110010100110011110100101", 
"11101001011111111100101000011010100011101101101001011011110011001111111110010100010000100100101100101101000100000011110100000000001001011000110100000001110100011110010110011001000100100100010010011000", 
"00010011010110100101010110010111110110011100011110011110010110110101000111010110001000101011100100100110110101000100110000011101111101011100100000010011111011111101010010010101111111101110111100110011", 
"11101100111000111000111101010100001101101101000111100000000100100010100000011011111111000001000111000110110001011011011010111001101101100011110110001111101101100011111100101111000010011111000101001110", 
"01000000001111100001101000001001001100101001011001110011100100011101011111001101001000111000100101101101100011011100100001011110000101000010111001110001010011110111111111011011011111010001000100101010"]


from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import DBSCAN
import math
from adjustText import adjust_text
#python -mpip install -U pip
#python -mpip install -U matplotlib

"""
Counts how many ones and zeros for each person.
"""
def nr_of_tails():
	tails = []
	human = []

	for toss in tosses:
		tail_count = 0
		#one_count = 0
		for num in toss:
			#print(type(num))
			if num == '0':
				tail_count += 1
			#elif num == '1':
				#one_count += 1
		tails.append(tail_count)
		if abs(tail_count - 100) > 10:
			human.append(tosses.index(toss))
			
	return tails
	
"""
Generates list of dictionaries containing number of consecuetive digits for all persons.
"""	
def consecutive():
	toss_sequences = []
	same_count = 1
	for toss in tosses:
		sequences = []
		#print(len(toss))
		# reset counter if not the same any more
		for index, num in enumerate(toss[:-1]):
		#https://stackoverflow.com/questions/522563/accessing-the-index-in-python-for-loops
			if num == toss[index + 1]:
				same_count += 1
			else:
				sequences.append(same_count)
				same_count = 1
		
		sequences.append(same_count)
		same_count = 1

		toss_sequences.append(sequences)
	
	
	cons = []
	
	for sequence in toss_sequences:
		con = {}
		for num in sequence:
			if num not in con:
				con[num] = 1
			else:
				con[num] += 1
		cons.append(con)

	return cons
	
	#print(cons)

"""
Input: 
	cons: List of dictionaries containing number of consecuetive digits
	n: number of consecuetive digits to look for
Output: List of number of n consecuetive digits for each person
"""
def count_consecutive(cons, n):
	con_ns = []
	for con in cons:
		if n in con.keys():
			con_ns.append(con[n])
		else:
			con_ns.append(0)
	#print(con_ns)
	return con_ns

"""
Scales dataset to values between 0 and 1
Input: dataset with one or more dimensions
Output: scaled dataset as list of lists
"""
def scale_data(d):
	scaled_dataset = []
	for dimension in d:
		scaled_dataset.append([entry/max(dimension) for entry in dimension])
	return scaled_dataset


"""
Generates dataset as lists with tree different characteristics.
"""	
def create_dataset():
	consec_2 = count_consecutive(consecutive(), 2)
	consec_3 = count_consecutive(consecutive(), 3)
	consec_5 = count_consecutive(consecutive(), 5)

	return (consec_2, consec_3, consec_5)

"""
Performs pca on 3D to 2D. 
Input: dataset with three lists
Output: two list with principal component 1 and 2
"""
def perform_pca(dataset):
	# Standardizing the features
	#print(dataset)
	x = StandardScaler().fit_transform(dataset)
	#print(x)
	pca = PCA(n_components=2)
	principalComponents = pca.fit_transform(x)
	variance = pca.explained_variance_ratio_
	print(pca.components_)
	print(variance[0] + variance[1])
	print("Ok!")
	pc1 = []
	pc2 = []
	for elem in principalComponents:
		pc1.append(elem[0])
		pc2.append(elem[1])
	#print(pc1)
	return (pc1, pc2)


"""
Takes two lists and zips it to one list of tuples
"""
def format_data_2D(x, y):
	return list(zip(x, y))

"""
Takes dataset with three dimensions in separate lists and zips it to one list with 3-tuples.
"""
def format_data_3D(dataset):
	return list(zip(dataset[0], dataset[1], dataset[2]))

"""
Takes dataset with three dimensions in separate lists and cluster labels. Zips it to one list with 4-tuples.
"""
def format_cluster_data_3D(dataset, labels):
	return list(zip(dataset[0], dataset[1], dataset[2], labels))

"""
Clusters datapoints with DBScan.
Input: coordinates as separate lists, epsilon and minimum points in cluster
Output: db which contains labels on which cluster every point belongs to
"""
def cluster(coordinates, eps, min_samples):
	db = DBSCAN(eps=eps, min_samples=min_samples).fit(coordinates)
	labels = db.labels_
	print(labels)
	n_clusters_ = len(set(labels)) - (1 if -1 else 0)
	print('Estimated number of clusters: %d' % n_clusters_)
	return db
	#https://www.programcreek.com/python/example/103494/sklearn.cluster.DBSCAN


"""
2D-plots clusters.
Input: separate lists with coordinates, list with labels and tuple of axis labels, and color of dots
"""
def plot_2D_clusters(data_x, data_y, labels, axis_labels, color):
	plt.scatter(data_x, data_y, marker='o', edgecolor='black', c=color)

	# Add labels that do not overlap
	texts = []
	for label, x, y in zip(labels, data_x, data_y):
		texts.append(plt.text(x, y, label, size="7"))
	adjust_text(texts, arrowprops=dict(arrowstyle='-'))

	plt.xlabel(axis_labels[0])
	plt.ylabel(axis_labels[1])
	plt.show()

"""
3D-plots clusters.
Input: dataset with three separate dimensions, list of cluster number
"""
def plot_3D_clusters(dataset, clusters):
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(dataset[0], dataset[1], dataset[2], c=clusters)
	ax.set_xlabel('X: C2')
	ax.set_ylabel('Y: C3')
	ax.set_zlabel('Z: C5')
	plt.show()



"""
Creates list with data points that are inside standard deviation
Input: standard deviation, total number of tosses and list of number of heads for each toss
Output: List with numbers of data points
"""
def within_strd_dev(stdr_dev, N):
	tail_count = nr_of_tails()
	nrs = []
	for i in range(0, len(tail_count)):
		if tail_count[i] < (N/2 + stdr_dev) and tail_count[i] > (N/2 - stdr_dev):
			nrs.append(i)
	return nrs

"""
Returns a dataset with the values in the positions in keep kept and the rest removed.
Input: dataset with separate dimensions, list with indexes of elements to keep
Output: dataset with elements removed
"""
def remove_non_selected(dataset, keep):
	filtered_dataset = []
	for dimension in dataset:
		temp = []
		for i in range(0, len(dimension)):
			if i in keep:
				temp.append(dimension[i])
		filtered_dataset.append(temp)
	return filtered_dataset


dataset = create_dataset()

scaled_dataset = scale_data(dataset)

strd_dev = math.sqrt(0.5*0.5*200)
keep = within_strd_dev(strd_dev, 200)

filtered_scaled_dataset = remove_non_selected(scaled_dataset, keep)
#print(len(filtered_dataset[0]))


# ***** PCA ******
#pca = perform_pca(format_data_3D(filtered_dataset))
#plot_2D_clusters(pca[0], pca[1], keep, ("X: Pca1", "Y:Pca2"), 'red')



# ***** 2D plot of 3 dimensions *****
plot_2D_clusters(filtered_scaled_dataset[0], filtered_scaled_dataset[1], keep, ("X: C2", "Y:C3"), 'red')
plot_2D_clusters(filtered_scaled_dataset[0], filtered_scaled_dataset[2], keep, ("X: C2", "Y:C5"), 'blue')
plot_2D_clusters(filtered_scaled_dataset[1], filtered_scaled_dataset[2], keep, ("X: C3", "Y:C5"), 'green')

# **** Clustering ******
#db = cluster(format_data_3D(filtered_scaled_dataset), 0.13, 5)
#labels = db.labels_
#plot_3D_clusters(filtered_scaled_dataset, labels)

	
