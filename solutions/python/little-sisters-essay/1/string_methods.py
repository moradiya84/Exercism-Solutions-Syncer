"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    Parameters:
        title (str): Essay title that needs title casing.

    Returns:
        str: The title string in title case (first letters capitalized).
    """
    if len(title)==0:
        return title
    ans=""
    for i in range(len(title)):
        if(i!=0 and title[i-1]!=' '):
            ans+=title[i];
        else:
            ans+=title[i].upper()
    return ans


def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    Parameters:
        sentence (str): A sentence to check.

    Returns:
        bool: Is the sentence punctuated correctly?
    """
    return sentence[-1]=='.'
    pass


def clean_up_spacing(sentence):
    """Trim any leading or trailing whitespace from the sentence.

    Parameters:
        sentence (str): A sentence to clean of leading and trailing space characters.

    Returns:
        str: A sentence that has been cleaned of leading and trailing space characters.
    """
    idxl=-1
    idxr=0
    for i in range(len(sentence)):
        if sentence[i]!=' ':
            idxr=i
            if idxl==-1:
                idxl=i
    return sentence[idxl:idxr+1]


def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    Parameters:
        sentence (str): A sentence to replace words in.
        old_word (str): The word to replace.
        new_word (str): The replacement word.

    Returns:
        str: Input sentence with new words in place of old words.
    """
    len_old=len(old_word)
    len_new=len(new_word)
    ans=""
    i=0
    while i<len(sentence):
        if i+len_old<=len(sentence) and sentence[i:i+len_old]==old_word:
            ans+=new_word
            i+=len_old-1
        else:
            ans+=sentence[i]
        i+=1
    return ans
