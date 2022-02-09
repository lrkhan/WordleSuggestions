
def loadWords():
     with open('words.txt') as wordFile:
          words = set(wordFile.read().split())
     
     words = list(words)
     validWords = []
     for word in words:
          if len(word) == 5:
               validWords.append(word)

     return validWords

def wordsContaining(letter, index, array):
     validList = []

     for i in array:
          j = i.lower()
          if letter in j:
               if index >= 0:
                    if j[index] == letter:
                         validList.append(j)
               else:
                    validList.append(j)
                    
     
     return validList

def removeOptions(array, letter):
     validList = []

     for i in array:
          if letter not in i:
               validList.append(i)
     
     return validList

def main():
     wlist = list(loadWords())

     placement = {
          "r":1,
          "a":2,
          "e":4,
          "f":0
     }

     grayWords = ['c','n','b','v','g','p','s']

     for key in placement:
          wlist = wordsContaining(key, placement[key], wlist)

     for letter in grayWords:
          wlist = removeOptions(wlist,letter)

     print(wlist)

if __name__ == "__main__":
     main()
