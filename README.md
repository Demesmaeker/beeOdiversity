# beeOdiversity

The purpose of this code is to determine if there is a risk of pesticides or heavy metal level to be above the european recommendatation, based on the area and type of land around a point.

The datas comes from analysing the pollen of 63 different beehives.

We were given different datasets :
- Corine Land Cover for sites analysed.
- Heavy Metal seen by sites
- Pesticides seen by sites
- MRL and classification for pesticides
- MRL for heavy metal


## Map

![Map](https://github.com/Demesmaeker/beeOdiversit/blob/main/preview/Plan.svg)


## Who
This is a group project for the hackaton BeeOdiversity, the members are :
- [Thomas De Cleen](https://github.com/ThomasDeCleen) (Accenture)
- [Jonathan Decleire](https://github.com/JonathanDecleire) (BeCode Student)
- [Mathieu Leers](https://github.com/leersmathieu) (BeCode Student)
- [Morgane Demesmaeker](https://github.com/Demesmaeker) (BeCode Student)


## Objectives
Do some (not all) of the objectives :
Probability to have :

- 1 pesticide
- 1 fungicide
- 1 insecticide
- 1 herbicide

- 1 pesticide>MRL
- 1 fungicide>MRL
- 1 insecticide>MRL
- 1 herbicide>MRL

- 1 heavy metal
- 1 Pb>MRL
- 1 Cd>MRL
- 1 Cu>MRL

- Hg Absence/Presence


## When
- Start : 08/02/2021
- Deadline: 12/02/2021

Working after work


## Where
All the work done was made during the BeeOImpact Hackaton of 2021.


## Summary/Preview

### Preprocessing

#### Exploring the data
- Example : Classification of the pesticides
![Classification Pesticides](https://github.com/Demesmaeker/beeOdiversity/blob/main/preview/classe_pesti.svg)

- Exemple : Dataset of distances from the beehives
![Distances](https://github.com/Demesmaeker/beeOdiversity/blob/main/preview/distances.svg)


#### Modifying the data to get interesting columns


- Example for the heavy metals :
- 0 -> level under MRL (or no mercury)
- 1 -> level above MRL (or has mercury)
![Heavy metals](https://github.com/Demesmaeker/beeOdiversity/blob/main/preview/group_hm.svg)

- Example for the pesticides :
![Pesticides](https://github.com/Demesmaeker/beeOdiversity/blob/main/preview/group_pesti.svg)

- Getting a value for each zone influenced by area and the distance :
![Area/distance](https://github.com/Demesmaeker/beeOdiversity/blob/main/preview/area_distance.png)


#### Merging the datasest

![One big final Dataset](https://github.com/Demesmaeker/beeOdiversity/blob/main/preview/merged_all.svg)


### Modeling


## Limitations

There was only a few datas, only 63 different sites, even with there was 4 years of datas, and 4 anayses/years, we had to aggregate them by sites. The risks we had to find could not depend on the date. We had to find the worst case scenario here, so we aggregate them and took the maximum we could have.

But with so few datas, the models weren't very effective.
