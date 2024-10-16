# Bookbot
my first project

## Purpose
- This is the first guided project of [boot.dev](https://www.boot.dev)
- I ended up writing the first solution of bookbot in about 40 minutes
- That said there are some obvious areas for improvement:
    - Give the tool more utility: add CLI flags to let the user find out more of what they actually want to know
    - Single-pass the text: In my current implementation building the report takes multiple passes, we could do it in one

## Thoughts on v2
- What might someone actually want to know about a file or set of files?
    - How frequently do certain words or patterns occur?
    - What are the differences between a set of files in occurance of words, patterns, or characters?
    - Only knowing some of the information:
        - Just get the frequency of word occurance
        - Just get the frequency of character occurance
        - Get the occurance of all characters, not just alphabetical ones
        - Get the occurance of only digits
        - Get the number of lines of the file
        - Give the option to only return some number of results in either ascending or descending order
    - Returning all or some of the lines where a word, pattern, or character occurs
- For particularly large files, the user may want results cached if the file hasn't changed
