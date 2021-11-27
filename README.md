<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Primestone API</h3>

  <p align="center">
    Minimalist API REST made in flask with different functionalities.
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a multipurpose api that contains 3 functionalities:
- prime number generator
- Inches to meters converter
- Data storage.


### Built With

This Project was developed with following technologies:

* [Python](https://www.python.org)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Postgres](https://www.postgresql.org)
* [SQLAlchemy](https://www.sqlalchemy.org)


### Prerequisites

To run this project it is necessary to have at least Python 3.6 and a local PostgreSQL server

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
2. Install python dependences, go to the root project directory an run:
   ```sh
   pip install -r requirement.txt
   ```
3. Create a new Postgres database named 'primestone_api'

4. Run server:
   ```sh
   python3 app.py
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The server consists of 3 endpoints

* Prime numbers generator: 
  
  This endpint generates prime numbers from 1 to argument specified.
  To use this endpoint send a GET http request to the endpoint 'http://localhost:5000/get-prime-numbers?limit=10'. Change `limit` argument for any value.
  
  ```sh
  curl -X GET http://127.0.0.1:5000/get-prime-numbers?limit=10
  ```
  
* Inches to meters converter: 
  
  This endpoint recieves json data in the following format 
  ```js
  {
  “name”: “Pedro”,
  “height”: “70 pulgadas”
  }
  ```
  
  And answers in the same format but instead of inches it converts it to metters
  ```js
  {
  "name": "pedro",
  "height": "1.78 metros"
  }
  ```
  To use this endpoint send a POST http request to the endpoint 'http://127.0.0.1:5000/convert-height'.
  
  ```sh
  curl -X POST http://127.0.0.1:5000/convert-height -H "Content-Type: application/json" -d '{"name":"pedro","height":"70 pulgadas"}'
  ```
    
  
* Data storage

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p>
