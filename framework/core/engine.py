"""
Generation Engine for SDV GenAI Framework
Handles multi-language code generation using specialized generators
"""

from typing import Dict, Any
from pathlib import Path

from ..generators.code_gen_cpp import CppGenerator
from ..generators.code_gen_rust import RustGenerator
from ..generators.code_gen_java import JavaGenerator


class GenerationEngine:
    """Multi-language code generation engine"""
    
    def __init__(self):
        self.generators = {
            'cpp': CppGenerator(),
            'c': CppGenerator(),  # Reuse C++ generator for C
            'rust': RustGenerator(),
            'java': JavaGenerator()
        }
    
    def generate_service_code(self, service_spec: Dict[str, Any]) -> str:
        """
        Generate service code based on specification
        
        Args:
            service_spec: Service specification including name, language, interfaces, dependencies
            
        Returns:
            Generated source code as string
        """
        language = service_spec.get('language', 'cpp')
        generator = self.generators.get(language)
        
        if not generator:
            raise ValueError(f"Unsupported language: {language}")
        
        return generator.generate(service_spec)
    
    def generate_data_model(self, model_spec: Dict[str, Any], language: str) -> str:
        """Generate data model code"""
        generator = self.generators.get(language)
        
        if not generator:
            raise ValueError(f"Unsupported language: {language}")
        
        return generator.generate_data_model(model_spec)
    
    def get_supported_languages(self) -> list:
        """Get list of supported languages"""
        return list(self.generators.keys())
