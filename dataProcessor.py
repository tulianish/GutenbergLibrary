import time
import datetime
from pymongo import MongoClient

count = 0
processed = 0

client = MongoClient('localhost', 27017)
db = client['gutenberg']
collection = db['books']

for year in range(1996,2021):
    start_time = datetime.datetime.now()
    # if year>1996:
    #   time.sleep(5)
    f = open('GutenbergData/GUTINDEX.'+ str(year) +'.txt', 'r')

    lines = [line for line in f.readlines() if line.strip()]
    total_lines = len(lines)

    for linenumber, line in enumerate(lines):
        currentline = (line.strip()).split()
        cur_length = (len(currentline))

        if linenumber < total_lines - 1:
            nextline_ = (lines[linenumber + 1].strip()).split()
            nl_length = len(nextline_)
            counter = 2
            if not (nextline_[nl_length - 1].isdigit()):
                while (linenumber+counter)<(linenumber-1):
                    next_to_next_line = (lines[linenumber + counter].strip()).split()
                    nn_length = len(next_to_next_line)
                    if next_to_next_line[nn_length - 1].isdigit():
                        break
                    else:
                        counter = counter + 1

        if 'by' not in currentline and 'by' not in nextline_:
            continue

        if 'by' not in currentline and 'by' in nextline_ and currentline[cur_length - 1].isdigit():
            book_number = currentline[cur_length - 1]
            currentline = currentline + nextline_
            bypos = currentline.index('by')
            numpos = currentline.index(book_number)
            book_name = ''
            author = ''
            for x in range(0, bypos):
                if book_name == '':
                    book_name = (book_name + currentline[x])
                elif book_name!='' and currentline[x]!=book_number:
                    book_name = (book_name + ' ' + currentline[x])
                    book_name = book_name.replace(',', '')
            book_name = book_name.replace('.', '')
            for x in range(bypos +1, len(currentline)):
                if author == '':
                    author = (author + currentline[x])
                else:
                    author = (author + ' ' + currentline[x])
            author = author.replace('.', '')
            print(book_number)
            document = { 'book_id' : processed ,'author' : author , 'book_name': book_name }
            print(document)
            collection.insert(document)
            count = count + 1
            processed += 1
            continue

        if 'by' in currentline and currentline[cur_length - 1].isdigit() and not ('[Language:' in nextline_):
            book_number = currentline[cur_length - 1]
            bypos = currentline.index('by')
            numpos = currentline.index(book_number)
            book_name = ''
            author = ''
            for x in range(0,bypos):
                if book_name =='':
                    book_name = (book_name + currentline[x])
                else:
                    book_name = (book_name + ' ' + currentline[x])
            book_name = book_name.replace(',','')
            book_name = book_name.replace('.', '')
            for x in range(bypos+1,numpos):
                if author == '':
                    author = (author + currentline[x])
                else:
                    author = (author + ' ' + currentline[x])
            author = author.replace('.', '')
            print(book_number)
            count = count + 1
            processed += 1
            document = {'book_id' : processed, 'author': author, 'book_name': book_name}
            print(document)
            collection.insert_one(document)


        if 'by' in currentline and currentline[cur_length - 1].isdigit() and ('[Language:' in nextline_):
            print("Discarded " + currentline[cur_length - 1])
            processed += 1

        continue
    end_time=datetime.datetime.now()
    each_time = end_time-start_time
    print(str(year) + " - " + str(each_time))
print("Total Records touched :" + str(processed))
print("Total Cleaned records found: " + str(count))