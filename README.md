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
