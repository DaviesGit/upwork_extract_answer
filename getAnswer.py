import sys
for fileName in sys.argv:
##for fileName in ["5_4.9.simplify.txt"]:
    if __file__==fileName:
        continue
    with open(fileName, mode='r',encoding='utf-8', errors='ignore') as file:
        origin = file.read()
        outputFileName = file.name
        outputFileSimplify = outputFileName.replace('.txt', '.Answer.txt')
        file.close()
    loca1 = loca2 = 0
    tempL = strLen = n = 0
    answer = answerTemp = questionID = finalAnswer = ''
    while True:
        loca1 = origin.find('question_id:', loca2) + 13
        if loca1 < 13:
            break
        loca2 = origin.find(' ', loca1)
        tempL=origin.find('\n', loca1)
        if (-1==loca2) | (tempL<loca2):
            loca2=loca1
            continue
            
        questionID = origin[loca1:loca2]
        while 7 > len(questionID):
            questionID += ' '
        loca1 = loca2 + 1
        while ' '==origin[loca1:loca1+1]:
            loca1+=1
        loca2 = origin.find('\n', loca1)
        tempL = origin.find('\r', loca1)
        if (tempL < loca2) & (-1 != tempL):
            loca2 = tempL
        answerTemp = origin[loca1:loca2]
        strLen = len(answerTemp)
        answer = ''
        for n in range(strLen):
            if n+1 == strLen:
                answer += "'" + answerTemp[n:n+1] + "'"
            else:
                answer += "'" + answerTemp[n:n+1] + "',"
        answer = '[' + answer + ']'
        finalAnswer += questionID + ':' + answer + '\n'
    with open(outputFileSimplify, mode='x',encoding='utf-8', errors='ignore') as fileSimplify:
        fileSimplify.write(finalAnswer)
