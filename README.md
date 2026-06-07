# AI Powered Resume Scanner

## Overview
AI Powered Resume Scanner is an NLP based system developed for resume screening, ranking, and candidate filtering.
The project automatically compares resumes against job descriptions and ranks candidates using similarity scoring techniques.
---

## Features
* Resume PDF extraction
* Resume ranking
* Job description matching
* NLP processing using SpaCy
* TF-IDF similarity scoring
* Candidate filtering automation
---

## Technologies Used
* Python
* SpaCy
* PDFPlumber
* Scikit-Learn
* Pandas
* NLP
---

## Project Workflow
1. Generate resumes
2. Extract resume text
3. Process text using NLP
4. Compare with job descriptions
5. Rank resumes using similarity scores
---

## Installation
Install dependencies:
pip install spacy pdfplumber pandas numpy scikit-learn

Download NLP model:
python -m spacy download en_core_web_sm

Run:
python generate-resume.py

python resume-scanner.py
---

## Output
The system generates ranked resumes according to similarity with job requirements.
Example:
1. resume_1.pdf
2. resume_2.pdf
3. resume_3.pdf
---

## Future Improvements
* Resume upload interface
* ATS score generation
* Resume recommendation system
---

Developed by Heena Kousar
