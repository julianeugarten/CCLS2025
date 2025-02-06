# CCLS2025
Code and derived data for a paper submitted to CCLS2025.

Specifically, this repo contains:
- riveter_runfile.py for running [Riveter](https://github.com/maartensap/riveter-nlp/tree/main) on your own set of texts and pickling your Riveter-object. To run this file you will need a csv of work-ids for fanfiction on AO3, which you can collect using [Radiolorian's AO3-Scraper](https://github.com/radiolarian/AO3Scraper).
- Notebook 1 for getting Riveter scores out of the Riveter-object and into a Pandas dataframe and/or csv file, and for calculating difference scores between selected entities.
- CCLS2025.csv, which contains Riveter scores (on both power and agency) for the selected entities (Hades and Persephone) analyzed in the paper *A Powerful Hades is an Unpopular Dude* submitted to CCLS2025. This file also contains assorted metadata on the fanfiction, taken from [MythFic Metadata](https://doi.org/10.34973/2mye-8468), including the data on violence and popularity metrics used in the paper.
- Notebook 2 for re-creating the plots included in the paper. Some of the code used in this notebook was adapted from [Yang & Pianzola's Omegaverse Study (2024)](https://github.com/GOLEM-lab/Omegaverse_Study).
- Notebook 3 for re-creating the correlation matrices included in the paper. 

