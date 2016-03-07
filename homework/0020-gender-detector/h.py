from os.path import join, basename

datadirect= "tempdata"
csvpath=join('tempdata', 'wrangled2014.csv')
opencsv=open(csvpath, 'r')

newlist= []
for line in opencsv:
	year,name,gender,ratio,females,males,total = line.split(',')
	if ratio <= '60' and ratio != '100':
		newlist.append([name, gender, ratio, total.strip()])
def most(newlist):
	return int(newlist[3])

orderlist=sorted(newlist, key=most, reverse=True)

print("Most popular names with <= 60% gender skew:")
for x in range(0,5):
	print(orderlist[x][0].ljust(11), orderlist[x][1].rjust(1),
		orderlist[x][2], orderlist[x][3])