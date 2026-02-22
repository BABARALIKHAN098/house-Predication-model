# 🏠 House Predication Project (Upto Production)

This project provides a professional-grade House Price Prediction system built using Scikit-Learn and deployed via Streamlit. It includes a comprehensive analytics dashboard for visualizing regional housing trends.

## 🚀 Key Features

- **Dynamic Valuation**: Real-time property appraisal based on 8 key features.
- **Interactive Insights**: Market visualization tab showing price distributions and factor impacts (Area, Parking, City Tier).
- **ML Pipeline**: Uses a robust predictive model (`pipe.pkl`) capable of handling preprocessing and categorical encoding.
- **Premium UI**: Modern, responsive dashboard design with a clean user experience.

## 📁 Project Structure

```text
├── Data.csv                # Raw housing dataset
├── pipe.pkl                # Trained Scikit-Learn Model Pipeline
├── app.py                  # Main Streamlit Application
├── requirements.txt        # Project Dependencies
├── predication_house_sale.ipynb # Data Exploration Notebook
└── house_report.html       # Automated Data Profiling Report
```

## 🛠️ Installation & Setup

1. **Clone the repository** (or navigate to the folder):
   ```bash
   cd "House Predication project upto production"
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🏃 Run the Application

Execute the following command to start the web dashboard:

```bash
streamlit run app.py
```

## 📊 Dataset Features

- **Taxi_dist / Market_dist / Hospital_dist**: Distance in meters to essential services.
- **Carpet_area / Builtup_area**: Property dimensions in square feet.
- **Parking_type**: Type of parking available (Open, Covered, etc.).
- **City_type**: Categorization of the city (CAT A, B, C).
- **Rainfall**: Regional annual rainfall metrics.

## 📝 License
This project is for educational and professional demonstration purposes.
