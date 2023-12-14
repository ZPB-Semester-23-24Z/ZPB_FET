import pandas as pd


class fr:
    path=r"res\FETs.xlsx"
    df=0
    def read(self):
        self.df= pd.read_excel(self.path)
    def get_df(self):
        return self.df




