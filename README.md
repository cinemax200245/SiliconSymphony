# SliconSymphony: Unraveling Defects in WM-811K WaferMaps using Deep Learning

**Enhancing Wafer Defect Classification using Convolutional Neural Networks (CNN)**

In the realm of modern manufacturing, the accurate identification of specific class defects within products, such as wafermaps, holds paramount significance. The ability to swiftly discern anomalies not only aids in understanding potential production chain glitches but also empowers prompt, targeted interventions. In this repository, our collective endeavor revolves around the development of a streamlined Convolutional Neural Network (CNN) that effectively tackles the intricate challenge of wafermap defect classification.

**The Problem and Objective**

Our focus is centered on the critical task of identifying nine distinct defect classes in wafermaps, encompassing Center, Donut, Edge-Loc, Edge-Ring, Loc, Near-full, Random, Scratch, and none. These diverse defect types encapsulate a range of anomalies that may arise during the manufacturing process. The primary aim of our project is to create an intelligent system that can accurately assign each wafermap to its corresponding defect category.

**Navigating Imbalanced Data**

A significant hurdle in our endeavor is the considerable imbalance prevalent in the dataset. Imbalance emerges both among the different failure classes and between the non-failure class (none) and the failure classes. Recognizing this challenge, we undertook a strategic approach to address this imbalance.

**Synthetic Data Generation and Augmentation Techniques**

To counteract the imbalance and enhance the efficacy of our model, we embarked on a twofold strategy. Firstly, we leveraged the potential of synthetic data generation. This involved creating additional training samples for the underrepresented defect classes. Complementing this, we harnessed classical augmentation techniques to enrich the diversity of the training data. This two-pronged approach synergistically worked to enhance the model's ability to distinguish intricate defect patterns.

**Refined Model Performance**

The culmination of our efforts resulted in a refined CNN model that exhibited remarkable improvements over its earlier iterations. Notably, the final model demonstrated a more balanced performance across all defect classes, mitigating the undue influence of the dataset's imbalance. Furthermore, the model showcased an elevated mean percentage of accurately classified images, indicative of its enhanced robustness in real-world scenarios.

By sharing our journey and outcomes, we aspire to contribute to the realm of defect detection within manufacturing processes. Our work underscores the significance of intelligent algorithms in expediting defect identification and, consequently, enabling swift, precise corrective measures. We invite you to explore this repository and delve into the intricacies of our approach, offering insights and inspiration for similar endeavors.

<p align="center"> Center - Donut - Edge-Loc - Edge-Ring - Loc - Near-full - Random - Scratch - none </p>

Due to the **extreme imbalance of the dataset**, both among failure classes and between the non failure class (none) and the failure classes, we have focused on the **generation of synthetic data** that together with classical augmentation techniques have lead in improve model performance. In particular, the final model shows more uniform performance across classes than the initial one as well as a greater mean percentual of correct classified images.


| Failure   | Final Model Performance |
|-----------|:-----------------------:|
| Center    |         89.65%          |
| Donut     |         86.52%          |
| Edge-Loc  |         87.00%          |
| Edge-Ring |         96.64%          |
| Loc       |         64.72%          |
| Near-full |         91.67%          |
| Random    |         90.58%          |
| Scratch   |         67.57%          |
| None      |         98.80%          |
---------------------------------------
| Mean      |         85.90%          |  

More details can be found in the *Presentation slides.pdf* file. 

