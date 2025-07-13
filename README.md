# Salary-Prediction-Using-Regression

📊 Salary Prediction using Multivariate Linear Regression
This project demonstrates how to predict employee salaries using multiple variables such as:

Years of Experience

Education Level

Performance Rating

Location

The model is built using Ordinary Least Squares (OLS) regression with the statsmodels Python package.

Dataset
A  dataset of 250 employees was used with the following columns:

Column	Description
Name full names
Age	Age (22–60 years)
YearsExperience	Estimated based on age
EducationLevel	High School, Associate, Bachelor, Master, PhD
PerformanceRating	Poor, Average, Good, Excellent
Location	One of five U.S. cities
Salary	Calculated based on all above factors

Model Details
A multivariate regression model was used to understand how each factor impacts salary.

R-squared: 0.982
This means 98.2% of the salary variation is explained by the model — indicating high accuracy.



| Feature             | Effect on Salary                                                                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `YearsExperience`   | +\$2,165 per year                                                                                                                                |
| `EducationLevel`    | Higher education = higher salary:<br>• Bachelor: +\$13.5K<br>• Master: +\$27K<br>• PhD: +\$40K<br>• High School: -\$5.7K (compared to Associate) |
| `PerformanceRating` | • Good: +\$4.7K<br>• Excellent: +\$7.3K<br>• Poor: -\$2.4K (compared to Average)                                                                 |
| `Location`          | Salaries vary by city:<br>• New York: +\$8.7K<br>• LA: +\$5.8K<br>• Houston: -\$4.4K<br>• Phoenix: -\$6.9K (compared to Chicago)                 |




<img width="893" height="99" alt="image" src="https://github.com/user-attachments/assets/c2b10684-20af-4110-8d09-1431f52797cb" />



echnologies Used
Python

Pandas

NumPy

Statsmodels

Matplotlib

Seaborn

Jupyter Notebook














