#Write a function called garble_this. This function should
#take two parameters, both strings. The first string is the
#filename of a file to which to write (output_file), and the
#second string is the filename of a file from which to read
#(input_file).
#
#garble_this should copy the contents of input_file into
#output_file, but make the following changes:
#
# - Replace all vowels with the next vowel in order (a -> e,
#   e -> i, i -> o, o -> u.
# - Replace all consonants with the next consonant, b -> c,
#   c -> d, d -> f, etc.) Replace z with b.
# - Leave everything else in the file unchanged.
#
#For example, if these were the contents of input_file (the
#second parameter):
#

# this is some text. woo text yay!
#
#Then garble_this would write this text to output_file (the
#first parameter):
#
# vjot ot tuni viyv. xuu viyv zez!
#
#No other characters should be changed. Note that the file
#to be copied will have multiple lines of text. You may assume
#the input file will be all lower-case.
#
#We've included two files for you to test on: anInputFile.txt
#and anOutputFile.txt. The test code below will copy the text
#from the first file to the second. Feel free to modify the
#first to test different setups.
#
#Hints: 
# - Remember, you can increment a letter by 1 by finding its
#   ordinal, adding one, and converting it back to a letter.
#   If a_char is a character, then chr(ord(a_char) + 1) would
#   give you the next character.
# - You might also use dictionaries to establish what each
#   letter gets replaced by.
# - In ASCII, the character that comes after "z" is "{". You
#   want to replace "z" with "a", though.
# - Consider writing multiple functions! You could (but you
#   do not have to) write a dedicated function called
#   change_letter that handles a single letter, then
#   repeatedly call it to handle the file as a whole.


#Write your function here!

def garble_this(output_file, input_file): 
    my_input = open(input_file, 'r')
    line = my_input.read() 
    vowels = ['a','e','i','o','u']
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    for character in range(len(line)): 
        if line[character] in vowels:
            new_vowel = vowels[(vowels.index(line[character]) + 1) % 5]
            line = line[:character] + new_vowel + line[(character + 1):]
        elif line[character] in consonants: 
            new_consonant = consonants[(consonants.index(line[character])+1) % len(consonants)]
            line = line[:character] + new_consonant + line[(character + 1):] 
    my_input.close() 
    my_output = open(output_file, 'w') 
    my_output.write(line) 
    

#  in_file = open(input_file, 'r')
 #  out_file = open(output_file, 'w')
   #out_file.write(line)

 #  line = in_file.read()  


  # in_file.close() 


#The code below will test your function. You can find the two
#files it references in the drop-down in the top left. If your
#code works, anOutputFile.txt should have the text:
#ecdfigh
#joklmnp
#uqrstva
#wxyzb.!
#1234567
#890&$%#

garble_this("anOutputFile.txt", "anInputFile.txt")
print("Done running! Check anOutputFile.txt for the result.")

