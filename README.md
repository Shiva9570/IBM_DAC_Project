# Air Quality Analysis in Tamil Nadu

## Project Overview
This repository contains the code and resources for analyzing air quality data from monitoring stations in Tamil Nadu. The objective of this project is to gain insights into air pollution trends, identify pollution hotspots, and develop predictive models for RSPM/PM10 levels based on SO2 and NO2 levels. The analysis approach involves data cleaning, preprocessing, exploratory data analysis, visualization, and predictive modeling.

## Data Source
The air quality data used in this project is sourced from -- link .

## Project Phases
### Phase 1: Project Definition and Design Thinking
- Defined project objectives.
- Planned analysis approach and visualization techniques.

### Phase 2: Innovation
- Incorporated machine learning algorithms for predictive modeling.

### Phase 3: Development Part 1
- Loaded and preprocessed the dataset.
- Conducted exploratory data analysis.

### Phase 4: Development Part 2
- Performed air quality analysis.
- Created visualizations using Matplotlib and Seaborn.

### Phase 5: Project Documentation & Submission
- Documented the project objectives, analysis approach, and visualization techniques.
- Summarized key findings from the analysis.

## Folder Structure
- data/: Contains the raw and processed datasets.
- notebooks/: Includes Jupyter notebooks for each phase of the project.
- scripts/: Contains Python scripts for data preprocessing and modeling.
- visualizations/: Contains visualizations generated during the analysis.

## Setup Instructions
1. Clone the repository: git clone https://github.com/Shiva9570/IBM_DAC_Project.git
2. Navigate to the project directory: cd air-quality-analysis
3. Install the required Python libraries: pip install -r requirements.txt
4. Run the Jupyter notebooks or Python scripts in the notebooks/ and scripts/ directories, respectively.

## Dependencies
- Python 3.x
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn

## Contributors
- [Shibendra narayan mishra ](https://github.com/Shiva9570)
- Facult evalautor

## License
This project is licensed under the [MIT License](LICENSE).


## Code - <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Air Quality Index (AQI) in Tamil Nadu</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        canvas {
            max-width: 700px;
            margin: 0 auto;
            display: block;
        }
    </style>
</head>
<body>

<h1>Air Quality Index (AQI) in Tamil Nadu</h1>
<canvas id="aqiChart"></canvas>

<script>
    // Shadow AQI data for Tamil Nadu cities
    const cities = ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem", "Erode"];
    const aqiValues = [120, 95, 110, 85, 130, 100]; // Example AQI values

    // AQI colors based on categories
    const aqiColors = aqiValues.map(aqi => {
        if (aqi <= 50) return 'green';               // Good
        else if (aqi <= 100) return 'yellow';        // Moderate
        else if (aqi <= 150) return 'orange';        // Unhealthy for Sensitive Groups
        else if (aqi <= 200) return 'red';           // Unhealthy
        else if (aqi <= 300) return 'purple';        // Very Unhealthy
        return 'maroon';                             // Hazardous
    });

    // Create the chart
    const ctx = document.getElementById('aqiChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: cities,
            datasets: [{
                label: 'Air Quality Index (AQI)',
                data: aqiValues,
                backgroundColor: aqiColors,
                borderColor: 'black',
                borderWidth: 1
            }]
        },
        options: {
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function (context) {
                            const aqi = context.raw;
                            let category = '';
                            if (aqi <= 50) category = 'Good';
                            else if (aqi <= 100) category = 'Moderate';
                            else if (aqi <= 150) category = 'Unhealthy for Sensitive Groups';
                            else if (aqi <= 200) category = 'Unhealthy';
                            else if (aqi <= 300) category = 'Very Unhealthy';
                            else category = 'Hazardous';
                            return `${context.raw} (${category})`;
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Air Quality Index (AQI)'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Cities in Tamil Nadu'
                    }
                }
            }
        }
    });
</script>

</body>
</html>
