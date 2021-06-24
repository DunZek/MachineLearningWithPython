# Chapter 7 - Prepare Your Data For Machine Learning

Transforming data to best expose the structure of the problem to the modeling algorithms

**Summary:**
1. Rescale data
2. Standardize data
3. Normalize data
4. Binarize data

**7.1 Need For Data Pre-processing:**
- Always needed
- However, proper data preparation can eliminate the requirement for pre-processing to get better results.
- Create a variety of views and data transformations to exercise a handful of algorithms on each one to help reveal the problem better.

**7.2 Data Transforms:**
- Structure of data pre-processing:
    1. Load the dataset (URL/local)
    2. Split the dataset into the input and output variables for machine learning
    3. Apply a pre-processing transform to the input variables
    4. Summarize the data to show the change
- 4 different data pre-processing recipes
- Scikit-learn documentation on various pre-processing methods:
    - Fit and Multiple Transform (preferred)
        - Call `fit()` to prepare the parameters of the transform once on your data.
        - Call `transform()` to prepare the data for modeling and again on the test or validation dataset or new data for the future.
    - Combined Fit-And-Transform