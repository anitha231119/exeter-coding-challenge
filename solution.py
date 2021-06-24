#Importing required packages
import time
import csv
import pandas
import os
import psutil
from tqdm import tqdm

#Program execution start time
#The t8.shakespeare text document is read
st_time = time.time();
with open("./t8.shakespeare.txt") as content:
    sentence = content.read()

#Frequency is counted
def count(word_dict):
    #temp_dict consist of key value pairs
    #element is the key in temp_dict
    for element in tqdm(word_dict):
        #doc variable consist of all data from t8.shakespeare.txt
        with open("t8.shakespeare.txt") as doc:
            #sentence consist of data in each line
            for sentence in doc:
                #term consist each word in sentence
                for term in sentence.split():
                    #if term and element matches, count is incremented
                    if element == term:
                        word_dict[element]= word_dict[element]+1
    return word_dict

#Function to replace words
def Replace(text, wordDict):
    print("Translating the Shakespeare.txt to possible French Words!")
    for key in tqdm(wordDict):
        #Replace english word with french word
        text = text.replace(key, wordDict[key])
    return text

#french_dictionary.csv file is read in file_reader variable
file_reader = csv.reader(open(r'./french_dictionary.csv', 'r'))
print("Reading the French Dictionary and converting it into a Python Dictionary...")
#Empty list to store key value pairs
french_dict = {}

#To iterate over each value
for field in file_reader:
   #field consist of key and value
   #key is eng and value is french
   key, value = field
   french_dict[key] = value
print("Python dictionary --> 'french_dict has been successfully created")
   
string_new = Replace(sentence, french_dict)
file = open(r'./Result/t8.shakespeare.translated.txt', mode = "w")
file.write(string_new)
file.close()
print("Translated text stored in Results Directory..")

#empty dictionary to store key value pairs
word_dict = {}
#find_words consist of all data from find_words.txt
with open("find_words.txt") as find_words:
    # data in everline is stored in terms
    for terms in find_words:
        # removing new line character in each term and storing in key
        key = terms.rstrip("\n")
        # value of key is assigned as 0 in temp_dict
        word_dict[key] = 0
temp_dict = count(word_dict)

#Storing data in csv file
english_wd=[]
french_wd=[]
count=[]

for element in temp_dict.keys():
    english_wd.append(element)
    french_wd.append(french_dict[element])
    count.append(temp_dict[element])

end_frame = {'Words-English':english_wd,'Words-French':french_wd,'Count':count}
dataframe = pandas.DataFrame(end_frame)
print("Writing the english word, french word equivalent along with count to csv file..")
dataframe.to_csv(r'./Result/frequency.csv')
print("CSV File saved successfully in Results directory..")

#Time and Memory Calculation
#Calculating stop time
sp_time = time.time()
#Total_time is the total time taken in seconds
total_time = sp_time - st_time
#Conversion of seconds to minutes
minutes = total_time // 60
#Conversion to seconds
seconds = total_time % 60
#print("Time taken to process : %d minutes %d seconds" % (minutes, seconds))
total_memory = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
#print(f"Memory Used : {round(total_memory,2)} MB")

with open("./Result/Performance.txt", mode = "w") as per:
    per.write("Performance of Translator\n")
    per.write(f"Time taken to process : {round(minutes,0)} minutes {round(seconds,0)} seconds\n")
    per.write(f"Memory Used : {round(total_memory,2)} MB\n")
print("Performance text file is generated in Result directory..")