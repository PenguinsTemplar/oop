I.  Python Serial Generator
    A. Given a starting number, auto increment by one.
        i.  Need to review the components, so I need to go back to mabye the Counter?
        ii.  Not counter, counter counts things in the provided argument.  Just need a function that +=1 to increment up.
        iii.
    B.  Had to set up venv and ipython

II.  Python Random Word Generator

    A.  Has a profided fiile to look through, words.txt

    B.  I think dictionary is a thing, going to look at the lists video

    C.  Need to know how to load a list from a file.  When we resume, review List video in the Intro, and further list and dictionary info in the Data Structure lesson.
        i. First test/check is to count the words, using the len method

    D.  Dictionaries are a seperate critter from lists.  Key value pairs instead of arrays.
        i.  Keys are strings; even if you reference it as a number it will convert.  Must be an imutable type.  String key's need to be in ''.  You can reference with the dictionary[1] style reference

    E. Printing Words out after read
        i. gotta reference the file as the dictionary source
        ii. counts the number of words in the file, seperated by line

    F. Display random word
        i. has to be off a variable set to the dictionary, don't want to re-read the file every time.
        ii.  Python has a new line character, need to strip that out.  line.strip() does that, basically it cleans out whats at the beging and end of the string that aren't characters and returns a cleaned string.
    
    G. Subclassed word finder to deal with special characters
        i. Subclass seems to be a new class, not nested, that uses the main class as a paramater. when you reference it as such: class SpecialWordFinder(WordFinder)
        This causes the class to inherit the referenced classes stuff.  the method with the same name "load_words" overwrites the original; this is what you have to re-do.


9/3/25  10:15am Start
        10:30am Bathroom
        10:40am Resume
        11:00am Figured out that I was working on the practice files instead of the regular files
        11:15am Break for Gym prep
Total time of session: 50 min
Mostly focused, didn't wander to other things to do, mostly poked around at the Doc, reviewed video content, wrote code and debugged with Gemini.
        1:15pm Resumed work, reviewing Python Lists, eating lunch
        2:00pm Break
Total time of session: 45 min
        3:15pm Working on the WordFinder function
        3:40 Completed project, published to github, posted link to Springboard
