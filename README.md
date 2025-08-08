# mini-MES: Flask-based Simulation of DELMIA Apriso Modules (Production, Quality, Warehouse)

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

### HTML UI for MES Routes Testing
![HTML UI for API Test](https://github.com/vbx14/mini-mes/blob/b500d2ed0b5606ff879062ac8ab976059d35546d/screenshots/HTML%20UI%20for%20API%20Test.png)

### /POST Routes
![MES Routes OK Tested](https://github.com/vbx14/mini-mes/blob/b500d2ed0b5606ff879062ac8ab976059d35546d/screenshots/MES%20Routes%20OK%20Tested.png)

![MES Routes OK Tested 2](https://github.com/vbx14/mini-mes/blob/b500d2ed0b5606ff879062ac8ab976059d35546d/screenshots/MES%20Routes%20OK%20Tested%202.png)

### /GET Routes
![GET Endpoint](https://github.com/vbx14/mini-mes/blob/b500d2ed0b5606ff879062ac8ab976059d35546d/screenshots/GET%20Endpoint.png)

![GET Endpoint 2](https://github.com/vbx14/mini-mes/blob/b500d2ed0b5606ff879062ac8ab976059d35546d/screenshots/GET%20Endpoint%202.png)

### Prometheus Metrics
![Prometheus Metric](https://github.com/vbx14/mini-mes/blob/b500d2ed0b5606ff879062ac8ab976059d35546d/screenshots/Prometheus%20Metric.png)

![Prometheus Metric 2](https://github.com/vbx14/mini-mes/blob/b500d2ed0b5606ff879062ac8ab976059d35546d/screenshots/Prometheus%20Metric%202.png)

![Prometheus Metric 3](https://github.com/vbx14/mini-mes/blob/b500d2ed0b5606ff879062ac8ab976059d35546d/screenshots/Prometheus%20Metric%203.png)

![Prometheus Graph](https://github.com/vbx14/mini-mes/blob/b500d2ed0b5606ff879062ac8ab976059d35546d/screenshots/Prometheus%20Graph.png)

### Grafana Visualization 
![Grafana Metrics Visualization](https://github.com/vbx14/mini-mes/blob/b500d2ed0b5606ff879062ac8ab976059d35546d/screenshots/Grafana%20Metrics.png)


