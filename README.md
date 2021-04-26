# finalproject

## Project Overview
This project focuses on:
1- Finding a problem worth solving, analyzing, or visualizing
2- Use ML in the context of technologies learned.
3- Must use Scikit-Learn and or another machine learning library.
4- Must use at least two of the below:
5- Python Pandas, Python Matplotlib, HTML/CSS/Bootstrap, JavaScript Plotly, JavaScript D3.js, JavaScript Leaflet, QL Database, MongoDB Database, Google Cloud SQL, Amazon AWS, Tableau
6- Host application using Heroku.


What are we working with?
For the model I will use the following following 9 variables. The original dataset has 44 variables.

Dependent variable:

Total cup points: Number of points the end product coffee has stored by the CQI jury (1-100 points; 100 is the highest score)
Independent variables:

Country of origin: Where the coffee comes from
Harvest year: Which year it was harvested
Variety: Which variety of coffee it is
Processing method: Which method was used to process it before roasting
Color: Which color the coffee in the cup has
Category one defects: How many cat. 1 defects the coffee has
Category two defects: How many cat. 2 defects the coffee has
Mean altitude (m): At which mean altitude this coffee is cultured

## Resources
- Data Source: [https://www.kaggle.com/reminho/coffee-quality-score-prediction-using-tree-models
https://u.osu.edu/ryanrichardscoffeecommoditychain/
http://www.coffeeresearch.org/agriculture/processing.htm
https://www.coffeereview.com/interpret-coffee/
https://library.sweetmarias.com/glossary/body/
https://seasia.co/2018/01/27/the-coffee-belt-a-world-map-of-the-major-coffee-producers]

- Software: HTML/CSS, JavaScript, Visual Studio Code 1.49.1, BootStrap 4.0.0, pandas/Lux, sklearn, Google Maps.

## Results

### Link to Coffee Quality Predictor webpage
https://coffee7.herokuapp.com/




### Search Criteria Procedure

#### Index page
This is the initial page. The user can re-initialize the page by clicking on the navbar at the top.
<p align="center">
    <img src="https://user-images.githubusercontent.com/68669675/95640606-285aa000-0a63-11eb-9bee-08b8b7b208ce.png" class="img-responsive" alt="Responsive image"> 
</p>

#### Filtering by event date
The user enters the desired date, the change is detected and the table is updated accordingly.
<p align="center">
    <img src="https://user-images.githubusercontent.com/68669675/95657151-7bbb0580-0ad8-11eb-83fd-f9612cea0301.png" class="img-responsive" alt="Responsive image"> 
</p>

#### Filtering by city
The user enters the desired city, the change is detected and the table is updated accordingly.
<p align="center">
    <img src="https://user-images.githubusercontent.com/68669675/95657153-7c539c00-0ad8-11eb-9ed0-8ec629dc28d1.png" class="img-responsive" alt="Responsive image"> 
</p>

#### Filtering by country
The user enters the desired country, the change is detected and the table is updated accordingly.
<p align="center">
    <img src="https://user-images.githubusercontent.com/68669675/95657154-7cec3280-0ad8-11eb-9aa2-747ca64af497.png" class="img-responsive" alt="Responsive image"> 
</p>

#### Filtering by state and shape
The user enters the desired state and shape observed, the changes are detected and the table is updated accordingly.
<p align="center">
    <img src="https://user-images.githubusercontent.com/68669675/95657155-7cec3280-0ad8-11eb-8b37-2a7b9871d1dd.png" class="img-responsive" alt="Responsive image"> 
</p>
All filter parameters can be entered simultaneously.
<br>

## Summary
- One drawback of this design is the difficulty for the user to know what parameter to use for the filtering. For example to pick a city, the user would have to go through the table a find the city desired for the analysis.
- A way to address this would be to present drop-down lists including all filter values in place of the input fields.<br>
Each list would need to update after a parameter is selected in any filter.
- Including a button to clear the filters is also needed. The button would be located below the last filter.


Other resources:
https://www.kaggle.com/reminho/coffee-quality-score-prediction-using-tree-models
https://u.osu.edu/ryanrichardscoffeecommoditychain/
http://www.coffeeresearch.org/agriculture/processing.htm
https://www.coffeereview.com/interpret-coffee/
https://library.sweetmarias.com/glossary/body/
https://seasia.co/2018/01/27/the-coffee-belt-a-world-map-of-the-major-coffee-producers


