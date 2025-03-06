# Function to check if a given string is a palindrome
def is_palindrome(s: str) -> bool:
    # Convert the string to lowercase and remove spaces to ensure case and spaces don't affect the result
    s = s.lower().replace(" ", "")
    # Check if the string is the same when reversed
    return s == s[::-1]

# Main execution block
if __name__ == "__main__":
    # Prompt the user to enter a word
    word = input("Enter a word: ")
    
    # Check if the entered word is a palindrome
    if is_palindrome(word):
        print("It's a palindrome!")  # Print if the word is a palindrome
    else:
        print("Not a palindrome.")  # Print if the word is not a palindrome
