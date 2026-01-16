# Build Instructions for Vehicle Health Services

## C++ Services

### VehicleDataService

```bash
cd applications/vehicle_health/services/VehicleDataService
mkdir build && cd build
cmake ..
make

# Run demo
./vehicle_data_demo

# Run tests (requires GoogleTest)
cd ../../tests/VehicleDataService
g++ -std=c++17 test_vehicle_data_service.cpp -lgtest -lgtest_main -pthread -o test_runner
./test_runner
```

## Rust Services

### AnalyticsService

```bash
cd applications/vehicle_health/services/AnalyticsService

# Run demo
cargo run --bin analytics_demo

# Run tests
cargo test

# Build release
cargo build --release
```

### PredictionService

```bash
cd applications/vehicle_health/services/PredictionService

# Run demo
cargo run --bin prediction_demo

# Run tests
cargo test

# Build release
cargo build --release
```

### BatteryDegradationService

```bash
cd applications/vehicle_health/services/BatteryDegradationService

# Run demo (if Cargo.toml is added)
cargo run

# Run tests
cargo test
```

## Framework

### Run Application Generator

```bash
# From repository root
python -m framework demo

# Or directly
python applications/generate_vehicle_health.py
```

### Run with specific app

```bash
python -m framework generate my_app_name
```

## Docker Build

```bash
# Build image
docker build -t viscar-sdv-generator .

# Run framework
docker run -e GEMINI_API_KEY=$GEMINI_API_KEY viscar-sdv-generator

# Run with volume mount
docker run -e GEMINI_API_KEY=$GEMINI_API_KEY \
  -v $(pwd)/output:/app/output \
  viscar-sdv-generator
```

## Example Output

### VehicleDataService Demo

```
Running telemetry simulation for 10 iterations...

Update #1:
  Speed: 73.2 km/h
  Battery: 84.5 %
  Gear: 4
  EV Range: 418.3 km
  Sensors: 6 active
```

### AnalyticsService Demo

```
Trend Analysis:
  speed: INCREASING (avg: 74.52, min/max: 60.00/98.00)
  battery_soc: DECREASING (avg: 62.45, min/max: 56.50/85.00)
  tyre_pressure: STABLE (avg: 32.12, min/max: 31.54/32.68)
```

### PredictionService Demo

```
Component: battery
  Health Score: 71.00%
  Risk Level: MEDIUM
  Confidence: 85.50%
  Recommendation: Monitor battery closely
  Predicted Failure: 45.3 days
```
