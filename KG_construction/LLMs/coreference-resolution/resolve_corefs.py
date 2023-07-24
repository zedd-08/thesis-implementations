from typing import List
from spacy.tokens import Doc, Span
import spacy
import neuralcoref
from allennlp.predictors.predictor import Predictor

import argparse

def load_models():
    allen_url = 'https://storage.googleapis.com/allennlp-public-models/coref-spanbert-large-2020.02.27.tar.gz'
    predictor = Predictor.from_path(allen_url)
    nlp = spacy.load('en_core_web_sm')
    neuralcoref.add_to_pipe(nlp)
    return predictor, nlp

def core_logic_part(document: Doc, coref: List[int], resolved: List[str], mention_span: Span):
    final_token = document[coref[1]]
    if final_token.tag_ in ["PRP$", "POS"]:
        resolved[coref[0]] = mention_span.text + "'s" + final_token.whitespace_
    else:
        resolved[coref[0]] = mention_span.text + final_token.whitespace_
    for i in range(coref[0] + 1, coref[1] + 1):
        resolved[i] = ""
    return resolved

def get_span_noun_indices(doc: Doc, cluster: List[List[int]]) -> List[int]:
    spans = [doc[span[0]:span[1]+1] for span in cluster]
    spans_pos = [[token.pos_ for token in span] for span in spans]
    span_noun_indices = [i for i, span_pos in enumerate(spans_pos)
        if any(pos in span_pos for pos in ['NOUN', 'PROPN'])]
    return span_noun_indices

def get_cluster_head(doc: Doc, cluster: List[List[int]], noun_indices: List[int]):
    head_idx = noun_indices[0]
    head_start, head_end = cluster[head_idx]
    head_span = doc[head_start:head_end+1]
    return head_span, [head_start, head_end]

def is_containing_other_spans(span: List[int], all_spans: List[List[int]]):
    return any([s[0] >= span[0] and s[1] <= span[1] and s != span for s in all_spans])

def improved_replace_corefs(document, clusters):
    resolved = list(tok.text_with_ws for tok in document)
    all_spans = [span for cluster in clusters for span in cluster]  # flattened list of all spans

    for cluster in clusters:
        noun_indices = get_span_noun_indices(document, cluster)

        if noun_indices:
            mention_span, mention = get_cluster_head(document, cluster, noun_indices)

            for coref in cluster:
                if coref != mention and not is_containing_other_spans(coref, all_spans):
                    core_logic_part(document, coref, resolved, mention_span)

    return "".join(resolved)

# def parse_args():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--input_text', default='input_text.txt')
#     parser.add_argument('--output_text', default='resolved_input_text.txt')

#     return parser.parse_args()


if __name__ == "__main__":
    # args = parse_args()

    predictor, nlp = load_models()
    with open('../worldGenKG/input_text.txt', 'r') as f:
        text = f.read()

#     text = "Link awakens from a deep slumber and a mysterious voice guides him to discover what has become of the ruined country of Hyrule Kingdom. Link leaves the Shrine of Resurrection and looks out at Hyrule on top of the Great Plateau. Link then meets an Old Man by a campfire. The Old Man promises Link his Paraglider, which is the only way to get down from the plateau. However, he first wants Spirit Orbs from nearby Shrines, in particular the Oman Au Shrine, Ja Baij Shrine, Owa Daim Shrine, and the Keh Namut Shrine. After Link gets the spirit orbs, the Old Man appears, then mysteriously disappears, telling Link to meet him in the Temple of Time. The Old Man reveals himself as the spirit of the deceased King of Hyrule, King Rhoam. Link learns from King Rhoam that 100 years prior, a great evil known as the Calamity Ganon rose up and laid waste to the kingdom and its people. Unable to be defeated, it was sealed within Hyrule Castle, while the ruins of the land were ravaged by nature over time. Although trapped, the Calamity Ganon has grown in power, and Link must defeat it before it breaks free once more and destroys the world. The mysterious voice turns out to be Zelda, who is the daughter of King Rhoam. \
# \
# After escaping the confines of the plateau, Link is directed to meet the wise Sheikah elder Impa, and learn about the Guardians and Divine Beasts: 10,000 years prior these machines were created and successfully used by another Hero and another Princess to defeat the Calamity Ganon. But throughout the ages, knowledge about the ancient technology was lost until excavations in Hyrule Kingdom brought them to light once more, coinciding with the expected return of Calamity Ganon a hundred years ago. The Guardians were reactivated and four Champions were chosen to control the Divine Beasts: the Zora princess Mipha, the Goron warrior Daruk, the Gerudo chief Urbosa, and the Rito archer Revali. All the while, Zelda was unsuccessfully trying to gain access to her own prophesied powers, accompanied on her quests by her knight, the Hylian Champion Link. When the Calamity Ganon ultimately attacked, it devastated the Kingdom of Hyrule Kingdom by taking control of the ancient machines and turning them against the Hyruleans. As a last resort, Zelda was able to place the gravely wounded Link in the Shrine of Resurrection and use her awoken sealing powers to trap herself with Calamity Ganon in Hyrule Castle.\
# \
# As Link sets off on his quest to defeat Calamity Ganon, he is asked to investigate the fate of the Divine Beasts and their former Champions. His ultimate goal remains to reach the Calamity Ganon and free the trapped Zelda before the whole world is laid to waste. But with the entire Kingdom of Hyrule before him to explore, it is up to Link himself to decide how he wishes to fulfill his foretold role as the Hylian Champion, and to save Hyrule Kingdom."
    clusters = predictor.predict(text)['clusters']
    doc = nlp(text)
    resolved_text = improved_replace_corefs(doc, clusters)
    print(resolved_text)
    # with open(args.output_text, 'w') as f:
    #     f.write(resolved_text)
