import logging
import spacy

nlp = spacy.load('en_core_web_lg')

def ner_remove(s) -> str:
    doc = nlp(s)
    clean_s = s

    for ent in doc.ents:
        #if ent.label_ in ['PERSON', 'GPE', 'ORG', 'DATE', 'CARDINAL', 'PRODUCT']:
        clean_s = clean_s.replace(ent.text, f' [{ent.label_}] ')
    return clean_s


def anon_username(s=None) -> str:
    if s is None:
        return s
    return s

def anon_password(s=None) -> str:
    if s is None:
        return s
    return '*********'

def anon_name(s=None) -> str:
    if s is None:
        return s
    return s

def anon_bio(s=None) -> str:
    if s is None:
        return s
    return s

def anon_prompt(s=None) -> str:
    if s is None:
        return s
    s = ner_remove(s)
    return s

def anon_response(s=None) -> str:
    if s is None:
        return s
    s = ner_remove(s)
    return s