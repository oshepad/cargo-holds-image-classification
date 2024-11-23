# Dirty Cargo Holds
___

### Problem Statement

Vessel Operators often have to decide a vessel's next cargo without knowing the likelihood of the suitability of her cargo holds to meet the cleanliness standard for that cargo.  The goal of this project is to provide a model that can assess the conditions of the holds and advise the probability that it is matches the cleanliness standard for the intended cargo.
___

### Background



___


### Executive Summary

Dry Bulk cargo is often seen as a leading indicator of the global economy.  The industry comprises the trade of materials that often are required for industrial growth; steel, energy, food, construction, industrial supplies, amongst other commodities.  These bulk cargoes are typically traded in global markets requiring transporation of thousands of miles of tens of thousands of tonnes pf cargo aboard dry bulk cargo vessels.  

The workhorses of this fleet are the handysize, supramax, and ultramax vessels that are capable of transitioning from one cargo to the other. Many times a year, a dry bulk vessel prepares her holds for her next cargo.  Often times, there are various cargos available that require different cleanliness standards.  Depending on several factors from previous cargo, the crew's experience and capability, to the condition of the vessel's holds; there is a lot of uncertainty in how a vessel will meet the standards for the next cargo.

This project aims to reduce that uncertainty by creating a model to assess the conditions of the vessels cargo holds, likelohood to meet the standards of the intended cargoes under consideration, necessary cleaning steps, and provide an evaluation metric for the vessel crew's performance.

___


### File Directory

* Assets
* Code
* Data
* Presentation
___

### Data Dictionary

The data for this project was provided by Three D's Marine Inc.
https://www.threedsmarine.com/ 

The initial dataset was simply divided between clean and dirty cargo holds.
The ongoing project is working to further classify this data as follows:

* Soda Ash clean
* Pot Ash clean
* Grain Clean
* Sugar Clean
* Salt Clean
* Sulfur Clean
* Petcoke Clean
* Cement Clean
* Clinker Clean
* Gypsum Clean
* Steel Products Clean
* Failing Paint
* Chipped Paint
* Rust scale
* Rust scarring
* Cargo residues
* Hatch coamings

Additionally, the initial data underwent augmentation to the training set to increase the 
___

### Conclusions

It is important to acknowledge that pictures do not capture other variables for a holds inspection, such as dryness and odors.  Holds are to be dry and odor-free.

The model's results are only as good as the content the images capture.  If the photo omits critical portions of a cargo hold (chipped paint, cargo residues, etc) the results will be misleading.  It is important that the photos capture the overall condition of the hold as well as highlighting any questionable areas.

The model is not going to be perfect in every sense.  It will likely be very accurate, more accurate than a human, as assessing the quality of holds given a photo.  The actual condition of the holds are determined by a human, right or wrong, with different opinions and focus than the computer.
___

### Next Steps

* Gather and label data into further labels
* Catalogue vessels time, equipment, crews cleaning effort from cargo to cargo.
* Add section for cleaning steps, estimated time requirement, estimated cleaning materials
___

### Sources

___

### Visualizations

___