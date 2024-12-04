import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
#im King of coding
# Function to upload CSV file and display summary statistics
@st.cache_data  # Cache the loaded data
def load_data(uploaded_file):
    # Load only a portion of the data for faster initial loading
    return pd.read_csv(uploaded_file, nrows=10000)  # Load only first 10,000 rows

def upload_and_analyze_csv():
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        # Show a spinner while loading data
        with st.spinner("Loading data..."):
            try:
                # Load the CSV file into a DataFrame
                df = load_data(uploaded_file)

                # Display the number of rows loaded
                st.success(f"Loaded {len(df)} rows successfully!")

                # Display basic statistics for numeric columns
                st.subheader("Summary Statistics")
                st.write(df.describe())

                # Display information about the dataset
                st.subheader("Data Information")
                st.write(df.info())

                # Display only a sample of 100 rows initially for large datasets
                st.subheader("Sample Data")
                st.dataframe(df.sample(n=100) if len(df) > 100 else df)

                # Check for numeric columns to plot histograms
                #
                numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
                if numeric_cols:
                    for col in numeric_cols:
                        plt.figure(figsize=(10, 5))
                        df[col].hist(bins=10)
                        plt.title(f'Distribution of {col}')
                        plt.xlabel(col)
                        plt.ylabel('Frequency')
                        st.pyplot(plt)

                # Check for categorical columns to plot bar charts
                categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
                if categorical_cols:
                    for col in categorical_cols:
                        plt.figure(figsize=(10, 5))
                        df[col].value_counts().plot(kind='bar')
                        plt.title(f'Count of Unique Values in {col}')
                        plt.xlabel(col)
                        plt.ylabel('Count')
                        st.pyplot(plt)

            except Exception as e:
                st.error(f"An error occurred: {e}")

# Streamlit app configuration
st.title("CSV File Upload and Analysis Tool")

# Introduction about Vinod and the project
st.markdown("""
### Hey, I'm Vinod! 👋

Welcome to my CSV File Upload and Analysis Tool! This project allows you to easily upload any CSV file and get insightful statistics and visualizations. Here’s what you can expect:

- 📊 **Dynamic Analysis**: Automatically analyzes any dataset without needing specific column names.
- 📈 **Visualizations**: Generates histograms for numeric data and bar charts for categorical data.
- 📋 **Summary Statistics**: Displays comprehensive statistics to help you understand your data better.
- 🚀 **User-Friendly Interface**: Built using Streamlit for a smooth user experience.

Feel free to upload your CSV files and explore the data! 
""")

upload_and_analyze_csv()