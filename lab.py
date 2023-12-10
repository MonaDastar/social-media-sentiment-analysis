punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(wrd):
    """
    Removes punctuation characters from a word.

    Args:
        wrd (str): The input word.

    Returns:
        str: The word without punctuation characters.
    """
    for c in punctuation_chars:
        wrd = wrd.replace(c, '')
    return wrd

negative_words = []
with open("negative_words.txt") as neg_f:
    for line in neg_f:
        if line[0] != ';' and line[0] != '\n':
            negative_words.append(line.strip())

def get_neg(sentences):
    """
    Counts the number of negative words in a sentence.

    Args:
        sentences (str): The input sentence.

    Returns:
        int: The count of negative words.
    """
    wrds = sentences.split()
    nag_count = 0
    for wrd in wrds:
        temp_wrd = strip_punctuation(wrd.lower())
        if temp_wrd in negative_words:
            nag_count += 1
    return nag_count

positive_words = []
with open("positive_words.txt") as pos_f:
    for line in pos_f:
        if line[0] != ';' and line[0] != '\n':
            positive_words.append(line.strip())

def get_pos(sentences):
    """
    Counts the number of positive words in a sentence.

    Args:
        sentences (str): The input sentence.

    Returns:
        int: The count of positive words.
    """
    wrds = sentences.split()
    pos_count = 0
    for wrd in wrds:
        temp_wrd = strip_punctuation(wrd.lower())
        if temp_wrd in positive_words:
            pos_count += 1
    return pos_count

with open("project_twitter_data.csv", "r") as input_file, open("resulting_data.csv", "w") as output_file:
    header = "Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n"
    output_file.write(header)
    
    lines = input_file.readlines()[1:]
    
    for line in lines:
        data = line.strip().split(',')
        
        twt_txt, rtwt_num, twt_rpl = data[0], int(data[1]), int(data[2])
        
        pos_score = get_pos(twt_txt)
        neg_score = get_neg(twt_txt)
        net_score = pos_score - neg_score
        
        result = f"{rtwt_num},{twt_rpl},{pos_score},{neg_score},{net_score}\n"
        
        output_file.write(result)
