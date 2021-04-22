import sys
import plotly.express as px
import pandas as pd
from .models import CryptBD

class UserInput:
    state = True # the input-field doesn`t blocked
    def __init__(self, st_date, end_date, coin_inp, intervals = None, investments = None):
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
    def getDataRange(self):
        return self.df


class Plot:
    def draw(self):
        #df = pd.read_csv("C:\\Users\\Jul\\Desktop\\BTC__USD.csv")
        data_inst = Data()
        fig = px.line(data_inst.df.iloc[::-1], x='date', y='close', color_discrete_sequence=['#14213d']) #x:date; y:price
        fig.update_layout(
            font_family="Times New Roman",
            font_color = '#14213d',
            xaxis_title="Date",
            yaxis_title="Price",
            paper_bgcolor = "white",
            margin=dict(l=0, r=0, t=15, b=15),
            plot_bgcolor = '#FFE5D9',
        )
        # fig.show()
        fig.write_html("genie\\templates\\genie\\inc\\_plot_path.html",
                full_html=False,
                include_plotlyjs='cdn')







