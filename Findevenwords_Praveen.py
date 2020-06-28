st_2 = 'Print every word in this sentence that has an even number of letters'
spl = st_2.split(' ')
for word in spl:
    if len(word) % 2 == 0:
        print("even!: ", 'The word in the sentence:', word, '. The length of word:', len(word))

print("Program ended....")