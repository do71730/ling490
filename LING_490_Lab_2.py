# Welcome to Lab #2

# We will be using Python and the Natural Language Toolkit (NLTK)
# to learn the basics of natural language processing.

# We will complete Lab #1 in a Python file just like this one.
# The lab is divided into Tasks for you to complete. Once you have completed
# all the tasks, you are done with the lab.

# At the end of the lab, you will be given code to export your answers (i.e. the output)
# to a .txt file.
# To turn in the lab, upload the Python file and the .txt file to your website.
# Post it under the tab "Labs"

# NOTE:
# This video assumes you have:
    # Python installed
    # PyCharm installed
    # NLTK downloaded and installed
    # a new project opened in PyCharm
    # Lab #2 downloaded from Blackboard

# A few things about Python
    # Add a # at the beginning of a line to add comments to your code.
    # This is important so you know what the code means now when you complete the lab and
    # later when you want to use these tools to analyze your own texts

    # If you want Python to display the output of your request, you need to add the print()
    # function at the beginning of the request.
    #For example
        #print(text1) instead of text1

# Make sure that Python is using floating point division
from __future__ import division

# Ok let's start the lab
# We will be following along with chapter 1 of Natural Language Processing with Python -
# Analyzing Text with the Natural Language Toolkit available here: http://www.nltk.org/book_1ed/


# TASK #1
# Import the NLTK package and download "all"
print("______________________________________Task #1_________________________________\n")
import nltk
#nltk.download()

# Import the "book" module from NLTK
from nltk.book import *

# Verify that the "book" module was imported by calling specific texts.
# You can do this by just typing the name of each file.
# For example
print(text1)

print(text2)


# TASK #2
# Search text by concordances
print("______________________________________Task #2_________________________________\n")
print("\nAll the occurance of the word \"monstrous\" in text1")
print(text1.concordance("monstrous"))

# YOUR TURN
# Do 2 of your own searches by concordances

# Search 1
print("\nAll the occurance of the word \"Grail\" in text6")
print(text6.concordance("Grail"))

# Search 2
print("\nAll the occurance of the word \"beginning\" in text3")
print(text3.concordance("beginning"))


# TASK #3
print("______________________________________Task #3_________________________________\n")
# Search text for words that appear in a similar range of contexts

print("\nAll the words that occurred in a similar context as the word \"monstrous\" in text1")
print(text1.similar("monstrous"))

print("\nAll the words that occurred in a similar context as the word \"monstrous\" in text2")
print(text2.similar("monstrous"))

# YOUR TURN
# Do 2 of your own searches by similarity

# Search 1
print("\nAll the words that occurred in a similar context as the word \"Grail\" in text6")
print(text6.similar("Grail"))

# Search 2
print("\nAll the words that occurred in a similar context as the word \"beginning\" in text3")
print(text3.similar("beginning"))


# TASK #4
print("______________________________________Task #4_________________________________\n")
# Search text for contexts that are shared by two or more words, such
# as "monstrous" and "very"
print("\nAll the common contexts were 'monstrous' and 'very' appears in text2:")
print(text2.common_contexts(["monstrous", "very"]))

# YOUR TURN
# Do 2 of your own searches by common context

# Search 1
print("\nAll the common contexts were 'Grail' and 'Lord' appears in text6:")
print(text6.common_contexts(["Grail", "Lord"]))

# Search 2
print("\nAll the common contexts were 'beginning' and 'earth' appears in text3:")
print(text3.common_contexts(["beginning", "earth"]))

# TASK #5
print("______________________________________Task #5_________________________________\n")
# Search for the lexical dispersion of a given word or words across a text
print("\nThe lexical dispersion of the words: 'citizens', 'democracy', 'freedom', 'duties',and 'America' in text4")
print(text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"]))

# HEADS UP
# You need to have Python's NumPy and Matplotlib packages installed in order to produce
# the graphical plots used in this lab and in the book.
# Here is a video that shows how to install NumPy and Matplotlib: https://www.youtube.com/watch?v=kcHkE-Ejf0E
    # The installation begins at about 1:30 into the video.
    # The video also shows how to install the package Pandas. We will use this package later
    # so it's not a bad idea to install it now.

# YOUR TURN
# Do 2 of your own searches to examine the lexical dispersion of words in a text.

# Search 1
print("\nThe lexical dispersion of the words: 'stocks', 'inflation', 'money',and 'America' in text")
print(text7.dispersion_plot(['stocks', 'inflation', 'money', 'America']))

# Search 2
print("\nThe lexical dispersion of the words: 'Marianne', 'love', 'death', 'age',and 'Henry' in text2")
print(text2.dispersion_plot(["love", "Marianne", "death", "age", "Henry"]))


# TASK #6
print("______________________________________Task #6_________________________________\n")
# Counting Vocabulary
# Find the length of a text by total word count + punctuation marks

# This gives us the total TOKENS in a text
print("\n The length of text3: ",len(text3))

# Print a sorted list of vocabulary items
print("\nThe sorted list of vocabulary in text3: ", sorted(set(text3)))

# Find the total word TYPES in a text by using the "set()" function.
print("\nThe total word types in text3: ",len(set(text3)))

# YOUR TURN
# Do 2 of your own searches to examine the word count in a text.

# Search 1
# Tokens
print("\nThe length of text8: ",len(text8))

# Search 1
# Types
print("The total word types in text8: ",len(set(text8)))

# Search 2
# Tokens
print("\n The length of text9: ",len(text9))

# Search 2
# Types
print("The total word types in text9: ",len(set(text9)))

# TASK #7
print("\n______________________________________Task #7_________________________________\n")
# Lexical richness

# Let's calculate a measure of lexical richness in a text by dividing
# the total TOKENS by the total TYPES. This shows the average that each word is used
# in the text
print("Lexical richness of text3: ",len(text3) / len(set(text3)))

# Count the occurrences of a word in a particular text
print("Number of occurence of the word 'smote' in text3: ",text3.count("smote"))

# Calculate the percentage of a text that is taken up by one word
print("The percentage of 'a' found in text4: ",100 * text4.count("a") / len(text4))

# YOUR TURN
# Do 2 of your own searches to examine lexical richness.

# Search 1
# How many times does the word "lol" appear in "text5"? How much is this as a percentage
# of the total number of words in the text?
print("\nNumber of occurence of the word 'lol' in text5: ",text5.count("lol"))
print("The percentage of 'lol' found in text5: ",100 * text5.count("lol") / len(text5))

# Search 2
# Pick a word and text to examine
print("\nNumber of occurence of the word 'Thursaday' in text9: ",text9.count("Thursaday"))
print("The percentage of 'Thursaday' found in text9: ",100 * text9.count("Thursaday") / len(text9))

# TASK #8
print("\n______________________________________Task #8_________________________________\n")
# Writing our first functions :)

# Write a function to calculate the lexical diversity of a text
def lexical_diversity(text):
    return len(text) / len(set(text))

# Write a function that calculates the percentage of a text that one word takes up
def percentage(count, total):
    return 100 * count / total

# Try your new functions out
print("Lexical Diversity of text3: ",lexical_diversity(text3),'\n')

print("The percentage of 'a' in text4: ",percentage(text4.count("a"), len(text4)),'\n')


# TASK #9
print("______________________________________Task #9_________________________________\n")
# Frequency distributions
# Let's count how often each word occurs in a text and rank them by frequency. In other
# words, let's get its frequency distribution
fdist1 = FreqDist(text1)
print('\n',"Frequency distribution of text1: ",fdist1)

# Let's get the 50 most frequent words and count how many times each appears in a text
# NOTE: The textbook uses different code that produced an error for me in this section so
# I replaced it with code that worked.
print('\n',"The 50 most frequent words and count in text1",fdist1.most_common(50))

# Count the times a particular word appears in a text
print('\n',"Number of times 'whale' occured in text1",fdist1["whale"])

# Plot the frequency distribution of words in a text
# Pay attention to the curve of the graph. This curve is pretty consistent across texts.
# For more info look into Ziph's law
print('\n',fdist1.plot(50, cumulative=True))

# Sometimes the most frequent words don't tell us too much about the text so we can look
# at the hapaxes, or words that appear only once in the text
print('\n',fdist1.hapaxes())

# YOUR TURN
# Calculate the frequency distribution of another text in NLTK (e.g. text2, text3, etc.)
# NOTE: You need to remove the # sign located to the left of the code below for the code
# to run
fdist2 = FreqDist(text6)
print("\nFrequency distribution of text6: ",fdist2)

# Get the (50) most frequent words from the text
# NOTE: You need to remove the # sign located to the left of the code below for the code
# to run
print("\nThe 50 most frequent words and count in text6",fdist2.most_common(50))

# Plot the frequency distribution of the text
# NOTE: You need to remove the # sign located to the left of the code below for the code
# to run
print('\n',fdist2.plot(50, cumulative=True))

# Find the hapaxes in the text
# NOTE: You need to remove the # sign located to the left of the code below for the code
# to run
print('\n',fdist2.hapaxes())

# QUESTION
# Do the most frequent or least frequent words give you important information about the
# text? yes, it can help us figure out what words we need to worry about when reading the book. The punctuation does not help much.
# Sometimes we need to look deeper

# TASK #10
print("\n______________________________________Task #10_________________________________\n")
# Fine grained selection of words
# Let's look at the length of words to see if that tells us something, starting with the
# long words

# First we need to write code to look for words longer than 15 letters. We'll create 2
# objects to do this.
# This is giving me a syntax error for some reason, although it did work earlier :/
V = set(text1)
long_words = [w for w in V if len(w) > 15]

# Now let's look at the set of long_words in text1
print("Words with length greater than 15: ",sorted(long_words),'\n')

# YOUR TURN
# Try out the previous statements to evaluate word length and experiment with changing
# the text and changing the length condition
# NOTE: You need to remove the # sign located to the left of the code below for the code
# to run
V_1 = set(text5)
long_words = [w for w in V_1 if len(w) > 20]
print("Words with length greater than 20: ",sorted(long_words),'\n')

# TASK #11
print("\n______________________________________Task #11_________________________________\n")
# Collocations and Bigrams
# Let's count bigrams and collocations in text
# We'll come back to how we find collocations later
print("\nCollocations in text4",text4.collocations(),'\n')

print("\nCollocations in text5",text5.collocations(),'\n')

# YOUR TURN
# Use the "collocations" function to search for collocations in other texts.
# Do the results of collocations tell us something significant about the text?
# Are they good keywords?

# Collocation search 1
print("\nCollocations in text6",text6.collocations(),'\n')

# Collocation search 2
print("\nCollocations in text7",text7.collocations(),'\n')

#END OF LAB #2

# Now that we have finished Lab #1, we should save our Python file and print the output
# To print the output, one option is to use the print icon in the run window

# Turn in your lab by uploading the Python file and the printed output to your website