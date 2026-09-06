import sys
from datetime import datetime
from cryptography.fernet import Fernet, InvalidToken
import getpass
import os

def cipher_encryption():
    
    # To check if an argument was passed and if not stop the program
    if len(sys.argv) < 2:
        print("Error: Please provide a file path as an argument.")
        print("Usage: python script.py <filename.txt>")
        sys.exit(1)
    
    allowed_extensions = (".txt", ".json", ".csv", ".py", ".html",
                          ".png", ".jpg", ".jpeg", ".gif",
                          ".mp3", ".wav", ".docx", ".pdf")   
    
    # Check what type of file did the user use
    if not sys.argv[1].lower().endswith(allowed_extensions):
        print("Invalid file type!!!")
        print("This script supports plain-text files.")
        print("Allowed_extensions are " + " ".join(allowed_extensions))
        sys.exit(1)
         
    encrypted_text = ""
    decrypted_text = ""
    
    mode = input("Which mode would you like to do.\nTo encrypt a file enter 'e' and to decrypt a file enter 'd': ")
    if mode not in ["e", "d"]:
        print("Invalid mode selection")
        sys.exit(1)    
        
    file_path = sys.argv[1]
    extension = os.path.splitext(file_path)[1]
    
    try:

        if mode == "e":
            print(f"Generating a key...")
            key = Fernet.generate_key()
            print(f"The generated key is: {(key.decode())}\nPlease save the key as it is required to decrypt the file!!!")
            cipher_suite = Fernet(key)
        elif mode == "d":
            key = getpass.getpass("Enter a key to decrypt the file:")
            key = key.encode()    
            cipher_suite = Fernet(key)
        
        
        with open(file_path, "rb") as file:
            file_data = file.read()
            
            if mode == "e":
                encrypted_text = cipher_suite.encrypt(file_data)
                print("File encrypted successfully.🔒")
            elif mode == "d":
                decrypted_text = cipher_suite.decrypt(file_data)
                print("File decrypted successfully.🔓")
                    

            
        # Make the user choose whether they want to name the file themselves or use the default naming                
        choice = input(f"Do you want to name the file or use the default naming (decryptedData_time{extension})\n(Enter 'yes' for new name or 'no' for default): ").lower()
            
        while choice not in ["yes", "no"]:
            print("Invalid input. Please choose between 'no' and 'yes'.")
            choice = input("Try again: ")
            
        # Write the encrypted/decrypted text into a new file    
        if choice == "no":
            now = datetime.now()
                
            if mode == "d":
                new_file = "decryptedData_" + now.strftime("%Y-%m-%d_%H-%M-%S") + extension
                with open(new_file, "wb") as file:
                    file.write(decrypted_text)
            elif mode == "e":
                new_file = "encryptedData_" + now.strftime("%Y-%m-%d_%H-%M-%S") + extension                      
                with open(new_file, "wb") as file:
                    file.write(encrypted_text)  
                            
        else:
            new_file = input("Enter a name to save the file to and don't forget to specify the file extension: ")
            if not new_file.lower().endswith(allowed_extensions):
                new_file += extension
            if mode == "d":
                with open(new_file, "wb") as file:
                    file.write(decrypted_text)
            elif mode == "e":                      
                with open(new_file, "wb") as file:
                    file.write(encrypted_text)
                    
            print(f"Results saved to {new_file}")     
               
    except FileNotFoundError:
        print("File not found, check spelling")
        sys.exit(1)
    except InvalidToken:
        print("Error: Invalid key or corrupted file. Decryption failed.")
        sys.exit(1)    
    except PermissionError:
        print("Error: Access denied.")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
cipher_encryption()                                                             