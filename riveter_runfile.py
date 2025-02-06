# conda activate riveterEnv (create your own virtual env if desired)

#import libraries
import os
import random
from riveter import Riveter 
import pandas as pd

#load the data
hadper_df = pd.read_csv('dataset.csv', on_bad_lines='skip') # change filename to your own
work_ids = hadper_df["work_id"].to_list() # your column of work-ids may have a different name
stories = hadper_df["story"].to_list() # your column of texts may have a different name

#load lexicon and train model
riveter = Riveter()
riveter.load_sap_lexicon('power') # you can change 'power' to 'agency' to get another dimension
riveter.train(stories,
              work_ids)


# save the model under a chosen filename
riveter.save('yourname_power.pkl')

# load saved results into riveter this way:
# riveter = Riveter(filename = "yourname_power.pkl")

