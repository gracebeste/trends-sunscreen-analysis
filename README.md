# Rising Temperatures and Interest in Sunscreen
NOTE: This project is currently in a draft state and is awaiting finalization of files from my local drive.

This repository houses my data analytics project on the effect of weather patterns and changes in public sentiment regarding skin protection.

Table of Contents:
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Folder Structure](#folder-structure)
4. [Datasets](#datasets)
5. [Analysis](#analysis)
6. [Results and Discussion](#results-and-discussion)

## Introduction
This project investigates the relationship between weather patterns and public interest in sun protection. By analyzing historical weather data alongside Google Trends search data, the goal is to uncover trends and potential correlations between changing environmental conditions and consumer behavior. The study focuses on data from 2020 to 2024, with an emphasis on maximum temperatures in the United States and the popularity of search terms related to sun protection, namely "sunscreen," "SPF," "UV protection," and "skincare."

## Prerequisites

Before you begin this project, ensure you have the following installed:

1. **Programming Language**:
   - Python 3.13.1 or higher.

2. **Dependencies**:
   - Install the required libraries using the `requirements.txt` file:
     ```bash
     pip3 install -r requirements.txt
     ```

3. **API Keys**:
   - Obtain an API key from:
     - [Visual Crossing Weather](https://www.visualcrossing.com/)
     - Note that no API key is required for the Google trends data using the pytrends library.
   - Save the VC Weather API key in an `.env` file as follows:
     ```
     VC_API_KEY=[your_visual_crossing_key]
     ```

4. **Tools**:
   - Git for version control (download from [git-scm.com](https://git-scm.com/)).

5. **System Requirements**:
   - Tested on macOS Monterey 12.5.
  
6. **Environment Setup**:
   - Optional: While not required, creating a virtual environment is recommended to isolate project dependencies and prevent conflicts with other Python projects. To create and activate a virtual environment, run the following in your command prompt:
     ```bash
     python -m venv env
     source env/bin/activate  # macOS command
     ```

## Folder Structure

## Datasets
Two primary datasets are used in this analysis:

- Weather Data:

  - Source: Visual Crossing Weather, a platform providing historical and forecast weather data.
  - Content: Maximum daily temperatures across the United States from 2020 to 2024.
  - Methodology: A Python script was employed to extract the data from the Visual Crossing Weather API.

- Google Trends Data:

  - Source: Google Trends, accessed via the Pytrends library.
  - Content: Search interest for keywords: "sunscreen," "SPF," "UV protection," and "skincare," over the same 2020–2024 timeframe.
  - Methodology: A Python script leveraging the Pytrends library was used to collect the search popularity data for each keyword.

These datasets provide the foundation for analyzing potential correlations between weather conditions and public interest in sun protection.

## Analysis

## Results and Discussion
