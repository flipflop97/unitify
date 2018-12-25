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
            unit += token.text + token.whitespace_
            continue

        if token.is_title:
            word = word.capitalize()
        elif token.is_upper:
            word = word.upper()

        unit += word + token.whitespace_

    return unit
