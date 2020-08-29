# ML2
# Med Cabinet API

Med Cabinet is a cannibis recommendation service. Users are able to query a 2K + database to get recommendations based on medical conditions/symptoms, positive effects they wish to experience, and specific strains types they are interested. If the user knows or wants to find out more about a specific strain, they can query the name directly, as well. 


## BASE URL
https://med-finder-2020.herokuapp.com/

Leads to landing page indicating "App Online"

### ENDPOINTS
* `` /search/<user_input>``

User enters a string query for a strain name and they get a json object, similar to the one below: 
https://med-cabinet-project.herokuapp.com/Afpak

```
Description: "Spawn from Afghani and Big Bud, Afghan Big Bud (or Big Bud Afghani) is characterized as a large plant with broad leaves and thick stems. It has a dense appearance, similar to Big Bud,
              and maintains the taste of Afghani, resulting in the best of both worlds. The effects come relatively quick but usually dissipate under two hours."
Flavor: 	 "Pungent","Lemon","Peach"
Effects: 	 "Depression,Insomnia,Pain,Stress,Lack of Appetite"
Name:        "Afghan Big Bud"
Nearest":    "Mangolicious","Bc Big Bud","Big Bud","Big Mac","Big Kush"
Rating: 	 2.73
Type: 	     "Indica"
_id:         1978
```
## Code Links

Below are links to resources used to create this project:

* Datasets (https://github.com/Med-Cab-2020-Aug-PT/ML2/tree/master/app/data/csv) 
cannabis.csv is created from [Kaggle](https://www.kaggle.com/kingburrito666/cannabis-strains). 

* Pickled models https://github.com/Med-Cab-2020-Aug-PT/ML2/tree/master/app/data/pickled_models
These are the pickled dictionaries used for the home route and the strains route

* API https://github.com/Med-Cab-2020-Aug-PT/ML2/tree/master/app
This is where the code for creating the different endpoints can be located. 

* Packages/Technologies used
https://github.com/Med-Cab-2020-Aug-PT/ML2/blob/master/requirements.txt


## Testing
used curl to test that endpoints were able to retrieve correct information 
Example: ``curl medcab-finder-2020.herokuapp.com/search/happy``

```
[{"Description":"Caramelicious is a hybrid cannabis variety that has sticky buds and a caramel flavor. A favorite after dinner smoke for some, provides a sweet taste and happy high.",
"Effects":["Focused","Happy","Relaxed","Euphoric","Creative"],
"Flavors":["Vanilla","Sweet","Coffee"],
"Name":"Caramelicious",
"Nearest":["Blueberry Haze","Sweet Kush","Cream Caramel","Caramel Candy Kush","Cannalope Kush"],
"Rating":3.18,
"Type":"Hybrid",
"_id":1828}]
```