from pathlib import Path

import seaborn as sns
import matplotlib.pyplot as plt

from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui
#import bslib

from Regressionizer import *
from OutlierIdentifiers import *

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Dark mode
ui.input_dark_mode()

# Seaborn
#plt.style.use("dark_background")
#sns.set(style="ticks", context="talk")


plt.style.use("dark_background")
sns.set_theme(style="darkgrid")
sns.set(rc={
    "grid.color": "dimgray", 
    "grid.linewidth": 0.8,
    "axes.labelcolor": "Ivory",  # Label color
    "xtick.color": "Ivory",      # Tick color
    "ytick.color": "Ivory",      # Tick color
})    

# Load the gzipped CSV files
epoch_start = "1970-01-01"
dirName = "../../../Python-Regressionizer/Regressionizer/resources"
fileName = dirName + "/dfDistributionData.csv.zip"
dfDistributionData = pd.read_csv(fileName, compression='zip')

fileName = dirName + "/dfFinancialData.csv.zip"
dfFinancialData = pd.read_csv(fileName, compression='zip')
dfFinancialData['Time'] = pd.to_datetime(dfFinancialData['Time'], format='%Y-%m-%d')
#start_date = pd.Timestamp(epoch_start)
offset_time = 2208988800;
#dfFinancialData['Time'] = dfFinancialData['Time'].apply(lambda x: start_date + pandas.to_timedelta(x, unit='s'))
dfFinancialData['Time'] = dfFinancialData['Time'].apply(lambda x: x.timestamp() + offset_time)

fileName = dirName + "/dfTemperatureData.csv.zip"
dfTemperatureData = pd.read_csv(fileName, compression='zip')

dictData = {"Distribution": dfDistributionData, "Financial" : dfFinancialData, "Temperature" : dfTemperatureData}

# Generic seaborn function over Regressionizer object
def sns_plot(obj,
    title="", width=800, height=600,
    data_color: (str | None) = "grey",
    date_plot: bool = False, epoch_start="1900-01-01",
    background_color="#1f1f1f",
    point_size=2,
    **kwargs):
    """
    Plot data and regression quantiles using seaborn.
    :param title: Title of the plot.
    :param width: Width of the plot.
    :param height: Height of the plot.
    :param data_color: Color of the data points.
    :param date_plot: Whether to plot as a date-time series.
    :param epoch_start: Start of epoch when regressor is in seconds.
    :param background_color: Background color of the plot.
    :param grid_lines: Whether to show grid lines.
    :param kwargs: Additional keyword arguments to be passed to seaborn's plotting functions.
    :return: The instance of the Regressionizer class.
    """
    start_date = pd.Timestamp(epoch_start)
    xs = obj.take_data()[:, 0]
    if date_plot:
        xs = start_date + pd.to_timedelta(xs, unit='s')

    # Create a matplotlib figure and axis
    fig, ax = plt.subplots(figsize=(width / 100, height / 100))

    # Set background color
    ax.set_facecolor(background_color)


    # Plot data points
    sns.scatterplot(
        x=xs, 
        y=obj.take_data()[:, 1], 
        color=data_color, ax=ax, size=point_size, linewidth=0, alpha = 1, legend=False)

    # Plot each regression quantile
    for i, p in enumerate(obj.take_regression_quantiles().keys()):
        y_fit = [obj.take_regression_quantiles()[p](xi) for xi in obj.take_data()[:, 0]]
        sns.lineplot(x=xs, y=y_fit, ax=ax, label=f'{p}', linewidth=3)

    # Set title
    ax.set_title(title)
    ax.set(
        xlabel = "Regressor",
        ylabel = "Value")

    # Do not show the plot
    #plt.close(fig)

    # Result
    obj._value = fig

    return obj

# Style variables/constants
template='plotly_dark'
data_color='gray'

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


app_ui = ui.page_fluid(
    ui.input_dark_mode(),
    ui.input_select(id = "dataset", label = "Data:",
        choices=["Distribution", "Financial", "Temperature"], 
        selected="Distribution"
    ),
    ui.input_slider("knots", "Number of knots:", min=2, max=200, value=10),
    ui.input_text("probs", "Probabilities:", "0.1, 0.5, 0.9"),
    ui.input_slider("order", "Interpolation order", min=0, max=10, value=2, step=1),
    ui.input_checkbox("datePlotQ", "Date axis", value=True),
    ui.card(
        ui.output_plot("distPlot"),
    )
)

def server(input: Inputs, output: Outputs, session: Session):
    @reactive.Calc
    def probs_arr():
        return [float(num.strip()) for num in input.probs().split(",") if is_float(num.strip())]

    @render.plot
    def distPlot():

        dfData = dictData.get(input.dataset()).to_numpy()

        obj = (
            Regressionizer(dfData)
            .quantile_regression(knots=input.knots(), probs=probs_arr(), order=input.order())
        )

        obj = sns_plot(obj,
            title="",
            date_plot=input.datePlotQ(), 
            template=template,
            data_color=data_color,
            background_color = '#1F1F1F',
            point_size = 2,
            width = 800, height = 300)

        return obj.take_value()
  


app = App(app_ui, server)