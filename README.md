# Assignment 1 - Extracting linguistic features using spaCy
This assignment is ***Part 1*** of the portfolio exam for ***Language Analytics S23***. The exam consists of 5 assignments in total (4 class assignments and 1 self-assigned project).

## 1.1. Contribution
The initial assignment was created partially in collaboration with other students in the course, also making use of code provided as part of the course. The final code is my own. Several adjustments have been made since the initial hand-in.

Here is the link to the GitHub repository containing the code for this assignment: https://github.com/keresztalina/cds_lang_1

## 1.2. Assignment description by Ross
*(**NB!** This description has been edited for brevity. Find the full instructions in ```README_rdkm.md```.)*

This assignment concerns using ```spaCy``` to extract linguistic information from a corpus of texts.

The corpus is an interesting one: *The Uppsala Student English Corpus (USE)*. All of the data is included in the folder called ```in``` but you can access more documentation via [this link](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457).

For this exercise, you should write some code which does the following:

- Loop over each text file in the folder called ```in```
- Extract the following information:
    - Relative frequency of Nouns, Verbs, Adjective, and Adverbs per 10,000 words
    - Total number of *unique* PER, LOC, ORGS
- For each sub-folder (a1, a2, a3, ...) save a ```.csv``` table which contains the above information.

## 1.3. Methods
The purpose of this script is to loop through a series of text documents, extract a number of linguistic features from them, and then save this data in a ```.csv``` format. The data is contained within a folder, ```USEcorpus```. There are 14 subfolders, each containing a varying number of ```.txt``` files. 

First, some key structural data established. The path to the ```USEcorpus``` directory is established and the subfolders identified. In order to help with extracting certain linguistic features, the associated codes (e.g. ```"NOUN"``` or ```"LOC"```) are prepared. The structure of the resulting ```.csv``` files is also established. Some helper functions are also created.

Secondly, the script loops through every folder and the files contained within are listed. A dataframe is prepared to receive the output for the folder. The script then loops through every file in the folder. The text is loaded and cleaned of punctuation, new lines, etc, then passed into the ```spaCy``` model. Taking the pre-established list of word types, it finds their quantity in the text and divides the number by the overall number of words, resulting in the word type's relative frequency. Then, the named entities are extracted from the text and counts the entity types listed in the pre-established list of necessary entity types. The relative frequencies and the named entity counts are pulled into the pre-established dataframe and the dataframe is saved as a ```FOLDER_NAME.csv``` file with the following format:

|Filename|RelFreq NOUN|RelFreq VERB|RelFreq ADJ|RelFreq ADV|Unique PER|Unique LOC|Unique ORG|
|---|---|---|---|---|---|---|---|
|file1.txt|---|---|---|---|---|---|---|
|file2.txt|---|---|---|---|---|---|---|
|etc|---|---|---|---|---|---|---|

## 1.4. Usage
### 1.4.1. Prerequisites
This code was written and executed in the UCloud application's Coder Python interface (version 1.77.3, running Python version 3.9.2). UCloud provides virtual machines with a Linux-based operating system, therefore, the code has been optimized for Linux and may need adjustment for Windows and Mac.

### 1.4.2. Installations
1. Clone this repository somewhere on your device. The data is already contained within the ```/cds_lang_1/in``` folder.
2. Open a terminal and navigate into the ```/cds_lang_1``` folder. Run the following lines in order to install the necessary packages and load the required language model:
        
        pip install --upgrade pip
        python3 -m pip install -r requirements.txt
        python3 -m spacy download en_core_web_md

### 1.4.3 Run the script.
In order to run the script, make sure your current directory is still the ```/cds_lang_1``` folder. From command line, run:

        python3 src/extract_features.py

The 14 output files can be found in  ```/cds_lang_1/out```.

### 1.5 Discussion
Overall, the script functioned as expected. For each text, all required information has been extracted and is in a form that is suitable for conducting further analyses.










