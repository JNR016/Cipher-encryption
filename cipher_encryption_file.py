import string
import sys
from datetime import datetime

def cipher_encryption():
    
    # To check if an argument was passed and if not stop the program
    if len(sys.argv) < 2:
        print("Error: Please provide a file path as an argument.")
        print("Usage: python script.py <filename.txt>")
        sys.exit(1)
    
    allowed_extensions = (".txt", ".json", ".csv", ".py", ".html")   
    
    # Check what type of file did the user use
    if not sys.argv[1].lower().endswith(allowed_extensions):
        print("Invalid file type!!!")
        print("This script supports plain-text files.")
        print("Allowed_extensions are " + " ".join(allowed_extensions))
        sys.exit(1)
         
    # characters we will use to encrypt a file    
    characters = " " + string.punctuation + string.digits + string.ascii_letters
    encrypted_text = ""
    decrypted_text = ""
    
    mode = input("Which mode would you like to do.\nTo encrypt a file enter 'e' and to decrypt a file enter 'd': ")
    if mode not in ["e", "d"]:
        print("Invalid mode selection")
        sys.exit(1)
        
    try:    
        key = int(input("Enter a key: "))
    except ValueError:
        print("Error: The key must be a whole number.")
        sys.exit(1)    
        
    file_path = sys.argv[1]
    
    # When mode is decrypt then the key should be negative
    if mode == "d":
        key = -key
        
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                for words in line:
                    index = characters.find(words)
                        
                    if index == -1:                  # If the index for that letter isn't found then it should add it as it is
                        if mode == "d":
                            decrypted_text += words
                        elif mode == "e":
                            encrypted_text += words    
                    else:
                        new_index = (index + key) % len(characters) # To make sure that the new index isn't greater than the length of the characters
                        if mode == "d":
                            decrypted_text += characters[new_index]
                        elif mode =="e":               
                            encrypted_text += characters[new_index]
         
        # Make the user choose whether they want to name the file themselves or use the default naming                
        choice = input("To save a file in the name you want to give it enter 'new' and to save it using a default name enter 'default' (decryptedData_time.txt): ").lower()
        
        while choice not in ["default", "new"]:
            print("Invalid input. Please choose between 'default' and 'new'.")
            choice = input("Try again: ")
        
        # Write the encrypted/decrypted text into a new file    
        if choice == "default":
            now = datetime.now()
            
            if mode == "d":
                new_file = "decryptedData_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
                with open(new_file, "w", encoding="utf-8") as file:
                    file.writelines(decrypted_text)
            elif mode == "e":
                new_file = "encryptedData_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"                      
                with open(new_file, "w", encoding="utf-8") as file:
                    file.writelines(encrypted_text)  
                        
        else:
            new_file = input("Enter a name to save the file to and don't forget to specify the file extension: ")
            if not new_file.lower().endswith(allowed_extensions):
                new_file += ".txt"
            if mode == "d":
                with open(new_file, "w", encoding="utf-8") as file:
                    file.writelines(decrypted_text)
            elif mode == "e":                      
                with open(new_file, "w", encoding="utf-8") as file:
                    file.writelines(encrypted_text)
                
        print(f"Results saved to {new_file}")     
               
    except FileNotFoundError:
        print("File not found, check spelling")
        sys.exit(1)
        
    except PermissionError:
        print("Error: Access denied.")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
cipher_encryption()                                                             