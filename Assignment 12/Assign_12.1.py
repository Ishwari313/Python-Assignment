# WRITE A PROGRAM WHICH ACCEPTS ONE CHARACTER AND CHECKS WHETHER IT IS VOWEL OR CONSONANT

def CheckVowel(ch):
    ch=ch.lower()

    if ch in ['a','e','i','o','u']:
        return True
    else:
        return False
    
def main():

    ch=input("Enter Character: ")

    if CheckVowel(ch):
        print("Vowel")
    else:
        print("Consonant")

if __name__=="__main__":
    main()