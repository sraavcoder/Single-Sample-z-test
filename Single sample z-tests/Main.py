import plotly.figure_factory as ff
import plotly.graph_objs as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv(
    "C:/Users/sraav_1jk4baa/OneDrive/Desktop/WhitehatJr Python/Projects/Single sample z-tests/Data.csv")

data = df["reading_time"].tolist()

population_mean = statistics.mean(data)


def randomSetOfMean(counter):
    dataSet = []
    for i in range(0, counter):
        randomIndex = random.randint(0, len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    ReadingScore_Mean = statistics.mean(dataSet)
    return ReadingScore_Mean


meanList = []
for i in range(0, 100):
    setOfMeans = randomSetOfMean(30)
    meanList.append(setOfMeans)

ReadingScore_SD = statistics.stdev(meanList)

SampleMean = statistics.mean(meanList)

ReadingScore_first_std_deviation_start, ReadingScore_first_std_deviation_end = population_mean - \
    ReadingScore_SD, population_mean+ReadingScore_SD
ReadingScore_second_std_deviation_start, ReadingScore_second_std_deviation_end = population_mean - \
    (2*ReadingScore_SD), population_mean+(2*ReadingScore_SD)
ReadingScore_third_std_deviation_start, ReadingScore_third_std_deviation_end = population_mean - \
    (3*ReadingScore_SD), population_mean+(3*ReadingScore_SD)

fig = ff.create_distplot([meanList], ["Population"], show_hist=False)
fig.add_trace(go.Scatter(x=[population_mean, population_mean], y=[
    0, 0.8], mode="lines", name="Mean"))

fig.add_trace(go.Scatter(x=[ReadingScore_first_std_deviation_start, ReadingScore_first_std_deviation_start], y=[
    0, 0.8], mode="lines", name="Start STD 1"))
fig.add_trace(go.Scatter(x=[ReadingScore_first_std_deviation_end, ReadingScore_first_std_deviation_end], y=[
    0, 0.8], mode="lines", name="End STD 1"))

fig.add_trace(go.Scatter(x=[ReadingScore_second_std_deviation_start, ReadingScore_second_std_deviation_start], y=[
    0, 0.8], mode="lines", name="Start STD 2"))
fig.add_trace(go.Scatter(x=[ReadingScore_second_std_deviation_end, ReadingScore_second_std_deviation_end], y=[
    0, 0.8], mode="lines", name="End STD 2"))

fig.add_trace(go.Scatter(x=[ReadingScore_third_std_deviation_start, ReadingScore_third_std_deviation_start], y=[
    0, 0.8], mode="lines", name="Start STD 3"))
fig.add_trace(go.Scatter(x=[ReadingScore_third_std_deviation_end, ReadingScore_third_std_deviation_end], y=[
    0, 0.8], mode="lines", name="End STD 3"))

fig.add_trace(go.Scatter(x=[SampleMean, SampleMean], y=[
    0, 0.8], mode="lines", name="Sample 1 Mean"))

zScore = (SampleMean-population_mean) / ReadingScore_SD

print("zScore of the Data is ", zScore)

fig.show()
