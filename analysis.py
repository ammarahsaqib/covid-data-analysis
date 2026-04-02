import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("owid-covid-data.csv")

countries = ['United States', 'United Kingdom', 'India', 'Brazil', 'Germany']
df_filtered = df[df['country'].isin(countries)].copy()
df_filtered['date'] = pd.to_datetime(df_filtered['date'])

for country in countries:
    country_data = df_filtered[df_filtered['country'] == country]
    plt.plot(country_data['date'], country_data['new_cases'], label=country)

plt.title('Daily New COVID-19 Cases by Country')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend()
plt.tight_layout()
plt.savefig('covid_chart.png')
plt.close()

fig = px.line(df_filtered, x='date', y='new_cases', color='country',
              title='Interactive COVID-19 Cases by Country')
fig.write_html('covid_interactive.html')

print("Done! Two files saved:")
print("  - covid_chart.png")
print("  - covid_interactive.html")
