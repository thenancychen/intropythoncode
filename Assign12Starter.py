# Nancy Chen - CS 110A Assignment 12 starter file
# Program to count how many words have double letters.

def main():
    # Write your code here, following the above instructions and rules.
    #change to while input - and then do doubleletter ture or false

    #user input
    double_letter_words = []
    
    #if condition is true, the loop will run over and over again
    ask = "yes"
    while ask[0] == "y" or ask[0] == "Y":
      s = input("Please enter a word: ") 

      #if input has double letters, store in list
      if hasDoubleLetter(s.lower()):
        double_letter_words.append(s)
        print("It has a double letter")

      elif hasDoubleLetter(s.lower()) == False:
        print("It doesn't have a double letter")
      ask = input("Do you want to enter another word? ")
    
    words = ", ".join(double_letter_words)
     
    if ask[0] == "n" or ask[0] == "N":
        print("You entered the following " + str(len(double_letter_words)) + " words that had double letters: " + str(words))
      
def hasDoubleLetter(s):
    '''
    Returns True if the string s has a double letter, or False otherwise.
    '''
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False
  
main()

'''
Sample output:
Please enter a word: lettuce
It has a double letter
Do you want to enter another word? y
Please enter a word: happy
It has a double letter
Do you want to enter another word? y
Please enter a word: chocolate
It doesn't have a double letter
Do you want to enter another word? y
Please enter a word: snoopy
It has a double letter
Do you want to enter another word? y
Please enter a word: boop
It has a double letter
Do you want to enter another word? y
Please enter a word: haha
It doesn't have a double letter
Do you want to enter another word? n
You entered the following 4 words that had double letters: lettuce, happy, snoopy, boop

Please enter a word: HAPPY
It has a double letter
Do you want to enter another word? y
Please enter a word: pePPY
It has a double letter
Do you want to enter another word? YES
Please enter a word: donut
It doesn't have a double letter
Do you want to enter another word? yEs
Please enter a word: COllagE
It has a double letter
Do you want to enter another word? nO
You entered the following 3 words that had double letters: HAPPY, pePPY, COllagE
'''
