from os.path import join, basename
from glob import glob
datadirect= 'tempdata'
allfiles_path= join(datadirect, '*.txt')
allfiles_names = glob(allfiles_path)

namefiles= []
for filename in allfiles_names:
	bname = basename(filename)
	year = bname[3:7]
	if int(year) >= 1950:
		namefiles.append(filename)
#gives us a list of all the names of the txt files that
#we will want to call on
genderdict = {'M':0, 'F':0}
for x in namefiles:
    babyfile = open(x, "r")
    for line in babyfile:
        name, gender, number = line.split(',')
        genderdict[gender] += int(number)


print("F:", str(genderdict['F']).rjust(6),
      "M:", str(genderdict['M']).rjust(6))


f_to_m_ratio = round(100 * genderdict['F'] / genderdict['M'])
print("F/M baby ratio:", f_to_m_ratio)


