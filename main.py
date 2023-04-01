import spacy
from spacy.training import Example, offsets_to_biluo_tags
import random
from spacy.util import minibatch, compounding
from data import TRAIN_DATA


def train_ner_model(train_data, model=None, n_iter=100):
    if model is not None:
        nlp = spacy.load(model)
    else:
        nlp = spacy.blank("en")

    if "ner" not in nlp.pipe_names:
        ner = nlp.add_pipe("ner")
    else:
        ner = nlp.get_pipe("ner")

    for _, annotations in train_data:
        for ent in annotations.get("entities"):
            ner.add_label(ent[2])

    nlp.initialize()  # Initialize the NLP pipeline before creating examples
    examples = [Example.from_dict(nlp.make_doc(text), annotations) for text, annotations in train_data]
    nlp.initialize(lambda: examples)  # Now, use the initialized NLP pipeline

    # Check the alignment of entities
    for text, annotations in TRAIN_DATA:
        doc = nlp.make_doc(text)
        tags = offsets_to_biluo_tags(doc, annotations["entities"])
        print(f"Tags for '{text}': {tags}")

    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
    with nlp.disable_pipes(*other_pipes):
        if model is None:
            nlp.begin_training()
        else:
            nlp.resume_training()

        for itn in range(n_iter):
            random.shuffle(examples)
            batches = minibatch(examples, size=compounding(4.0, 32.0, 1.001))
            losses = {}

            for batch in batches:
                nlp.update(batch, drop=0.5, losses=losses)

    return nlp

# Train the NER model
nlp = train_ner_model(TRAIN_DATA)

# Save the trained model to disk
nlp.to_disk("C:\\Users\\Farhan Ali Rahmoon\\Desktop\\moonath\\pythonProject")
