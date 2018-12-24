import spacy

NLP = spacy.load("en_core_web_sm")


def unitify(line):
    unit = ""

    for token in NLP(line):
        if token.tag_ == 'NN':
            word = 'unit'
        elif token.tag_ == 'NNS':
            word = 'units'
        else:
            word = token.text

        if token.is_title:
            word = word.capitalize()

        unit += word + token.whitespace_

    return unit
