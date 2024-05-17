import os
import math
import random
file_path = "files/practice.txt"


class FilesHandler():
    
    empty_text = "The file specified is empty!"
    text_file, csv_file = False, False
    mode, encoding, newline, errors = "r", "utf-8", "\n", "strict"
      
    def __init__(self,filepath):
        self.filepath = filepath    
    
    # a method to check if the file to be open is a text or csv(comma seperated values) file
    def extention_type(self):
        if self.filepath.endswith(".txt"):
            self.text_file = True
            self.csv_file = False
        elif self.filepath.endswith(".csv"):
            self.csv_file = True
            self.text_file = False
    
    # a method to return an error message to the user when a file is not found
    def not_found_text(self):
        error_text = 'Could not find  "{}" within the current working directory!\n'.format(self.filepath)
        error_text+= "Check that path specified is correct"
        return error_text
    
    # a method that reads a text file and returns the output
    def read_from_file(self,mode=mode,encoding=encoding,newline=newline,errors=errors):
        # change text_file
        self.extention_type() 
        
        try:
            with open(self.filepath,mode=mode,encoding=encoding,newline=newline,errors=errors) as file:
                if self.text_file:
                    content = file.read()
                else:
                    content = "cannot read file"
        
        # if file not found return an error meesage to user
        except FileNotFoundError:
            return self.not_found_text()
        
        # if permission was denied in opening file, return an error to user
        except PermissionError:
            error_text = 'An error occured accessing "{}"'.format(self.filepath)
            return error_text
        except OSError:
            return "an error occured trying to access file!"
        else:
            if not content:
                return self.empty_text
            return content
          
