import os
import pdfplumber
import spacy
import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ==========================
# LOAD NLP MODEL
# ==========================

nlp = spacy.load("en_core_web_sm")


# ==========================
# EXTRACT TEXT FROM PDF
# ==========================

def extract_text_from_pdf(pdf_path):

    with pdfplumber.open(pdf_path) as pdf:

        text = ""

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

    return text.strip()


# ==========================
# EXTRACT RESUME DETAILS
# ==========================

def extract_resume_details(text):

    doc = nlp(text)

    skills = set()

    education = set()

    experience = set()


    for ent in doc.ents:

        if ent.label_ in ["ORG"]:

            education.add(ent.text)

        elif ent.label_ in ["WORK_OF_ART","PRODUCT"]:

            experience.add(ent.text)


    for token in doc:

        if token.pos_ in ["NOUN","VERB"] and token.is_alpha:

            skills.add(token.lemma_)


    return {

        "Skills":list(skills),

        "Education":list(education),

        "Experience":list(experience),

        "Full Text":text

    }


# ==========================
# RANK RESUMES
# ==========================

def rank_resumes(

        resume_texts,

        job_description

):

    corpus=[job_description]+resume_texts

    vectorizer=TfidfVectorizer()

    tfidf_matrix=vectorizer.fit_transform(

        corpus

    )

    similarity_scores=cosine_similarity(

        tfidf_matrix[0],

        tfidf_matrix[1:]

    )

    ranked_resumes=sorted(

        enumerate(

            similarity_scores[0]

        ),

        key=lambda x:x[1],

        reverse=True

    )

    return ranked_resumes


# ==========================
# JOB DESCRIPTION
# ==========================

job_description="""

Python Developer with expertise in NLP,

Machine Learning,

data analysis,

Scikit-learn,

Pandas,

NLTK preferred.

"""


# ==========================
# LOAD RESUMES
# ==========================

resume_folder="resumes"

resume_texts=[]

resume_files=[]


for filename in os.listdir(

        resume_folder

):

    if filename.endswith(

            ".pdf"

    ):

        filepath=os.path.join(

            resume_folder,

            filename

        )

        text=extract_text_from_pdf(

            filepath

        )

        resume_texts.append(

            text

        )

        resume_files.append(

            filename

        )


# ==========================
# RANKING
# ==========================

ranked_resumes=rank_resumes(

    resume_texts,

    job_description

)


# ==========================
# OUTPUT
# ==========================

print(

"\n🎯 Ranked Resumes:\n"

)

for rank,(index,score) in enumerate(

        ranked_resumes

):

    print(

f"{rank+1}. {resume_files[index]} ---- Score: {score:.2f}"

)
