# CCLS2025
Code and derived data for a paper submitted to CCLS2025. [You can already read a preprint here](https://tuprints.ulb.tu-darmstadt.de/30143/).

Specifically, this repo contains:
- riveter_runfile.py for running [Riveter](https://github.com/maartensap/riveter-nlp/tree/main) on your own set of texts and pickling your own Riveter-object. To run this file you will need a csv of work-ids for fanfiction on AO3, which you can collect using [Radiolorian's AO3-Scraper](https://github.com/radiolarian/AO3Scraper).
- Notebook 0, which explores the two pickled (and redacted) Riveter objects from the paper. Some of the code used in this notebook was adapted from [Antoniak et al.'s repo of Riveter documentation](https://github.com/maartensap/riveter-nlp).
- These Riveter objects are also included in the repo: 'hadper_power_CCLS_redacted.pkl' and 'hadper_agency_CCLS_redacted.pkl'. Note that the fanfiction-texts themselves have been redacted from these models.
- Notebook 1 for getting Riveter scores out of a Riveter-object -- your own, or the ones included in the repo -- and into a Pandas dataframe and/or csv file, and for calculating difference scores between selected entities.
- CCLS2025.csv, which contains Riveter scores (on both power and agency) for the selected entities (Hades and Persephone) analyzed in the paper. This file also contains assorted metadata on the fanfiction, taken from [MythFic Metadata](https://doi.org/10.34973/2mye-8468), including the data on violence and popularity metrics used in the paper.
- Notebook 2 for re-creating the plots included in the paper. Some of the code used in this notebook was adapted from [Yang & Pianzola's Omegaverse Study (2024)](https://github.com/GOLEM-lab/Omegaverse_Study).
- Notebook 3 for re-creating the correlation matrices included in the paper. 
- Finally, the folder 'correlations_by_year' contains correlation tables between Riveter scores and popularity metrics (including the kudos/hits ratio) for every year for which statistically significant correlations were found.

