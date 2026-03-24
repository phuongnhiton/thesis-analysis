#  French Thesis Metadata Miner (thesis.fr)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Requests](https://img.shields.io/badge/Library-Requests-red.svg)
![Regex](https://img.shields.io/badge/Logic-Regex-yellow.svg)

An end-to-end data mining pipeline designed to scrape, archive, and parse academic thesis records from the official French portal **thesis.fr**. This tool focuses on harvesting metadata for the "Lettres modernes" discipline (1965–2019).

---

##  Workflow Overview
The project operates in two distinct phases to ensure data integrity and manageable processing:

###  Phase 1: Discovery (`downloader.py`)
* Connects to the central search engine with specific filters (Date: 1965-2019, Discipline: Lettres modernes).
* Uses custom **HTTP headers** to mimic browser behavior.
* Identifies and collects unique thesis permalinks.

###  Phase 2: Harvesting & Parsing (`index.py`)
* Reads the collected links from a local registry.
* Systematically downloads the full HTML content of each thesis page.
* **Metadata Extraction (WIP):** Utilizes Regular Expressions (Regex) to extract critical academic fields:
    * **DC.creator:** The author of the thesis.
    * **Thesis Directors:** The supervisors governing the research.

## Tech Stack
| Component | Technology |
| :--- | :--- |
| **Networking** | `requests` (with timeout & status handling) |
| **Parsing** | `re` (Regular Expressions for pattern matching) |
| **Data Flow** | File-based buffering (`.txt` & `.pickle`) |
| **Encoding** | Full `UTF-8` support for French accents (é, à, è) |

##  Project Structure
```text
├── downloader.py    # Phase 1: Search and link discovery
├── index.py         # Phase 2: Content downloading and parsing
├── liens.txt        # Intermediate file storing discovered URLs
└── results/         # (Generated) Individual thesis text files
