# All code other than the remove_punctuation, prepare_text, and end_chat were edited by me.

""" Import string function to use later"""
import string

def remove_punctuation(input_string):
    """Removes punctuation from the user's input.
    
    Parameters
    ----------
    input_string : string
        String that the user inputs into the chatbot
        
    Returns
    -------
    out_string : string
        String with all the punctuation removed from the original input string.
    """
    
    out_string = ''
    for char in input_string:
        if char not in string.punctuation:
            out_string += char
        else:
            continue
    return out_string

def prepare_text(input_string):
    """Prepares the user's input for the chatbot to understand. 
    
    Parameters
    ----------
    input_string : string
        String that the user inputs into the chatbot.
        
    Returns
    -------
    out_list : list
        List containing all the user's input prepared for the chatbot to interpret.
    """
    
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    return out_list 

def prepare_numbers(numbers):
    """Prepares the numbers for the chatbot to interpret.
    
    Parameters
    ----------
    numbers : list
        Numbers that the user has input into the chatbot
        
    Returns
    -------
    numb : list
        List of integers that the chatbot can use to put into the calculator.
    """
    
    numb = []
    for item in numbers:
        numb.append(int(item))
    return numb

def calculate(numbers, operator):
    """Calculator function for the chatbot
    
    Parameters
    ----------
    numbers : list
        List of numbers that the user input into the chatbot.
    operator : str
        String that tells the calculator which function to run.
        
    Returns
    -------
    result : int
        Integer that is the result of the function called on the numbers the user input.
    """
    
    if operator == 'add':
        return add(prepare_numbers(numbers))
    elif operator == 'subtract':
        return subtract(prepare_numbers(numbers))
    elif operator == 'multiply':
        return multiply(prepare_numbers(numbers))
    elif operator == 'divide':
        return divide(prepare_numbers(numbers))
    elif operator == 'remainder':
        return remainder(prepare_numbers(numbers))
    elif operator == 'power':
        return power(prepare_numbers(numbers))

def end_chat(input_list):
    """Function to end the chat.
    
    Parameters
    ----------
    input_list : list
        List that contains the input that the user input to the chatbot.
        
    Returns
    -------
    output : bool
        Returns True to end chat or False to continue chat.
    """
    
    if str('quit') in input_list:
        output = True
        return output
    else:
        output = False
        return output

def encryption(msg):
    """Encrypts the message that the user inputs to the chatbot.
    
    Parameters
    ----------
    msg : string
        String that the user inputs.
        
    Returns
    -------
    encoded : string
        String containing the encoded message with 'Encoded Message:    ' in front of it.
    """
    
    start_key = 123
    key_increment = 4
    string = []
    encoded = []
    key = start_key
    message = msg
    for c in range(0, len(message)):
        code = ord(message[c])
        change = code+key
        new = chr(change)
        string += new
        key += key_increment
    
    encoded = ''.join(string)
    return ('Encoded Message:\t' + encoded)

def decryption(msg):
    """Decrypts the message that was encoded.
    
    Parameters
    ----------
    msg : string
        String that the chatbot encoded.
        
    Returns
    -------
    decoded : string
        String containing the decoded message with 'Decoded Message:    ' in front of it.
    """
    
    start_key = 123
    key_increment = 4
    string = []
    decoded = []
    key = start_key
    message = msg
    for c in range(0, len(message)):
        code = ord(message[c])
        change = code-key
        new = chr(change)
        string += new
        key += key_increment
    decoded = ''.join(string)
    return ('Decoded Message:\t' + decoded)

def add(numbers):
    """Function for adding numbers together.
    
    Parameters
    ----------
    numbers : list
        List of numbers that the user inputs.
        
    Returns
    -------
    result : int
        Integer that is the result of the numbers added together.
    """
    
    result = numbers[0]
    for n in numbers[1:]:
        result = n + result
    return result

def subtract(numbers):
    """Function for subtracting numbers from each other.
    
    Parameters
    ----------
    numbers : list
        List of numbers that the user inputs.
        
    Returns
    -------
    result : int
        Integer that is the result of the numbers subtracted from one another.
    """
    
    result = numbers[0]
    for n in numbers[1:]:
        result = result - n
    return result

def multiply(numbers):
    """Function for multiplying numbers together.
    
    Parameters
    ----------
    numbers : list
        List of numbers that the user inputs.
        
    Returns
    -------
    result : int
        Integer that is the result of the numbers multiplied together.
    """
    
    result = numbers[0]
    for n in numbers[1:]:
        result = n * result
    return result

def divide(numbers):
    """Function for dividing numbers.
    
    Parameters
    ----------
    numbers : list
        List of numbers that the user inputs.
        
    Returns
    -------
    result : int
        Integer that is the result of the numbers divided.
    """
    
    result = numbers[0]
    for n in numbers[1:]:
        result = result / n
    return result

def remainder(numbers):
    """Function for finding the remainder of 2 numbers divided.
    
    Parameters
    ----------
    numbers : list
        List of numbers that the user inputs.
        
    Returns
    -------
    result : int
        Integer that is the remainder of the numbers divided.
    """
    
    return numbers[0] % numbers[1]

def power(numbers):
    """Function for raising numbers to the power of the next number.
    
    Parameters
    ----------
    numbers : list
        List of numbers that the user inputs.
        
    Returns
    -------
    result : int
        Integer that is the result of the numbers raised to the power of the next number.
    """
    
    result = numbers[0]
    for n in numbers[1:]:
        result = result ** n
    return result

def wiri():
    """The function that runs the chatbot."""

    chat = True
    print('Hello, I am Wiri. Choose either encrypt, add, subtract, multiply, divide, remainder, or power.')
    print('If using remainder, input only two numbers. For the calculator, input numbers separated by a space or comma.')
    print('If using encrypt please write encrypt then in the next messsage input the text to encrypt.')
    print("To exit the chatbot, please enter 'quit'")
    while chat:
        
        msg = input('Input :\t')
        out_msg = None

        msg = prepare_text(msg)

        if end_chat(msg):
            out_msg = 'Bye!'
            chat = False

        if not end_chat(msg):
            outs = []
            
            if msg[0] == 'encrypt':
                message = input ('What message do you want to encrypt?')
                outs.append(encryption(message))
            elif msg[0] == 'decrypt':
                message = input ('What message do you want to decrypt?')
                outs.append(decryption(message))
            elif msg[0] == 'add' or msg[0] =='subtract' or msg[0] =='multiply' or msg[0] =='divide' or msg[0] =='remainder' or msg[0] =='power':
                message = input ('What numbers do you want to calculate?')
                outs.append(calculate(prepare_text(message), msg[0]))
            else:
                outs.append("Error please enter one of the options at the beginning of the chat")
                
            out_msg = outs[0]
            
        print('OUTPUT:', out_msg)