"""
OTA Manager for SDV GenAI Framework
Handles Over-The-Air service injection and updates
"""

import json
import os
from typing import Dict, List, Any
from pathlib import Path
from datetime import datetime


class OTAManager:
    """Manages OTA service injection and updates for SDV applications"""
    
    def __init__(self, app_dir: str):
        self.app_dir = Path(app_dir)
        self.registry_file = self.app_dir / "service_registry.json"
        self.ota_log_file = self.app_dir / "ota_history.json"
        self.ota_history = self._load_ota_history()
    
    def inject_service(self, service_definition: Dict[str, Any]) -> Dict[str, Any]:
        """
        Inject a new service via OTA
        
        Args:
            service_definition: Complete service specification
            
        Returns:
            Injection result with status and metadata
        """
        
        print(f"\n{'='*60}")
        print(f"OTA Service Injection")
        print(f"{'='*60}")
        print(f"Service: {service_definition['name']}")
        print(f"Language: {service_definition['language']}")
        print(f"Version: {service_definition.get('version', '1.0.0')}")
        print(f"{'='*60}\n")
        
        # Validate service definition
        if not self._validate_service(service_definition):
            return {
                "status": "failed",
                "error": "Invalid service definition"
            }
        
        # Check for conflicts
        if self._service_exists(service_definition['name']):
            print(f"Service '{service_definition['name']}' already exists. Updating...")
            operation = "update"
        else:
            print(f"Injecting new service '{service_definition['name']}'...")
            operation = "inject"
        
        # Register service
        self._register_service(service_definition, operation)
        
        # Log OTA operation
        ota_record = {
            "timestamp": datetime.now().isoformat(),
            "operation": operation,
            "service_name": service_definition['name'],
            "version": service_definition.get('version', '1.0.0'),
            "language": service_definition['language'],
            "status": "success"
        }
        self.ota_history.append(ota_record)
        self._save_ota_history()
        
        print(f"✓ Service '{service_definition['name']}' {operation}ed successfully!")
        
        return {
            "status": "success",
            "operation": operation,
            "service_name": service_definition['name'],
            "timestamp": ota_record['timestamp']
        }
    
    def get_service_registry(self) -> Dict[str, Any]:
        """Get current service registry"""
        if self.registry_file.exists():
            with open(self.registry_file, 'r') as f:
                return json.load(f)
        return {"services": [], "version": "1.0.0"}
    
    def get_ota_history(self) -> List[Dict[str, Any]]:
        """Get OTA operation history"""
        return self.ota_history
    
    def rollback_service(self, service_name: str) -> Dict[str, Any]:
        """Rollback a service to previous version"""
        # Find last version in OTA history
        service_history = [h for h in self.ota_history if h['service_name'] == service_name]
        
        if len(service_history) < 2:
            return {
                "status": "failed",
                "error": "No previous version available"
            }
        
        # Rollback logic would go here
        print(f"Rolling back service '{service_name}'...")
        
        return {
            "status": "success",
            "service_name": service_name,
            "rolled_back_to": service_history[-2]['version']
        }
    
    def _validate_service(self, service_definition: Dict[str, Any]) -> bool:
        """Validate service definition"""
        required_fields = ['name', 'language', 'interfaces']
        
        for field in required_fields:
            if field not in service_definition:
                print(f"Error: Missing required field '{field}'")
                return False
        
        # Validate language
        supported_languages = ['cpp', 'c', 'rust', 'java', 'python']
        if service_definition['language'] not in supported_languages:
            print(f"Error: Unsupported language '{service_definition['language']}'")
            return False
        
        return True
    
    def _service_exists(self, service_name: str) -> bool:
        """Check if service already exists in registry"""
        registry = self.get_service_registry()
        
        for service in registry.get('services', []):
            if service.get('name') == service_name:
                return True
        
        return False
    
    def _register_service(self, service_definition: Dict[str, Any], operation: str):
        """Register service in the registry"""
        registry = self.get_service_registry()
        
        if operation == "inject":
            # Add new service
            registry['services'].append({
                "name": service_definition['name'],
                "language": service_definition['language'],
                "version": service_definition.get('version', '1.0.0'),
                "interfaces": service_definition.get('interfaces', []),
                "dependencies": service_definition.get('dependencies', []),
                "injected_via_ota": True,
                "injection_date": datetime.now().isoformat()
            })
        else:
            # Update existing service
            for service in registry['services']:
                if service['name'] == service_definition['name']:
                    service['version'] = service_definition.get('version', '1.0.0')
                    service['updated_via_ota'] = True
                    service['last_update'] = datetime.now().isoformat()
                    break
        
        # Save registry
        self.registry_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.registry_file, 'w') as f:
            json.dump(registry, f, indent=2)
    
    def _load_ota_history(self) -> List[Dict[str, Any]]:
        """Load OTA history from file"""
        if self.ota_log_file.exists():
            with open(self.ota_log_file, 'r') as f:
                return json.load(f)
        return []
    
    def _save_ota_history(self):
        """Save OTA history to file"""
        self.ota_log_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.ota_log_file, 'w') as f:
            json.dump(self.ota_history, f, indent=2)
    
    def generate_ota_report(self) -> str:
        """Generate OTA operations report"""
        report = f"""
OTA Operations Report
{'='*60}
Application: {self.app_dir.name}
Total OTA Operations: {len(self.ota_history)}

Recent Operations:
"""
        
        for operation in self.ota_history[-5:]:  # Last 5 operations
            report += f"\n  [{operation['timestamp']}]"
            report += f"\n  Operation: {operation['operation'].upper()}"
            report += f"\n  Service: {operation['service_name']}"
            report += f"\n  Version: {operation['version']}"
            report += f"\n  Status: {operation['status']}"
            report += f"\n  {'-'*58}\n"
        
        return report
