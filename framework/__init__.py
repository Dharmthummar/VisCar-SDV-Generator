"""SDV GenAI Framework - Main Entry Point"""

__version__ = "1.0.0"
__author__ = "VisCar Team"

from .core import SDVOrchestrator, GenerationEngine
from .llm import GeminiClient, JulesClient
from .soa import ServiceBase, ServiceRegistry
from .ota import OTAManager
from .compliance import MISRAChecker, ASPICEMapper

__all__ = [
    'SDVOrchestrator',
    'GenerationEngine',
    'GeminiClient',
    'JulesClient',
    'ServiceBase',
    'ServiceRegistry',
    'OTAManager',
    'MISRAChecker',
    'ASPICEMapper'
]
