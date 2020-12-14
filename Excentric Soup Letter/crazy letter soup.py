import string

def minus1Boundaries(x, y):
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    return (x,y)
def plus1Boundaries(x, y, maxX, maxY):
    if x > maxX:
        x = maxX
    if y > maxY:
        y = maxY
    return (x,y)

def aux(matrix, word, wordSeeker, lineN, columnN, count, oldLine, oldColumn):
        if wordSeeker == word[-1] and count == len(word)-1:              #checks if its done
            values = {}
            for index, letter in enumerate(string.ascii_uppercase):
                values[index] = letter
            return (str(values[oldLine]) + str(oldColumn+1))       
        if len(wordSeeker) == len(word):
            return "overflow"
        print(columnN, lineN, matrix[lineN][columnN])
        
        (xm, ym) = minus1Boundaries(columnN-1, lineN-1)
        (xp, yp) = plus1Boundaries(columnN+1, lineN+1, len(matrix[0])-1, len(matrix)-1)
        
        count += 1
        a= word[count]
        print(word[count])
        print(wordSeeker)

        if matrix[ym][xm] == word[count]:       ##check all 8 positions around for next letter in word
            wordSeeker = matrix[ym][xm]
            result2 = aux(matrix, word, wordSeeker, ym, xm, count, oldLine, oldColumn)
            if result2 != None:
                return result2
        
        if matrix[ym][columnN] == word[count]:
            wordSeeker = matrix[ym][columnN]
            result2 = aux(matrix, word, wordSeeker, ym, columnN, count, oldLine, oldColumn)
            if result2 != None:
                return result2
        
        if matrix[ym][xp] == word[count]:
            wordSeeker = matrix[ym][xp]
            result2 = aux(matrix, word, wordSeeker, ym, xp, count, oldLine, oldColumn)
            if result2 != None:
                return result2
        
        if matrix[lineN][xp] == word[count]:
            wordSeeker = matrix[lineN][xp]
            result2 = aux(matrix, word, wordSeeker, lineN, xp, count, oldLine, oldColumn)
            if result2 != None:
                return result2
        if matrix[yp][xp] == word[count]:
            wordSeeker = matrix[yp][xp]
            result2 = aux(matrix, word, wordSeeker, yp, xp, count, oldLine, oldColumn)
            if result2 != None:
                return result2
        if matrix[yp][columnN] == word[count]:
            wordSeeker = matrix[yp][columnN]
            result2 = aux(matrix, word, wordSeeker, yp, columnN, count, oldLine, oldColumn)
            if result2 != None:
                return result2
        if matrix[yp][xm] == word[count]:
            wordSeeker = matrix[yp][xm]
            result2 = aux(matrix, word, wordSeeker, yp, xm, count, oldLine, oldColumn)
            if result2 != None:
                return result2
        if matrix[lineN][xm] == word[count]:
            wordSeeker = matrix[lineN][xm]
            result2 = aux(matrix, word, wordSeeker, lineN, xm, count, oldLine, oldColumn)
            if result2 != None:
                return result2
            
def soup(matrix, word):
    for line in matrix:             #visualizar
        print(line)    
    for lineN in range(0, len(matrix)):            #experimentar cada caso
        for columnN in range(0, len(matrix[lineN])):
            wordSeeker = ""
            if matrix[lineN][columnN] != word[0]: #stop if first letter is not in word
                continue
            else:                                     #else run aux function
                wordSeeker += matrix[lineN][columnN]
                result = aux(matrix, word, wordSeeker, lineN, columnN, 0, lineN, columnN) 
                if result != None:
                    return result

print(soup(  (('J', 'D', 'C', 'P', 'C', 'P', 'X', 'O', 'A', 'A'), ('Z', 'X', 'V', 'O', 'V', 'X', 'F', 'R', 'V', 'V'), ('N', 'D', 'L', 'E', 'I', 'R', 'B', 'I', 'E', 'A'), ('Y', 'T', 'R', 'Q', 'O', 'M', 'O', 'I', 'I', 'O'), ('F', 'Z', 'Z', 'A', 'P', 'Z', 'E', 'R', 'T', 'Q'), ('X', 'A', 'U', 'E', 'O', 'E', 'O', 'O', 'T', 'O'), ('P', 'O', 'R', 'T', 'U', 'O', 'A', 'Z', 'L', 'Z'), ('C', 'Z', 'N', 'O', 'Q', 'U', 'P', 'U', 'O', 'P')), 'PORTO'   ))
