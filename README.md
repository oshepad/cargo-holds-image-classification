# Dirty Cargo Holds
___

### Problem Statement

Vessel Operators often have to decide a vessel's next cargo without knowing the likelihood of the suitability of her cargo holds to meet the cleanliness standard for that cargo.  The goal of this project is to provide a model that can assess the conditions of the holds and advise the probability that it is matches the cleanliness standard for the intended cargo.
___

### Background

The normal workflow to evaluate a vessel's holds is a dynamic and fluid process.  It starts when the vessel is initially hired and her hold conditions are reviewed with her cargo history.  There are two exceptions to the normal workflow, ones for new vessels and vessels leaving drydock.  New vessels, the cargo holds are assumed to be hospital clean with no blemishes whatsoever.  It is possible that the coatings were not applied well, water and or other construction debris infilitrated the holds on her maiden ballast leg, and some other scenarios that could impede this assumption, though highly unliklely.  The other scenario, a vessel leaving drydock, is similar, but deserves separate attention.  The vessel's cargo holds are not always recoated or recoated well.  In some cases, the holds are sandblasted to remove rust and impurities and the sand is not completely or properly removed leaving holds that have not been coated well.  Both of these scenarios fall outside the scope of this model and the process of their evaluation is different.

All other vessels, coming off a previous cargo, have a cargo history.  Each cargo has its own set of characteristics that affect the cleanliness and condition of the holds.  Some can stain (petcoke), leave dust (gypsum), leave hard residues (cement), increase rusting (steel products), and or corrode the coatings and underlying steel (sulphur).  Some leave the holds largely intact and need a good sweeping and rinsing (grains).  Knowing the cargo history is an important step in considering what amount of time, effort, and materials will be needed to prepare the cargo holds for the next cargo.

The crew performance and motivation can also be a determining factor in the holds conditions.  Crews are individual to a vessel and always changing as crew members come and go.  Some are better than others and some are rewarded for their efforts better than others.

The geographical area of where the vessel is unloading her cargo will also impact what cargos are considered next for the vessel.  Some are available within a reasonable distance while others are not.  Cleaning equipment and materials may or may not be readily available to augment those that are on board the vessel.

The vessel operator takes these considerations into account along with the companies overall plan for that vessel and their program.  They might have sent that vessel to a certain area to load another cargo they have already booked for instance.  Others are nearing the end of their hire duration and must be sent in a particular direction for redelivery.  Or they may be allowed or not allowed to carry certain cargoes due to either regulations on the vessel and or restrictions in the charter party.

It is at this moment where the model can assist the vessel operator.  Either before booking the "last cargo" or before booking the "next cargo."  The vessel operator will have pictures of the cargo holds from the last time the vessel was ready to load.  They may have pictures of the holds after it just unloaded depending on where they are in the life cycle of the charter.

___


### Executive Summary

Dry Bulk cargo is often seen as a leading indicator of the global economy.  The industry comprises the trade of materials that often are required for industrial growth; steel, energy, food, construction, industrial supplies, amongst other commodities.  These bulk cargoes are typically traded in global markets requiring transporation of thousands of miles of tens of thousands of tonnes pf cargo aboard dry bulk cargo vessels.  

The workhorses of this fleet are the handysize, supramax, and ultramax vessels that are capable of transitioning from one cargo to the other. Many times a year, a dry bulk vessel prepares her holds for her next cargo.  Often times, there are various cargos available that require different cleanliness standards.  Depending on several factors from previous cargo, the crew's experience and capability, to the condition of the vessel's holds; there is a lot of uncertainty in how a vessel will meet the standards for the next cargo.

This project aims to reduce that uncertainty by creating a model to assess the conditions of the vessels cargo holds, likelohood to meet the standards of the intended cargoes under consideration, necessary cleaning steps, and provide an evaluation metric for the vessel crew's performance.

The model performance will be evaluated on accuracy, precision, recall, and F1 score

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

chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://www.standard-club.com/fileadmin/uploads/standardclub/Documents/Import/publications/standard-cargo/23964-15056CargoJan2011Bulletinv06.pdf 
___

### Visualizations

___