##### IMPORT PACKAGES
import os
import sys
import pandas as pd
import spacy
import regex as rx

##### SETUP FOR MAIN CODE
# Load language model
nlp = spacy.load(
    "en_core_web_md")

# Navigation within corpus
# path to whole corpus
corpus_path = os.path.join(
    "in", 
    "USEcorpus")
# folders within corpus
corpus_dir = os.listdir(
    corpus_path)

# Lists to wrangle inputs and outputs
# relative frequency types of interest
word_types = [
    "NOUN", 
    "VERB", 
    "ADJ", 
    "ADV"]
# named entity types of interest
entity_types = [
    "PERSON", 
    "LOC", 
    "ORG"]
# columns for output file
cols = [
    "Filename", 
    "RelFreq NOUN", 
    "RelFreq VERB", 
    "RelFreq ADJ", 
    "RelFreq ADV", 
    "Unique PER", 
    "Unique LOC", 
    "Unique ORG"]

##### FUNCTIONS
# function for counting relative frequency
def count_types(tokens, position, per_no_tokens):
    count = 0
    for token in tokens:
        if token.pos_ == position:
            count += 1
    rel_freq = count / len(tokens) * per_no_tokens
    rel_freq = round(rel_freq, 2)
    return(rel_freq)

# function for extracting a list of entities with type also included
def extract_entities(tokens):

    # get tokens
    entities = []
    for ent in tokens.ents:
        entities.append(ent.text)
    
    # get labels
    labels = []
    for ent in tokens.ents:
        labels.append(ent.label_)
    
    # zip
    ent_labels = zip(entities, labels)

    # turn into searchable data frame
    entities_list = pd.DataFrame(ent_labels, columns=["tokens", "pos"])

    return(entities_list)

# function for counting unique named entities
def count_entities(list_of_entities, position):
    filtered = list_of_entities[list_of_entities['pos'] == position]
    unique = filtered.drop_duplicates()
    unique_count = len(unique)
    return(unique_count)

##### MAIN
def main():

    for folder in corpus_dir:

        # find path of the folder we want to go into
        folder_path = os.path.join(
            "in", 
            "USEcorpus", 
            folder)
        # list files within folder
        folder_dir = os.listdir(
            folder_path)

        # set up data frame to receive output
        summary = pd.DataFrame(
            columns = cols)

        # loop through files in folders
        for document in folder_dir:

            ##### LOAD & PREPROCESS
            # find path of document
            doc_path = os.path.join(
                "in", 
                "USEcorpus", 
                folder, 
                document)

            # load document
            with open(doc_path, "r", encoding = "latin-1") as file:
                text = file.read()
            
            # clean text
            text = rx.sub(
                '<.*?>', 
                '', 
                text)
            text = rx.sub(
                '[\n\t]', 
                ' ', 
                text)
            
            # pass into NLP model
            doc = nlp(
                text)

            ##### COUNT RELATIVE FREQUENCIES
            # setup for relative frequency counts
            rel_freq_list = []

            # get the relative frequencies
            for word_type in word_types:
                rf = count_types(
                    doc, 
                    word_type, 
                    10000)
                rel_freq_list.append(
                    rf)
            
            ##### COUNT UNIQUE NAMED ENTITIES
            # recognize all entities in text
            entities = extract_entities(
                doc)

            # setup for unique entity count
            unique_ent_list = []

            # get the unique entity count
            for entity_type in entity_types:
                ue = count_entities(
                    entities, 
                    entity_type)
                unique_ent_list.append(
                    ue)
            
            ##### GET ALL THE DATA TOGETHER
            # make data frame from the data for this document
            docname = [document] # turn into list otherwise python complains
            docinfo_list = docname + rel_freq_list + unique_ent_list # pull together
            docinfo = pd.DataFrame(
                [docinfo_list], 
                columns = cols) # turn into data frame

            # append to overall data frame
            summary = pd.concat([
                summary, 
                docinfo])

        # prep file name
        filename = str(folder) + ".csv"

        # save dataframe
        outpath = os.path.join(
            "out", 
            filename)
        summary.to_csv(
            outpath, 
            index = False)

if __name__ == "__main__":
    main()