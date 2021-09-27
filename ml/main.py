import spacy
import pandas as pd
import os
from ml.extraction import *
import json

def extract_skills(resume_text):
    # load pre-trained model
    nlp = spacy.load('en_core_web_sm')

    nlp_text = nlp(resume_text)
    noun_chunks=nlp(resume_text).noun_chunks
    # removing stop words and implementing word tokenization
    tokens = [token.text for token in nlp_text if not token.is_stop]
    
    # reading the csv file
    data = pd.read_csv("ml/skills.csv") 
    
    # extract values
    skills = list(data.columns.values)
    
    skillset = []
    
    # check for one-grams (example: python)
    for token in tokens:
        if token.lower() in skills:
            skillset.append(token)
    
    # check for bi-grams and tri-grams (example: machine learning)
    for token in noun_chunks:
        token = token.text.lower().strip()
        if token in skills:
            skillset.append(token)
    
    return {'skills:':[i.capitalize() for i in set([i.lower() for i in skillset])]}

def extract_data(path):
    # print("Loading from", 'ml/models(03-03-2021_22;54;12)/NER_model')

    nlp2 = spacy.load('ml/models(03-03-2021_22;54;12)/NER_model')
    ref=main(path)
    doc2 = nlp2(ref)

    dic={}
    # for ent in doc2.ents:
    #     # print(ent.text,'------->',ent.label_)
    #     dic[ent.label_]=ent.text
    # skills=extract_skills(ref)
    # dic.update(skills)
    # with open('output.json', 'w') as outfile:
    #     json.dump(dic, outfile)
    # # print(dic)
    # return dic

    for ent in doc2.ents:
#     print(ent.label_,':',ent.text)
        dic[ent.text]=ent.label_
    dic2={'Name':[],'Email':[],'Phone No':[],'Education':[],'Companies worked at':[],'Designation':[],'Location':[],'Year of experience':[]}
    for key,val in dic.items():
        if(val in dic2.keys()):
            dic2[val].append(key)
        
    skills=extract_skills(ref)
    dic2.update(skills)
    with open('output.json', 'w') as outfile:
        json.dump(dic2, outfile)


    # insert(dic2)
    # print(dic2)
    return dic2


