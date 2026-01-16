#!/usr/bin/env python3
"""
Vehicle Health Application Generator
Uses the SDV GenAI Framework to generate a complete vehicle health monitoring application
"""

import sys
import os
from pathlib import Path

# Add framework to path
sys.path.insert(0, str(Path(__file__).parent.parent / "framework"))

from framework import SDVOrchestrator, OTAManager


def main():
    """Generate Vehicle Health SDV Application"""
    
    # Problem Statement for Vehicle Health Monitoring
    problem_statement = """
    Problem Statement: Vehicle Health & Diagnostics System
    
    Develop a comprehensive vehicle health monitoring and diagnostic system for 
    Software-Defined Vehicles (SDV) supporting ICE, Hybrid, and EV variants.
    
    Requirements:
    1. Real-time vehicle data collection (speed, battery SoC, tyre pressure, gear, 
       throttle/brake, steering angle, EV range)
    2. Continuous diagnostics and fault detection
    3. Trend analysis and predictive analytics
    4. Early fault prediction using ML
    5. OTA capability for service injection
    6. Vehicle variant awareness (ICE/Hybrid/EV)
    7. ASPICE Level 2 compliance
    8. MISRA-C++:2023 compliance for safety-critical components
    9. ISO 26262 ASIL-B safety requirements
    
    Services Required:
    - VehicleDataService (C++) - Data collection and streaming
    - DiagnosticsService (C++) - Fault detection and diagnostics
    - AnalyticsService (Rust) - Trend analysis and reporting
    - PredictionService (Rust) - ML-based failure prediction
    - OTAFeatureService (C++) - Dynamic service injection
    """
    
    print("\n" + "="*70)
    print("VisCar SDV GenAI Generator")
    print("Vehicle Health & Diagnostics Application")
    print("="*70 + "\n")
    
    # Initialize orchestrator
    orchestrator = SDVOrchestrator(output_dir="applications")
    
    # Generate application
    print("Starting application generation...")
    result = orchestrator.generate_application(
        problem_statement=problem_statement,
        app_name="vehicle_health"
    )
    
    print("\n" + "="*70)
    print("Application Generation Summary")
    print("="*70)
    print(f"Application: {result['app_name']}")
    print(f"Output Directory: {result['output_dir']}")
    print(f"Services Generated: {len(result['generated_services'])}")
    print("\nGenerated Services:")
    for service in result['generated_services']:
        print(f"  • {service['name']} ({service['language']})")
    print("\nCompliance:")
    compliance = result['compliance_report']
    print(f"  • ASPICE Level: {compliance['aspice_level']}")
    print(f"  • MISRA Compliance: {compliance['misra_compliance']}")
    print(f"  • ISO 26262 ASIL: {compliance['iso26262_asil']}")
    print(f"  • Test Coverage: {compliance['test_coverage']}")
    print("="*70 + "\n")
    
    # Demonstrate OTA Service Injection
    print("\n" + "="*70)
    print("Demonstrating OTA Service Injection")
    print("="*70 + "\n")
    
    # Define new OTA service
    battery_degradation_service = {
        "name": "BatteryDegradationService",
        "language": "rust",
        "version": "1.0.0",
        "interfaces": [
            "predict_degradation",
            "estimate_remaining_life",
            "get_health_index"
        ],
        "dependencies": ["VehicleDataService", "AnalyticsService"],
        "data_model": ["BatteryHealthData", "DegradationModel"]
    }
    
    # Inject via OTA
    ota_result = orchestrator.inject_ota_service(
        app_name="vehicle_health",
        service_definition=battery_degradation_service
    )
    
    print(f"\nOTA Injection Result:")
    print(f"  • Service: {ota_result['service_name']}")
    print(f"  • Status: {ota_result['status'].upper()}")
    print(f"  • Timestamp: {ota_result['timestamp']}")
    
    print("\n" + "="*70)
    print("✓ Vehicle Health Application Generated Successfully!")
    print("="*70 + "\n")
    
    return result


if __name__ == "__main__":
    try:
        result = main()
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
