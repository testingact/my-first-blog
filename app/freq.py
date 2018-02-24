from konlpy.tag import Twitter
from collections import Counter
import pandas as pd
import csv
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

file_dir = "C:/Users/Ronaldo/Desktop/crawling_save/"
result_dir = "C:/Users/Ronaldo/Desktop/text_analysis/"

def get_tags(text, ntags=50):
    spliter = Twitter()
    nouns = spliter.nouns(text)
    count = Counter(nouns)
    return_list = []
    for n, c in count.most_common(ntags):
        temp = {'tag': n, 'count': c}
        return_list.append(temp)
    return return_list

def make_word_freq(output_file_name, noun_count):
    #open_text_file = open(file_dir + txt_file_name, 'r', encoding="utf-8")
    text = csv.reader("C:/Users/Ronaldo/Desktop/crawling_save/result.csv")
    tags = get_tags(text, noun_count)
    #open_text_file.close()
    open_output_file = open(result_dir + output_file_name, 'w')
    df = pd.DataFrame(columns=["word", "freq"])
    for tag in tags:
        noun = tag['tag']
        count = tag['count']
        row = [noun, count]
        df.loc[len(df)] = row
    df.to_csv(open_output_file)
    open_output_file.close()
    return df

'''
f = pd.read_csv("C:/Users/Ronaldo/Desktop/crawling_save/result.csv")
keep_col = ['타이틀','본문']
new_f = f[keep_col]
new_f.to_csv("C:/Users/Ronaldo/Desktop/crawling_save/newFile.csv", index=False)
'''
def word_freq(csv_file):
    words = []
    words = csv_file['본문'].tolist()
    word = ' '.join(words)
    spliter = Twitter()
    nouns = spliter.nouns(word)
    count = Counter(nouns)
    df = pd.DataFrame(columns=["word", "freq"])
    for n, c in count.most_common(50):
        df.loc[len(df)] = [n, c]
    df.plot(kind='bar', x='word', y='freq', color='grey', legend=None)
    plt.xticks(rotation=90)
    plt.show()

#text = csv.reader("C:/Users/Ronaldo/Desktop/crawling_save/result.csv")
#d = pd.read_csv("C:/Users/Ronaldo/Desktop/crawling_save/newFile.csv", encoding='utf-8')

'''
words= []
with open("C:/Users/Ronaldo/Desktop/crawling_save/result.csv", 'r', encoding='utf-8') as text:
    reader = pd.read_csv(text, delimiter=',', encoding='utf-8')
    print(type(reader))
    #print(reader['타이틀'])
    #reader = reader.drop('주소', 1)
    #print(reader)
    words = reader['본문'].tolist()
    print(words)
    #next(reader)
    #for row in reader:
    #    print(row)

word = ' '.join(words)
spliter = Twitter()
nouns = spliter.nouns(word)
count = Counter(nouns)
v1 = pd.Series(nouns)
v2 = pd.Series(count)
print(type(v1))
print(type(count))
print(count)
df = pd.DataFrame(columns=["word", "freq"])
print(len(df))
for n, c in count.most_common(50):
    df.loc[len(df)] = [n, c]

print(df)
print(len(df))
plt.barh(range(0, len(df)), df['freq'])
plt.yticks(range(0, len(df)), df['word'])
plt.gca().invert_yaxis()
#df.plot(kind='bar', x='word', y='freq', color='grey', legend=None)
#plt.xticks(rotation=90)
plt.show()
'''
'''

return_list = {'item': []}
for n, c in count.most_common(50):
    temp = {'tag': n, 'count': c}
    return_list['item'].append(temp)
tags=[]
counts=[]
for i in range(0, len(return_list['item'])):
    tag = return_list['item'][i]['tag']
    count = return_list['item'][i]['count']
    tags.append(tag)
    counts.append(count)
print(len(return_list['item']))

plt.bar(tags, counts)
plt.xticks(rotation=90)
plt.show()
print(words)
print('------------')
print(word)
print('------------')
print(type(return_list))
print(return_list)
print('------------')
print(nouns)
print('------------')
print(count)
print(type(count))
'''
'''    
#print(len(d))
with open('C:/Users/Ronaldo/Desktop/crawling_save/output.txt', 'w', encoding='uft-8') as f:
    with open("C:/Users/Ronaldo/Desktop/crawling_save/result.csv", 'r', encoding='utf-8') as text:
        reader = csv.reader(text)
        next(reader)
        for row in reader:
            title = row[1]
            content = row[2]
            f.write(title)
            f.write('/')
            f.write(content)
            f.write('\n')
    f.close()


with open("C:/Users/Ronaldo/Desktop/crawling_save/result.csv", 'r') as text:
    reader = csv.reader(text)
    next(reader)
    for row in reader:
        print(row)
'''
'''
for row in text:
    #title = row.str.replace(',', ' ')
    title = row
    #content = row[1]
    with open('C:/Users/Ronaldo/Desktop/crawling_save/output.txt', 'w') as f:
        f.write(title)
        #f.write(content)
f.close()
'''

'''
words_counted = []
for i in words:
  x = words.count(i)
  words_counted.append((i, x))

with open('C:/Users/Ronaldo/Desktop/crawling_save/output.csv', 'wb') as f:
  writer = csv.writer(f)
writer.writerows(edgl)
set(words_counted)
'''
#df = make_word_freq("word_freq.csv", 100)
#print(df)

