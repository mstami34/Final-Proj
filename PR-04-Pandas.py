#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Initialize Otter
import otter
grader = otter.Notebook("PR-04-Pandas.ipynb")


# # Project 4: 
# 
# ### Data Analysis with Pandas
# 

# 
# 
# ---

# ## Instructions
# 
# Pick one problem and complete it. Then run the last cell in the notebook to export your work.
# 
# ### Grading Rubric
# 
# Your submission will be evaluated based on the following criteria (see on ELMS for more info):
# * __Correctness__: _Does the program adequately solve the problem posed for the project? (Note we use autograder to determine this.)_
# * __Logic__: _Regardless of execution, is the solution approach taken sound (i.e., likely to lead to a solution)? Note: this requirement can be satisfied even if the program isn’t passing the autograder tests!_
# * __Style__: _Is the code understandable and well documented?_
#   * _Is the variable names clear and intuitive (e.g. `rate` instead of `x`) and there are no conflicts with names of existing functions (e.g. you call your list `list_of_numbers` instead of `list`, etc.)?_
#   * _Are the key elements of the code clearly documented with comments?_
#   * _Are the main functions documented with a complete docstring?_
# * __Final Checklist__: _All steps in the "Submission checklist" below have been followed_.
# 
# ### Working on Multiple Problems
# 
# You do not have to complete all problems in the notebook: if your code passes all the tests in a single problem it will pass the autograder for the whole project. That said, you will earn credit for passing any test in the notebook. This means that if you are not passing all the tests in a given problem, you can attempt a different problem and see if you can pass any of its tests. However, keep in mind that we will consider all the problems you submit when grading for logic and style.

# <br/>
# <br/>
# <br/>
# <br/>
# <br/>
# <br/>
# 
# ---

# ## Problem 1:  Flexible Course Prerequisites
# 
# The file `"testudo_fall2020.csv"` shows course descriptions from Fall 2020 at UMD. We are investigating whether and how  different schools/areas of the university vary, in being flexible with regard to prerequisites for their courses.  Your dataset must provide this information (transformed from the original), with the 6 most and 6 least flexible schools/areas. (as measured by percentage of courses with rigid or flexible prerequisites).
# 
# If all goes well your solution should return the following data frame:
# 
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>area</th>
#       <th>flexibility</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>INFM</td>
#       <td>1.000000</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>SPHL</td>
#       <td>1.000000</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>PLCY</td>
#       <td>0.892857</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>URSP</td>
#       <td>0.857143</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>ENSP</td>
#       <td>0.833333</td>
#     </tr>
#     <tr>
#       <th>5</th>
#       <td>AMST</td>
#       <td>0.777778</td>
#     </tr>
#     <tr>
#       <th>6</th>
#       <td>PHSC</td>
#       <td>0.600000</td>
#     </tr>
#     <tr>
#       <th>7</th>
#       <td>PSYC</td>
#       <td>0.447368</td>
#     </tr>
#     <tr>
#       <th>8</th>
#       <td>BMGT</td>
#       <td>0.433962</td>
#     </tr>
#     <tr>
#       <th>9</th>
#       <td>MATH</td>
#       <td>0.408163</td>
#     </tr>
#     <tr>
#       <th>10</th>
#       <td>STAT</td>
#       <td>0.400000</td>
#     </tr>
#     <tr>
#       <th>11</th>
#       <td>ECON</td>
#       <td>0.265625</td>
#     </tr>
#   </tbody>
# </table>
# 
# ### Hint
# 
# To read this particular dataset correctly with the `read_csv` function, make sure to pass `keep_default_na=False`. Otherwise, some entries in the CSV file may not be recognized correctly. 
# 
# ---
# 
# ⬇️⬇️⬇️ Enter your solution in the cell below ⬇️⬇️⬇️

# In[1]:


import pandas as pd

def flexible_course_prerequisites(filename):
    data = pd.read_csv(filename, keep_default_na=False)

    # Clean and preprocess the data
    data["prereqs"] = data["prereqs"].str.lower()
    data["flexibility"] = data["prereqs"].apply(lambda x: 1 if "permission" in x or "or" in x or "recommended" in x or "restriction" in x else 0)

    # Calculate the percentage of flexible courses for each area
    area_flexibility = data.groupby("area")[["flexibility"]].mean().reset_index()
    area_flexibility.columns = ["area", "flexibility"]

    # Sort the areas by flexibility
    area_flexibility = area_flexibility.sort_values(by="flexibility", ascending=False).reset_index(drop=True)

    # Select the top 6 and bottom 6 areas
    top_areas = area_flexibility.head(6)
    bottom_areas = area_flexibility.tail(6)

    # Create the desired output dataframe
    output = pd.concat([top_areas, bottom_areas])
    output.index = range(len(output))

    return output

## Test your solution
fn = "testudo_fall2020.csv"
my_cp_df = flexible_course_prerequisites(fn)
my_cp_df


# In[11]:


grader.check("prob1")


# <br/>
# <br/>
# <br/>
# <br/>
# <br/>
# <br/>
# 
# ---

# 
# ## Problem 2: Gender Gap in Labor Statistics
# 
# The file `"bls-by-category.csv"` shows number of workers and weekly earnings broken down by occupation, occupation category, and gender. Our aim is to find out how the average weekly earnings gap between males and females varies across occupation category. The final dataset (transformed from the original), must present this information, alongwith the 6 categories that have the largest <span style="text-decoration: underline;">average</span> gender gap in weekly earnings, and the 6 categories that have the smallest <span style="text-decoration: underline;">average</span> gender gap in weekly earnings. NOTE: For missing data, a data cleaning step may be required. Also, since earnings gap is not available in original data, it must be computed.     
# 
# If all goes well your solution should return the following data frame:
# 
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>Category</th>
#       <th>Gap_weekly</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>SCIENCE</td>
#       <td>367.000000</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>SALES</td>
#       <td>311.545455</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>MANAGEMENT</td>
#       <td>306.125000</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>BUSINESS</td>
#       <td>287.916667</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>COMPUTATIONAL</td>
#       <td>218.714286</td>
#     </tr>
#     <tr>
#       <th>5</th>
#       <td>HEALTHCARE PROFESSIONAL</td>
#       <td>207.714286</td>
#     </tr> 
#     <tr>
#       <th>6</th>
#       <td>CULINARY</td>
#       <td>81.000000</td>
#     </tr>
#     <tr>
#       <th>7</th>
#       <td>OFFICE</td>
#       <td>74.411765</td>
#     </tr>
#     <tr>
#       <th>8</th>
#       <td>HEALTHCARE SUPPORT</td>
#       <td>69.000000</td>
#     </tr>
#     <tr>
#       <th>9</th>
#       <td>AGRICULTURAL</td>
#       <td>62.000000</td>
#     </tr>
#     <tr>
#       <th>10</th>
#       <td>SOCIAL SERVICE</td>
#       <td>61.333333</td>
#     </tr>
#     <tr>
#       <th>11</th>
#       <td>PROTECTIVE SERVICE</td>
#       <td>54.000000</td>
#     </tr>
#   </tbody>
# </table>
# 
# 
# ---
# 
# ⬇️⬇️⬇️ Enter your solution in the cell below ⬇️⬇️⬇️

# In[ ]:


import pandas as pd

def labor_stats_gender_gap(filename):


## Test your solution
fn = "bls-by-category.csv"x
my_stats_df = labor_stats_gender_gap(fn)
my_stats_df


# In[ ]:


grader.check("prob2")


# <br/>
# <br/>
# <br/>
# <br/>
# <br/>
# <br/>
# 
# ---

# ## Problem 3: NCAA Basketball Coaches Winrates 
# 
# The file `"ncaa-team-data.csv"` contains data of season statistics for NCAA basketball teams and their associated head coaches. Our aim is to learn how the season winrates (defined as the \% of wins over total number of matches) vary across coaches. 
# 
# Our final dataset (transformed from the original), must present this information of the 6 coaches that have the best <span style="text-decoration: underline;">average</span> winrates (across seasons), and the 6 coaches that have the worst <span style="text-decoration: underline;">average</span> winrates (across seasons).
# 
# A couple of things to keep in mind:
# 1. Consider only the coaches that have participated in at least 3 seasons;
# 2. The `"wl"` column is the winrate for each season. You can also compute the winrate from columns `"w"` and `"l"` though you will see a small discrepancy in some cases;
# 3. Some teams had multiple coaches in a season; consider only the first one.
# 
# If all goes well your solution should return the following data frame:
# 
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>Coach</th>
#       <th>winrate</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>Thomas Mills</td>
#       <td>0.966667</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>George Sweetland</td>
#       <td>0.916750</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>Joseph Raycroft</td>
#       <td>0.901250</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>Carlisle Cutchin</td>
#       <td>0.890333</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>Theo Bellmont</td>
#       <td>0.888750</td>
#     </tr>
#     <tr>
#       <th>5</th>
#       <td>B.C. Edwards</td>
#       <td>0.887500</td>
#     </tr>
#     <tr>
#       <th>6</th>
#       <td>Larry Smith</td>
#       <td>0.134000</td>
#     </tr>      
#     <tr>
#       <th>7</th>
#       <td>Tony Relvas</td>
#       <td>0.132000</td>
#     </tr>
#     <tr>
#       <th>8</th>
#       <td>Louis Gillesby</td>
#       <td>0.128500</td>
#     </tr>
#     <tr>
#       <th>9</th>
#       <td>Arthur Badenoch</td>
#       <td>0.122667</td>
#     </tr>
#     <tr>
#       <th>10</th>
#       <td>Howie Evans</td>
#       <td>0.121000</td>
#     </tr>
#     <tr>
#       <th>11</th>
#       <td>Franklyn Ashcraft</td>
#       <td>0.073667</td>
#     </tr>
#   </tbody>
# </table>
# 
# ---
# 
# ⬇️⬇️⬇️ Enter your solution in the cell below ⬇️⬇️⬇️

# In[ ]:


import pandas as pd

...

def ncaa_basketball_coach_winning(filename):
    ...

## Test your solution
fn = "ncaa-team-data.csv"
my_coaches_df = ncaa_basketball_coach_winning(fn)
my_coaches_df


# In[ ]:


grader.check("prob3")


# <br/>
# <br/>
# <br/>
# <br/>
# <br/>
# <br/>
# 
# ---

# ## Problem 4: Restaurant Transactions by Time of Day 
# 
# The file `"BreadBasket_DMS.csv"` contains data of time-stamped transactions from a restaurant. We would like to know the most popular items by time of day, in the following 6 categories: 1) breakfast (opening to 10am), 2) preLunch (between 10am and 12pm), 3) lunch (12-3pm), 4) postLunch (between 3p and 6pm) 5) dinner (6-8pm), and 6) lateDinner (8pm to close). Our final dataset must be transformed from the original dataset, and provide an answer to our question. NOTE: the time categories are not in the original dataset (only time stamps), so you will need to compute them.
# 
# If all goes well your solution should return the following data frame:
# 
# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>Time_Category</th>
#       <th>item</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>breakfast</td>
#       <td>Coffee</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>dinner</td>
#       <td>Coffee</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>lateDinner</td>
#       <td>Postcard</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>lunch</td>
#       <td>Coffee</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>postLunch</td>
#       <td>Coffee</td>
#     </tr>
#     <tr>
#       <th>5</th>
#       <td>preLunch</td>
#       <td>Coffee</td>
#     </tr>
#   </tbody>
# </table>
# 
# ---
# 
# ⬇️⬇️⬇️ Enter your solution in the cell below ⬇️⬇️⬇️

# In[ ]:


import pandas as pd

...
    
def restaurant_transactions_by_time_day(filename):
    data = pd.read_csv(filename)


## Test your solution
fn = "BreadBasket_DMS.csv"
my_restaurant_df = restaurant_transactions_by_time_day(fn)
my_restaurant_df


# In[ ]:


grader.check("prob4")


# <br/>
# <br/>
# <br/>
# <br/>
# <br/>
# <br/>
# 
# ---

# <div class="alert alert-info"> <b><i>Note:</i></b> Do not forget to run this cell before exporting the ZIP file for Gradescope! </div>

# In[13]:


get_ipython().system('jupyter nbconvert --to script PR-04-Pandas.ipynbx')


# ## Submission
# 
# Make sure you have run all cells in your notebook in order before running the cell below, so that all images/graphs appear in the output. The cell below will generate a zip file for you to submit.

# In[12]:


grader.export(pdf=False, force_save=True, run_tests=True, files=['PR-04-Pandas.py'])


#  
