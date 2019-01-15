import prog4_1 
import prog4_2
import sys

print('Assignment #4-3, Anthony Reese, areese@sdsu.edu')
fileName = sys.argv[1]
lines = []
tokenizedLines = []
parsedLines= []


lines = [line.rstrip('\n') for line in open(fileName)]

for x in lines :
    tokenizedLines.append(prog4_1.Tokenize(x))

for x in tokenizedLines:                
    parsedLines.append(prog4_1.Parse(x))

while prog4_2.currentLine <= len(tokenizedLines):
        prog4_2.StackMachine.Execute(tokenizedLines[prog4_2.currentLine-1])
        
print('Program terminated correctly')
