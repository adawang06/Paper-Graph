# Paper Graph

• Built a distributed big data pipeline on AWS to facilitate data collection and graph annotation for Open Research Corpus Dataset with 45 Millions academic research papers. The pipeline allowed researchers to identify the mostimportant papers related to their papers of interest. 

• Designed a multi-node Spark cluster-computing framework processing modules. Applied minHash locality sensitive hashing algorithm to compare similarities between papers, optimized Pyspark jobs performance by tuning and comparing different Spark operations-transformations and user defined functions (UDF).

• Deployed a Neo4j database to store graph-based relationship between academic papers, including citation relation- ships and also similarity relationships, Neo4j database supported front-end query demands for graph illustration.

## Demo
* [Paper Graph](http://deproject.club)
* [video](https://www.youtube.com/watch?v=wckz3nzaRNw&feature=youtu.be)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system


## Data Source

* [Semantic Scholar](https://api.semanticscholar.org/corpus/) - Over 45 million published research papers in Computer Science, Neuroscience, and Biomedical fields provided as an easy-to-use JSON archive.

## Built With

* [PySpark](https://spark.apache.org/docs/2.3.0/api/python/pyspark.html) - PySpark is the Python API for Spark.
* [Neo4j](https://neo4j.com/) - Graph database management system
* [AWS_S3](https://aws.amazon.com/s3/) - Simple Storage Service is a service offered by Amazon Web Services
* [PostgreSQL](https://www.postgresql.org/) -  Relational database management system
![image](https://user-images.githubusercontent.com/35754641/60793938-8c364080-a11d-11e9-9999-06f3a667f9c5.png)


## Contributing

Please read [CONTRIBUTING.md](https://www.google.com/) for details on our code of conduct, and the process for submitting pull requests to us.


## Author

* **Da Wang** - *Initial work* - [Paper Graph](http://deproject.club)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
* Billie Thompson's template
