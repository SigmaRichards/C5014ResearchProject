#Research Proposal - Outline
## Title: A comparison of segmentation techniques using confidential mine site data from Rio Tinto
## Author: Daniel Hess
## Supervisor: Professor Eun-Jung Holden
## Degree: MDS (12 point project)

### Background
 - Photographs used in computers for analysis, classification and decision making
 - Accessing height data or distance data allows us to create 3d surfaces
 - Many techniques exist for processing image data, can find patterns where humans can't, processing times much faster.
 - Convolutions, filtering and NNs can be used with labelled data to produce deep analysis into the data
 - Sadly supervised techniques require large amounts of labelled data to be useful
 - Performance is great on test data similar to training data, however not as good on unique data e.g. 10 mine sites across 10 regions each with different strata and vegetation
 - Unsupervised techniques can be good on single pieces of data e.g. a single mine site, and can be adapted to many different areas
 - Kmeans, ACO and ABees: Broad use techniques, adapted to work on image data
 - SLIC, Kielch: image specific techniques
 
### Aim
 - Explore the effectiveness of different types of segmentation techniques
 - Expect general purpose techniques such as kmeans to perform better on metadata e.g. aeromagnetics
 - Texture segments will be used as a general purpose overlay for the aerial data
 - Computer aided visualisation and segmentation that can be reapplied to many locations
 - Applications to geologists, technicians and other decision makers in the mining process
 
### Method
 - Implementation will largely done in python
 - Implement techniques and adapt them to the image workflow
 - Standardise input output workflow for easier comparison of the techniques
 - Compare different segmentation techniques
 - - ACO, ABees, Kmeans (General Purpose)
 - - SLIC, Kielch Model (Image specific)
 - - Factorization, PMCFA (Metric specific)
 - Compare metrics used for quantifying each techniques
 - - Desireable features???
 
### Software / Hardware Requirements
#### Software
 - Python
 - Packages for specific techniques
 - - KMeans: sklearn
 - - ACO: github.com/johnberroa/Ant-Colony-Optimization
 - - ABees: Hive
 - - SLIC: scikit-image
 - - Kielch
 - - Factorization: github.com/yuanj07/FSEG_py
 - - PMCFA
#### Hardware
 - Non-specific
 - GPUs? Implemtations exist but necessary?
