# Chapter 8 - Feature Selection For Machine Learning

**8.6 Summary**
- Learned feature selection for preparing machine learning data in Python using scikit-learn. There were 4 different automatic techniques:
  1. Univariate Selection
  2. Recursive Feature Elimination
  3. Principle Component Analysis
  4. Feature Importance
- Afterwards -> learn to evaluate machine learning algorithms.

Machine learning models are affected by the data features you choose to use. Irrelevant or even partially relevant features can negatively impact model performance. This chapter introduces automatic features selection techniques used to prepare machine learning data using scikit-learn.

1. Univariate Selection
2. Recursive Feature Elimination
3. Principle Component Analysis
4. Feature Importance

**8.1 Feature Selection:**
- A process where data features that most contribute to prediction variable or output is automatically selected. Algorithms especially lienar ones such as linear and logistic regression can be negatively affected by irrelevant features. There are three benefits of performing feature selection before data modelling:
- *Overfitting reduction* - Reducing decision making processes based upon noise.
- *Accuracy improvement* - Modelling accuracy improves with lesser misleading data
- *Training time reduction* - Algorithms train faster with lesser data

---

### Footnotes

- *You can learn mroe about feature selection with scikit-learn in the article Feature selection. Each feature selection recipes will use the Pima Indians onset of diabetes dataset.*
  - <https://scikit-learn.org/stable/modules/feature_selection.html>
- *You can learn more about the RFE class in the scikit-learn documentation.*
  - <http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#>
- *Learn more about the PCA calss in scikit-learn by reviewing the API.*
  - <http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html>
- *You can learn more about the ExtraTreesClassifier class in the scikit-learn API*
  - <http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.>