# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 11:08:56 2018

@author: stollpa

work with pandas and read table

"""

import pandas as pd
import numpy as np

table = pd.read_excel("nbt.2489-S2.xlsx")  #read the source table
df_tot = pd.DataFrame(table[3:])
df_tot = df_tot.drop(df_tot.columns[[9, 10,11,12,13,14,15,16]], axis=1)  #delete unnecessery columns
#change column names
#df_tot.columns=table.loc[2]
#df_tot = df_tot.rename(columns = {'Absolute (mM)':'Type'}) 
#df_tot = df_tot.rename(columns = {1:'Type'}, inplace = True) #does not work yet
df_tot.columns = ['Type', 'Metabolite', '10', '15', '25', '40', '45', '55', '70']

# making different tables
df_mean=df_tot.iloc[::2] #every second row
df_mean = df_mean.reset_index(drop=True) #new index

df_sd = df_tot.iloc[1::2] #every other second row
df_sd = df_sd.reset_index(drop=True) #new index
df_sd.loc[57]=np.nan #add the last missing row
df_sd['Metabolite'] = df_mean['Metabolite'].values #rename the metabolites
df_sd = df_sd.drop('Type', 1) #delete column type

df_type = pd.DataFrame(df_mean['Type']) #new df type
df_type = df_type.reset_index(drop=True) #new index
df_type['Metabolite'] = df_mean['Metabolite'] #rename the metabolites

df_mean = df_mean.drop('Type', 1) #delete column type


## change metabolite names --> dictionary
metaboliteID = {
        'asparagine' : 'asn__L',
        'glutamine' : 'gln__L',
        'citrulline' : 'citr__L',
        'diaminopimelate' : '', ##
        'Homoserine' : 'hom__L',
        'Ga6P' : 'gam6p', ##???
        'Guanine' : 'gua',
        'Tyrosine' : 'tyr__L',
        'phenylalanine' : 'phe__L',
        'aspartate' : 'asp__L',
        'glutamate' : 'glu__L',
        'Lactate' : 'lac__L',
        'tryptophane' : 'trp__L',
        'G6P' : 'g6p',
        'Ms6P' : '', ##
        'R5P' : 'r5p',
        'F6P' : 'f6p',
        'GlycerolP' : 'glyc1p',
        'G1P' : 'g1p',
        'S7P' : 's7p',
        'Ru5P' : '', #L or D ? ru5p__D / L
        'Xu5P' : '', #L or D? xu5p__D
        'GTTred' : 'gthrd', # Reduced glutathione ?
        'DHAP' : 'dhap',
        'NAD' : 'nad',
        'Panthothenate' : 'pnto__R',
        'cAMP' : 'camp',
        'Succinate' : 'succ',
        'GTTox' : 'gthox', # Oxidized glutathione ?
        'Malate' : 'mal__L', # L???
        'UDP-hexose': '', ##
        'alpha ketoglutarate' : 'akg', # 2-Oxoglutarate?
        'fumarate' : 'fum',
        'ADP-hexose' : '',##
        'ADP-pentose' : '',##
        'xPG' : '',##
        '6PG' : '',##
        'NADH' : 'nadh',
        'Aconitate' : 'acon_C', # acon_C cis/Trans?
        'NADP' : 'nadp',
        'PEP' : 'pep',
        'FBP' : 'f26bp', ## or fructose16bisphosphate
        'methylcitrate_methylisocitrate' : '',##
        'citrate_isocitrate' : '', ##
        'isocitrate' : 'icit',
        'FMN' : 'fmn',
        'BPG' : '', # bisphosphoglycerate?
        'FAD' : 'fad',
        'AcCoA' : 'accoa',
        'NADPH' : 'nadph',
        'PRPP' : 'prpp',
        'ATP' : 'atp',
        'ADP' : 'adp',
        'AMP' : 'amp',
        'GTP' : 'gtp',
        'GDP' : 'gdp',
        'GMP' : 'gmp'
        }
