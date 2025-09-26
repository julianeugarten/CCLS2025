# CCLS2025
Code and derived data for a paper submitted to CCLS2025. [You can already read a preprint here](https://tuprints.ulb.tu-darmstadt.de/30143/).

# Note: run all notebooks in Python 3.9.18.

# What this repo contains
- notebooks folder, containing 4 notebooks:
    - Notebook 0 for exploring the Riveter-objects I created for the paper and (optionally) your own Riveter-objects. Some of the code used in this notebook was adapted from [Antoniak et al.'s repo of Riveter documentation](https://github.com/maartensap/riveter-nlp). To run Riveter on fanfiction from AO3, you will need a csv of work-ids for the fanfiction, which you can collect using [Radiolorian's AO3-Scraper](https://github.com/radiolarian/AO3Scraper).
    - Notebook 1 for getting Riveter scores out of a Riveter-object -- your own, or the ones included in the repo -- and into a Pandas dataframe and/or csv file, and for calculating difference scores between selected entities.
    - Notebook 2 for re-creating the plots included in the paper. Some of the code used in this notebook was adapted from [Yang & Pianzola's Omegaverse Study (2024)](https://github.com/GOLEM-lab/Omegaverse_Study).
    - Notebook 3 for re-creating the correlation matrices included in the paper. 
    - CCLS2025.csv, which contains Riveter scores (on both power and agency) for the selected entities (Hades and Persephone) analyzed in the paper. Notebooks 1-3 run you through the process of analyzing data from this file. This file also contains assorted metadata on the fanfiction, taken from [MythFic Metadata](https://doi.org/10.34973/2mye-8468), including the data on violence and popularity metrics used in the paper.

- Other items, namely
    - Pickled Riveter objects : 'hadper_power_CCLS_redacted.pkl' and 'hadper_agency_CCLS_redacted.pkl'. Note that the fanfiction-texts themselves have been redacted from these models.
    - For completion's sake, a second copy of the csv-file with all the (meta)data
    - a folder titled correlations_by_year, where you can browse some of the outputs of Notebook 3.


# Dockerized Environment
This project is fully Dockerized, so you can run all notebooks in the same environment as I did. This is especially important for notebook 0, the other notebooks can probably be run without the Docker environments if you prefer.  

The prerequisites for the Dockerized environment are:

- Install [Docker Desktop](https://www.docker.com/products/docker-desktop)

- (Optional) Install [VS Code](https://code.visualstudio.com/) and the **Remote - Containers** extension

## To Build Docker Image

Open terminal in this folder and run:

```bash

docker build -t riveter-notebook .