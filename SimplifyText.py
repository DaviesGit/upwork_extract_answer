import sys
for fileName in sys.argv:
#for fileName in ["4_3.9.txt.back"]:
    if __file__ == fileName:
        continue
    with open(fileName, mode='r',encoding='utf-8', errors='ignore') as file:
        origin = file.read()
        outputFileName = file.name
        outputFileSimplify = outputFileName.replace('.txt', '.simplify.txt')
        file.close()
    loca1 = loca2 = loca3 = loca4 = 0
    tempL1 = tempL2 = tempL3 = 0
    n = n1 = n2 = n3 = 0
    questionNumber = question = notice = option = questionID = ''
    simplify = ''
    while True:
        loca1 = origin.find('<h2 class="oH2Low">', loca2) + 19;
        if loca1 < 19:
            break
        loca2 = origin.find('</h2>', loca1)
        questionNumber = origin[loca1:loca2]
        simplify += '    ' + questionNumber + '\r\n\r\n'
        loca1 = origin.find('<p class="oTxtMed"></p><pre>', loca2) + 28;
        loca2 = origin.find('</pre><p></p>', loca1);
        question = origin[loca1:loca2]
        simplify += question + '\r\n'
        tempL1 = origin.find('<p class="oGood" style="font-weight: bold;">', loca2) + 44;
        tempL2 = origin.find('<pre class="np">', loca2) + 16;
        if (tempL1 < tempL2) & (44 < tempL1):
            loca1 = tempL1;
            loca2 = origin.find('</p>', loca1);
            notice = origin[loca1:loca2]
            simplify += '  ' + notice + '\r\n'
        simplify += '\r\n'
        tempL1 = origin.find('name="question_id" type="hidden" value="', loca2) + 40;
        while True:
            loca1 = origin.find('<pre class="np">', loca2) + 16;
            if (tempL1 < loca1) | (loca1 < 16):
                break
            loca2 = origin.find('</pre>', loca1);
            option = origin[loca1:loca2]
            simplify += ' -> ' + option + '\r\n'
        loca1 = origin.find('name="question_id" type="hidden" value="', loca2) + 40;
        loca2 = origin.find('">', loca1)
        questionID = origin[loca1:loca2]
        simplify += '\r\n      question_id: ' + questionID + '\r\n\r\n\r\n'
    simplify = simplify.replace('&gt;', '>').replace('&lt;', '<').replace('<p>', '').replace('</p>', '')
    with open(outputFileSimplify, mode='x',encoding='utf-8', errors='ignore') as fileSimplify:
        fileSimplify.write(simplify)


