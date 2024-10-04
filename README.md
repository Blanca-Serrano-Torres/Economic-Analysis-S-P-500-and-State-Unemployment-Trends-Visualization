# Economic-Analysis-S&P-500-and-State-Unemployment-Trends-Visualization

## Overview
This project focuses on analyzing and visualizing economic data, particularly related to the S&P 500 index and unemployment rates across different U.S. states. The data is sourced fromthe Federal Reserve Economic Data (FRED) API. The analysis is performed using Python,leveraging data processing and visualization libraries like pandas, matplotlib, and plotly.

## Features 
  - Data Retrieval: Fetches economic data (S&P 500 and unemployment rates) using the 
    FRED API.
  - Data Cleaning: Processes the data to remove missing values and redundant columns.
  - Data Visualization: Line Charts, Bar charts and Interactive visualizations using 
    plotly.

## Prerequisites 

The following Python libraries:

  - pandas
  - numpy
  - matplotlib
  - plotly
  - fredapi

### API Key
This project uses the FRED API to fetch economic data. To run the script, you will need a FRED API key. If you don't have one, you can request it from the FRED API website.

## Data Visualization
The script generates various plots that allow you to analyze: 

  - S&P 500 Index: A line chart showing the S&P 500 trends over time.
  - State-wise Unemployment Rates: A bar chart comparing unemployment rates across U.S. 
    states.
  - Intercative Charts: You can generate interactive visualizations using plotly,
    offering hover features and zooming capabilities.

## Economic Context Analysis and Measures 
To provide economic insights based on the Python script's analysis, let's break down what the data is revealing in the context of the S&P 500 and state-wise unemployment rates: 

### S&P 500 Index Trends 

  - Analysis: The script pulls the historical data of the S&P 500 and plots its trend 
    over time. The S&P 500 is composed of different sectors. Comparing overall index
    performance to individual sectors can reveal how specific parts of the economy are 
    performing.
  
  - Insights:

     - The S&P 500 is a crucial indicator of the overall health of stocks market and
       reflects the perdormance of 500 of the largest companies of the U.S.
     - Long-term trends: Upward trends typically indicate investor confidence, economic 
       growth, and strong corporate performance. This could be driven by strong 
       corporate earnings, low interest rates, or economic stimuli(tax cuts, monetary 
       policy). 
     - Short-term volatility: Downward trends could signal economic downturns, market 
       corrections, or external shocks. Providing a high volatility periods comparision
       with major conomic or political events to see how sensitive the market is to 
       external factors.
     - Impact of interest rates: Historically, low interest rates encourage investment 
       in equities, boosting the S&P 500. However, if interest rates rise too quickly 
       to curb inflation, the market could react negatively.

### Unemployment Rate Insights
Unemployment rates are a critical indicator of economic health, directly reflecting the labor market's strenght.

  - Insights:

     - High unemployment rates: Consistently high unemployment in certain states or
       could indicate structural problems in those economies, such as decline in a key 
       industry. High unemployment remains persistently high despite national economic
       recovery, this could point to regional economic disparities or the need for 
       targeted policy interventions.
     - Low unemployment rates: A state with lower unemployment is generally experiencing
       higher economic activity, given low employment often leads to wahe pressures, 
       which can contribute to inflation.

 - Regional Analysis:

     - Impact of regional industries: Some states' economies are more reliant on 
       specific industries. For instance, oil-dependent states may have higher 
       unemployment during periods of low oil prices, whereas states with diverse 
       economies may be more resilient.
     - Labor market disparities: Comparing states with historically low unemployment 
       (like North Dakota) to those with persistent labor market challenges (like West 
       Virginia) can highlight economic policy differences, workforce skill levels, and 
       industrial strenghts or weaknesses.

### Correlation between S&P 500 and Unemployment Rates
Typically, there is an inverse relationship between stock market performance and unemployment. As the economy improves and businesses grow, unemployment tends to decrease because companies hire workers. 

  - Insights:
      
      - Diverging trends: If the S&P 500 is risi g but unemployment remains high, this  
        could suggest thar corporate profits are being driven by factors other than 
        labor market strenght, or that the benefits of economic recovery are not being 
        evenly distributed. This is often referred to as "jobless recovery". If this 
        divergence is persisitent, it could signal increasing wealth inequality, as 
        stock market gains typically benefit investors more than the general population.
      - Economic overheating: If both the S&P 500 and employment are rising rapidly, it 
        could suggest that economy is growing quickly, but there might be a risk of 
        inflation. The Federal Reserve may rise interest rates to prevent overheating, 
        which could slow down both market growth and job creation.

## Economic Analysis given the visualizations obtained

### Unemployment Rate by State (May 2024)
Let's dive into a deeper economic analysis providing a top list of most/lowest unemployment and geographical trends.

   - Top Unemployment States: Puerto Rico, the District of Columbia, California, and 
     Nevada exhibit the highest unemployment rates, with Puerto Rico leading at nearly 
     6%. These areas may be facing structural economic challenges or have industries 
     that are more sensitive to economic downturns, such as turism in Nevada and Puerto 
     Rico, and tech layoffs in California.
   - States with Lowest Unemployment: States like South Dakota, North Dakota, Vermont, 
     and Nebraska show very low unemployment rates, below 2.5%. These states typically 
     have more stable, less cyclical industries such as agriculture or local 
     services.This suggests that these states'labor markets are healthier, or that they 
     have reached more effectively from recent economic disruptions.
   - Geographical Trends: There's a notable concentration of higher unemployment rates 
     on the West Coast (California, Nevada, and Washington), while states in the 
     Midwest and Plains regions exhibit lower rates. This could suggest that coastal 
     economies are more affecetd by macroeconomic factors, such as inflation and the 
     higher cost of living, than central U.S. states.

## Unemployment vs Labor Force Participation
This graph shows California's unemployment and participation ratesover time:

   - Unemployment Trends: California's unemployment rate peaked around early 2020, 
     likely due to the COVID-19 pandemic, reaching nearly 16%. This aligns with the 
     national experience during the pandemic, where businesses shut down and 
     unemployment soared. However, since mid-2020, unemployment has seen a sharp 
     decline, stabilizing around 4-5% by 2024.
   - Labor Force Participation: California's participation rate(percentage of wroking- 
     age population actively employed or looking for work)  

      
