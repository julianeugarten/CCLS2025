# conda activate riveterEnv

#import libraries
import os
import random
from riveter import Riveter 
import pandas as pd

#load the data
hadper_df = pd.read_csv('hadper_short_stories.csv', on_bad_lines='skip')
work_ids = hadper_df["work_id"].to_list()
stories = hadper_df["story"].to_list()

#load lexicon and train model
riveter = Riveter()
riveter.load_sap_lexicon('agency') # you can change 'power' to 'agency' to get another dimension
riveter.train(stories,
              work_ids)


# save the model
riveter.save('hadper_CCLS_agency.pkl')

# load saved results into riveter this way:
# riveter = Riveter(filename = "hadper_power.pkl")

