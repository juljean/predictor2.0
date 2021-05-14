import sys
import plotly.express as px
import pandas as pd
from .models import CryptBD

class UserInput:
    state = True # the input-field doesn`t blocked
    def __init__(self, st_date, end_date, coin_inp = "BTC", intervals = None, investments = None):
        self.startDate = st_date
        self.endDate = end_date
        self.coin = coin_inp
        self.granularity = intervals
        self.investments = investments


    def setStartDate(self, st_date):
        self.startDate = st_date

    def setEndDate(self, end_date):
        self.endDate = end_date

    def setCoin(self, coin_inp):
        self.coin = coin_inp

    def setGranularity(self, interval):
        self.granularity = interval

    def setInvestments(self, money):
        self.investments = money

    def setState(self, state_inp): #triggered by generate btn
        self.state = state_inp

class Data:
    def __init__(self):
        self.df = pd.DataFrame(list(CryptBD.objects.values('date', 'close')))
        for i in range(len(self.df['date'])):
            old_val = self.df._get_value(i, 'date')
            new_val = old_val.replace("/", "-")
            self.df['date'] = self.df['date'].replace([old_val], new_val)
        #print(self.df)

    def getDataRange(self):
        return self.df


class Plot:
    def __init__(self, raw_start = "11-3-2014" ,raw_end = "3-3-2020"):
        self.raw_start = raw_start
        self.raw_end = raw_end
    def draw(self):
        #df = pd.read_csv("C:\\Users\\Jul\\Desktop\\BTC__USD.csv")
        data_inst = Data()
        df = data_inst.df[::-1]
        #print(df)
        start_ind = data_inst.df.index[df['date'] == self.raw_start].tolist()[0]
        end_ind = data_inst.df.index[df['date'] == self.raw_end].tolist()[0]
        print(start_ind, end_ind)
        fig = px.line(df.iloc[start_ind:end_ind], x='date', y='close', color_discrete_sequence=['#14213d']) #x:date; y:price
        fig.update_layout(
            font_family="Times New Roman",
            font_color = '#14213d',
            xaxis_title="Date",
            yaxis_title="Price",
            paper_bgcolor = "white",
            margin=dict(l=0, r=0, t=15, b=15),
            plot_bgcolor = '#FFE5D9',
        )
        #fig.show()
        fig.write_html("genie\\templates\\genie\\inc\\_plot_path.html",
                full_html=False,
                include_plotlyjs='cdn')







