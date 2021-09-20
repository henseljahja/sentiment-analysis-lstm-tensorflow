<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.5 18.203125 "/></g></g></g></svg>
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- [![LinkedIn][linkedin-shield]][linkedin-url] -->

<!-- PROJECT LOGO -->
<br />
<p align="center">  
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://raw.githubusercontent.com/henseljahja/henseljahja/main/assets/hensel.svg" alt="Logo" width="200" height="200">
  </a>

  <h2 align="center">Sentiment Analysis using Tensorflow and Spark  </h2>
  
<h2 align="center">

<!-- [![MIT License][license-shield]][license-url] -->

[![Open In Colab][colab-shield]][colab-url]

</h2>
  <p align="center">
    Sentiment Analysis, with spark as resilient data loader, and Tensorflow multiworker for distributed training
    <!-- <br /> -->
    <!-- <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a> -->
    <!-- <br /> -->
    <!-- <br /> -->
    <!-- <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a> -->
    <!-- · -->
    <!-- <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    · -->
    <!-- <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a> -->
  </p>
</p>
<h4 align = "center">Built with:

![Python][python-shield]
![Tensorflow][tensorflow-shield]
![scikit-learn][scikitlearn-shield]

</h4>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li> -->
  </ol>
</details>
<!-- ABOUT THE PROJECT -->

# About The Project

Analysis is needed for reporting the customer feedback from a product, this project aim at analysis and report of customer insight,

<!-- GETTING STARTED -->

# Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

# Prerequisites

You need to install these dependency

- [Python](python.org)
- [Kaggle Api](https://github.com/Kaggle/kaggle-api)

  Optional

  - [Poetry](https://python-poetry.org/docs/#installation)

# Installation

1. Clone the repo and get navigate to directory

   ```sh
   git clone git@github.com:henseljahja/sentiment-analysis-lstm-tensorflow.git
   ```

   then

   ```sh
   cd sentiment-analysis-lstm-tensorflow
   ```

2. Create virtual environment on terminal

   ```sh
   python3 venv -m ./sentiment_analysis/
   ```

   or

   ```sh
   python venv -m ./sentiment_analysis/
   ```

3. Activate the virtual environment

   ```sh
   source ./sentiment_analysis/bin/activate
   ```

4. Install packages from poetry

   ```sh
   poetry install
   ```

   or

   ```sh
   pip install -r requirements.txt
   ```

5. Get the data

   - Kindle Reviews dataset

   ```sh
   kaggle datasets download -d bharadwaj6/kindle-reviews
   ```

   - Glove dataset

   ```sh
   kaggle datasets download -d thanakomsn/glove6b300dtxt
   ```

# Usage

Run the projects,

```sh
python3 main.py
```

and see the figure at `/figures`

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

[![Gmail][gmail-shield]][gmail-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com -->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/henseljahja/sentiment-analysis-lstm-tensorflow/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/henseljahja/sentiment-analysis-lstm-tensorflow/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/henseljahja/sentiment-analysis-lstm-tensorflow/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/henseljahja/sentiment-analysis-lstm-tensorflow/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/henseljahja
[product-screenshot]: images/screenshot.png
[tensorflow-shield]: https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white
[python-shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[gmail-url]: henseljahja@gmail.com
[gmail-shield]: https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white
[scikitlearn-shield]: https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white
[colab-shield]: https://colab.research.google.com/assets/colab-badge.svg
[colab-url]: https://colab.research.google.com/github/henseljahja/sentiment-analysis-lstm-tensorflow/blob/main/LSTM-sentiment-analysis.ipynb
