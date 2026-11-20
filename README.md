# Solar & Wind Energy Transition vs. Grid Carbon Emissions (2020–2026)

A Class X Artificial Intelligence (417) capstone project exploring the relationship between renewable energy generation and grid CO₂ emissions in an institutional and urban smart-grid cluster in Bengaluru.

**Project team:** Aryan Bhose and Aarush Yadav  
**School:** Delhi Public School Bangalore North  
**Academic session:** 2026–2027  
**SDG alignment:** SDG 7 (Affordable and Clean Energy) and SDG 13 (Climate Action)

## Open the dashboard

The repository's `index.html` is a static, responsive dashboard. After enabling GitHub Pages, it can be opened directly in a browser. It uses Chart.js from a CDN, so charts require an internet connection.

## Run the Python analysis

Requires Python 3.10 or newer.

```bash
python -m venv .venv
# Windows:
.venv\\Scripts\\activate
# macOS / Linux:
source .venv/bin/activate

pip install -r requirements.txt
python src/sdg_energy_analysis.py
```

The script reads `data/energy_emissions_2020_2026.csv`, derives total renewable generation, total energy and renewable share, prints summary metrics, and saves two charts plus a processed CSV in `outputs/`.

## Repository structure

```text
.
├── .github/workflows/pages.yml
├── data/
│   └── energy_emissions_2020_2026.csv
├── outputs/
├── src/
│   └── sdg_energy_analysis.py
├── index.html
├── requirements.txt
└── README.md
```

## Key findings from the report

- Solar generation increases from 420 MWh (2020) to 2,050 MWh (2026), a reported growth of 388.1%.
- Wind generation increases from 310 MWh to 830 MWh.
- Combined renewable generation first exceeds coal-based grid energy in 2024: 1,950 MWh versus 1,800 MWh.
- Renewable share rises from 22.81% to 71.11%.
- CO₂ emissions decline from 2,180 to 1,015 metric tons, a reported reduction of 53.4%.
- Pearson correlation between total renewable generation and CO₂ emissions is reported as approximately -0.9988.

## Data and interpretation note

The CSV values are transcribed from the team's project report (Section 4, pages 6–7; source code and console output, pages 8–11). The report describes the data as covering an institutional and urban smart-grid cluster in Bengaluru. It does not include an independently downloadable raw dataset or a detailed measurement methodology. Therefore, this repository labels the figures as **project-study data** and does not present them as verified official citywide statistics.

A strong negative correlation describes an association; it does not by itself prove causation. The two trend series also use different units, so the browser dashboard places them on separate vertical axes.

## References listed in the project report

1. Central Board of Secondary Education (CBSE), Artificial Intelligence Curriculum (Subject Code 417), Class X Guidelines.
2. United Nations Department of Economic and Social Affairs, Sustainable Development Goals (SDG 7 and SDG 13).
3. Hunter, J. D. (2007). “Matplotlib: A 2D Graphics Environment.” *Computing in Science & Engineering*, 9(3), 90–95.
4. McKinney, W. (2010). “Data Structures for Statistical Computing in Python (pandas).” *Proceedings of the 9th Python in Science Conference*.
5. Ministry of New and Renewable Energy (MNRE) and Karnataka Renewable Energy Development Ltd. (KREDL), Solar Policy Reports.

## Publish with GitHub Pages

1. Create a new **public** repository on GitHub, for example `solar-wind-energy-analysis`.
2. Upload all files and folders from this project, keeping their folder structure.
3. Open **Settings → Pages**.
4. Under **Build and deployment**, choose **GitHub Actions**.
5. The included workflow deploys `index.html` automatically when you push to the `main` branch.
6. Your site will appear at `https://YOUR-USERNAME.github.io/solar-wind-energy-analysis/`.

The exact URL depends on your GitHub username and repository name.
