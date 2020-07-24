def most_frequent(word):
    word_set=set(word)
    word_dict=dict()
    for ele in word_set:
        word_dict[ele]=word.count(ele)
    word_dict=sorted(word_dict.items(),key=lambda x:x[1],reverse=True)
    for i in word_dict:
        print(i[0],"=",i[1])
        

string=input()
most_frequent(string)







