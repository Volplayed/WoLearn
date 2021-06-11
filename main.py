import time
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
    ui.progressBar.setValue(0)
    playedWordsList = []
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

def setNewWord(wordList, type):
    rightAnswer = [None]
    word = [None]
    if len(wordList) > 0:

        word[0] = wordList[randint(0, len(wordList))]
        if type == 'wtt':
            ui.lineEdit_3.setText(word[0][0])
            rightAnswer[0] = word[0][1]

        elif type == 'ttw':
            ui.lineEdit_3.setText(word[0][1])
            rightAnswer[0] = word[0][0]

        elif type == 'r':
            a = randint(0, 2)
            if a == 0:
                ui.lineEdit_3.setText(word[0][0])
                rightAnswer[0] = word[0][1]


            elif a == 1:
                ui.lineEdit_3.setText(word[0][1])
                rightAnswer[0] = word[0][0]
        return word[0], rightAnswer[0]
    else:
        ui.textEdit.setVisible(True)
        ui.frame.setVisible(True)
        ui.pushButton_5.setVisible(False)
        ui.lineEdit_4.setText('')
        ui.lineEdit_3.setText('')
        return word[0], rightAnswer[0]

def checkIsTheAnswerRight(rightAnswer, wordlist, word, type):

    writtenWord = ui.lineEdit_4.text()
    if writtenWord.capitalize() == rightAnswer[0].capitalize():
        ui.progressBar.setValue(ui.progressBar.value() + 1)
        if word[0] in wordlist:
            wordlist.pop(wordlist.index(word[0]))
            word[0], rightAnswer[0] = setNewWord(wordlist, type)

    else:
        ui.lineEdit_4.setText("Неправильно")

def openFile(words, lastWordNum):
    file = open(filedialog.askopenfilename(), 'r')
    words.clear()
    ui.textEdit.clear()
    lastWordNum[0] = 0
    counter = 1
    for line in file:
        lt = line.split()
        if len(lt) == 3:
            words[str(counter)] = [lt[0].capitalize(), '-', lt[2].capitalize(), '\n']
            counter += 1
    lastWordNum[0] = counter
    ui.progressBar.setMaximum(counter - 1)
    print(words)
    convertToTextEditText(words)
    file.close()

def saveFile(words):
    file = open(filedialog.asksaveasfilename(), 'w')
    for i in range(len(words)):
        value = words[str(i+1)]
        line = f'{value[0]} - {value[2]}\n'
        file.write(line)
    file.close()


ui.pushButton.clicked.connect(lambda: addWord(lastWordNum, words))
ui.pushButton_2.clicked.connect(lambda: changeWord(words))
ui.pushButton_3.clicked.connect(lambda: deleteWord(words, lastWordNum))
ui.pushButton_4.clicked.connect(lambda: startPlay(words))
ui.actionOpen.triggered.connect(lambda: openFile(words, lastWordNum))
ui.actionSave.triggered.connect(lambda: saveFile(words))

sys.exit(app.exec_())
