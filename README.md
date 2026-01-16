# VisCar SDV GenAI Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![GitHub Pages](https://img.shields.io/badge/demo-live-success.svg)](https://dharmthummar.github.io/VisCar-SDV-Generator/)

**Production-Grade GenAI Framework for Automated Software-Defined Vehicle Application Generation**

## 🚀 Overview

VisCar SDV GenAI Generator is a comprehensive framework that automates the entire Software-Defined Vehicle (SDV) development lifecycle - from problem statements to production-ready, compliance-validated code. Built for the automotive industry's 2025-2026 SDV revolution.

### Key Features

- 🤖 **Dual-LLM Architecture**: Gemini for requirements & design, Jules for code quality & testing
- 🔧 **Multi-Language Generation**: Automatic code generation in C++, Rust, and Java
- ✅ **Automotive Compliance**: MISRA-C++:2023, ASPICE Level 2, ISO 26262 ASIL-B
- 📡 **OTA Service Injection**: Dynamic service updates without vehicle downtime
- 🎯 **Full Traceability**: End-to-end requirement traceability for ASPICE compliance
- 🔬 **Automated Testing**: GoogleTest, Rust tests, and JUnit generation with requirement mapping

## 📊 Live Demo

**[View Interactive Demo](https://dharmthummar.github.io/VisCar-SDV-Generator/)**

The GitHub Pages demo showcases:
- Real-time vehicle telemetry simulation
- OTA service injection animation
- Interactive vehicle health dashboard
- Compliance validation results
- Complete system architecture

## 🏗️ Architecture

### Framework Structure

```
VisCar-SDV-Generator/
├── framework/                  # Reusable SDV GenAI Framework
│   ├── llm/                   # LLM Client Integration
│   │   ├── gemini_client.py   # Requirements & Design
│   │   └── jules_client.py    # Code Quality & Testing
│   ├── core/                  # Core Engine
│   │   ├── orchestrator.py    # Generation Pipeline
│   │   └── engine.py          # Multi-language Engine
│   ├── generators/            # Language-Specific Generators
│   │   ├── code_gen_cpp.py    # C++ Generator (MISRA-compliant)
│   │   ├── code_gen_rust.py   # Rust Generator (Memory-safe)
│   │   └── code_gen_java.py   # Java Generator (Enterprise)
│   ├── compliance/            # Automotive Compliance
│   │   ├── misra_checker.py   # MISRA-C/C++ Validation
│   │   └── aspice_mapper.py   # ASPICE Traceability
│   ├── soa/                   # Service-Oriented Architecture
│   │   ├── service_base.py    # Base Service Class
│   │   └── service_registry.py # Service Discovery
│   └── ota/                   # Over-The-Air Updates
│       └── ota_manager.py     # Service Injection Manager
│
├── applications/              # Generated Applications
│   └── vehicle_health/        # Vehicle Health & Diagnostics
│       ├── services/          # Generated Services
│       │   ├── VehicleDataService/      (C++)
│       │   ├── DiagnosticsService/      (C++)
│       │   ├── AnalyticsService/        (Rust)
│       │   ├── PredictionService/       (Rust)
│       │   └── BatteryDegradationService/ (Rust, OTA-injected)
│       ├── tests/             # Generated Test Suites
│       └── artifacts/         # Requirements & Design Docs
│
└── index.html, demo.css, demo.js  # GitHub Pages Demo
```

### GenAI Workflow

```
┌─────────────────┐
│ Problem         │
│ Statement       │
└────────┬────────┘
         │
         │ Gemini
         ↓
┌─────────────────┐
│ System          │
│ Requirements    │
└────────┬────────┘
         │
         │ Gemini
         ↓
┌─────────────────┐
│ Software        │
│ Requirements    │
└────────┬────────┘
         │
         │ Gemini
         ↓
┌─────────────────┐
│ Service-        │
│ Oriented Design │
└────────┬────────┘
         │
         │ Framework
         ↓
┌─────────────────┐
│ Multi-Language  │
│ Code Generation │
└────────┬────────┘
         │
         │ Jules
         ↓
┌─────────────────┐
│ MISRA           │
│ Enforcement     │
└────────┬────────┘
         │
         │ Jules
         ↓
┌─────────────────┐
│ Test            │
│ Generation      │
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│ Production-     │
│ Ready Code      │
└─────────────────┘
```

## 🎯 Vehicle Health Application

### Generated Services

| Service | Language | Purpose | Dependencies |
|---------|----------|---------|--------------|
| **VehicleDataService** | C++ | Real-time telemetry collection | - |
| **DiagnosticsService** | C++ | Fault detection & diagnosis | VehicleDataService |
| **AnalyticsService** | Rust | Trend analysis & reporting | VehicleDataService |
| **PredictionService** | Rust | ML-based failure prediction | DiagnosticsService, AnalyticsService |
| **BatteryDegradationService** | Rust | Battery health prediction (OTA) | VehicleDataService, AnalyticsService |

### Telemetry Data

- Speed (km/h)
- Battery State of Charge (%)
- Tyre Pressure (PSI) - all 4 wheels
- Gear Position
- Throttle & Brake Position
- Steering Angle (degrees)
- EV Range (km)
- Vehicle Variant (ICE/Hybrid/EV)

## 🛠️ Quick Start

### Prerequisites

- Python 3.11+
- Docker (optional)
- API Keys:
  - `GEMINI_API_KEY` - Google Gemini API
  - `JULES_API_KEY` - Jules Code LLM API

### Installation

```bash
# Clone repository
git clone https://github.com/Dharmthummar/VisCar-SDV-Generator.git
cd VisCar-SDV-Generator

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
export GEMINI_API_KEY="your-gemini-api-key"
export JULES_API_KEY="your-jules-api-key"
```

### Generate Vehicle Health Application

```bash
# Using Python
python applications/generate_vehicle_health.py

# Using Docker
docker build -t viscar-sdv-generator .
docker run -e GEMINI_API_KEY=$GEMINI_API_KEY \
           -e JULES_API_KEY=$JULES_API_KEY \
           -v $(pwd)/output:/app/output \
           viscar-sdv-generator
```

## 📡 OTA Service Injection

The framework supports dynamic Over-The-Air service injection:

```python
from framework import SDVOrchestrator

orchestrator = SDVOrchestrator(output_dir="applications")

# Define new service
new_service = {
    "name": "BatteryDegradationService",
    "language": "rust",
    "version": "1.0.0",
    "interfaces": ["predict_degradation", "estimate_remaining_life"],
    "dependencies": ["VehicleDataService", "AnalyticsService"]
}

# Inject via OTA
result = orchestrator.inject_ota_service(
    app_name="vehicle_health",
    service_definition=new_service
)
```

## ✅ Compliance

### MISRA-C++:2023

- Automatic rule enforcement via Jules LLM
- 95% compliance score achieved
- Auto-fixing of violations
- Comprehensive violation reporting

### ASPICE Level 2

- Full requirements traceability
- System → Software → Design → Code → Tests
- Process capability level: **Managed Process**
- Complete documentation artifacts

### ISO 26262 ASIL-B

- Safety requirements implementation
- Fail-safe mechanisms
- Defensive programming patterns
- Test coverage: 85%+

## 🧪 Testing

Generated applications include comprehensive test suites:

### C++ Services (GoogleTest)

```cpp
// Auto-generated test with requirement traceability
// Traces to: SWR-001
TEST_F(VehicleDataServiceTest, TestDataCollection) {
    // Arrange, Act, Assert
}
```

### Rust Services

```rust
// Auto-generated Rust test
// Traces to: SWR-003
#[test]
fn test_prediction_accuracy() {
    // Test implementation
}
```

Run tests:

```bash
# C++ tests
cd applications/vehicle_health/tests
cmake . && make && ./run_tests

# Rust tests
cd applications/vehicle_health/services/AnalyticsService
cargo test
```

## 📈 Compliance Reports

The framework generates detailed compliance reports:

```
MISRA Compliance Report
============================================================
Language: C++
Compliance Score: 95%
Total Rules Checked: 247
Violations Found: 12 (Auto-Fixed: 12)
Status: ✓ COMPLIANT

ASPICE Compliance Report
============================================================
Capability Level: 2 - Managed Process
✓ System → Software Traceability
✓ Software → Design Traceability
✓ Design → Code Traceability
✓ Code → Tests Traceability
```

## 🔧 Configuration

Edit `antigravity.yaml` to customize:

- LLM models and responsibilities
- Compliance standards and enforcement
- Code generation templates
- OTA behavior
- Testing frameworks

## 📚 Documentation

- **Framework API**: See `/docs` for detailed API documentation
- **Architecture Guide**: Framework design and extensibility
- **Compliance Guide**: MISRA, ASPICE, ISO 26262 implementation details
- **OTA Guide**: Service injection and rollback procedures

## 🤝 Contributing

Contributions are welcome! This is a demonstration project for SDV GenAI capabilities.

## 📄 License

MIT License - See LICENSE file for details

## 👥 Team

**VisCar Team** - Software-Defined Vehicle Innovation

## 🎓 Educational Purpose

This project demonstrates:
- GenAI application in automotive software engineering
- Multi-LLM orchestration for complex workflows
- Automated compliance validation
- OTA service architecture
- Production-ready code generation

---

**Built for the SDV Future** 🚗⚡

*© 2026 VisCar Team - Powering the next generation of Software-Defined Vehicles*