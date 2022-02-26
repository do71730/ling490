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
print(text1.concordance("monstrous"))

# YOUR TURN
# Do 2 of your own searches by concordances

# Search 1


# Search 2



# TASK #3
# Search text for words that appear in a similar range of contexts
print(text1.similar("monstrous"))

print(text2.similar("monstrous"))

# YOUR TURN
# Do 2 of your own searches by similarity

# Search 1


# Search 2


# TASK #4
# Search text for contexts that are shared by two or more words, such
# as "monstrous" and "very"
print(text2.common_contexts(["monstrous", "very"]))

# YOUR TURN
# Do 2 of your own searches by common context

# Search 1


# Search 2


# TASK #5
# Search for the lexical dispersion of a given word or words across a text
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


# Search 2


# TASK #6
# Counting Vocabulary
# Find the length of a text by total word count + punctuation marks
# This gives us the total TOKENS in a text
print(len(text3))

# Print a sorted list of vocabulary items
print(sorted(set(text3)))

# Find the total word TYPES in a text by using the "set()" function.
print(len(set(text3)))

# YOUR TURN
# Do 2 of your own searches to examine the word count in a text.

# Search 1
# Tokens


# Search 1
# Types


# Search 2
# Tokens


# Search 2
# Types


# TASK #7
# Lexical richness

# Let's calculate a measure of lexical richness in a text by dividing
# the total TOKENS by the total TYPES. This shows the average that each word is used
# in the text
print(len(text3) / len(set(text3)))

# Count the occurrences of a word in a particular text
print(text3.count("smote"))

# Calculate the percentage of a text that is taken up by one word
print(100 * text4.count("a") / len(text4))

# YOUR TURN
# Do 2 of your own searches to examine lexical richness.

# Search 1
# How many times does the word "lol" appear in "text5"? How much is this as a percentage
# of the total number of words in the text?


# Search 2
# Pick a word and text to examine


# TASK #8
# Writing our first functions :)

# Write a function to calculate the lexical diversity of a text
def lexical_diversity(text):
    return len(text) / len(set(text))

# Write a function that calculates the percentage of a text that one word takes up
def percentage(count, total):
    return 100 * count / total

# Try your new functions out
print(lexical_diversity(text3))

print(percentage(text4.count("a"), len(text4)))


# TASK #9
# Frequency distributions
# Let's count how often each word occurs in a text and rank them by frequency. In other
# words, let's get its frequency distribution
fdist1 = FreqDist(text1)
print(fdist1)

# Let's get the 50 most frequent words and count how many times each appears in a text
# NOTE: The textbook uses different code that produced an error for me in this section so
# I replaced it with code that worked.
print(fdist1.most_common(50))

# Count the times a particular word appears in a text
print(fdist1["whale"])

# Plot the frequency distribution of words in a text
# Pay attention to the curve of the graph. This curve is pretty consistent across texts.
# For more info look into Ziph's law
print(fdist1.plot(50, cumulative=True))

# Sometimes the most frequent words don't tell us too much about the text so we can look
# at the hapaxes, or words that appear only once in the text
print(fdist1.hapaxes())

# YOUR TURN
# Calculate the frequency distribution of another text in NLTK (e.g. text2, text3, etc.)
# NOTE: You need to remove the # sign located to the left of the code below for the code
# to run
#fdist2 = FreqDist()
#print(fdist2)

# Get the (50) most frequent words from the text
# NOTE: You need to remove the # sign located to the left of the code below for the code
# to run
#print(fdist2.most_common(50))

# Plot the frequency distribution of the text
# NOTE: You need to remove the # sign located to the left of the code below for the code
# to run
#print(fdist2.plot(50, cumulative=True)))

# Find the hapaxes in the text
# NOTE: You need to remove the # sign located to the left of the code below for the code
# to run
#print(fdist2.hapaxes()

# QUESTION
# Do the most frequent or least frequent words give you important information about the
# text?
# Sometimes we need to look deeper

# TASK #10
# Fine grained selection of words
# Let's look at the length of words to see if that tells us something, starting with the
# long words

# First we need to write code to look for words longer than 15 letters. We'll create 2
# objects to do this.
# This is giving me a syntax error for some reason, although it did work earlier :/
V = set(text1)
long_words = [w for w in V if len(w) > 15]

# Now let's look at the set of long_words in text1
print(sorted(long_words))

# YOUR TURN
# Try out the previous statements to evaluate word length and experiment with changing
# the text and changing the length condition
# NOTE: You need to remove the # sign located to the left of the code below for the code
# to run
#V_1 = set()
#long_words = [w for w in V_1 if len(w) > 15]


# TASK #11
# Collocations and Bigrams
# Let's count bigrams and collocations in text
# We'll come back to how we find collocations later
print(text4.collocations())

print(text5.collocations())

# YOUR TURN
# Use the "collocations" function to search for collocations in other texts.
# Do the results of collocations tell us something significant about the text?
# Are they good keywords?

# Collocation search 1


# Collocation search 2


#END OF LAB #2

# Now that we have finished Lab #1, we should save our Python file and print the output
# To print the output, one option is to use the print icon in the run window

# Turn in your lab by uploading the Python file and the printed output to your website