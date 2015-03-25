from heapq import heappush, heappop, heapify
from collections import defaultdict
import math

def encode(symb2freq):
    """Huffman encode the given dict mapping symbols to weights"""
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
 
txt = "this is an example for huffman encoding"
txtfile = open('output.txt','r')
#reshuff = open('chienhuff.txt','w')

#Count
#symb2freq = defaultdict(int)
single_both  = defaultdict(int)
single_left  = defaultdict(int)
single_right = defaultdict(int)
diff_left    = defaultdict(int)
diff_right   = defaultdict(int)
diff_both    = defaultdict(int)
diff_lr      = defaultdict(int)
diff_diff    = defaultdict(int)

#To Count
prev_diff_l  = 0
prev_diff_r  = 0
prev_diff_b  = 0
prev_diff_d  = 0
 
for line in txtfile:
    	temp = line.split(',')
    	temp[0] = int(float(temp[0]) * 32768)
    	temp[1] = int(float(temp[1]) * 32768)
    	#symb2freq[(temp[0]-prev)] += 1	
    	#symb2freq[temp[1]-temp[0]-prev] += 1
    	#prev = temp[1] - temp[0]

	#Single Channel
	#BOTH
	single_both[temp[0]] += 1
	single_both[temp[1]] += 1

	#LEFT
	single_left[temp[0]] +=1

	#RIGHT 
	single_right[temp[1]] += 1

	#Difference single
	#LEFT
	diff_left[(temp[0] - prev_diff_l)] += 1
	prev_diff_l = temp[0]

	#RIGHT
	diff_right[(temp[1] - prev_diff_r)] += 1
	prev_diff_r = temp[1]

	#Difference - Both channel one after the other
	diff_both[(temp[0] - prev_diff_b)] += 1
	diff_both[(temp[1] - temp[0])] += 1
	prev_diff_b = temp[1]
	
	#Difference between left and right
	diff_lr[(temp[0] - temp[1])] += 1

	#Difference of difference between left and right 
	diff_diff[(temp[0] - temp[1] - prev_diff_d)] += 1
	prev_diff_d = temp[0] - temp[1]

#Encoding into huffman
#huff = encode(symb2freq)
huff_sing_both  = encode(single_both)
huff_sing_left  = encode(single_left)
huff_sing_right = encode(single_right)
huff_diff_left  = encode(diff_left)
huff_diff_right = encode(diff_right)
huff_diff_both  = encode(diff_both)
huff_diff_lr    = encode(diff_lr)
huff_diff_diff  = encode(diff_diff)
#reshuff.write("Symbol\tWeight\tHuffman Code\n")

total_sing_both = 0
for p in huff_sing_both:
	total_sing_both += single_both[p[0]]
total_sing_left = 0
for p in huff_sing_left:
        total_sing_left +=  single_left[p[0]]
total_sing_right = 0
for p in huff_sing_right:
        total_sing_right += single_right[p[0]]
total_diff_left = 0
for p in huff_diff_left:
        total_diff_left += diff_left[p[0]]
total_diff_right = 0
for p in huff_diff_right:
        total_diff_right += diff_right[p[0]]
total_diff_both = 0
for p in huff_diff_both:
        total_diff_both += diff_both[p[0]]
total_diff_lr = 0
for p in huff_diff_lr:
        total_diff_lr += diff_lr[p[0]]
total_diff_diff = 0
for p in huff_diff_diff:
        total_diff_diff += diff_diff[p[0]]


##Calculating Entropy
entropy = 0.0
avglength = 0.0
for p in huff_sing_both:
	prob = float(single_both[p[0]])/total_sing_both
	#reshuff.write("%f \n"% (prob))
	entropy = entropy + ((prob*math.log(prob))/math.log(2))
	avglength = avglength + prob*(len(str(p[1])))
print "Single Channel Both"
print ("Entropy = %f" % (-1*entropy))
print ("Average Length = %f \n" % (avglength))

entropy = 0.0
avglength = 0.0
for p in huff_sing_left:
        prob = float(single_left[p[0]])/total_sing_left
        #reshuff.write("%f \n"% (prob))
        entropy = entropy + ((prob*math.log(prob))/math.log(2))
        avglength = avglength + prob*(len(str(p[1])))
print "Single Channel Left"
print ("Entropy = %f" % (-1*entropy))
print ("Average Length = %f \n" % (avglength))

entropy = 0.0
avglength = 0.0
for p in huff_sing_right:
        prob = float(single_right[p[0]])/total_sing_right
        #reshuff.write("%f \n"% (prob))
        entropy = entropy + ((prob*math.log(prob))/math.log(2))
        avglength = avglength + prob*(len(str(p[1])))
print "Single Channel Right"
print ("Entropy = %f" % (-1*entropy))
print ("Average Length = %f \n" % (avglength))

entropy = 0.0
avglength = 0.0
for p in huff_diff_left:
        prob = float(diff_left[p[0]])/total_diff_left
        #reshuff.write("%f \n"% (prob))
        entropy = entropy + ((prob*math.log(prob))/math.log(2))
        avglength = avglength + prob*(len(str(p[1])))
print "Difference Channel Left"
print ("Entropy = %f" % (-1*entropy))
print ("Average Length = %f \n" % (avglength))

entropy = 0.0
avglength = 0.0
for p in huff_diff_right:
        prob = float(diff_right[p[0]])/total_diff_right
        #reshuff.write("%f \n"% (prob))
        entropy = entropy + ((prob*math.log(prob))/math.log(2))
        avglength = avglength + prob*(len(str(p[1])))
print "Difference Channel Right"
print ("Entropy = %f" % (-1*entropy))
print ("Average Length = %f \n" % (avglength))

entropy = 0.0
avglength = 0.0
for p in huff_diff_both:
        prob = float(diff_both[p[0]])/total_diff_both
        #reshuff.write("%f \n"% (prob))
        entropy = entropy + ((prob*math.log(prob))/math.log(2))
        avglength = avglength + prob*(len(str(p[1])))
print "Difference Channel Both (one after the other)"
print ("Entropy = %f" % (-1*entropy))
print ("Average Length = %f \n" % (avglength))

entropy = 0.0
avglength = 0.0
for p in huff_diff_lr:
        prob = float(diff_lr[p[0]])/total_diff_lr
        #reshuff.write("%f \n"% (prob))
        entropy = entropy + ((prob*math.log(prob))/math.log(2))
        avglength = avglength + prob*(len(str(p[1])))
print "Difference between Channels (L-R)"
print ("Entropy = %f" % (-1*entropy))
print ("Average Length = %f \n" % (avglength))

entropy = 0.0
avglength = 0.0
for p in huff_diff_diff:
        prob = float(diff_diff[p[0]])/total_diff_diff
        #reshuff.write("%f \n"% (prob))
        entropy = entropy + ((prob*math.log(prob))/math.log(2))
        avglength = avglength + prob*(len(str(p[1])))
print "Difference between Difference of channels (L-R)"
print ("Entropy = %f" % (-1*entropy))
print ("Average Length = %f \n" % (avglength))
