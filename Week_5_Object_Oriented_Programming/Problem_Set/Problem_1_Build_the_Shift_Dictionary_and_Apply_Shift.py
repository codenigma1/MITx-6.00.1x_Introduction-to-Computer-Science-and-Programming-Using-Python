# Encryption is the process of obscuring information to make it unreadable without special knowledge. For centuries, people have devised schemes to encrypt messages - some better than others - but the advent of the computer and the Internet revolutionized the field. These days, it's hard not to encounter some sort of encryption, whether you are buying something online or logging into a shared computer system. Encryption lets you share information with other trusted people, without fear of disclosure.

# A cipher is an algorithm for performing encryption (and the reverse, decryption). The original information is called plaintext. After it is encrypted, it is called ciphertext. The ciphertext message contains all the information of the plaintext message, but it is not in a format readable by a human or computer without the proper mechanism to decrypt it; it should resemble random gibberish to those for whom it is not intended.

# A cipher usually depends on a piece of auxiliary information, called a key. The key is incorporated into the encryption process; the same plaintext encrypted with two different keys should have two different ciphertexts. Without the key, it should be difficult to decrypt the resulting ciphertext into readable plaintext.

# This assignment will deal with a well-known (though not very secure) encryption method called the Caesar cipher. Some vocabulary to get you started on this problem:

# Encryption - the process of obscuring or encoding messages to make them unreadable until they are decrypted
# Decryption - making encrypted messages readable again by decoding them
# Cipher - algorithm for performing encryption and decryption
# Plaintext - the original message
# Ciphertext - the encrypted message. Note: a ciphertext still contains all of the original message information, even if it looks like gibberish.
# The Caesar Cipher

# The idea of the Caesar Cipher is to pick an integer and shift every letter of your message by that integer. In other words, suppose the shift is k . Then, all instances of the i-th letter of the alphabet that appear in the plaintext should become the (i+k)-th letter of the alphabet in the ciphertext. You will need to be careful with the case in which i + k > 26 (the length of the alphabet). Here is what the whole alphabet looks like shifted three spots to the right:

# Original:  a b c d e f g h i j k l m n o p q r s t u v w x y z
#  3-shift:  d e f g h i j k l m n o p q r s t u v w x y z a b c
# Using the above key, we can quickly translate the message "happy" to "kdssb" (note how the 3-shifted alphabet wraps around at the end, so x -> a, y -> b, and z -> c).

# Note!! We are using the English alphabet for this problem - that is, the following letters in the following order:

# >>> import string
# >>> print string.ascii_lowercase
# abcdefghijklmnopqrstuvwxyz
# We will treat uppercase and lowercase letters individually, so that uppercase letters are always mapped to an uppercase letter, and lowercase letters are always mapped to a lowercase letter. If an uppercase letter maps to "A", then the same lowercase letter should map to "a". Punctuation and spaces should be retained and not changed. For example, a plaintext message with a comma should have a corresponding ciphertext with a comma in the same position.

# |    plaintext    |  shift    |  ciphertext      |
# | ----------------|-----------|------------------|
# | 'abcdef'        |    2      |  'cdefgh'        |
# | 'Hello, World!' |    5      |  'Mjqqt, Btwqi!' |
# | ''              | any value |  ''              |
# We implemented for you two helper functions: load_words and is_word. You may use these in your solution and you do not need to understand them completely, but should read the associated comments. You should read and understand the helper code in the rest of the file and use it to guide your solutions.

# Getting Started

# To get started, download the ps6.zip file. Extract it to your working directory. The files inside are:

# ps6.py - a file containing three classes that you will have to implement.
# words.txt - a file containing valid English words (should be in the same folder as your ps6..py file).
# story.txt - a file containing an encrypted message that you will have to decode (should be in the same folder as your ps6..py file).
# This will be your first experience coding with classes! We will have a Message class with two subclasses PlaintextMessage and CiphertextMessage .

######################################################################################################

# Problem 1 - Build the Shift Dictionary and Apply Shift
# 20.0/20.0 points (graded)
# The Message class contains methods that could be used to apply a cipher to a string, either to encrypt or to decrypt a message (since for Caesar codes this is the same action).

# In the next two questions, you will fill in the methods of the Message class found in ps6.py according to the specifications in the docstrings. The methods in the Message class already filled in are:

# __init__(self, text)
# The getter method get_message_text(self)
# The getter method get_valid_words(self), notice that this one returns a copy of self.valid_words to prevent someone from mutating the original list.
# In this problem, you will fill in two methods:

# Fill in the build_shift_dict(self, shift) method of the Message class. Be sure that your dictionary includes both lower and upper case letters, but that the shifted character for a lower case letter and its uppercase version are lower and upper case instances of the same letter. What this means is that if the original letter is "a" and its shifted value is "c", the letter "A" should shift to the letter "C".

# If you are unfamiliar with the ordering or characters of the English alphabet, we will be following the letter ordering displayed by string.ascii_lowercase and string.ascii_uppercase:

# >>> import string
# >>> print(string.ascii_lowercase)
# abcdefghijklmnopqrstuvwxyz
# >>> print(string.ascii_uppercase)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# A reminder from the introduction page - characters such as the space character, commas, periods, exclamation points, etc will not be encrypted by this cipher - basically, all the characters within string.punctuation, plus the space (' ') and all numerical characters (0 - 9) found in string.digits.

# Fill in the apply_shift(self, shift) method of the Message class. You may find it easier to use build_shift_dict(self, shift). Remember that spaces and punctuation should not be changed by the cipher.

# Paste your implementation of the Message class in the box below.


class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # Code Here #
        lower_keys = list(string.ascii_lowercase)
        lower_values = list(string.ascii_lowercase)
        lower_shift_values = lower_keys[shift:] + lower_values[:shift]

        upper_keys = list(string.ascii_uppercase)
        upper_values = list(string.ascii_uppercase)
        upper_shift_values = upper_keys[shift:] + upper_values[:shift]

        combine_keys = lower_keys + upper_keys
        shift_combine_keys = lower_shift_values + upper_shift_values

        self.shift_dict = dict(zip(combine_keys, shift_combine_keys))
        return self.shift_dict


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        #delete this line and replace with your code here

        new_text = []
        for i in self.message_text:
        	if i not in self.build_shift_dict(shift).keys():
        		new_text.append(i)
        	else:
        		new_text.append(self.build_shift_dict(shift)[i])
        return "".join(new_text)

# Correct