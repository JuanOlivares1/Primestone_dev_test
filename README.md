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


<!-- ABOUT THE PROJECT -->
## About The Project

This is a multipurpose api that contains 3 functionalities:
- Prime number generator
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
   git clone https://github.com/JuanOlivares1/Primestone_dev_test.git
   ```
2. Install python dependences, go to the root project directory and run:
   ```sh
   pip install -r requirements.txt
   ```
3. Create a new Postgres database named 'primestone_api' and create a valid user if you haven't

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
  
  - Example:

    ![image](https://user-images.githubusercontent.com/48563349/143718428-747c7c6f-07a8-48e1-b015-3fad9c3ea7e8.png)

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
    
  - Example:

    ![image](https://user-images.githubusercontent.com/48563349/143718501-511d0469-22c6-4c7e-bd95-3454bcedcf6f.png)
  
* Data storage

  This endpoint recieves json data in any format, it always saves the json on postgres database, unless it's empty,  no matter the content
  
  To use this endpoint send a PUT http request to the endpoint 'http://127.0.0.1:5000/set-data'.
  
  ```sh
  curl -X PUT http://127.0.0.1:5000/set-data -H "Content-Type: application/json" -d '{"name":"Lucas","age":"35"}'
  ```
  
  If method worked correctly it answers with 'Created', otherwise 'Failed' is sent. But you can ensure data was saved by psql as follows:
  
  ```sh
  psql primestone_api
  ```
  
  And quering the data:
  
  ```sql
  SELECT * FROM data
  ```
  
  
  - Example:

    ![image](https://user-images.githubusercontent.com/48563349/143718541-79fade11-85ab-4df8-8003-cc15f0ad7535.png)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Juan DAvid Olivares Padilla - [@OlivaresP____](https://twitter.com/OlivaresP____) - jdop2000@gmail.com

Project Link: [https://github.com/JuanOlivares1/Primestone_dev_test](https://github.com/JuanOlivares1/Primestone_dev_test)

<p align="right">(<a href="#top">back to top</a>)</p>
