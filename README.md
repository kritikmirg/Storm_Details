# Storm_Details
Extracted and cleaned data from the NCDC Storm Events Database and analyzed factors such as frequency of weather patterns and change in weather patterns over time. Project combines 10 data sets organized by year into one cohesive chronological set containing every recorded weather event between 2008-2018. Using python functions were written to narrow down the data by state, or by state and year. With a combination of pandas, Matplotlib, .json files, API’s, and data analysis techniques, graphs are outputted based user’s input of state and year. Points are plotted onto a map of the United States displaying weather events on specific state and corresponding year. View Storm_Graphs.ipynb for visuals about storm data in the United States from 2008 - 2018.

## How to use Storm_Details.ipynb

### Step 1: Run produce_details(comb_D) cell

### Step 2: Enter Year 
From 2008 - 2018

### Step 3: Enter State or USA for whole country
Includes all 50 states and GULF OF MEXICO, ATLANTIC SOUTH, AMERICAN SAMOA, LAKE MICHIGAN, VIRGIN ISLANDS, ATLANTIC NORTH, DISTRICT OF COLUMBIA, GUAM, E PACIFIC, GULF OF ALASKA, PUERTO RICO, LAKE ERIE, LAKE HURON, LAKE ONTARIO, LAKE SUPERIOR, LAKE ST CLAIR, HAWAII WATERS, ST LAWRENCE R

### Step 4: Wait to be directed to a map of the United States
Map is zoom friendly, zoomable to street level
 
**Legend:** <br>
  **Dark Blue:** Flood Events: Flash Flood, Flood, Heavy Rain, Lakeshore Flood <br>
  **Purple:** Winter Events: Avalanche, Blizzard, Cold/Wind Chill, Extreme Cold/Wind Chill, Freezing Fog, Frost/Freeze, Heavy     Snow, Ice Storm, Winter Storm, Winter Weather <br>
  **Light Blue:**  Rain Events: Hail, Heavy Rain, Hurricane, Hurricane (Typhoon), Tropical Depression,Tropical Storm,             Waterspout, Sleet <br>
  **Orange:** Heat Events, Drought, Dust Devil, Dust Storm, Excessive Heat, Heat, Wildfire, Volcanic Ashfall <br>
  **Red:** Lightning Events: Lightning, Strong Wind, Thunderstorm Wind, Tornado <br>
  **Green:** Other <br>


![storm_gif](https://user-images.githubusercontent.com/57408020/71432613-cb932200-26a8-11ea-90a6-15ff830c9de0.gif)
