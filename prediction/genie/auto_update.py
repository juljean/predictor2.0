import datetime as dt
import sqlite3
import pandas_datareader.data as web

class LiveUpdate:
    def __init__(self, cr_name):
        self.cr_name = cr_name
        self.end = dt.date.today()
        self.conn = sqlite3.connect('predictor_2.0\\prediction\\db.sqlite3')
        self.c = self.conn.cursor()

    # Designate the start value basically
    def start_designation(self):
        start_dt = self.data_read()[2]  # + 1 from the last one
        start = dt.datetime.strptime(start_dt, '%Y-%m-%d')
        start += dt.timedelta(days=2)
        return start

    # Check if we need to update it
    def validation(self):
        start = self.start_designation()
        print(start.date())
        if dt.datetime.today().date() != start.date():
            self.scratch_data(start)
        else:
            print("No need to update")

    # Scratch the data from the web and convert it to dictionary for iterating
    def scratch_data(self, start):
        df = web.DataReader(['{}-USD'.format(self.cr_name)], 'yahoo', start, self.end)
        dates = []
        for i in df.index.values:
            dates.append(str(i)[:10])
        df[('Date', '{}-USD'.format(self.cr_name))] = dates
        df_records = df.to_dict('records')

        self.data_entry(df_records)

    # Get the last row for start value to set the start variable
    def data_read(self):
        self.c.execute('SELECT * FROM genie_{}BD ORDER BY date DESC LIMIT 1'.format(self.cr_name))
        data = self.c.fetchone()
        return data

    # Entry new rows of data
    def data_entry(self, df_records):
        for record in df_records:
            date = record[('Date', '{}-USD'.format(self.cr_name))]
            close = record[('Close', '{}-USD'.format(self.cr_name))]
            self.c.execute("INSERT INTO genie_BtcBD (date, close) VALUES (?, ?)",
                      (date, close))
            self.conn.commit()
        self.c.close()
        self.conn.close()

LiveUpdate("BTC").validation()