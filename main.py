
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow
from tkinter import filedialog
import sys
from numpy.random import randint


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
ui.pushButton_5.setVisible(False)
ui.pushButton_5.setCheckable(False)
ui.progressBar.setMaximum(1)
ui.progressBar.setValue(0)
lastWordNum = [1]
currentOpenedFile = [None]
words = {}

def addWord(lastWordNum, words):
    word = ui.lineEdit.text()
    translation = ui.lineEdit_2.text()
    if word == '':
        word = 'None'
    if translation == '':
        translation = 'None'
    ui.textEdit.append(f'{lastWordNum[0]} {word.capitalize()} - {translation.capitalize()}')
    words[str(lastWordNum[0])] = [word.capitalize(), '-', translation.capitalize(), '\n']
    ui.spinBox.setMaximum(lastWordNum[0])
    if lastWordNum[0] > 1:
        ui.progressBar.setMaximum(ui.progressBar.maximum() + 1)
    lastWordNum[0] += 1



def convertToTextEditText(words):
    a = 1
    text = ''
    for i in range(len(words)):
        key = str(i + 1)
        textPart = f'{a} {words[key][0]} {words[key][1]} {words[key][2]} {words[key][3]}'
        text = ''.join((text, textPart))
        a += 1

    text = text[:-2]
    ui.textEdit.clear()
    ui.textEdit.setText(text)

def changeWord(words):
    wordNum = ui.spinBox.text()
    newWord = ui.lineEdit.text()
    newTranslation = ui.lineEdit_2.text()
    words[str(wordNum)][0] = newWord.capitalize()
    words[str(wordNum)][2] = newTranslation.capitalize()
    convertToTextEditText(words)

def deleteWord(words, lastNum):
    wordNum = ui.spinBox.text()
    if lastNum[0] > 1:
        del words[str(wordNum)]
        a = 1
        newWords = {}
        for (key, value) in words.items():
            newWords[str(a)] = value
            a += 1
        words.clear()
        for i in range(len(newWords)):
            words[str(i + 1)] = newWords[str(i + 1)]
        convertToTextEditText(words)
        lastNum[0] -= 1
        ui.spinBox.setMaximum(lastNum[0] - 1)
        if ui.spinBox.maximum() < 1:
            ui.spinBox.setMaximum(1)
            ui.spinBox.setMinimum(1)
        if ui.progressBar.maximum() > 1:
            ui.progressBar.setMaximum(ui.progressBar.maximum() - 1)

def startPlay(words):
    playedWordsList = []
    if ui.pushButton_4.text() == 'Почати':
        ui.progressBar.setValue(0)
        ui.pushButton_4.setText('Зупинити')

        ui.textEdit.setVisible(False)
        ui.frame.setVisible(False)
        ui.pushButton_5.setVisible(True)
        lt = list(words.items())
        for a in range(len(lt)):
            playedWordsList.append([lt[a][1][0], lt[a][1][2]])



        if ui.radioButton.isChecked():
            type = 'wtt'

        elif ui.radioButton_2.isChecked():
            type = 'ttw'

        elif ui.radioButton_3.isChecked():
            type = 'r'
        word = [None]
        rightAnswer = [None]
        word[0], rightAnswer[0] = setNewWord(playedWordsList, type)
        ui.pushButton_5.clicked.connect(lambda: checkIsTheAnswerRight(rightAnswer, playedWordsList, word, type))
        return
    else:
        ui.textEdit.setVisible(True)
        ui.frame.setVisible(True)
        ui.pushButton_5.setVisible(False)
        ui.lineEdit_4.setText('')
        ui.lineEdit_3.setText('')
        ui.pushButton_4.setText('Почати')
        try:
            ui.pushButton_5.disconnect()
        except:
            pass




def setNewWord(wordList, type):
    rightAnswer = [None]
    word = [None]
    if len(wordList) > 0:

        word[0] = wordList[randint(0, len(wordList))]
        if type == 'wtt':
            ui.lineEdit_3.setText(word[0][0])
            rightAnswer[0] = word[0][1]
            rightAnswer[0] = multiplyAnswersSet(rightAnswer)

        elif type == 'ttw':
            ui.lineEdit_3.setText(word[0][1])
            rightAnswer[0] = word[0][0]
            rightAnswer[0] = multiplyAnswersSet(rightAnswer)

        elif type == 'r':
            a = randint(0, 2)
            if a == 0:
                ui.lineEdit_3.setText(word[0][0])
                rightAnswer[0] = word[0][1]
                rightAnswer[0] = multiplyAnswersSet(rightAnswer)


            elif a == 1:
                ui.lineEdit_3.setText(word[0][1])
                rightAnswer[0] = word[0][0]
                rightAnswer[0] = multiplyAnswersSet(rightAnswer)
        return word[0], rightAnswer[0]
    else:
        ui.textEdit.setVisible(True)
        ui.frame.setVisible(True)
        ui.pushButton_5.setVisible(False)
        ui.lineEdit_4.setText('')
        ui.lineEdit_3.setText('')
        ui.pushButton_4.setText('Почати')
        return word[0], rightAnswer[0]

def multiplyAnswersSet(rightAnswer):
    lt = rightAnswer[0]
    if ',' in lt:
        comletedList = []
        commaAmount = lt.count(',')
        for i in range(commaAmount):
            commaIndex = lt.index(',')
            a = lt[:commaIndex]
            lt = lt[commaIndex + 2:]
            comletedList.append(a.capitalize())
        comletedList.append(lt.capitalize())
        return comletedList
    else:
        return rightAnswer[0]

def checkIsTheAnswerRight(rightAnswer, wordlist, word, type):
    writtenWord = ui.lineEdit_4.text()
    if writtenWord.capitalize() in rightAnswer[0]:
        ui.progressBar.setValue(ui.progressBar.value() + 1)
        if word[0] in wordlist:
            wordlist.pop(wordlist.index(word[0]))
            word[0], rightAnswer[0] = setNewWord(wordlist, type)

    else:
        ui.lineEdit_4.setText("Неправильно")

def openFile(words, lastWordNum, openedFile):
    filename = filedialog.askopenfilename()
    file = open(filename, 'r')
    openedFile[0] = filename
    words.clear()
    ui.textEdit.clear()
    lastWordNum[0] = 0
    counter = 1
    for line in file:
        lt = line.split()
        if '-' in line:
            defIndex = lt.index('-')
            word = ' '.join(lt[:defIndex])
            translation = ' '.join(lt[defIndex + 1:])
            words[str(counter)] = [word.capitalize(), '-', translation.capitalize(), '\n']
            counter += 1
    lastWordNum[0] = counter
    ui.progressBar.setMaximum(counter - 1)
    convertToTextEditText(words)
    file.close()

def saveAsFile(words, openedFile):
    filename = filedialog.asksaveasfilename()
    file = open(filename, 'w')
    openedFile[0] = filename
    for i in range(len(words)):
        value = words[str(i+1)]
        line = f'{value[0]} - {value[2]}\n'
        file.write(line)
    file.close()

def saveFile(words, openedFile):
    file = open(openedFile[0], 'w')
    for i in range(len(words)):
        value = words[str(i+1)]
        line = f'{value[0]} - {value[2]}\n'
        file.write(line)
    file.close()

def newFile(words, lastWordNum, openedFile):
    words.clear()
    lastWordNum[0] = 1
    openedFile[0] = None
    ui.textEdit.setVisible(True)
    ui.frame.setVisible(True)
    ui.pushButton_5.setVisible(False)
    ui.lineEdit_4.setText('')
    ui.lineEdit_3.setText('')
    ui.pushButton_4.setText('Почати')
    ui.progressBar.setMaximum(1)
    ui.textEdit.setText('')
    try:
        ui.pushButton_5.disconnect()
    except:
        pass

def saveAndNewFile(words, lastWordNum, openedFile):
    if openedFile[0] == None:
        saveAsFile(words, openedFile)
        newFile(words, lastWordNum, openedFile)

    else:
        saveFile(words, currentOpenedFile)
        newFile(words, lastWordNum, openedFile)

ui.pushButton.clicked.connect(lambda: addWord(lastWordNum, words))
ui.pushButton_2.clicked.connect(lambda: changeWord(words))
ui.pushButton_3.clicked.connect(lambda: deleteWord(words, lastWordNum))
ui.pushButton_4.clicked.connect(lambda: startPlay(words))
ui.actionOpen.triggered.connect(lambda: openFile(words, lastWordNum, currentOpenedFile))
ui.actionSaveAs.triggered.connect(lambda: saveAsFile(words, currentOpenedFile))
ui.actionSave.triggered.connect(lambda: saveFile(words, currentOpenedFile))
ui.actionDon_t_save.triggered.connect(lambda: newFile(words, lastWordNum, currentOpenedFile))
ui.actionSave_2.triggered.connect(lambda: saveAndNewFile(words, lastWordNum, currentOpenedFile))


sys.exit(app.exec_())
