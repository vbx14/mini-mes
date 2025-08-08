# mini-MES: Flask-based Simulation of Apriso Modules (Production, Quality, Warehouse)

- A minimal Manufacturing Execution System (MES) simulation in Flask, designed to emulate Apriso modules for Production, Quality Inspection, and Warehouse Inventory, with monitoring using Prometheus and Grafana. 
- Built for simulating basic MES functionality with production-grade monitoring hooks. Ideal for backend prototyping and IoT integrations. 

## Project Structure

```
mini-mes/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models/
│   │   ├── job.py
│   │   ├── inspection.py
│   │   └── inventory.py
│   ├── routes/
│   │   ├── production.py
│   │   ├── quality.py
│   │   └── warehouse.py
│   └── utils/
│       └── metrics.py
├── static/
│   └── index.html
├── grafana/
│   └── dashboard.json
├── prometheus/
│   └── prometheus.yml
├──screenshots
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── run.py
```

## Setup

### 1. Clone and Set Up Environment
```
git clone <repo-url>
cd mini-mes
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Create and Initialize Database
```
python run.py  # First run creates mes.db and initializes tables
```

### 3. Start App Locally
```
python run.py  # Runs on http://localhost:5000
```

## API Routes

### Production
- `POST /create` – Create a job
- `GET /list` – List all jobs

### Quality
- `POST /quality/log` – Log inspection result
- `GET /quality/list` – List inspections

### Warehouse
- `POST /warehouse/update` – Add inventory
- `GET /warehouse/list` – List inventory items

| Module       | Method | Endpoint              | Description                  |
|--------------|--------|-----------------------|------------------------------|
| Production   | POST   | `/create`             | Create a new job             |
| Production   | GET    | `/list`               | List all jobs                |
| Quality      | POST   | `/quality/log`        | Log a quality inspection     |
| Quality      | GET    | `/quality/list`       | List all inspection records  |
| Warehouse    | POST   | `/warehouse/update`   | Update/add inventory item    |
| Warehouse    | GET    | `/warehouse/list`     | List all inventory entries   |
| Metrics      | GET    | `/metrics`            | Expose Prometheus metrics    |

## Prometheus Metrics

- Visit: `http://localhost:5000/metrics`
- Example counters:
  - `jobs_created_total`
  - `inspections_logged_total`
  - `inventory_updates_total`

### Example
```
curl http://localhost:5000/list
curl http://localhost:5000/quality/list
curl http://localhost:5000/warehouse/list
```

## Monitoring with Grafana + Prometheus

### 1. Start Services
```
docker-compose up --build
```

### 2. Access Dashboards
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (default login: `admin` / `admin`)

### 3. Sample Prometheus Queries
```prometheus
jobs_created_total
inspections_logged_total
inventory_updates_total
```

## Sample Payloads

### Create Job
```json
{
  "job_name": "Test Job"
}
```

### Log Inspection
```json
{
  "job_id": 1,
  "result": "Pass",
  "notes": "All specs met"
}
```

### Update Inventory
```json
{
  "item_name": "Raw Material A",
  "quantity": 50
}
```

## Screenshots


