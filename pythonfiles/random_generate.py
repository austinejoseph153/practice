import random
#USING THE PYTHON BUILT IN RANDOM MODULE TO GENERATE RANDOM VALUES

class GenerateRandom():
    
    def __init__(self):
        pass
    
    # this method takes in a integer argument and generates a random integers as specified.  
    def generate_random_numbers(self,number_length=None,print_result=False):
        
        if not number_length:
            print("hjshjas")
            return
        # sets a max length so that numbers generated do not exceed 16 values 
        max_length = 16
        if type(number_length) == str:
            try:
                number_length = int(number_length)
            except:
                raise ValueError("only numbers are allowed!")
        if number_length < 16:
            generated = ""
            for _ in range(number_length):
                generated+= str(random.randint(1,9))
        else:
            generated = ""
            for _ in range(16):
                generated+= str(random.randint(1,9))
        if not print_result:
            return generated
        print(generated)

number_one = GenerateRandom()
number_one.generate_random_numbers()
    
