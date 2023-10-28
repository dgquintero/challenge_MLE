# Software Engineer (ML & LLMs) Challenge


# Part I

## Resolving issues
- An issue was found in the usage of sns.barplot when the 'x' and 'y' keys were not specified
- An issue was found in the test_model.py with the location od data.csv

## Choosing a Model

Choosing XGBoost over Logistic Regression, despite their similar overall performance, is based on the subtle yet crucial advantage of XGBoost in F1-Score, specifically for Class 1. The F1-Score balances precision and recall and, in this case, XGBoost's slightly higher F1-Score of 0.37 compared to Logistic Regression's 0.36 implies a better ability to handle specific instances. This advantage can be crucial in scenarios where accurate identification of Class 1 is vital, making XGBoost the preferred choice.

### Metrics Comparison

| Metric               | XGBoost (Class 0 / Class 1) | Logistic Regression (Class 0 / Class 1) |
|----------------------|------------------------------|-----------------------------------------|
| **Precision**        | 0.88 / 0.25                  | 0.88 / 0.25                             |
| **Recall**           | 0.52 / 0.69                  | 0.52 / 0.69                             |
| **F1-Score**         | 0.66 / 0.37                  | 0.65 / 0.36                             |
| **Accuracy**         | 0.55                         | 0.55                                    |
| **Macro Avg Precision** | 0.56                     | 0.56                                    |
| **Macro Avg Recall**    | 0.61                     | 0.60                                    |
| **Macro Avg F1-Score**  | 0.51                     | 0.51                                    |
| **Weighted Avg Precision** | 0.76                 | 0.76                                    |
| **Weighted Avg Recall**    | 0.55                 | 0.55                                    |
| **Weighted Avg F1-Score**  | 0.60                 | 0.60                                    |
| **Support**           | Class 0: 18294, Class 1: 4214 | Class 0: 18294, Class 1: 4214         |


**Using Google Cloud Platform (GCP) in Your Project**

In this project, we have chosen to harness the power and versatility of Google Cloud Platform (GCP) to host and manage our cloud resources. GCP offers a wide range of services and tools that have been instrumental in achieving our project goals.

**Some key benefits of GCP include**:

1. **Elasticity and Scalability**: GCP allows us to adjust our resources as per project requirements, providing efficient scalability without disruptions.

2. **Enterprise-Grade Security**: Security is of utmost importance, and GCP provides robust security measures and compliance with regulations.

3. **Ease of Management**: The GCP management console is intuitive and user-friendly, simplifying the management of our cloud resources.

4. **Diverse Services**: GCP offers a wide array of services, from data storage and analytics to machine learning, enabling us to access the right tools for each phase of our project.

5. **Flexible Payment Options**: With pay-as-you-go options, GCP accommodates our budget and avoids unnecessary costs.

## FastAPI Integration

This project leverages the power of FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. FastAPI provides an easy and efficient way to create RESTful APIs with automatic validation, documentation, and interactive capabilities.

**Key Features**:

- **High Performance**: FastAPI is designed for speed and can handle high loads with ease.

- **Interactive Docs**: Built-in interactive documentation and automatic OpenAPI and JSON Schema generation make API development a breeze.

- **Type Hints**: Utilize Python's type hints to define data models, making your API robust and self-documenting.

- **Asynchronous Support**: FastAPI supports asynchronous programming, allowing for efficient handling of concurrent requests.

- **Authentication and Security**: Easily implement authentication and security measures to protect your API.

FastAPI simplifies API development, making it the ideal choice for this project. Get started with FastAPI by following our setup instructions in the README.

## FastAPI Integration

This project leverages the power of FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. FastAPI provides an easy and efficient way to create RESTful APIs with automatic validation, documentation, and interactive capabilities.

**Key Features**:

- **High Performance**: FastAPI is designed for speed and can handle high loads with ease.

- **Interactive Docs**: Built-in interactive documentation and automatic OpenAPI and JSON Schema generation make API development a breeze.

- **Type Hints**: Utilize Python's type hints to define data models, making your API robust and self-documenting.

- **Asynchronous Support**: FastAPI supports asynchronous programming, allowing for efficient handling of concurrent requests.

- **Authentication and Security**: Easily implement authentication and security measures to protect your API.

FastAPI simplifies API development, making it the ideal choice for this project. Get started with FastAPI by following our setup instructions in the README.



## DOCKER

## Build the Docker Image

```
docker build -t myimage .
```

## Start the Docker Container

```
docker run -d --name mycontainer -p 80:80 myimage

```
