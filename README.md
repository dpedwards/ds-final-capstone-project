# Data Science Capstone Project

<img width="450" alt="data_science_cycle" src="https://user-images.githubusercontent.com/2211088/117272062-173c0b00-ae5b-11eb-947e-6e8c41855ce8.png">

## Project description
### **Market and customer analysis of e-commerce channels with AI to determine advertising campaigns**

Predicting customer shopping behaviour on the Google Merchandise Store during a specific timeperiod.

![Google_Merchandise_Store_Analysis](https://user-images.githubusercontent.com/2211088/117272421-7437c100-ae5b-11eb-9064-e1bd0889754a.png)

Companies need to take a closer look at their customer base in order to launch targeted marketing campaigns. Machine lerarning helps to effectively analyze characteristics such as access device, demographic information, surfing / consumer behavior & media usage and to derive forecasts.

AI-powered models and analytics insights to help advertisers determine the best campaigns across different e-commerce advertising channels at specific times for their customers behavior to maximize customer revenue.


### Dataset 
Download the datasets and place it in the subfolder :file_folder: data :exclamation:

:cloud: https://drive.google.com/file/d/1yKfVN6l4Ge4F6xftLhcVwAuqOuez8PvP/view?usp=sharing

### Environment
  - Use the requirements file in this repo to create a new environment. For this you can either use make setup or the following commands:

        pyenv local 3.8.5
        python -m venv .venv
        source .venv/bin/activate
        pip install --upgrade pip
        pip install -r requirements.txt
        pip install pycaret
        python3 -m pip install nb-clean

### Note(s)
Cleanup jupyter notebooks before push to GitHub:
```
jupyter nbconvert --clear-output --inplace my_notebook.ipynb
```
