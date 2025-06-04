# Media Metadata Manager

A powerful desktop + backend + DevOps project that extracts, stores, and manages video metadata — complete with GUI interface, logging, Dockerization, CI/CD, and monitoring.

---

## Project Overview

The **Media Metadata Manager** is a comprehensive, production-ready pipeline that allows users to:

- Extract metadata from YouTube videos
- Store it in a local SQLite database
- View, search, delete, and download videos using a **Tkinter GUI**
- Automatically log user actions with a **rotating logging system**
- Dockerize the entire system for portability
- Monitor metrics using **Prometheus & Grafana**
- Build and test via **GitHub Actions CI/CD pipeline**

This project demonstrates an end-to-end understanding of application development, DevOpsification, and observability.

---

## Tech Stack

| Layer        | Technology Used            |
|-------------|-----------------------------|
| GUI         | Python Tkinter              |
| Backend     | SQLite, yt_dlp              |
| Logging     | Loguru (with rotation)      |
| CI/CD       | GitHub Actions              |
| Container   | Docker                      |
| Monitoring  | Prometheus + Grafana        |
| Scripting   | Python 3.x                  |

---

## Features

- **Video Metadata Extraction** — using `yt_dlp`, supports duration, format, and URL parsing
- **SQLite Database Storage** — persistent, light-weight, and fast
- **Beautiful Tkinter GUI** — search, delete, download, and clear video entries
- **Logging System** — rotating logs with compression using `loguru`
- **Dockerized App** — app + monitoring ready-to-run in containers
- **Prometheus Metrics** — custom `/metrics` endpoint exporting Python-based counters
- **Grafana Dashboards** — real-time visual metrics
- **CI/CD Integration** — GitHub Actions pipeline for testing/building
- **Clean Project Structure** — Modularized into folders: `metadata`, `Logging`, `utils`, `GUI`, etc.

---

## Project Structure

```
media-metadata-manager/
│
├── metadata/               # Core logic for fetch, delete, and download
├── utils/                  # Custom utilities like Prometheus metrics & logger
├── GUI/                    # Tkinter frontend interface
├── Logging/                # Log storage (auto-created)
├── .github/workflows/      # GitHub Actions CI pipeline
├── prometheus.yml          # Prometheus config file
├── Dockerfile              # Container instructions
├── README.md               # This file
├── requirements.txt        # Python dependencies
└── main.py                 # Entry-point script (GUI launcher)
```

---

## Docker Instructions

### Build the Docker Image
```bash
docker build -t metadata-manager .
```

### Run the Container
```bash
docker run -it metadata-manager
```

---

## Monitoring Setup

### Start Prometheus
```bash
docker run -d   --name prometheus   -p 9090:9090   -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml   prom/prometheus
```

### Expose Python Metrics
```bash
python3 utils/metrics_exporter.py
# Then open http://localhost:8000/metrics
```

### Connect Prometheus to Scrape `/metrics`
Edit your `prometheus.yml` to add:

```yaml
- job_name: 'python-metrics'
  static_configs:
    - targets: ['host.docker.internal:8000']
```

---

## GitHub Actions CI/CD

GitHub Actions pipeline automatically runs on every push to:

- Install dependencies
- Run test script (if added)
- Build Docker image

Path: `.github/workflows/ci.yml`

---

## Screenshots (optional)

> ![image](https://github.com/user-attachments/assets/a9129be8-c1df-4e09-bc23-ddf6d645979f)

> ![image](https://github.com/user-attachments/assets/3b47814b-3b3c-499e-959e-9053f3ac9013)

---

## Future Enhancements

- Web dashboard using Flask/FastAPI (postponed)
- DevSecOps integration (planned)
- Email notifications on download completion (optional)

---

## Author Notes

This project reflects real-world DevOps integration applied to a Python desktop tool. A perfect blend of:

- GUI app design
- Backend database logic
- Logging & Monitoring
- Docker & CI/CD

---

