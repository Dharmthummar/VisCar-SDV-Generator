#!/usr/bin/env python3
"""
Main entry point for SDV GenAI Framework
Run standalone application generator
"""

import sys
import os
from pathlib import Path

# Ensure framework is in path
sys.path.insert(0, str(Path(__file__).parent))

def main():
    """Main framework entry point"""
    print("="*70)
    print("VisCar SDV GenAI Framework")
    print("="*70)
    print()
    
    print("Available commands:")
    print("  python -m framework generate <app_name>  - Generate new SDV application")
    print("  python -m framework ota <app_name>        - Inject OTA service")
    print("  python -m framework demo                  - Run example generation")
    print()
    
    if len(sys.argv) < 2:
        print("Running demo generation...")
        run_demo()
    elif sys.argv[1] == "demo":
        run_demo()
    elif sys.argv[1] == "generate" and len(sys.argv) > 2:
        generate_app(sys.argv[2])
    else:
        print("Invalid command. See usage above.")
        sys.exit(1)

def run_demo():
    """Run demonstration generation"""
    from applications.generate_vehicle_health import main as gen_main
    gen_main()

def generate_app(app_name):
    """Generate a new application"""
    from framework import SDVOrchestrator
    
    orchestrator = SDVOrchestrator(output_dir="applications")
    
    problem = f"""
    Generate SDV application: {app_name}
    Basic vehicle monitoring and control services.
    """
    
    result = orchestrator.generate_application(problem, app_name)
    print(f"\nApplication '{app_name}' generated successfully!")

if __name__ == "__main__":
    main()
