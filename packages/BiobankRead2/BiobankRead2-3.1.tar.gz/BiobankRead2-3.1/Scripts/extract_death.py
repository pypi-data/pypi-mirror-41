# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 18:29:00 2018

@author: Deborah
"""

import os
import sys
import argparse
import pandas as pd
import numpy as np

'''Example run:
    python extract_death.py \
        --csv <csv file> \
        --html <html file> \
        --excl x/y/z.csv \
        --out <results folder> \
        --codes ['C34'] \ ## death by lung cancer. Default is 'All', returns all deaths by any cause in UKB
        --primary True \ ## parse primary cause of death
        --secondary False \ ## parse contributing causes to death
'''

# Function to deal nicely with Boolean parser options
# https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

parser = argparse.ArgumentParser(description="\n BiobankRead HES_extract. Extracts data from HES records as made available within UKB")

in_opts = parser.add_argument_group(title='Input Files', description="Input files. The --csv and --html option are required")
in_opts.add_argument("--csv", metavar="{File1}", type=str,required=False, default=None, help='Specify the csv file associated with the UKB application.')
in_opts.add_argument("--html", metavar="{File2}", type=str,required=False, default=None, help='Specify the html file associated with the UKB application.')

out_opts = parser.add_argument_group(title="Output formatting", description="Set the output directory and common name of files.")
out_opts.add_argument("--out", metavar='PREFIX', type=str, help='Specify the name prefix to output files')
out_opts.add_argument("--codes", metavar="{File3}", nargs='+', type=str, default='All', help='Specify cause of death codes to extract')

options = parser.add_argument_group(title="Optional input", description="Apply some level of selection on the data")
options.add_argument("--primary", type=str2bool, nargs='?', const=True, default=True,  help="Primary cause of death")
options.add_argument("--secondary", type=str2bool, nargs='?', const=True, default=False,  help="Secondary cause of death")
options.add_argument("--excl", metavar="{File5}", type=str, default=None, help='Specify the csv file of EIDs to be excluded.')
############################################################################################################


# class Object(object):
#    pass
# args = Object()
# args.out='/media/storage/codes/BiobankRead-Bash'
# args.html=r'/media/storage/UkBiobank/Application_236/R4528/ukb4528.html'
# args.csv=r'/media/storage/UkBiobank/Application_236/R4528/ukb4528.csv'
# args.codes=['I110',
#'I132',
#'I500',
#'I501',
#'I509']
# args.primary=True
# args.secondary=True
###################

def getcodes(UKBr, args):
    #argnames = vars(args)
    #codes = argnames['codes'][0]
    codes = args.codes
    if UKBr.is_doc(codes):
        Codes=UKBr.read_basic_doc(codes)
    else:
        Codes = codes
    #print(Codes)
    Codes = UKBr.find_ICD10_codes(select=Codes)
    return Codes

# NEEDS SORRTING OUT
# SHOULD BE POSSIBLE TO STRIP OUT MUCH OF THE LOOP
# USING EG df.isin(codes_list) OR SIMILAR
# I think the above reverse the logic
# Maybe this:
# df[df[colname]].str.contains(code)
def count_codes_new(UKBr, df,args):
    codes_list=getcodes(UKBr, args)
    #ids = list(set(df['eid'].tolist()))
    cols = ['eid']+codes_list
    df_new=pd.DataFrame(columns=cols)
    for c in df.columns[1::]:
        new_ymp=pd.DataFrame(columns=['eid'])
        df_new[c] = df[c].copy()
        df_new = df.isin(codes_list)
        df_new = df_new[1::]
        
        # Look for each code d in column c
        for d in codes_list:
            ymp = df[df[c].str.contains(d)==True]
            if(len(ymp)>0):
                # Found some hits
                ymp_sub=pd.DataFrame()
                ymp_sub['eid']=ymp['eid'].tolist()
                # Create column for current code
                ymp_sub[d]=1
                # Merge results for this code with master in new_ymp
                new_ymp=pd.merge(new_ymp,ymp_sub,on='eid',how='outer')
        if(len(new_ymp)>0):
            df_new=pd.merge(df_new,new_ymp,on='eid',how='outer')
        #df_new=pd.concat([df_new,new_ymp],ignore_index=False,sort=True)
    for d in codes_list:
        # Get columns containing code
        cols = [c for c in df_new.columns if str(d) in str(c)]
        # Sum across columns containing code
        df_new[d]=df_new[cols].fillna(value=0).sum(axis=1)
        df_new[d]=[1*(V>0) for V in df_new[d]]
    df_new=df_new[['eid']+codes_list]
    return df_new

def count_codes(UKBr, df,args):
    codes_list=getcodes(UKBr, args)
    #ids = list(set(df['eid'].tolist()))
    cols = ['eid']+codes_list
    df_new=pd.DataFrame(columns=cols)
    for c in df.columns[1::]:
        new_ymp=pd.DataFrame(columns=['eid'])
        for d in codes_list:
            ymp=df[[str(d) in str(x) for x in df[c]]]
            if(len(ymp)>0):
                ymp_sub=pd.DataFrame()
                ymp_sub['eid']=ymp['eid'].tolist()
                ymp_sub[d]=1
                new_ymp=pd.merge(new_ymp,ymp_sub,on='eid',how='outer')
        if(len(new_ymp)>0):
            df_new=pd.merge(df_new,new_ymp,on='eid',how='outer')
        #df_new=pd.concat([df_new,new_ymp],ignore_index=False,sort=True)
    #
    #df_new_test = df.isin(codes_list)
    for d in codes_list:
        cols = [c for c in df_new.columns if str(d) in str(c)]
        df_new[d]=df_new[cols].fillna(value=0).sum(axis=1)
        df_new[d]=[1*(V>0) for V in df_new[d]]
    df_new=df_new[['eid']+codes_list]
    #j=0
    # Loop over eids
    ##print(len(ids))
    #for i in ids:
    #    # Select this eid
    #    df_sub=df[df['eid']==i]
    #    # tmp2 = data columns for this eid
    #    codes_this=list(df_sub.iloc[0][1:len(df_sub.columns)-1])
    #    # Get columns with matching codes as Boolean vector
    #    # Note - C34 also matches C340 C341 etc
    #    # Is this intended? YES
    #    res = [i]+[int(x in codes_this) for x in codes_list]
    #    df_new.loc[j]=res
    #    j += 1
    return df_new

def merge_primary(df):
    cols = df.columns.tolist()[1::]
    primary = [x for x in cols if '(primary)' in x]
    ids = list(set(df['eid'].tolist()))
    res=[]
    for i in ids:
        df_sub=df[df['eid']==i]
        res.append(df_sub[primary].values.any())
    df['primary cause of death']=res
    df.drop(primary, axis=1, inplace=True)
    return df

def rename_cols_death(df):
    cols = df.columns.tolist()[1::]
    secondary = [x for x in cols if '(secondary)' in x]
    for c in secondary:
        [a,b]=c.split('-')
        x = 'secondary cause of death-'+b
        df.rename(columns={c: x},inplace=True)
    return df

def extractdeath(UKBr, args):
    All_vars = UKBr.Vars
    if args.secondary and args.primary:
        SR = [x for x in All_vars if 'of death: ICD10' in str(x)]
        dead_df = UKBr.extract_many_vars(SR,baseline_only=False, dropNaN=True)
    else:
        string = 'Underlying (primary) cause'*args.primary + 'Contributory (secondary) causes'*args.secondary
        SR = [x for x in All_vars if string+' of death: ICD10' in str(x)]
        dead_df = UKBr.extract_variable(SR[0],baseline_only=False, dropNaN=True)
    dead_df.dropna(axis=0,how='all',subset=dead_df.columns[1::],inplace=True)
    if args.codes[0] != 'All':
        dead_df = count_codes(UKBr, dead_df, args)
        dead_df['all_cause'] = dead_df[dead_df.columns[1::]].sum(axis=1)
        dead_df=dead_df[dead_df.all_cause !=0]
    else:
        dead_df=merge_primary(dead_df)
        dead_df=rename_cols_death(dead_df)
    return dead_df

def dates_died(UKBr, df):
    dates=['Date of death','Age at death']
    dates_df = UKBr.extract_many_vars(dates,baseline_only=False, dropNaN=True)
    dates = [x for x in dates_df.columns.tolist()[1::] if 'Date' in x]
    ages = [x for x in dates_df.columns.tolist()[1::] if 'Age' in x]
    dates_df.dropna(axis=0,how='all',subset=dates_df.columns[1::],inplace=True)
    dates_df['death_date']=dates_df[dates].replace(np.nan,UKBr.end_follow_up).min(axis=1)
    #dates_df['death_date']=dates_df[dates].replace(np.nan,2199).min(axis=1)
    dates_df['death_age']=dates_df[ages].replace(np.nan,150).min(axis=1)
    # This fixes the type but doesn't fix the problem!
    df[['eid']] = df[['eid']].astype(np.int64)
    df2=pd.merge(dates_df[['eid','death_date','death_age']],df,on='eid',how='inner')
    return df2

if __name__ == '__main__':
    args = parser.parse_args()
    namehtml=args.html
    namecsv=args.csv
    nameexcl = args.excl
    
    ### import Biobankread package
    updatepath = os.path.join(os.path.dirname(os.path.abspath('__file__')), '..')
    sys.path.append(updatepath)
    # Note some issues with case of directory names on different systems
    try:
        import BiobankRead2.BiobankRead2 as UKBr2
        UKBr = UKBr2.BiobankRead(html_file = namehtml, csv_file = namecsv, csv_exclude = nameexcl)
        print("BBr loaded successfully")
    except:
        raise ImportError('UKBr could not be loaded properly')

    Df = extractdeath(UKBr, args)
    Df = dates_died(UKBr, Df)
    final_name = args.out+'.csv'
    print("Outputting to", final_name)
    Df.to_csv(final_name,sep=',',index=None)
