# Analytics Data Lake – JSON to Parquet using MinIO & ClickHouse

## Overview
This project demonstrates a data-lake style analytics pipeline where raw JSON data
is converted into Parquet format, stored in object storage (MinIO), and queried
directly using ClickHouse without ingesting data into the database.

The goal is to showcase:
- Proper data normalization
- Use of columnar storage (Parquet)
- Object storage (S3-compatible MinIO)
- Query-in-place analytics using ClickHouse
- Clear schema documentation

---

## Architecture

Raw JSON Files  
→ JSON to Parquet conversion (Python)  
→ Stored in MinIO (S3-compatible storage)  
→ Queried directly from ClickHouse using S3 engine  

ClickHouse acts as the **compute layer**, while MinIO acts as the **storage layer**.

---

## Technologies Used
- Python (pandas, pyarrow)
- MinIO (local S3-compatible object storage using Docker)
- ClickHouse (analytical OLAP database)
- Docker & Docker Compose

---

## Folder Structure

analytics-data-lake/
├── data/
│ ├── raw/ # Original JSON files (source of truth)
│ └── parquet/ # Normalized Parquet datasets
├── scripts/ # JSON → Parquet, upload scripts and schema inspection scripts
├── schemas/ # Schema documentation
├── docker-compose.yml
├── requirements.txt
└── README.md


---

## Data Modeling Approach

Each JSON file represents a **logical business entity**:
- Portfolio
- Portfolio Group
- Account
- Asset
- Relationship

Paginated JSON files (accounts) are merged into a single dataset because they
represent the same entity with identical schema.

Each entity is stored as **one Parquet dataset** to enable efficient analytics.

---

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Convert JSON to Parquet:
python scripts/*.py

3. Start services:
docker-compose up -d

4. Upload Parquet files to MinIO:
python scripts/upload_parquet_to_minio.py

5. Create S3 tables in ClickHouse and run queries.

---

## Key Concepts Demonstrated
- Query-in-place analytics (no ingestion)
- Separation of storage and compute
- Columnar storage optimization
- Schema-first data design

---

## Notes
MinIO is used locally via Docker for development. The same setup can be deployed
to AWS S3 or any S3-compatible storage without changing the logic.
