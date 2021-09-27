import spacy
from spacy.gold import GoldParse
from spacy.scorer import Scorer
import pickle

def evaluate(nlp, examples, ent=['Name','Email','Phone No','Address','Designation','Year of experience','Education','Companies worked at','Location']):
    scorer = Scorer()
    for input_, annot in examples:
        text_entities = []
        for entity in annot.get('entities'):
            for en in ent:
                if en in entity:
                    text_entities.append(entity)
        doc_gold_text = nlp.make_doc(input_)
        gold = GoldParse(doc_gold_text, entities=text_entities)
        pred_value = nlp(input_)
        scorer.score(pred_value, gold)
    return scorer.scores


nlp = spacy.load('models(03-03-2021_22;54;12)/NER_model')
with open ('dataset/spacy_labelstudio', 'rb') as fp:
    TEST_DATA = pickle.load(fp)
results = evaluate(nlp, TEST_DATA)
print(results)