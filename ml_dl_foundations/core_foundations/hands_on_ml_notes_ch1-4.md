# the more important notes to be taking
@ https://github.com/yanshengjia/ml-road/blob/master/resources/Hands%20On%20Machine%20Learning%20with%20Scikit%20Learn%20and%20TensorFlow.pdf

- machine learning is the science and art of programming computers so that they can learn from data

# 1. Supervised / unsupervised learning
- supervised, unsupervised, semisupervised, reinforcement learning

 1. supervised learning
  - a typical supervised learning task is *classification* 
  - ex. spam filter, trained with many instances of spam vs not spam (ham) emails

  - another typical task is to predict a *target* numeric value 
  - this is called **regression**
  - ex. predict price of car, based on mileage, age, brand, etc...
    - must give the program many instances of cars along with their predictors and labels

  - a *attribute* is a data type
  - a *feature* has several meanings depending on context, but usually refers to a label plus its value ("mileage", 15,000)

  - some regression algorithms can be used for classification, and vice versa.
  - ex. **logistic regression** is commonly used for classification, since its output is a value that corresponds to a probability of something being a certain class (20% chance the email is spam)

  Most important supervised learning algorithms covered in the book:
  * k-Nearst neighbors
  * linear regression
  * logistic regression
  * support vector machines (SVMs)
  * decision trees and random forests
  * neural networks

 2. Unsupervised learning

 * training data is unlabeled, and the system tries to learn without a teacher

 Important unsupervised learning algorithms
 * Clustering
    - k-means 
    - hierarchical cluster analysis (HCA)
    - expectation maximization
* visualization and dimensionality reduction
    - principal component analysis (PCA)
    - Kernel PCA
    - locally-linear embedding (LLE)
    - t-distributed stochastic neighbor embedding (t-SNE)
* association rule learning
    - apriori
    - eclat

- dimensionalty reduction
    - a task with the goal of simplifying data without losing too much information
     - a way to do this is by merging two or more features into one
     - ex. a car's mileage may be correlated with its age, so dimensionality reduction will merge them into one feature that measures the car's wear and tear. 
     - this is called *feature extraction*

     - running data through a dimensionality reduction algorithm before feeding it to a machine learning algorithm will allow it to take up much less space, and possibly run faster.

- anomaly detection
    - another important unsupervised learning task
    - ex. detecting unusual credit card transcations, catching manufacturing defects, or automatically removing outliers from a dataset
    - the system can detect between a normal instance and a likely anomaly instance

- association rule learning
    - task with goal of digging into large amounts of data and discovering interesting relations between attributes.
    - ex. for a supermarket, learning that those that buy BBQ sauce and potato chips often buy steak as well, suggesting that you might want to put those items next to each other.
