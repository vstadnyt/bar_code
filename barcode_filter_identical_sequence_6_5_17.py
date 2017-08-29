#This code text an input file with two columns 
# #		Barcode
# 1		aaagggttcccc 
# 2		aaagggttcccc 
# 3		aaagggttcccc 
# 4		...........
# 5		...........
# and cleans it with the follosing constrain: It keeps only barcode that do not have more than requested amount of identical letters in a series.
# The output file has the same format as the input file.
# Created by Valentyn Stadnytskyi, valentyn@purdue.edu from Purdue University
# Please, email me if you have any questions or need help with the code. I will be glad to help.
# Date of creating Jun 6, 2017
# Python version: 2.7.12 |Anaconda 4.1.1 (64-bit)| (default, Jun 29 2016, 11:07:13) [MSC v.1500 64 bit (AMD64)]

#input text file
print 'Enter the file name with .txt at the end. File has to be in the same directory'

# ask the desired number of bases in barcode
filename = str(raw_input("filename:"))

print 'how many sequencial letters shouldm not appear in the barcode'

# ask the desired number of bases in barcode
seq_length = int(raw_input("number of unwanted letters in a series:"))

barfile = open(filename, 'r')

a = barfile.read()
my_list = a.splitlines()
head, sep, tail = my_list[1].partition('\t')
my_list_short = []
for j in range(len(my_list)):
    head, sep, tail = my_list[j].partition('\t')
    my_list_short.append(tail)
    
    
import re
import time
my_list_clean = []

for j in range(len(my_list_short)):
    flag = True
    m = re.search('a{' + str(seq_length)+',}',my_list_short[j])
    if m:
        flag = False
        #print 'aaa'
        #print j
    m = re.search('c{' + str(seq_length)+',}',my_list_short[j])
    if m:
        flag = False
        #print 'ccc'
        #print j
    m = re.search('t{' + str(seq_length)+',}',my_list_short[j])
    if m:
        flag = False
        #print 'ttt'
        #print j
    m = re.search('g{' + str(seq_length)+',}',my_list_short[j])
    if m:
        flag = False
        #print 'ggg'
        #print j
    if flag:
        my_list_clean.append(my_list_short[j])
       
    
    
my_list_clean_final = []
new_filename =  str(int(time.time())) + '_clean_' + str(seq_length)+ '_' + filename 
thefile = open(new_filename, 'w')
for j in range(len(my_list_clean)):
    my_list_clean_final.append(str(j) + '\t' + my_list_clean[j])
    print>>thefile, str(j) + '\t' + my_list_clean[j]
print 'The length of new file is: ' + str(len(my_list_clean)) + ' barcodes out of original ' + str(len(my_list))
thefile.close()