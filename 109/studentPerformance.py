import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import statistics
df = pd.read_csv("data.csv")
data = df["reading score"].tolist()
mean = sum(data) / len(data)
dev = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)
firststdevstart, firststdevend = mean-dev, mean+dev
secondstdevstart, secondstdevend = mean-(dev*2), mean+(dev*2)
thirdstdevstart, thirdstdevend = mean-(dev*3), mean+(dev*3)
fig = ff.create_distplot([data], ["reading scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[firststdevstart,firststdevstart], y=[0, 0.17], mode="lines", name="first"))
fig.add_trace(go.Scatter(x=[secondstdevstart,secondstdevstart], y=[0, 0.17], mode="lines", name="second"))
fig.add_trace(go.Scatter(x=[thirdstdevstart,thirdstdevstart], y=[0, 0.17], mode="lines", name="third"))
fig.add_trace(go.Scatter(x=[firststdevend,firststdevend], y=[0, 0.17], mode="lines", name="first"))
fig.add_trace(go.Scatter(x=[secondstdevend,secondstdevend], y=[0, 0.17], mode="lines", name="second"))
fig.add_trace(go.Scatter(x=[thirdstdevend,thirdstdevend], y=[0, 0.17], mode="lines", name="third"))
fig.show()
list_of_data_in_first_stdev=[result for result in data if result>firststdevstart and result<firststdevend]
list_of_data_in_second_stdev=[result for result in data if result>secondstdevstart and result<secondstdevend]
list_of_data_in_third_stdev=[result for result in data if result>thirdstdevstart and result<thirdstdevend]
print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard deviation of this data is {}".format(dev))
print("{}% of data lies in first standard deviation".format(len(list_of_data_in_first_stdev)*100/len(data)))
print("{}% of data lies in second standard deviations".format(len(list_of_data_in_second_stdev)*100/len(data)))
print("{}% of data lies in third standard deviations".format(len(list_of_data_in_third_stdev)*100/len(data)))
