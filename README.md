# CCLS2025
Code and derived data for a paper submitted to CCLS2025. [You can already read a preprint here](https://tuprints.ulb.tu-darmstadt.de/30143/).

# What this repo contains
- notebooks folder, containing 2 notebooks:
    - Notebook 1 for re-creating the plots included in the paper. Some of the code used in this notebook was adapted from [Yang & Pianzola's Omegaverse Study (2024)](https://github.com/GOLEM-lab/Omegaverse_Study).
    - Notebook 2 for re-creating the correlation matrices included in the paper. 
    - CCLS2025.csv, which contains Riveter scores (on both power and agency) for the selected entities (Hades and Persephone) analyzed in the paper. This file also contains assorted metadata on the fanfiction, taken from [MythFic Metadata](https://doi.org/10.34973/2mye-8468), including the data on violence and popularity metrics used in the paper.

- Other items, namely
    - Pickled Riveter objects : 'hadper_power_CCLS_redacted.pkl' and 'hadper_agency_CCLS_redacted.pkl'. Note that the fanfiction-texts themselves have been redacted from these models. If you want to explore these models, you need to run [Riveter](https://github.com/maartensap/riveter-nlp). To run Riveter on fanfiction from AO3, you will need a csv of fanfiction including work-ids, which you can collect using [Radiolorian's AO3-Scraper](https://github.com/radiolarian/AO3Scraper).
    - For completion's sake, a second copy of the csv-file with all the (meta)data
    - a folder titled correlations_by_year, where you can browse some of the outputs of Notebook 1.
