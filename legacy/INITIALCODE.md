"""  
Algorithmic Optimization of Philippine Tree Functional Types  
for Caloocan Microclimate Regulation \- Revised Version

This revised version addresses:  
1\. Proper consideration of all species combinations (5C1 to 5C5)  
2\. Organized heatmap storage in a single folder  
"""

import numpy as np  
import pandas as pd  
import geopandas as gpd  
from shapely.geometry import Point, Polygon  
import matplotlib.pyplot as plt  
import seaborn as sns  
from scipy.spatial.distance import cdist  
from scipy.stats import percentileofscore  
import random  
from tqdm import tqdm  
import warnings  
import os  
import itertools  
from pathlib import Path  
warnings.filterwarnings('ignore')

\# \============================================================================  
\# 1\. DATA PREPARATION AND STUDY AREA DEFINITION  
\# \============================================================================

*class* StudyArea:  
   """Class to define the study area and urban morphology"""  
    
   *def* \_\_init\_\_(*self*, *width*\=70, *height*\=70, *resolution*\=1):  
       """  
       Initialize study area grid  
        
       Parameters:  
       \-----------  
       width : float  
           Width of study area in meters  
       height : float  
           Height of study area in meters  
       resolution : float  
           Grid resolution in meters  
       """  
       *self*.width \= *width*  
       *self*.height \= *height*  
       *self*.resolution \= *resolution*  
        
       \# Create grid points  
       *self*.x\_coords \= np.arange(0, *width*, *resolution*)  
       *self*.y\_coords \= np.arange(0, *height*, *resolution*)  
       *self*.grid\_points \= np.array(\[(x, y) for x in *self*.x\_coords  
                                    for y in *self*.y\_coords\])  
       *self*.n\_points \= len(*self*.grid\_points)  
        
       \# Initialize constraints  
       *self*.constraints \= {  
           'building\_footprints': \[\],  
           'infrastructure': \[\],  
           'planting\_zones': None  \# Will be set later  
       }  
        
       \# Social vulnerability layers  
       *self*.vulnerability\_zones \= {  
           'schools\_health\_centers': \[\],  
           'high\_density\_residential': \[\],  
           'commercial\_industrial': \[\],  
           'parks\_empty\_lots': \[\]  
       }  
    
   *def* add\_constraint(*self*, *constraint\_type*, *geometry*):  
       """Add spatial constraint to study area"""  
       *self*.constraints\[*constraint\_type*\].append(*geometry*)  
    
   *def* set\_planting\_zones(*self*, *zones\_polygon*):  
       """Define areas where trees can be planted"""  
       *self*.constraints\['planting\_zones'\] \= *zones\_polygon*  
    
   *def* add\_vulnerability\_zone(*self*, *zone\_type*, *point*):  
       """Add social vulnerability point"""  
       *self*.vulnerability\_zones\[*zone\_type*\].append(*point*)  
    
   *def* is\_valid\_planting\_location(*self*, *point*):  
       """Check if a point is valid for tree planting"""  
       \# Check if in planting zones  
       if *self*.constraints\['planting\_zones'\]:  
           if not *self*.constraints\['planting\_zones'\].contains(Point(*point*)):  
               return False  
        
       \# Check if not in building footprints  
       for building in *self*.constraints\['building\_footprints'\]:  
           if building.contains(Point(*point*)):  
               return False  
        
       \# Check if not too close to infrastructure  
       for infra in *self*.constraints\['infrastructure'\]:  
           if infra.distance(Point(*point*)) \< 2:  \# 2m buffer  
               return False  
        
       return True  
    
   *def* get\_valid\_planting\_locations(*self*, *n\_locations*\=100):  
       """Get valid planting locations within study area"""  
       valid\_points \= \[\]  
       attempts \= 0  
       max\_attempts \= *n\_locations* \* 10  
        
       while len(valid\_points) \< *n\_locations* and attempts \< max\_attempts:  
           x \= np.random.uniform(0, *self*.width)  
           y \= np.random.uniform(0, *self*.height)  
           point \= (x, y)  
            
           if *self*.is\_valid\_planting\_location(point):  
               valid\_points.append(point)  
            
           attempts \+= 1  
        
       return np.array(valid\_points\[:*n\_locations*\])

\# \============================================================================  
\# 2\. TREE SPECIES DATA AND COOLING MODEL  
\# \============================================================================

*class* TreeSpecies:  
   """Class to manage tree species data and cooling properties"""  
    
   \# Philippine Tree Functional Types (TFTs) from Table 1  
   SPECIES\_DATA \= {  
       'Swietenia\_macrophylla': {  
           'common\_name': 'Honduras mahogany',  
           'height\_m': 38.0,  \# Average height  
           'crown\_diameter\_m': 35.0,  
           'cpa\_sqm': 962.0,  
           'total\_leaf\_area\_sqm': 3848.0,  
           'architecture': 'broad\_spreading',  
           'growth\_rate': 'fast',  
           'water\_requirement': 'high',  
           'native\_status': 'exotic',  
           'color': 'darkgreen'  
       },  
       'Mangifera\_indica': {  
           'common\_name': 'Mango Tree',  
           'height\_m': 30.0,  
           'crown\_diameter\_m': 9.0,  
           'cpa\_sqm': 64.0,  
           'total\_leaf\_area\_sqm': 289.0,  
           'architecture': 'broad\_spreading',  
           'growth\_rate': 'moderate',  
           'water\_requirement': 'moderate',  
           'native\_status': 'native',  
           'color': 'limegreen'  
       },  
       'Artocarpus\_heterophyllus': {  
           'common\_name': 'Jackfruit',  
           'height\_m': 16.5,  \# Average of 8-25m  
           'crown\_diameter\_m': 16.5,  \# Average of 8-25m  
           'cpa\_sqm': 491.0,  
           'total\_leaf\_area\_sqm': 1964.0,  
           'architecture': 'broad\_spreading',  
           'growth\_rate': 'moderate',  
           'water\_requirement': 'moderate',  
           'native\_status': 'native',  
           'color': 'green'  
       },  
       'Albizia\_lebbeck': {  
           'common\_name': 'Akleng-parang',  
           'height\_m': 30.0,  
           'crown\_diameter\_m': 10.0,  
           'cpa\_sqm': 79.0,  
           'total\_leaf\_area\_sqm': 314.0,  
           'architecture': 'umbrella\_shaped',  
           'growth\_rate': 'fast',  
           'water\_requirement': 'low',  
           'native\_status': 'native',  
           'color': 'olive'  
       },  
       'Pterocarpus\_indicus': {  
           'common\_name': 'Narra',  
           'height\_m': 33.0,  
           'crown\_diameter\_m': 20.0,  
           'cpa\_sqm': 314.0,  
           'total\_leaf\_area\_sqm': 1256.0,  
           'architecture': 'broad\_spreading',  
           'growth\_rate': 'moderate',  
           'water\_requirement': 'moderate',  
           'native\_status': 'native',  
           'color': 'forestgreen'  
       }  
   }  
    
   *def* \_\_init\_\_(*self*):  
       *self*.species\_list \= list(*self*.SPECIES\_DATA.keys())  
        
   *def* get\_species\_properties(*self*, *species\_name*):  
       """Get properties for a specific species"""  
       return *self*.SPECIES\_DATA.get(*species\_name*, {})  
    
   *def* calculate\_cooling\_coefficient(*self*, *species\_name*):  
       """Calculate normalized cooling coefficient based on crown diameter"""  
       props \= *self*.get\_species\_properties(*species\_name*)  
       if not props:  
           return 0  
        
       \# Normalize crown diameter to \[0, 1\] range  
       all\_diameters \= \[s\['crown\_diameter\_m'\] for s in *self*.SPECIES\_DATA.values()\]  
       normalized \= (props\['crown\_diameter\_m'\] \- min(all\_diameters)) / (max(all\_diameters) \- min(all\_diameters))  
        
       \# Adjust based on architecture type  
       architecture\_factors \= {  
           'broad\_spreading': 1.2,  
           'umbrella\_shaped': 1.0,  
           'columnar': 0.8,  
           'irregular': 0.9  
       }  
        
       factor \= architecture\_factors.get(props\['architecture'\], 1.0)  
       return normalized \* factor  
    
   *def* get\_crown\_radius(*self*, *species\_name*):  
       """Get crown radius for a species"""  
       props \= *self*.get\_species\_properties(*species\_name*)  
       return props.get('crown\_diameter\_m', 0) / 2  
    
   *def* get\_architecture\_category(*self*, *species\_name*):  
       """Classify tree architecture based on crown diameter to height ratio"""  
       props \= *self*.get\_species\_properties(*species\_name*)  
       if not props:  
           return 'unknown'  
        
       ratio \= props\['crown\_diameter\_m'\] / props\['height\_m'\]  
        
       if ratio \> 0.6:  
           return 'broad\_spreading'  
       elif 0.3 \<= ratio \<= 0.6:  
           return 'medium'  
       else:  
           return 'columnar'  
    
   *def* get\_all\_species\_combinations(*self*, *min\_species*\=1, *max\_species*\=5):  
       """Generate all possible species combinations"""  
       all\_combinations \= \[\]  
        
       for k in range(*min\_species*, *max\_species* \+ 1):  
           combos \= list(itertools.combinations(*self*.species\_list, k))  
           all\_combinations.extend(combos)  
        
       return all\_combinations  
    
   *def* get\_species\_color(*self*, *species\_name*):  
       """Get color for visualizing a species"""  
       props \= *self*.get\_species\_properties(*species\_name*)  
       return props.get('color', 'gray')

*class* CoolingModel:  
   """Cooling performance estimation using distance-decay function"""  
    
   *def* \_\_init\_\_(*self*, *decay\_lambda*\=0.01):  
       """  
       Initialize cooling model  
        
       Parameters:  
       \-----------  
       decay\_lambda : float  
           Decay constant for distance-decay function  
       """  
       *self*.decay\_lambda \= *decay\_lambda*  
       *self*.tree\_species \= TreeSpecies()  
    
   *def* calculate\_cooling\_contribution(*self*, *tree\_position*, *tree\_species*, *grid\_points*):  
       """  
       Calculate cooling contribution of a single tree at all grid points  
        
       Parameters:  
       \-----------  
       tree\_position : tuple (x, y)  
           Position of the tree  
       tree\_species : str  
           Species of the tree  
       grid\_points : np.array  
           Array of grid point positions  
        
       Returns:  
       \--------  
       np.array : Cooling contributions at each grid point  
       """  
       \# Get normalized crown diameter (cooling coefficient)  
       D\_j \= *self*.tree\_species.calculate\_cooling\_coefficient(*tree\_species*)  
        
       \# Calculate Euclidean distances  
       distances \= cdist(\[*tree\_position*\], *grid\_points*, 'euclidean')\[0\]  
        
       \# Apply distance-decay function: C(i,j) \= D\_j \* exp(-λ \* d\_ij^2)  
       cooling \= D\_j \* np.exp(\-*self*.decay\_lambda \* distances\*\*2)  
        
       return cooling  
    
   *def* calculate\_total\_cooling(*self*, *tree\_placements*, *tree\_species\_list*, *grid\_points*):  
       """  
       Calculate total cooling from all trees  
        
       Parameters:  
       \-----------  
       tree\_placements : list of tuples  
           Positions of all trees  
       tree\_species\_list : list of str  
           Species for each tree  
       grid\_points : np.array  
           Array of grid point positions  
        
       Returns:  
       \--------  
       np.array : Total cooling at each grid point  
       """  
       total\_cooling \= np.zeros(len(*grid\_points*))  
        
       for pos, species in zip(*tree\_placements*, *tree\_species\_list*):  
           cooling \= *self*.calculate\_cooling\_contribution(pos, species, *grid\_points*)  
           total\_cooling \+= cooling  
        
       return total\_cooling  
    
   *def* calculate\_cooling\_score(*self*, *tree\_placements*, *tree\_species\_list*, *grid\_points*):  
       """Calculate aggregated cooling score (sum of cooling across all grid points)"""  
       total\_cooling \= *self*.calculate\_total\_cooling(*tree\_placements*, *tree\_species\_list*, *grid\_points*)  
       return np.sum(total\_cooling)

\# \============================================================================  
\# 3\. ANT COLONY OPTIMIZATION (ACO) IMPLEMENTATION \- MULTI-SPECIES VERSION  
\# \============================================================================

*class* MultiSpeciesAntColonyOptimization:  
   """ACO for tree placement and species selection considering all species combinations"""  
    
   *def* \_\_init\_\_(*self*, *study\_area*, *cooling\_model*, *n\_trees*\=10,  
                *n\_ants*\=30, *n\_iterations*\=50, *evaporation\_rate*\=0.5,  
                *alpha*\=1.0, *beta*\=2.0):  
       """  
       Initialize multi-species ACO algorithm  
        
       Parameters:  
       \-----------  
       study\_area : StudyArea object  
       cooling\_model : CoolingModel object  
       n\_trees : int  
           Number of trees to place  
       n\_ants : int  
           Number of ants in colony  
       n\_iterations : int  
           Number of iterations  
       evaporation\_rate : float  
           Pheromone evaporation rate  
       alpha : float  
           Importance of pheromone  
       beta : float  
           Importance of heuristic information  
       """  
       *self*.study\_area \= *study\_area*  
       *self*.cooling\_model \= *cooling\_model*  
       *self*.n\_trees \= *n\_trees*  
       *self*.n\_ants \= *n\_ants*  
       *self*.n\_iterations \= *n\_iterations*  
       *self*.evaporation\_rate \= *evaporation\_rate*  
       *self*.alpha \= *alpha*  
       *self*.beta \= *beta*  
        
       \# Get valid planting locations  
       *self*.candidate\_locations \= *study\_area*.get\_valid\_planting\_locations(*n\_locations*\=100)  
       *self*.n\_candidates \= len(*self*.candidate\_locations)  
        
       \# Get available species  
       *self*.tree\_species \= TreeSpecies()  
       *self*.species\_list \= *self*.tree\_species.species\_list  
       *self*.n\_species \= len(*self*.species\_list)  
        
       \# Get all possible species combinations  
       *self*.species\_combinations \= *self*.tree\_species.get\_all\_species\_combinations()  
       *self*.n\_combinations \= len(*self*.species\_combinations)  
        
       print(*f*"Total species combinations to consider: {*self*.n\_combinations}")  
       for i, combo in enumerate(*self*.species\_combinations\[:10\]):  \# Show first 10  
           species\_names \= \[*self*.tree\_species.get\_species\_properties(s)\['common\_name'\] for s in combo\]  
           print(*f*"  Combination {i\+1}: {', '.join(species\_names)}")  
       if len(*self*.species\_combinations) \> 10:  
           print(*f*"  ... and {len(*self*.species\_combinations) \- 10} more combinations")  
        
       \# Initialize pheromone matrices  
       \# Pheromone for location selection  
       *self*.location\_pheromone \= np.ones(*self*.n\_candidates) / *self*.n\_candidates  
        
       \# Pheromone for species combination selection  
       *self*.combination\_pheromone \= np.ones(*self*.n\_combinations) / *self*.n\_combinations  
        
       \# Store best solution  
       *self*.best\_solution \= None  
       *self*.best\_score \= \-np.inf  
       *self*.best\_combination \= None  
        
   *def* heuristic\_information\_combination(*self*, *combo\_idx*):  
       """Calculate heuristic information for a species combination"""  
       combo \= *self*.species\_combinations\[*combo\_idx*\]  
        
       \# Heuristic based on average cooling coefficient  
       avg\_cooling \= np.mean(\[*self*.tree\_species.calculate\_cooling\_coefficient(s) for s in combo\])  
        
       \# Bonus for diversity (more species in combination)  
       diversity\_bonus \= len(combo) / *self*.n\_species  
        
       return avg\_cooling \* (1 \+ 0.2 \* diversity\_bonus)  
    
   *def* heuristic\_information\_location(*self*, *location\_idx*):  
       """Calculate heuristic information for a location"""  
       location \= *self*.candidate\_locations\[*location\_idx*\]  
        
       \# Locations near vulnerable zones get higher heuristic  
       point\_geom \= Point(location)  
       vulnerability\_score \= 0  
       for zone\_type, points in *self*.study\_area.vulnerability\_zones.items():  
           if points:  
               distances \= \[point\_geom.distance(Point(p)) for p in points\]  
               min\_distance \= min(distances) if distances else float('inf')  
               if min\_distance \<= 20:  
                   if zone\_type \== 'schools\_health\_centers':  
                       vulnerability\_score \+= 2.0  
                   elif zone\_type \== 'high\_density\_residential':  
                       vulnerability\_score \+= 1.5  
        
       return 1.0 \+ 0.5 \* min(1.0, vulnerability\_score)  
    
   *def* construct\_solution\_with\_combination(*self*, *combo\_idx*):  
       """Construct a solution using a specific species combination"""  
       combo \= *self*.species\_combinations\[*combo\_idx*\]  
       n\_species\_in\_combo \= len(combo)  
        
       \# Determine how many of each species to place  
       species\_counts \= {}  
       remaining\_trees \= *self*.n\_trees  
        
       \# Distribute trees among species in combination  
       for i, species in enumerate(combo):  
           if i \== len(combo) \- 1:  
               count \= remaining\_trees  \# Last species gets remaining trees  
           else:  
               count \= max(1, remaining\_trees // (len(combo) \- i))  
               remaining\_trees \-= count  
           species\_counts\[species\] \= count  
        
       \# Select locations based on pheromone  
       location\_indices \= \[\]  
       location\_probs \= *self*.location\_pheromone \*\* *self*.alpha  
       location\_probs \= location\_probs / location\_probs.sum()  
        
       \# Select distinct locations  
       selected\_indices \= np.random.choice(*self*.n\_candidates, *self*.n\_trees,  
                                         *replace*\=False, *p*\=location\_probs)  
        
       solution\_locations \= \[\]  
       solution\_species \= \[\]  
        
       \# Assign species to locations  
       species\_assignments \= \[\]  
       for species, count in species\_counts.items():  
           species\_assignments.extend(\[species\] \* count)  
        
       \# Shuffle species assignments  
       np.random.shuffle(species\_assignments)  
        
       for loc\_idx, species in zip(selected\_indices, species\_assignments):  
           location \= *self*.candidate\_locations\[loc\_idx\]  
           solution\_locations.append(location)  
           solution\_species.append(species)  
        
       return solution\_locations, solution\_species, combo  
    
   *def* evaluate\_solution(*self*, *locations*, *species*):  
       """Evaluate cooling score of a solution"""  
       grid\_points \= *self*.study\_area.grid\_points  
       score \= *self*.cooling\_model.calculate\_cooling\_score(*locations*, *species*, grid\_points)  
       return score  
    
   *def* update\_pheromones(*self*, *solutions*, *scores*, *combinations*):  
       """Update pheromone trails based on ant solutions"""  
       \# Evaporate pheromones  
       *self*.location\_pheromone \*= (1 \- *self*.evaporation\_rate)  
       *self*.combination\_pheromone \*= (1 \- *self*.evaporation\_rate)  
        
       \# Find best solution in this iteration  
       best\_idx \= np.argmax(*scores*)  
       best\_score \= *scores*\[best\_idx\]  
        
       \# Deposit pheromones based on solution quality  
       for (locations, species, combo), score in zip(*solutions*, *scores*):  
           \# Find combo index  
           combo\_tuple \= tuple(sorted(combo))  
           combo\_idx \= None  
           for i, c in enumerate(*self*.species\_combinations):  
               if tuple(sorted(c)) \== combo\_tuple:  
                   combo\_idx \= i  
                   break  
            
           if combo\_idx is None:  
               continue  
            
           \# Normalize score for pheromone deposit  
           normalized\_score \= score / best\_score if best\_score \> 0 else 0.1  
            
           \# Find indices of selected locations  
           location\_indices \= \[\]  
           for loc in locations:  
               \# Find closest candidate location  
               distances \= cdist(\[loc\], *self*.candidate\_locations)\[0\]  
               closest\_idx \= np.argmin(distances)  
               location\_indices.append(closest\_idx)  
            
           \# Deposit pheromones on locations  
           for loc\_idx in location\_indices:  
               *self*.location\_pheromone\[loc\_idx\] \+= normalized\_score  
            
           \# Deposit pheromone on combination  
           *self*.combination\_pheromone\[combo\_idx\] \+= normalized\_score  
    
   *def* run(*self*, *verbose*\=True):  
       """Run multi-species ACO optimization"""  
       history\_best \= \[\]  
       history\_avg \= \[\]  
       history\_combinations \= \[\]  
        
       for iteration in tqdm(range(*self*.n\_iterations), *desc*\="Multi-Species ACO Optimization"):  
           solutions \= \[\]  
           scores \= \[\]  
           combinations \= \[\]  
            
           \# Construct solutions for all ants  
           for ant in range(*self*.n\_ants):  
               \# Select species combination based on pheromone  
               combo\_probs \= *self*.combination\_pheromone \*\* *self*.alpha  
               combo\_probs \= combo\_probs / combo\_probs.sum()  
               combo\_idx \= np.random.choice(*self*.n\_combinations, *p*\=combo\_probs)  
                
               \# Construct solution with this combination  
               locations, species, combo \= *self*.construct\_solution\_with\_combination(combo\_idx)  
               score \= *self*.evaluate\_solution(locations, species)  
                
               solutions.append((locations, species, combo))  
               scores.append(score)  
               combinations.append(combo)  
                
               \# Update best solution  
               if score \> *self*.best\_score:  
                   *self*.best\_score \= score  
                   *self*.best\_solution \= (locations.copy(), species.copy())  
                   *self*.best\_combination \= combo  
            
           \# Update pheromones  
           *self*.update\_pheromones(solutions, scores, combinations)  
            
           \# Record statistics  
           history\_best.append(max(scores))  
           history\_avg.append(np.mean(scores))  
           history\_combinations.append(combinations\[np.argmax(scores)\])  
            
           if *verbose* and iteration % 10 \== 0:  
               best\_combo \= combinations\[np.argmax(scores)\]  
               combo\_names \= \[*self*.tree\_species.get\_species\_properties(s)\['common\_name'\] for s in best\_combo\]  
               print(*f*"Iteration {iteration}: Best \= {max(scores)*:.2f*}, Avg \= {np.mean(scores)*:.2f*}")  
               print(*f*"  Best combination: {', '.join(combo\_names)}")  
        
       return history\_best, history\_avg, history\_combinations

\# \============================================================================  
\# 4\. COMPREHENSIVE SPECIES COMBINATION ANALYSIS  
\# \============================================================================

*class* ComprehensiveSpeciesAnalysis:  
   """Analyze all species combinations systematically"""  
    
   *def* \_\_init\_\_(*self*, *study\_area*, *cooling\_model*, *n\_trees*\=10):  
       *self*.study\_area \= *study\_area*  
       *self*.cooling\_model \= *cooling\_model*  
       *self*.n\_trees \= *n\_trees*  
       *self*.tree\_species \= TreeSpecies()  
        
   *def* analyze\_all\_combinations(*self*, *n\_configurations\_per\_combo*\=5):  
       """Analyze all species combinations with multiple configurations"""  
       all\_combinations \= *self*.tree\_species.get\_all\_species\_combinations()  
       results \= {}  
        
       print(*f*"\\nAnalyzing all {len(all\_combinations)} species combinations...")  
        
       for combo\_idx, combo in enumerate(tqdm(all\_combinations, *desc*\="Analyzing combinations")):  
           combo\_key \= '+'.join(sorted(combo))  
           combo\_results \= {  
               'combo': combo,  
               'configurations': \[\],  
               'best\_score': \-np.inf,  
               'best\_configuration': None,  
               'average\_score': 0  
           }  
            
           scores \= \[\]  
            
           \# Test multiple configurations for this combination  
           for config\_idx in range(*n\_configurations\_per\_combo*):  
               \# Generate random configuration for this combination  
               valid\_locations \= *self*.study\_area.get\_valid\_planting\_locations(*n\_locations*\=100)  
               selected\_indices \= np.random.choice(len(valid\_locations), *self*.n\_trees, *replace*\=False)  
               locations \= valid\_locations\[selected\_indices\]  
                
               \# Distribute species from combination  
               species\_list \= \[\]  
               for i in range(*self*.n\_trees):  
                   species \= combo\[i % len(combo)\]  
                   species\_list.append(species)  
                
               \# Shuffle species to avoid patterns  
               np.random.shuffle(species\_list)  
                
               \# Calculate cooling score  
               grid\_points \= *self*.study\_area.grid\_points  
               score \= *self*.cooling\_model.calculate\_cooling\_score(locations, species\_list, grid\_points)  
                
               scores.append(score)  
                
               \# Store configuration if it's the best so far  
               if score \> combo\_results\['best\_score'\]:  
                   combo\_results\['best\_score'\] \= score  
                   combo\_results\['best\_configuration'\] \= (locations.copy(), species\_list.copy())  
                
               combo\_results\['configurations'\].append({  
                   'locations': locations,  
                   'species': species\_list,  
                   'score': score  
               })  
            
           combo\_results\['average\_score'\] \= np.mean(scores)  
           combo\_results\['std\_score'\] \= np.std(scores)  
           combo\_results\['min\_score'\] \= np.min(scores)  
           combo\_results\['max\_score'\] \= np.max(scores)  
            
           results\[combo\_key\] \= combo\_results  
        
       return results  
    
   *def* rank\_combinations(*self*, *results*):  
       """Rank species combinations by performance"""  
       ranked \= \[\]  
        
       for combo\_key, data in *results*.items():  
           ranked.append({  
               'combination': combo\_key,  
               'species\_count': len(data\['combo'\]),  
               'average\_score': data\['average\_score'\],  
               'best\_score': data\['best\_score'\],  
               'std\_score': data\['std\_score'\],  
               'combo\_list': data\['combo'\]  
           })  
        
       \# Sort by best score (descending)  
       ranked.sort(*key*\=*lambda* *x*: *x*\['best\_score'\], *reverse*\=True)  
        
       return ranked  
    
   *def* generate\_heatmaps\_for\_top\_combinations(*self*, *results*, *top\_n*\=10, *output\_folder*\='heatmaps'):  
       """Generate heatmaps for top-performing species combinations"""  
       \# Create output folder  
       Path(*output\_folder*).mkdir(*parents*\=True, *exist\_ok*\=True)  
        
       \# Get top combinations  
       ranked \= *self*.rank\_combinations(*results*)\[:*top\_n*\]  
        
       print(*f*"\\nGenerating heatmaps for top {*top\_n*} combinations in '{*output\_folder*}' folder...")  
        
       for rank, combo\_data in enumerate(tqdm(ranked, *desc*\="Generating heatmaps")):  
           combo\_key \= combo\_data\['combination'\]  
           best\_config \= *results*\[combo\_key\]\['best\_configuration'\]  
            
           if best\_config:  
               locations, species\_list \= best\_config  
                
               \# Calculate cooling distribution  
               grid\_points \= *self*.study\_area.grid\_points  
               cooling \= *self*.cooling\_model.calculate\_total\_cooling(locations, species\_list, grid\_points)  
                
               \# Create heatmap  
               fig, ax \= *self*.create\_combination\_heatmap(  
                   cooling, locations, species\_list, combo\_data, rank\+1  
               )  
                
               \# Save heatmap  
               filename \= *f*"{*output\_folder*}/rank\_{rank\+1*:02d*}\_{combo\_key}.png"  
               plt.savefig(filename, *dpi*\=300, *bbox\_inches*\='tight')  
               plt.close(fig)  
        
       print(*f*"Generated {len(ranked)} heatmaps in '{*output\_folder*}' folder")  
        
       \# Generate summary report  
       *self*.generate\_combination\_summary(ranked, *output\_folder*)  
    
   *def* create\_combination\_heatmap(*self*, *cooling*, *locations*, *species\_list*, *combo\_data*, *rank*):  
       """Create heatmap for a specific species combination"""  
       width \= *self*.study\_area.width  
       height \= *self*.study\_area.height  
        
       \# Reshape cooling values to grid  
       x\_coords \= *self*.study\_area.x\_coords  
       y\_coords \= *self*.study\_area.y\_coords  
       cooling\_grid \= *cooling*.reshape(len(x\_coords), len(y\_coords))  
        
       \# Create figure  
       fig, ax \= plt.subplots(*figsize*\=(12, 10))  
        
       \# Plot heatmap  
       im \= ax.imshow(cooling\_grid.T,  
                     *extent*\=\[0, width, 0, height\],  
                     *origin*\='lower',  
                     *cmap*\='coolwarm\_r',  
                     *aspect*\='auto')  
        
       \# Add colorbar  
       cbar \= plt.colorbar(im, *ax*\=ax)  
       cbar.set\_label('Cooling Effect (Normalized)', *fontsize*\=12)  
        
       \# Plot tree placements  
       species\_colors \= {}  
       for (x, y), species in zip(*locations*, *species\_list*):  
           color \= *self*.tree\_species.get\_species\_color(species)  
           species\_colors\[species\] \= color  
            
           \# Plot tree location  
           ax.scatter(x, y, *color*\=color, *s*\=120, *edgecolors*\='black',  
                     *linewidth*\=2, *zorder*\=5, *alpha*\=0.8)  
            
           \# Plot crown radius circle  
           props \= *self*.tree\_species.get\_species\_properties(species)  
           crown\_radius \= props.get('crown\_diameter\_m', 0) / 2 if props else 2  
           circle \= plt.Circle((x, y), crown\_radius, *color*\=color,  
                              *alpha*\=0.15, *linestyle*\='-', *linewidth*\=1)  
           ax.add\_patch(circle)  
        
       \# Create legend for species  
       from matplotlib.patches import Patch  
       legend\_elements \= \[\]  
       for species, color in species\_colors.items():  
           props \= *self*.tree\_species.get\_species\_properties(species)  
           common\_name \= props.get('common\_name', species)  
           legend\_elements.append(Patch(*facecolor*\=color, *alpha*\=0.8,  
                                       *label*\=*f*"{common\_name}"))  
        
       if legend\_elements:  
           ax.legend(*handles*\=legend\_elements, *loc*\='upper right', *fontsize*\=9)  
        
       \# Set title with combination info  
       species\_names \= \[\]  
       for species in *combo\_data*\['combo\_list'\]:  
           props \= *self*.tree\_species.get\_species\_properties(species)  
           species\_names.append(props.get('common\_name', species))  
        
       title \= *f*"Rank \#{*rank*}: {', '.join(species\_names)}\\n"  
       title \+= *f*"Best Score: {*combo\_data*\['best\_score'\]*:.2f*} | "  
       title \+= *f*"Avg Score: {*combo\_data*\['average\_score'\]*:.2f*} ± {*combo\_data*\['std\_score'\]*:.2f*}"  
        
       ax.set\_title(title, *fontsize*\=14, *fontweight*\='bold')  
       ax.set\_xlabel('Distance X (meters)', *fontsize*\=12)  
       ax.set\_ylabel('Distance Y (meters)', *fontsize*\=12)  
        
       \# Add grid  
       ax.grid(True, *alpha*\=0.2, *linestyle*\='--')  
        
       plt.tight\_layout()  
       return fig, ax  
    
   *def* generate\_combination\_summary(*self*, *ranked\_data*, *output\_folder*):  
       """Generate summary report of species combinations"""  
       summary\_file \= Path(*output\_folder*) / "species\_combinations\_summary.csv"  
        
       summary\_data \= \[\]  
       for rank, data in enumerate(*ranked\_data*, 1):  
           \# Convert species codes to common names  
           species\_names \= \[\]  
           for species in data\['combo\_list'\]:  
               props \= *self*.tree\_species.get\_species\_properties(species)  
               species\_names.append(props.get('common\_name', species))  
            
           summary\_data.append({  
               'Rank': rank,  
               'Combination\_Key': data\['combination'\],  
               'Species\_Count': data\['species\_count'\],  
               'Species\_Names': ', '.join(species\_names),  
               'Best\_Score': data\['best\_score'\],  
               'Average\_Score': data\['average\_score'\],  
               'Std\_Deviation': data\['std\_score'\]  
           })  
        
       df \= pd.DataFrame(summary\_data)  
       df.to\_csv(summary\_file, *index*\=False)  
        
       print(*f*"\\nSummary report saved to: {summary\_file}")  
        
       \# Also create a text summary  
       txt\_summary \= Path(*output\_folder*) / "top\_combinations\_summary.txt"  
       with open(txt\_summary, 'w') as f:  
           f.write("TOP SPECIES COMBINATIONS FOR URBAN COOLING\\n")  
           f.write("=" \* 60 \+ "\\n\\n")  
            
           for rank, data in enumerate(*ranked\_data*\[:20\], 1):  
               species\_names \= \[\]  
               for species in data\['combo\_list'\]:  
                   props \= *self*.tree\_species.get\_species\_properties(species)  
                   species\_names.append(props.get('common\_name', species))  
                
               f.write(*f*"Rank \#{rank}:\\n")  
               f.write(*f*"  Species: {', '.join(species\_names)}\\n")  
               f.write(*f*"  Number of species: {data\['species\_count'\]}\\n")  
               f.write(*f*"  Best cooling score: {data\['best\_score'\]*:.2f*}\\n")  
               f.write(*f*"  Average score: {data\['average\_score'\]*:.2f*} ± {data\['std\_score'\]*:.2f*}\\n")  
               f.write("-" \* 40 \+ "\\n")  
        
       print(*f*"Text summary saved to: {txt\_summary}")

\# \============================================================================  
\# 5\. MAIN EXECUTION PIPELINE \- REVISED  
\# \============================================================================

*def* main\_pipeline\_comprehensive():  
   """Main execution pipeline with comprehensive species combination analysis"""  
    
   print("=" \* 70)  
   print("COMPREHENSIVE ANALYSIS OF TREE SPECIES COMBINATIONS")  
   print("For Caloocan Microclimate Regulation")  
   print("=" \* 70)  
    
   \# Create output directories  
   heatmap\_dir \= "comprehensive\_heatmaps"  
   results\_dir \= "analysis\_results"  
   Path(heatmap\_dir).mkdir(*exist\_ok*\=True)  
   Path(results\_dir).mkdir(*exist\_ok*\=True)  
    
   \# Step 1: Initialize study area  
   print("\\nStep 1: Initializing study area...")  
   study\_area \= StudyArea(*width*\=70, *height*\=70, *resolution*\=1)  
    
   \# Add synthetic vulnerability zones  
   study\_area.add\_vulnerability\_zone('schools\_health\_centers', (20, 20))  
   study\_area.add\_vulnerability\_zone('schools\_health\_centers', (50, 50))  
   study\_area.add\_vulnerability\_zone('high\_density\_residential', (35, 35))  
    
   print(*f*"Study area: {study\_area.width}m x {study\_area.height}m")  
   print(*f*"Grid points: {study\_area.n\_points}")  
    
   \# Step 2: Initialize cooling model  
   print("\\nStep 2: Initializing cooling model...")  
   cooling\_model \= CoolingModel(*decay\_lambda*\=0.01)  
    
   \# Step 3: Comprehensive species combination analysis  
   print("\\nStep 3: Performing comprehensive species combination analysis...")  
   analyzer \= ComprehensiveSpeciesAnalysis(study\_area, cooling\_model, *n\_trees*\=10)  
    
   \# Analyze all combinations  
   combination\_results \= analyzer.analyze\_all\_combinations(*n\_configurations\_per\_combo*\=10)  
    
   \# Rank combinations  
   ranked\_combinations \= analyzer.rank\_combinations(combination\_results)  
    
   \# Step 4: Generate heatmaps for all combinations  
   print("\\nStep 4: Generating heatmaps for all species combinations...")  
   analyzer.generate\_heatmaps\_for\_top\_combinations(  
       combination\_results,  
       *top\_n*\=31,  \# All 31 combinations (5C1 \+ 5C2 \+ 5C3 \+ 5C4 \+ 5C5)  
       *output\_folder*\=heatmap\_dir  
   )  
    
   \# Step 5: Run multi-species ACO optimization  
   print("\\nStep 5: Running multi-species ACO optimization...")  
   multi\_aco \= MultiSpeciesAntColonyOptimization(  
       study\_area, cooling\_model,  
       *n\_trees*\=10, *n\_ants*\=20, *n\_iterations*\=30  
   )  
    
   history\_best, history\_avg, history\_combinations \= multi\_aco.run(*verbose*\=True)  
    
   \# Get optimized solution  
   optimized\_locations, optimized\_species \= multi\_aco.best\_solution  
   best\_combo \= multi\_aco.best\_combination  
    
   \# Calculate cooling for optimized solution  
   grid\_points \= study\_area.grid\_points  
   optimized\_cooling \= cooling\_model.calculate\_total\_cooling(  
       optimized\_locations, optimized\_species, grid\_points  
   )  
    
   \# Step 6: Generate comparison with single-species scenarios  
   print("\\nStep 6: Generating single-species comparison scenarios...")  
   tree\_species \= TreeSpecies()  
    
   single\_species\_results \= {}  
   for species in tree\_species.species\_list:  
       \# Create single-species scenario  
       valid\_locations \= study\_area.get\_valid\_planting\_locations(*n\_locations*\=100)  
       selected\_indices \= np.random.choice(len(valid\_locations), 10, *replace*\=False)  
       locations \= valid\_locations\[selected\_indices\]  
       species\_list \= \[species\] \* 10  
        
       \# Calculate cooling  
       cooling \= cooling\_model.calculate\_total\_cooling(locations, species\_list, grid\_points)  
       score \= np.sum(cooling)  
        
       props \= tree\_species.get\_species\_properties(species)  
       species\_name \= props.get('common\_name', species)  
        
       single\_species\_results\[species\_name\] \= {  
           'score': score,  
           'locations': locations,  
           'species\_list': species\_list,  
           'cooling': cooling  
       }  
    
   \# Step 7: Generate final visualizations  
   print("\\nStep 7: Generating final visualizations...")  
    
   \# Create comparison plots  
   fig1, ax1 \= plt.subplots(*figsize*\=(14, 8))  
    
   \# Plot 1: Top combinations vs single species  
   ax1.set\_title('Cooling Performance: Species Combinations vs Single Species',  
                *fontsize*\=16, *fontweight*\='bold')  
    
   \# Top combinations (bars)  
   top\_10\_combos \= ranked\_combinations\[:10\]  
   combo\_names \= \[\]  
   combo\_scores \= \[\]  
    
   for i, combo in enumerate(top\_10\_combos):  
       species\_list \= combo\['combo\_list'\]  
       names \= \[tree\_species.get\_species\_properties(s)\['common\_name'\] for s in species\_list\]  
       combo\_names.append(*f*"C{i\+1}\\n({len(names)} species)")  
       combo\_scores.append(combo\['best\_score'\])  
    
   x\_pos \= np.arange(len(combo\_names))  
   ax1.bar(x\_pos, combo\_scores, *alpha*\=0.7, *color*\='steelblue', *label*\='Top Combinations')  
    
   \# Single species (points)  
   single\_names \= list(single\_species\_results.keys())  
   single\_scores \= \[single\_species\_results\[name\]\['score'\] for name in single\_names\]  
    
   ax1.scatter(x\_pos\[:len(single\_names)\], single\_scores, *color*\='red', *s*\=100,  
              *marker*\='s', *label*\='Single Species', *zorder*\=5)  
    
   ax1.set\_xticks(x\_pos)  
   ax1.set\_xticklabels(combo\_names, *rotation*\=45, *ha*\='right', *fontsize*\=9)  
   ax1.set\_ylabel('Cooling Score', *fontsize*\=12)  
   ax1.legend(*fontsize*\=11)  
   ax1.grid(True, *alpha*\=0.3, *axis*\='y')  
    
   plt.tight\_layout()  
   plt.savefig(*f*'{results\_dir}/performance\_comparison.png', *dpi*\=300, *bbox\_inches*\='tight')  
   plt.close()  
    
   \# Plot 2: ACO convergence  
   fig2, ax2 \= plt.subplots(*figsize*\=(10, 6))  
   iterations \= range(len(history\_best))  
    
   ax2.plot(iterations, history\_best, 'b-', *linewidth*\=2, *label*\='Best Solution')  
   ax2.plot(iterations, history\_avg, 'r--', *linewidth*\=2, *label*\='Average Solution')  
    
   ax2.set\_xlabel('Iteration', *fontsize*\=12)  
   ax2.set\_ylabel('Cooling Score', *fontsize*\=12)  
   ax2.set\_title('Multi-Species ACO Optimization Convergence', *fontsize*\=14, *fontweight*\='bold')  
   ax2.legend(*fontsize*\=11)  
   ax2.grid(True, *alpha*\=0.3, *linestyle*\='--')  
    
   plt.tight\_layout()  
   plt.savefig(*f*'{results\_dir}/aco\_convergence.png', *dpi*\=300, *bbox\_inches*\='tight')  
   plt.close()  
    
   \# Plot 3: Optimized solution heatmap  
   fig3, ax3 \= plt.subplots(*figsize*\=(12, 10))  
    
   \# Create heatmap  
   width \= study\_area.width  
   height \= study\_area.height  
   cooling\_grid \= optimized\_cooling.reshape(len(study\_area.x\_coords), len(study\_area.y\_coords))  
    
   im \= ax3.imshow(cooling\_grid.T,  
                  *extent*\=\[0, width, 0, height\],  
                  *origin*\='lower',  
                  *cmap*\='coolwarm\_r',  
                  *aspect*\='auto')  
    
   cbar \= plt.colorbar(im, *ax*\=ax3)  
   cbar.set\_label('Cooling Effect (Normalized)', *fontsize*\=12)  
    
   \# Plot tree placements  
   species\_colors \= {}  
   for (x, y), species in zip(optimized\_locations, optimized\_species):  
       color \= tree\_species.get\_species\_color(species)  
       species\_colors\[species\] \= color  
        
       ax3.scatter(x, y, *color*\=color, *s*\=120, *edgecolors*\='black',  
                  *linewidth*\=2, *zorder*\=5, *alpha*\=0.8)  
        
       props \= tree\_species.get\_species\_properties(species)  
       crown\_radius \= props.get('crown\_diameter\_m', 0) / 2 if props else 2  
       circle \= plt.Circle((x, y), crown\_radius, *color*\=color,  
                          *alpha*\=0.15, *linestyle*\='-', *linewidth*\=1)  
       ax3.add\_patch(circle)  
    
   \# Title with combination info  
   combo\_names \= \[tree\_species.get\_species\_properties(s)\['common\_name'\] for s in best\_combo\]  
   title \= *f*"ACO-Optimized Solution: {', '.join(combo\_names)}\\n"  
   title \+= *f*"Cooling Score: {multi\_aco.best\_score*:.2f*}"  
    
   ax3.set\_title(title, *fontsize*\=14, *fontweight*\='bold')  
   ax3.set\_xlabel('Distance X (meters)', *fontsize*\=12)  
   ax3.set\_ylabel('Distance Y (meters)', *fontsize*\=12)  
   ax3.grid(True, *alpha*\=0.2, *linestyle*\='--')  
    
   plt.tight\_layout()  
   plt.savefig(*f*'{results\_dir}/aco\_optimized\_solution.png', *dpi*\=300, *bbox\_inches*\='tight')  
   plt.close()  
    
   \# Step 8: Generate comprehensive report  
   print("\\n" \+ "=" \* 70)  
   print("COMPREHENSIVE ANALYSIS RESULTS")  
   print("=" \* 70)  
    
   print(*f*"\\nTotal species combinations analyzed: {len(ranked\_combinations)}")  
   print(*f*"Heatmaps generated: {len(ranked\_combinations)} (in '{heatmap\_dir}' folder)")  
    
   print("\\nTOP 5 SPECIES COMBINATIONS:")  
   print("-" \* 60)  
   for rank, combo in enumerate(ranked\_combinations\[:5\], 1):  
       species\_names \= \[\]  
       for species\_code in combo\['combo\_list'\]:  
           props \= tree\_species.get\_species\_properties(species\_code)  
           species\_names.append(props\['common\_name'\])  
        
       print(*f*"\\nRank \#{rank}:")  
       print(*f*"  Species: {', '.join(species\_names)}")  
       print(*f*"  Number of species: {combo\['species\_count'\]}")  
       print(*f*"  Best cooling score: {combo\['best\_score'\]*:.2f*}")  
       print(*f*"  Average score: {combo\['average\_score'\]*:.2f*} ± {combo\['std\_score'\]*:.2f*}")  
    
   print("\\nSINGLE SPECIES PERFORMANCE:")  
   print("-" \* 60)  
   for species\_name, data in sorted(single\_species\_results.items(),  
                                   *key*\=*lambda* *x*: *x*\[1\]\['score'\], *reverse*\=True):  
       print(*f*"  {species\_name}: {data\['score'\]*:.2f*}")  
    
   print("\\nACO-OPTIMIZED SOLUTION:")  
   print("-" \* 60)  
   combo\_names \= \[tree\_species.get\_species\_properties(s)\['common\_name'\] for s in best\_combo\]  
   print(*f*"  Species combination: {', '.join(combo\_names)}")  
   print(*f*"  Cooling score: {multi\_aco.best\_score*:.2f*}")  
    
   \# Count species in optimized solution  
   species\_counts \= {}  
   for species in optimized\_species:  
       species\_counts\[species\] \= species\_counts.get(species, 0) \+ 1  
    
   print(*f*"  Species distribution in solution:")  
   for species, count in species\_counts.items():  
       props \= tree\_species.get\_species\_properties(species)  
       print(*f*"    {props\['common\_name'\]}: {count} trees")  
    
   print("\\n" \+ "=" \* 70)  
   print("OUTPUT FILES SUMMARY")  
   print("=" \* 70)  
   print(*f*"\\n1\. Heatmaps folder: '{heatmap\_dir}/'")  
   print(*f*"   Contains: {len(ranked\_combinations)} heatmaps for all species combinations")  
   print(*f*"   Naming: rank\_XX\_speciescombination.png")  
    
   print(*f*"\\n2\. Analysis results folder: '{results\_dir}/'")  
   print(*f*"   Contains:")  
   print(*f*"   \- performance\_comparison.png: Top combinations vs single species")  
   print(*f*"   \- aco\_convergence.png: ACO optimization progress")  
   print(*f*"   \- aco\_optimized\_solution.png: Best ACO solution heatmap")  
   print(*f*"   \- species\_combinations\_summary.csv: Detailed results (in heatmaps folder)")  
   print(*f*"   \- top\_combinations\_summary.txt: Text summary (in heatmaps folder)")  
    
   print("\\n3\. Key findings:")  
   print(*f*"   \- Total possible combinations: 31 (5C1 \+ 5C2 \+ 5C3 \+ 5C4 \+ 5C5)")  
   print(*f*"   \- Best performing combination: {', '.join(\[tree\_species.get\_species\_properties(s)\['common\_name'\] for s in ranked\_combinations\[0\]\['combo\_list'\]\])}")  
   print(*f*"   \- ACO-optimized combination: {', '.join(combo\_names)}")  
    
   return {  
       'study\_area': study\_area,  
       'cooling\_model': cooling\_model,  
       'combination\_results': combination\_results,  
       'ranked\_combinations': ranked\_combinations,  
       'single\_species\_results': single\_species\_results,  
       'aco\_optimized': (optimized\_locations, optimized\_species, optimized\_cooling),  
       'aco\_results': (history\_best, history\_avg)  
   }

\# \============================================================================  
\# 6\. QGIS INTEGRATION \- MULTI-SPECIES VERSION  
\# \============================================================================

*def* create\_qgis\_layers\_comprehensive(*study\_area*, *tree\_placements*, *species\_list*, *cooling\_values*, *combination\_name*):  
   """Create GeoDataFrames for QGIS with comprehensive species information"""  
    
   \# Convert study area grid to GeoDataFrame  
   grid\_points \= \[Point(x, y) for x, y in *study\_area*.grid\_points\]  
   grid\_gdf \= gpd.GeoDataFrame({  
       'geometry': grid\_points,  
       'cooling\_value': *cooling\_values*,  
       'combination': *combination\_name*  
   })  
    
   \# Convert tree placements to GeoDataFrame  
   tree\_points \= \[Point(x, y) for x, y in *tree\_placements*\]  
   trees\_gdf \= gpd.GeoDataFrame({  
       'geometry': tree\_points,  
       'species': *species\_list*,  
       'index': range(len(*tree\_placements*))  
   })  
    
   \# Add species properties  
   tree\_species \= TreeSpecies()  
   trees\_gdf\['common\_name'\] \= trees\_gdf\['species'\].apply(  
       *lambda* *x*: tree\_species.get\_species\_properties(*x*).get('common\_name', 'Unknown')  
   )  
   trees\_gdf\['crown\_diameter'\] \= trees\_gdf\['species'\].apply(  
       *lambda* *x*: tree\_species.get\_species\_properties(*x*).get('crown\_diameter\_m', 0)  
   )  
   trees\_gdf\['height'\] \= trees\_gdf\['species'\].apply(  
       *lambda* *x*: tree\_species.get\_species\_properties(*x*).get('height\_m', 0)  
   )  
   trees\_gdf\['architecture'\] \= trees\_gdf\['species'\].apply(  
       *lambda* *x*: tree\_species.get\_species\_properties(*x*).get('architecture', 'Unknown')  
   )  
   trees\_gdf\['combination'\] \= *combination\_name*  
    
   return grid\_gdf, trees\_gdf

*def* export\_top\_combinations\_to\_qgis(*ranked\_combinations*, *combination\_results*, *study\_area*, *cooling\_model*, *top\_n*\=5):  
   """Export top combinations to QGIS format"""  
   qgis\_dir \= "qgis\_output\_top\_combinations"  
   Path(qgis\_dir).mkdir(*exist\_ok*\=True)  
    
   tree\_species \= TreeSpecies()  
    
   print(*f*"\\nExporting top {*top\_n*} combinations to QGIS format...")  
    
   for rank, combo\_data in enumerate(*ranked\_combinations*\[:*top\_n*\], 1):  
       combo\_key \= combo\_data\['combination'\]  
       best\_config \= *combination\_results*\[combo\_key\]\['best\_configuration'\]  
        
       if best\_config:  
           locations, species\_list \= best\_config  
            
           \# Get species names for combination name  
           species\_names \= \[\]  
           for species in combo\_data\['combo\_list'\]:  
               props \= tree\_species.get\_species\_properties(species)  
               species\_names.append(props\['common\_name'\])  
            
           combination\_name \= *f*"Rank{rank}\_{'\_'.join(\[n.replace(' ', '\_') for n in species\_names\])}"  
            
           \# Calculate cooling  
           grid\_points \= *study\_area*.grid\_points  
           cooling \= *cooling\_model*.calculate\_total\_cooling(locations, species\_list, grid\_points)  
            
           \# Create QGIS layers  
           grid\_gdf, trees\_gdf \= create\_qgis\_layers\_comprehensive(  
               *study\_area*, locations, species\_list, cooling, combination\_name  
           )  
            
           \# Export to shapefiles  
           combo\_dir \= Path(qgis\_dir) / *f*"combination\_{rank*:02d*}"  
           combo\_dir.mkdir(*exist\_ok*\=True)  
            
           grid\_shp \= combo\_dir / "cooling\_grid.shp"  
           trees\_shp \= combo\_dir / "tree\_placements.shp"  
            
           grid\_gdf.to\_file(str(grid\_shp))  
           trees\_gdf.to\_file(str(trees\_shp))  
            
           print(*f*"  Rank {rank}: Exported to {combo\_dir}")  
    
   print(*f*"\\nAll top {*top\_n*} combinations exported to '{qgis\_dir}' folder")  
   print("\\nTo use in QGIS for each combination:")  
   print("1. Add both shapefiles as layers")  
   print("2. Style cooling\_grid with Graduated colors using 'cooling\_value'")  
   print("3. Style tree\_placements with Categorized symbols using 'common\_name'")  
    
   return qgis\_dir

\# \============================================================================  
\# 7\. EXECUTE THE COMPREHENSIVE PIPELINE  
\# \============================================================================

if \_\_name\_\_ \== "\_\_main\_\_":  
    
   \# Run the comprehensive pipeline  
   results \= main\_pipeline\_comprehensive()  
    
   \# Export top combinations to QGIS  
   print("\\n" \+ "=" \* 70)  
   print("QGIS EXPORT FOR TOP COMBINATIONS")  
   print("=" \* 70)  
    
   try:  
       qgis\_dir \= export\_top\_combinations\_to\_qgis(  
           results\['ranked\_combinations'\],  
           results\['combination\_results'\],  
           results\['study\_area'\],  
           results\['cooling\_model'\],  
           *top\_n*\=5  
       )  
        
       print(*f*"\\nQGIS files saved in: {qgis\_dir}")  
        
   except Exception as e:  
       print(*f*"\\nNote: QGIS export requires geopandas and may not work in all environments.")  
       print(*f*"Error: {e}")  
       print("\\nYou can still use the PNG visualizations and CSV summaries for analysis.")  
    
   print("\\n" \+ "=" \* 70)  
   print("COMPREHENSIVE ANALYSIS COMPLETE")  
   print("=" \* 70)  
