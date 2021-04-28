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

## Project Overview Requirements

This project focuses on:

1-  Finding a problem worth solving, analyzing, or visualizing

2-  Use ML in the context of technologies learned.

3-  Must use Scikit-Learn and or another machine learning library.

4-  Must use at least two of the below:

5-  Python Pandas, Python Matplotlib, HTML/CSS/Bootstrap, JavaScript Plotly, JavaScript D3.js, JavaScript Leaflet, QL Database, MongoDB Database, Google Cloud SQL, Amazon AWS, Tableau

6-  Host application using Heroku.

 

 

Project

 

1) Visualization charts for different variables like aroma, flavor against region/altitude/processing method.

 

2) Groupby region and calculate stats for every region/country

 

3) Predict the best set of variables for growing good quality coffee: Total cup points, altitude and other variables.

 

In creating the model, the following 9 variables were used. The original dataset has 44 variables.

 

Dependent variable:

 

Total cup points: Number of points the end product coffee has stored by the CQI jury (1-100 points; 100 is the highest score)

 

Independent variables:

 

Country of origin: Where the coffee comes from

Aroma: Aroma refers to sensations perceived by the olfactory bulb and conveyed to the brain; whether through the nose or retro-nasally: The aromatics of a coffee.

Species: Arabica and Robusta all with different varieties

Processing method: Which method was used to process it before roasting.

aftertaste: Refers to lingering residual sensations in the mouth after coffee has swallowed. It might be distinguished from finish which is the final sensations of the coffee while it leaves the mouth

Quackers - Category one defects: How many cat. 1 defects the coffee has

Category two defects: How many cat. 2 defects the coffee has

Mean altitude (m): At which mean altitude this coffee is cultured

Uniformity: Is refer to one of the particular amount of cups on which you evaluate if elements (acidity, body,etc) shows an stable behavior during the time (time in this case is in a each other slurp in that cup). Cleanness of cup is referred to the consistency of each cup according to it's uniformity.

Body: Associated with and sensed by mouthfeel How a coffee feels in the mouth or its apparent texture, a tactile sensation : A major component in the flavor profile of a coffee, it is a tactile sensation in the mouth used in more, body is sense of weight and thickness of the brew, caused by the percentage of soluble solids in the cup, including all organic grown without the use of artificial fertilizers, herbicides, etc.: Organic coffee has been grown according to organic farming techniques, typically without the use of artificial fertilizers. Some farms have more local Organic Certification than the More compounds that are extracted from brewing and end up in the cup. Body refers usually to thick or thin, heavy or light, full-bodied or watery. Mouthfeel is used to describe a much broader range of characteristics and textures.

Flavor: The overall impression in the mouth, including the origin
In coffee talk, it refers to a coffee-producing region or country; such as, "I was just at origin." Of course "Origin" for most product we use is not a beautiful farm in a temperate climate, More
 character as well as tastes that come from the roast.: This is the overall impression in the mouth, including the above ratings as well as tastes that come from the roast.

There are 5 “Primary Tastes” groupings (Sour, Sour is one of four basic sapid (in the mouth) tastes: Sour, Sweet, Salty, Bitter (and possibly a 5th called Umami which indicates savory flavors). In coffee, sourness in moderate amounts of favorable, although the More , Sweet ,Salty. Salty is one of four basic sapid (in the mouth) tastes: Sour, Sweet, Salty, Bitter (and possibly a 5th called Umami which indicates savory flavors). In coffee, saltiness is not usually a positive quality, but More
, Bittersalty-sweet-sour-bitter. Bitterness is one of 5 basic tastes: Sour, Sweet, Salty, Bitter and Umami (savory flavors). There are many types of bitterness, hence not one avenue to tracking down its source. Bitterness as a positive quality More , Savory (UmamiUmami-Mushroom Umami is a Japanese word that has been adopted to indicate savory flavor and scent, and is considered by some as the 5th core flavor along with sour, salty, sweet, and bitter.: Umami is a More ) and many “Secondary Tastes,” as you can see on the Taster’s Flavor Wheel A term that probably refers to the SCAA Flavor Wheel, an analysis tool adapted from the wine industry. (Actually the Beer wheel came before the Wine wheel) Half of it is dedicated to chiefly negative, More . As the primary category in taste evaluation (what coffee would you want to drink that smelled good and tasted awful?) it is of great importance. But in a sense the flavor impression is divided between this score AND the Finish Similar to aftertaste, but it refers to the impression as the coffee leaves the palate. Aftertaste is the sensations gathered after the coffee has left the mouth. We combine these to form the "final flavor More / Aftertaste Aftertaste refers to lingering residual sensations in the mouth after coffee has swallowed. It might be distinguished from "finish" which is the final sensations of the coffee while it leaves the mouth. Also see Afternose. More
 score.

Cupper Points: The cupper’s correction is a term we use to measure the “intangible” qualities of a cup: if, for instance, a coffee totals 88 points, but it is high quality enough that we feel it should< be a 90, we add in a +2 cupper's correction.: The cupper's correction is a term we use to measure the "intangible" qualities of a cup: if, for instance, a coffee totals 88 points, but it is high quality enough that we feel it should be a 90, we add in a +2 cupper's correction.

Sweetness: Sweetness is an important positive quality in fine coffees, and is one of five basic tastes: Sour Sour is one of four basic sapid (in the mouth) tastes: Sour, Sweet, Salty, Bitter (and possibly a 5th called Umami which indicates savory flavors). In coffee, sourness in moderate amounts of favorable, although the More , Sweet, Salty Salty is one of four basic sapid (in the mouth) tastes: Sour, Sweet, Salty, Bitter (and possibly a 5th called Umami which indicates savory flavors). In coffee, saltiness is not usually a positive quality, but More , Bittersalty-sweet-sour-bitter Bitterness is one of 5 basic tastes: Sour, Sweet, Salty, Bitter and Umami (savory flavors). There are many types of bitterness, hence not one avenue to tracking down its source. Bitterness as a positive quality More , Savory (UmamiUmami-Mushroom Umami is a Japanese word that has been adopted to indicate savory flavor and scent, and is considered by some as the 5th core flavor along with sour, salty, sweet, and bitter.: Umami is a More
). In coffee, sweetness is a highly desirable quality, and the green bean has sugars and polysaccharides. Sugars are converted during roasting but not found in the roasted bean, and some only form as intermediary compounds in the roast. So sweetness in coffee is less a matter of literal sweetness from sugars, as the perception of sweetness.

Total Cup Points: The cupper’s correction is a term we use to measure the “intangible” qualities of a cup: if, for instance, a coffee totals 88 points, but it is high quality enough that we feel it should< be a 90, we add in a +2 cupper's correction.: The cupper's correction is a term we use to measure the "intangible" qualities of a cup: if, for instance, a coffee totals 88 points, but it is high quality enough that we feel it should be a 90, we add in a +2 cupper's correction.

Clean Cup: Clean cup refers to a coffee free of taints and defects. It does not imply sanitary cleanliness, or that coffees that are not clean (which are dirty) are unsanitary. It refers to the flavors, specifically the absence of hard notes, fruity-fermenty flavors, earthy
Earthy is a flavor term with some ambivalence, used positively in some cases, negatively in others.: Sumatra coffees can have a positive earthy flavor, sometimes described as "wet earth" or "humus" or "forest" flavors. But More flavors or other off notes. 


