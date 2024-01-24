'''
Author : G Gopi Kumar
Date : 24/01/2024

Program : 1(a) Write a Python program using Function that will create a text file with the current timestamp.
1(b)Write a Python program using Function in which the file content should have the content of the current timestamp.
2) Write another Python function to read from a text file. The function will take the name of the text file and display 
the content of the file into the console

Logic : Create a class Name File_Handling and written three functions for create,read,write a file and then create a
file object for the class and called the functions as per the rquirement
'''


from datetime import datetime

class File_Handling:
    def __init__(self, file_name):
        self.file = file_name
   
    def create_file(self):
        file = open(self.file, "w")
        return file
    
    def read_file(self):
        file = open(self.file, "r")
        return file.read()


    def write_file(self, data):
        file = open(self.file, "w")
        file.write(data)
        return file


if __name__ == "__main__":
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    file = File_Handling(current_time + ".txt")   
    
    #1(a) Using create_file function we will create a text file with the current timestamp
    file.create_file()
    #1(b) Using write_file function we will write the content in the text file
    file.write_file(current_time)
    #2 Using read_file function we will read the content in the text file
    print(file.read_file())

