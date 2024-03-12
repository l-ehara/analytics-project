# Country Inflation Analytics
### Available [here](https://analytics-project-globaleconmetrics.streamlit.app/) online!

Welcome to the Country Inflation Analytics project! This interactive tool leverages historical data to visualize and analyze the inflation rates of various countries from 1980 to the present. Built with Python, Streamlit, and Polars, this application provides a user-friendly interface for exploring inflation trends and gaining insights into economic patterns over the decades.

## Features

- **Interactive Visualizations**: Utilize Streamlit's dynamic capabilities to interact with the data through graphs and charts.
- **Country-wise Analysis**: Drill down into each country's specific inflation data and trends over the years.
- **Historical Data Insights**: Explore how inflation has evolved since 1980 for each country in the dataset.
- **Data-Driven**: Powered by Polars, enjoy fast and efficient data manipulation and analysis.
- 
## Technologies

- **Python**: The backbone of our project, Python is utilized for developing the application logic and data analysis scripts. Its extensive ecosystem of libraries makes it an ideal choice for data science and web development.
- **Streamlit**: An innovative open-source framework that simplifies the process of building interactive and elegant web applications for Machine Learning and Data Science projects. Streamlit has been instrumental in creating a user-friendly interface for our analytics tool.
- **Polars**: This cutting-edge DataFrames library, written in Rust, provides lightning-fast data manipulation and analysis capabilities. Polars is the engine behind our efficient data processing, enabling real-time insights even with large datasets.
- **Plotly**: A comprehensive graphing library that allows us to create interactive, publication-quality graphs and visualizations directly from Python. Plotly enhances our application by offering dynamic, engaging, and responsive visualizations, making data exploration intuitive and insightful.
- **DuckDB**: An in-process SQL OLAP database management system that excels in fast analytical queries directly on dataframes, making it a perfect complement to Polars for advanced data analysis. DuckDB helps in managing complex queries and aggregations efficiently, ensuring our application remains swift and responsive even with intricate data analysis tasks.


## Getting Started

Follow these steps to get the Country Inflation Analytics application up and running on your local machine:

### Prerequisites

Ensure you have Python installed on your system. You can download Python [here](https://www.python.org/downloads/). This project is developed with Python 3.8+, so it is recommended to use a compatible version.

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/l-ehara/analytics-project.git
   ```

2. **Navigate to the project directory**

   ```bash
   cd analytics-project
   ```

3. **Install the required dependencies**

   It's recommended to create a virtual environment before installing the dependencies to keep your project isolated from the rest of your system.

   - Create a virtual environment:

     ```bash
     python -m venv venv
     ```

   - Activate the virtual environment:

     - On Windows:
       ```bash
       .\venv\Scripts\activate
       ```
     - On Unix or MacOS:
       ```bash
       source venv/bin/activate
       ```

   - Install the dependencies:

     ```bash
     pip install -r requirements.txt
     ```

### Running the Application

With the dependencies installed, you can now run the application using Streamlit:

```bash
streamlit run mainpage.py
```

Navigate to the local web address provided in the terminal to interact with the Country Inflation Analytics application.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests with your enhancements or bug fixes.

## Acknowledgments

- Data sources: You can find more informations about the Data source [here](https://www.kaggle.com/datasets/sazidthe1/global-inflation-data)
- Streamlit Community: You can find more information about Streamlit [here](https://streamlit.io/)
- Polars Documentation: You can find more information about Polars [here](https://pola.rs/)

Thank you for visiting the my project. Dive into the data and uncover the stories behind inflation rates across the globe!
