"""
Service Registry for SOA
Manages service discovery and lifecycle
"""

from typing import Dict, List, Any, Optional
import json
from pathlib import Path


class ServiceRegistry:
    """Central registry for managing SDV services"""
    
    def __init__(self):
        self.services = {}
        self.service_metadata = {}
    
    def register(self, service_name: str, service_instance: Any, metadata: Dict[str, Any] = None):
        """
        Register a service in the registry
        
        Args:
            service_name: Unique service identifier
            service_instance: Service instance
            metadata: Optional service metadata
        """
        if service_name in self.services:
            print(f"Warning: Service '{service_name}' already registered. Updating...")
        
        self.services[service_name] = service_instance
        self.service_metadata[service_name] = metadata or {}
        
        print(f"✓ Service '{service_name}' registered successfully")
    
    def unregister(self, service_name: str) -> bool:
        """
        Unregister a service
        
        Args:
            service_name: Service to unregister
            
        Returns:
            True if successful, False otherwise
        """
        if service_name not in self.services:
            print(f"Error: Service '{service_name}' not found")
            return False
        
        del self.services[service_name]
        del self.service_metadata[service_name]
        
        print(f"✓ Service '{service_name}' unregistered")
        return True
    
    def get_service(self, service_name: str) -> Optional[Any]:
        """
        Get service instance by name
        
        Args:
            service_name: Service identifier
            
        Returns:
            Service instance or None
        """
        return self.services.get(service_name)
    
    def get_all_services(self) -> Dict[str, Any]:
        """Get all registered services"""
        return self.services.copy()
    
    def get_service_metadata(self, service_name: str) -> Dict[str, Any]:
        """Get metadata for a service"""
        return self.service_metadata.get(service_name, {})
    
    def list_services(self) -> List[str]:
        """List all registered service names"""
        return list(self.services.keys())
    
    def find_services_by_tag(self, tag: str) -> List[str]:
        """
        Find services by metadata tag
        
        Args:
            tag: Tag to search for
            
        Returns:
            List of matching service names
        """
        matches = []
        
        for service_name, metadata in self.service_metadata.items():
            tags = metadata.get('tags', [])
            if tag in tags:
                matches.append(service_name)
        
        return matches
    
    def get_dependency_graph(self) -> Dict[str, List[str]]:
        """
        Build service dependency graph
        
        Returns:
            Dictionary mapping service names to their dependencies
        """
        graph = {}
        
        for service_name, metadata in self.service_metadata.items():
            dependencies = metadata.get('dependencies', [])
            graph[service_name] = dependencies
        
        return graph
    
    def validate_dependencies(self) -> Dict[str, List[str]]:
        """
        Validate that all service dependencies are met
        
        Returns:
            Dictionary of services with missing dependencies
        """
        missing = {}
        
        for service_name, metadata in self.service_metadata.items():
            dependencies = metadata.get('dependencies', [])
            missing_deps = [dep for dep in dependencies if dep not in self.services]
            
            if missing_deps:
                missing[service_name] = missing_deps
        
        return missing
    
    def save_registry(self, filepath: str):
        """Save registry metadata to file"""
        registry_data = {
            "services": list(self.services.keys()),
            "metadata": self.service_metadata
        }
        
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w') as f:
            json.dump(registry_data, f, indent=2)
    
    def load_registry(self, filepath: str):
        """Load registry metadata from file"""
        with open(filepath, 'r') as f:
            registry_data = json.load(f)
        
        self.service_metadata = registry_data.get('metadata', {})
    
    def generate_report(self) -> str:
        """Generate service registry report"""
        report = f"""
Service Registry Report
{'='*60}
Total Services: {len(self.services)}

Registered Services:
"""
        
        for service_name, metadata in self.service_metadata.items():
            report += f"\n  • {service_name}"
            report += f"\n    Language: {metadata.get('language', 'N/A')}"
            report += f"\n    Version: {metadata.get('version', 'N/A')}"
            deps = metadata.get('dependencies', [])
            if deps:
                report += f"\n    Dependencies: {', '.join(deps)}"
            report += "\n"
        
        # Check for missing dependencies
        missing = self.validate_dependencies()
        if missing:
            report += f"\n⚠ Missing Dependencies:\n"
            for service, deps in missing.items():
                report += f"  • {service}: {', '.join(deps)}\n"
        
        return report
