## MYR Exchange Rate Analysis

This repository contains Python code for analyzing exchange rate data and visualizing the percent change in exchange rates over different years.

### Dataset Source

https://data.gov.my/data-catalogue/exchangerates

### Prerequisites
- Python 3.1x
- Pandas
- Matplotlib

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/myr-exchange-rate-analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd myr-exchange-rate-analysis
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. **Data Preparation**:
   - Place your exchange rate data in CSV format in the `data` directory.

2. **Running the Code**:
   - Run the Python script `app.py`:
     ```bash
     python app.py
     ```

3. **Interpreting the Results**:
   - The script will generate visualizations showing the percent change in exchange rates for the years 2022, 2023, and 2024.
   - Each subplot displays the percent change for a specific year, and the final subplot shows the trend of percent change over the three-year period.
   - Text annotations are added to display the percent change values on each bar in the subplots for the years 2022, 2023, and 2024.


### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

