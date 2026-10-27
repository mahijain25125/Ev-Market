# Electric Vehicle Market Performance & Insights

## Overview
This repository provides a comprehensive analysis of the Electric Vehicle (EV) industry. It evaluates market performance across multiple vehicle categories (hatchbacks, sedans, SUVs, electric buses, trucks, two-wheelers), battery technology adoption (LFP, NMC, NCA, Sodium-Ion, Solid-State), manufacturer performance, customer satisfaction, and sustainability impact.

## Repository Structure
```
├── Data/
│   └── ev_market_dataset.csv       # Dataset containing EV sales, battery tech, range, pricing, etc.
├── Image/
│   ├── preview.png                 # Dashboard preview screenshot
│   └── i.txt                       # Image asset details
├── Website/
│   ├── app.py                      # Flask web application
│   ├── requirements.txt            # Python dependencies
│   ├── static/                     # CSS, JavaScript & image assets
│   └── templates/                  # HTML templates
├── EV Market Performance and Insights.twbx  # Tableau Packaged Workbook
└── README.md                       # Project documentation
```

## Setup Instructions

### Tableau Dashboard
Open `EV Market Performance and Insights.twbx` using Tableau Desktop or Tableau Reader to explore interactive visualizations.

### Web Application
1. Navigate to the `Website/` directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Access the web portal at `http://127.0.0.1:5000/`.
