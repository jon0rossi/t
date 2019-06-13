import csv
import scipy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
class ds:

    def __init__(self, job_code, df = None):
        self.job_code = job_code
        #self.csv_name
        self.df = df if df is not None else None
        self.y = 5 # read in our additional files here? 

    def sum(x):
        print(x)

    def t():
        print(4)
    
    def df_from_csv_name(csv_name):
        self.df = read_csv(csv_name)

    def g1(self): # graphs avg tpm per chromosome (avg over all 7 patients)
        df1 = pd.read_csv('ENS Ids By Chromosome.csv')
        df3 = self.df.join(df1.set_index('ENS ID'), on='ENS ID')
        del df3['Transcript length (including UTRs and CDS)']
        look1 = df3.groupby(['Chromosome']).mean()
        look1['meanp'] = look1.mean(axis=1)
        new1 = look1[['meanp']].copy()
        new1.plot()
        plt.show()

    def g2(self): # graphs avg tpm for each chromosome for each patient 
        df1 = pd.read_csv('ENS Ids By Chromosome.csv')
        df3 = self.df.join(df1.set_index('ENS ID'), on='ENS ID') # SHOULD I COPY SELF.DF!?
        del df3['Transcript length (including UTRs and CDS)']
        look1 = df3.groupby(['Chromosome']).mean()
        look1.plot()
        plt.show()

    def g3(self): # top 100 ens ids by avg tpm over all patients 
        df1 = self.df.copy()
        df1['avg'] = df1.mean(axis = 1)

        
        df1 = df1.sort_values(by = ['avg']).iloc[-100:]
        df1 = df1.reset_index()
        df1['index'] = df1.index
        #print(df1)
        df1.plot.scatter(x = 'index', y = 'avg')
        plt.show()

    def write_to_csv(self,file_name): # writes self.df to a csv named 'name'
        #  Example usage:        x.write_to_csv('test1.csv') where x is the ds instance(?)
        self.df.to_csv(file_name, index = False)





x = ds(5, pd.read_csv('patientlist.csv'))
#print(x.df)
#x.write_to_csv('test1.csv')