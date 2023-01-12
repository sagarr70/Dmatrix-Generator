import pandas as pd


def main(excel,cname):
    try:
        df = pd.read_excel(excel,dtype=str,na_filter=False)
        pincodes = df[cname].unique()
        return list(pincodes)
    except:
        return list()
    
    
if __name__=="__main__":
    main()
