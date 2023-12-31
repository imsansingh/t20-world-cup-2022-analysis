import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from matplotlib import pyplot as plt
pio.templates.default = "plotly_white"

data = pd.read_csv("t20_WC_2022.csv")
data.head()

#Now let’s look at the number of matches won by each team in the world cup:
figure = px.bar(data, x=data["winner"],
                title="Number of Matches Won by teams in t20 World Cup 2022")
figure.show()

from matplotlib import pyplot as plt
from matplotlib import style

x = data['first innings score']
y = data['first innings wickets']

style.use('ggplot')
plt.bar(x, y, color='red')
plt.title('Runs and wickets in first inning')
plt.xlabel('Runs')
plt.ylabel('wickets')
plt.show()

#Now let’s have a look at the number of matches won by batting first or second in the t20 world cup 2022:
won_by = data["won by"].value_counts()
label = won_by.index
counts = won_by.values
colors = ['blue','red']

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Number of Matches Won By Runs Or Wickets')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()

#Now, let’s have a look at the toss decisions by teams in the world cup:
toss = data["toss decision"].value_counts()
label = toss.index
counts = toss.values
colors = ['indigo','orange']

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Toss Decisions in t20 World Cup 2022')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()

#Now let’s have a look at the top scorers in the t20 world cup 2022:
figure = px.bar(data, 
                x=data["top scorer"], 
                y = data["highest score"], 
                color = data["highest score"],
                title="Top Scorers in t20 World Cup 2022")
figure.show()

#Now let’s have a look at the number of player of the match awards in the world cup:
figure = px.bar(data, 
                x = data["player of the match"], 
                color = data["player of the match"],
                title="Player of the Match Awards in t20 World Cup 2022")
figure.show()

#Now let’s have a look at the bowlers with the best bowling figures at the end of the matches:
figure = px.bar(data, 
                x=data["best bowler"],
                color=data['best bowler'],
                title="Best Bowlers in t20 World Cup 2022")
figure.show()

#Now let’s compare the runs scored in the first innings and second innings in every stadium of the t20 world cup 2022:
fig = go.Figure()
fig.add_trace(go.Bar(
    x=data["venue"],
    y=data["first innings score"],
    name='First Innings Runs',
    marker_color='blue'
))
fig.add_trace(go.Bar(
    x=data["venue"],
    y=data["second innings score"],
    name='Second Innings Runs',
    marker_color='red'
))
fig.update_layout(barmode='group', 
                  xaxis_tickangle=-45, 
                  title="Best Stadiums to Bat First or Chase")
fig.show()

#Now let’s compare the number of wickets lost in the first innings and second innings in every stadium of the t20 world cup 2022:
fig = go.Figure()
fig.add_trace(go.Bar(
    x=data["venue"],
    y=data["first innings wickets"],
    name='First Innings Wickets',
    marker_color='blue'
))
fig.add_trace(go.Bar(
    x=data["venue"],
    y=data["second innings wickets"],
    name='Second Innings Wickets',
    marker_color='red'
))
fig.update_layout(barmode='group', 
                  xaxis_tickangle=-45, 
                  title="Best Statiums to Bowl First or Defend")
fig.show()

# Summary
# So some highlights of the t20 world cup 2022 we found from our analysis are:
# England won the most number of matches.
# Virat Kohli scored highest in the most number of matches.
# Sam Curran was the best bowler in the most number of matches.
# More teams won by batting first.
# More teams decided to bat first.
# SCG was the best stadium to bat first.
# SCG was the best stadium to defend the target in the World Cup.
# The Optus Stadium was the best stadium to bowl first.

