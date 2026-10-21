# PM2.5 Air Quality Prediction

An end-to-end project for predicting PM2.5 air quality from AirQo sensor data. The workflow is organized as six Jupyter notebook stages, from data preparation and exploratory analysis through modeling, forecasting, monitoring, and deployment.

## Project layout

- `notebooks/Step1_Data_Preparation.ipynb` - clean and prepare the sensor data
- `notebooks/Step2_EDA.ipynb` - explore the prepared data
- `notebooks/Step3_Modeling.ipynb` - train and evaluate prediction models
- `notebooks/Step4_Forecasting.ipynb` - generate forecasts
- `notebooks/Step5_Monitoring.ipynb` - monitor model and data behavior
- `notebooks/Step6_Deployment.ipynb` - prepare the deployment stage
- `src/aq_common.py` - shared paths, data loading, feature engineering, and plotting helpers
- `run_all.py` - execute the six notebook stages in sequence
- `Sensor Data Jan - July 2026.csv` - input sensor dataset

Generated files are written under `outputs/`.

## Run the project

Use Python with the project dependencies installed, including Jupyter, NumPy, pandas, scikit-learn, Matplotlib, LightGBM, Evidently, and FastAPI.

From the project root, run all stages with:

```bash
python run_all.py
```

Alternatively, open and run the notebooks in `notebooks/` in order. The input CSV can be placed in the project root or in a `data/` directory.
