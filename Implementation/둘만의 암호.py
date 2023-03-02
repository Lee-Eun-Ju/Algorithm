skip = 'abcdefghij'; s = "z"; index = 20

english = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
english = english.split()
english_skip = [i for i in english if i not in skip]

answer=''
for j in s:
    k = english_skip.index(j)
    if (k+index)>(2*len(english_skip)-1):
        answer += english_skip[(k+index)-2*len(english_skip)]
    elif (k+index)>(len(english_skip)-1):
        answer += english_skip[(k+index)-len(english_skip)]
    else:
        answer += english_skip[(k+index)]

answer   