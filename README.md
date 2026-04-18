# 📊 Interactive Sales Executive Dashboard

## Project Overview
This project is an end-to-end data visualization solution designed to provide both **High-Level Executive Summaries** and **Granular Product Deep-Dives**. By combining the statistical power of **Seaborn** with the interactivity of **Plotly**, this dashboard allows users to identify broad sales trends and investigate specific product performance with a single click.

## 🎥 Dashboard Preview
![Sales Dashboard Demo](dashboard_demo.gif)

## 🚀 Key Features
* **Global KPI Metrics:** Real-time calculation of Total Revenue, Total Quantity, and Average Transaction Value.
* **Fixed Strategic Overview:** Static Seaborn visualizations showing Revenue by Category and Shop Performance that remain consistent for baseline comparison.
* **Interactive Deep-Dive Section:** Custom-built button navigation that filters specific Plotly and Seaborn visuals for a selected product category.
* **Drill-Down Capabilities:** Interactive Plotly scatter plots with hover data for detailed product-level analysis.

## 🛠️ Technical Skills Acquired
* **Seaborn Mastery:** Advanced use of `subplots` to create multi-plot grids and complex statistical charts (Box plots, Violin plots, and Heatmaps).
* **Interactive Plotting:** Implementation of **Plotly Express** for dynamic scatter plots to visualize hierarchical data.
* **Dashboard Architecture:** Building a stateful web application using **Streamlit**, managing "memory" with `st.session_state`, and optimizing performance with `@st.cache_data`.
* **UI/UX Design:** Designing a logical flow from "Global Overview" to "Local Analysis" without the need for cluttered sidebars.

## 💻 Development Workflow & AI Collaboration
In the spirit of professional transparency and modern development practices, this project was built using a **Pair Programming** approach with AI:

1.  **Architecture & Logic:** I designed the dashboard's hierarchy, determined the relationship between fixed and filtered visuals, and established the data flow logic.
2.  **Statistical Analysis:** I manually performed the initial data exploration and statistical calculations using Pandas and Seaborn in `dashboard.ipynb`.
3.  **Frontend Implementation:** I collaborated with an AI assistant to rapidly translate my architectural requirements into Streamlit code. Specifically, I provided detailed prompts for the button-trigger logic and session-state management to ensure a smooth user experience.
4.  **Problem Solving:** I used AI to debug complex layout issues and version-specific Seaborn warnings, allowing me to focus on the high-level data story.

## 📂 Project Structure
* `dashboard.py`: The main Streamlit application script.
* `dashboard.ipynb`: Experimental notebook containing data cleaning and initial chart prototypes.
* `visualizations/`: A collection of high-resolution static exports (Heatmaps, Violin plots, etc.).
* `requirements.txt`: List of dependencies required to run the project.
* `dashboard_demo.gif`: A visual walkthrough of the dashboard in action.
* `sales_data.csv`: The underlying dataset for the analysis.
* `Seaborn_notes.ipynb`: Personal learning notes and library exploration.

## 🏃 How to Run
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the dashboard: `streamlit run dashboard.py`