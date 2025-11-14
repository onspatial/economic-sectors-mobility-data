# Economic Sectors Mobility Data

This repository provides a comprehensive dataset detailing human mobility patterns across various economic sectors in the United States, spanning from **January 7, 2019**, to **January 2, 2023**. The dataset, aggregated weekly, is derived from foot traffic data collected via mobile devices. It includes key metrics such as:

- Total visitors
- Dwell time
- Travel distance

covering approximately **12 million Points of Interest (POIs)** categorized under the **North American Industry Classification System (NAICS)**.

### Highlights

The dataset focuses particularly on public locations, enabling valuable insights into:

- Economic activity
- Consumer behavior
- Mobility changes during significant events (e.g., COVID-19 pandemic)

Researchers can leverage this dataset to:

- Investigate sector-specific trends
- Understand spatial interaction dynamics
- Support decision-making in urban planning and public health initiatives

All data have been anonymized to protect individual privacy.

## Repository Structure

```
.
├── code/
│   ├── data.py                # Primary data loading and preprocessing
│   ├── dataset.ipynb          # generating the dataset
│   ├── validation.py          # Data validation scripts
│   └── utils/
│       ├── data_structure/
│       │   ├── dataframe.py
│       │   ├── dict.py
│       │   └── list.py
│       ├── files/
│       │   ├── basics.py
│       │   ├── check.py
│       │   ├── compress.py
│       │   ├── csv.py
│       │   ├── download.py
│       │   ├── gz.py
│       │   ├── json.py
│       │   ├── lines.py
│       │   ├── log.py
│       │   ├── path.py
│       │   ├── search.py
│       │   ├── text.py
│       │   └── zip.py
│       ├── string/
│       │   ├── match.py
│       │   ├── print.py
│       │   └── time.py
│       ├── constants.py
│       ├── loops.py
│       └── dewey.py
├── data/
│   └── info.txt               # Dataset information
└── figs/                      # placeholder for generated figures
```

## Environment Setup

dependencies:

- Python 3.12.9
- pandas==2.2.2
- matplotlib==3.8.4

```bash
pip install pandas==2.2.2 matplotlib==3.8.4
```

Operating System: Fedora Linux 40

## License

This dataset is licensed under the terms detailed in the [LICENSE](LICENSE) file.

---

For further information, questions, or contributions, please use the repository's issue tracker or contact the maintainer directly.

## Results for Smaller Regions

Results for smaller regions can be generated using the code in the `code/` directory. Follow the steps below:

1. Set the `division` variable in `data.py` to the desired region (for example, `custom_region1`).
2. Add an `elif` block for the custom region:
   ```python
   elif which == "custom_region1":
       division_codes = ("130", "131", "132")  # Example FIPS codes for custom region 1
   ```
3. Use `data-parallel.sh` or `data-serial.sh` to generate the data for the custom region.
4. Run `dataset.ipynb` to generate the dataset, plots, correlations, and summary statistics for the selected region.

Below we show example plots for Census Divisions 1 through 9.

### Census Fulton County GA

**Distance Mean Over Time for Fulton County GA**  
![Census Fulton County GA: distance mean](results/GA_FULTON/figs/line-distance-mean.png)

**Visitors Mean Over Time for Fulton County GA**  
![Census Fulton County GA: visitors mean](results/d5/figs/line-visitors-mean.png)

**Dwell Time Mean Over Time for Fulton County GA**  
![Census Fulton County GA: dwell mean](results/GA_FULTON/figs/line-dwell-mean.png)

### Census Division 1

**Distance Mean Over Time for Division 1**  
![Census Division 1: distance mean](results/d1/figs/line-distance-mean.png)

**Visitors Mean Over Time for Division 1**  
![Census Division 1: visitors mean](results/d1/figs/line-visitors-mean.png)

**Dwell Time Mean Over Time for Division 1**  
![Census Division 1: dwell mean](results/d1/figs/line-dwell-mean.png)

### Census Division 2

**Distance Mean Over Time for Division 2**  
![Census Division 2: distance mean](results/d2/figs/line-distance-mean.png)

**Visitors Mean Over Time for Division 2**  
![Census Division 2: visitors mean](results/d2/figs/line-visitors-mean.png)

**Dwell Time Mean Over Time for Division 2**  
![Census Division 2: dwell mean](results/d2/figs/line-dwell-mean.png)

### Census Division 3

**Distance Mean Over Time for Division 3**  
![Census Division 3: distance mean](results/d3/figs/line-distance-mean.png)

**Visitors Mean Over Time for Division 3**  
![Census Division 3: visitors mean](results/d3/figs/line-visitors-mean.png)

**Dwell Time Mean Over Time for Division 3**  
![Census Division 3: dwell mean](results/d3/figs/line-dwell-mean.png)

### Census Division 4

**Distance Mean Over Time for Division 4**  
![Census Division 4: distance mean](results/d4/figs/line-distance-mean.png)

**Visitors Mean Over Time for Division 4**  
![Census Division 4: visitors mean](results/d4/figs/line-visitors-mean.png)

**Dwell Time Mean Over Time for Division 4**  
![Census Division 4: dwell mean](results/d4/figs/line-dwell-mean.png)

### Census Division 5

**Distance Mean Over Time for Division 5**  
![Census Division 5: distance mean](results/d5/figs/line-distance-mean.png)

**Visitors Mean Over Time for Division 5**  
![Census Division 5: visitors mean](results/d5/figs/line-visitors-mean.png)

**Dwell Time Mean Over Time for Division 5**  
![Census Division 5: dwell mean](results/d5/figs/line-dwell-mean.png)

### Census Division 6

**Distance Mean Over Time for Division 6**  
![Census Division 6: distance mean](results/d6/figs/line-distance-mean.png)

**Visitors Mean Over Time for Division 6**  
![Census Division 6: visitors mean](results/d6/figs/line-visitors-mean.png)

**Dwell Time Mean Over Time for Division 6**  
![Census Division 6: dwell mean](results/d6/figs/line-dwell-mean.png)

### Census Division 7

**Distance Mean Over Time for Division 7**  
![Census Division 7: distance mean](results/d7/figs/line-distance-mean.png)

**Visitors Mean Over Time for Division 7**  
![Census Division 7: visitors mean](results/d7/figs/line-visitors-mean.png)

**Dwell Time Mean Over Time for Division 7**  
![Census Division 7: dwell mean](results/d7/figs/line-dwell-mean.png)

### Census Division 8

**Distance Mean Over Time for Division 8**  
![Census Division 8: distance mean](results/d8/figs/line-distance-mean.png)

**Visitors Mean Over Time for Division 8**  
![Census Division 8: visitors mean](results/d8/figs/line-visitors-mean.png)

**Dwell Time Mean Over Time for Division 8**  
![Census Division 8: dwell mean](results/d8/figs/line-dwell-mean.png)

### Census Division 9

**Distance Mean Over Time for Division 9**  
![Census Division 9: distance mean](results/d9/figs/line-distance-mean.png)

**Visitors Mean Over Time for Division 9**  
![Census Division 9: visitors mean](results/d9/figs/line-visitors-mean.png)

**Dwell Time Mean Over Time for Division 9**  
![Census Division 9: dwell mean](results/d9/figs/line-dwell-mean.png)
