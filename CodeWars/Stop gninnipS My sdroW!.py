# spinWords("Hey fellow warriors") => "Hey wollef sroirraw" 
# spinWords("This is a test") => "This is a test" 
# spinWords("This is another test") => "This is rehtona test"


def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

###################--------------

def spin_words(sentence):
    words = [word for word in sentence.split(" ")]
    words = [word if len(word) < 5 else word[::-1] for word in words]
    return " ".join(words)

#######-------------------



def spin_words(sentence):
    return ' '.join(word if len(word)<5 else word[::-1] for word in sentence.split())