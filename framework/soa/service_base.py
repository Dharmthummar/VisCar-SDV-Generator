"""
Base Service Class for SOA
Foundation for all SDV services
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List
from datetime import datetime
import logging


class ServiceBase(ABC):
    """Abstract base class for all SDV services"""
    
    def __init__(self, service_name: str):
        self.service_name = service_name
        self.initialized = False
        self.version = "1.0.0"
        self.start_time = None
        self.logger = self._setup_logger()
    
    def _setup_logger(self) -> logging.Logger:
        """Setup service logger"""
        logger = logging.getLogger(self.service_name)
        logger.setLevel(logging.INFO)
        
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            f'[{self.service_name}] %(asctime)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        return logger
    
    def initialize(self) -> bool:
        """
        Initialize the service
        
        Returns:
            True if successful, False otherwise
        """
        if self.initialized:
            self.logger.warning("Service already initialized")
            return False
        
        try:
            self.logger.info("Initializing service...")
            self._on_initialize()
            self.initialized = True
            self.start_time = datetime.now()
            self.logger.info("Service initialized successfully")
            return True
        except Exception as e:
            self.logger.error(f"Initialization failed: {e}")
            return False
    
    def shutdown(self) -> bool:
        """
        Shutdown the service
        
        Returns:
            True if successful, False otherwise
        """
        if not self.initialized:
            self.logger.warning("Service not initialized")
            return False
        
        try:
            self.logger.info("Shutting down service...")
            self._on_shutdown()
            self.initialized = False
            self.logger.info("Service shut down successfully")
            return True
        except Exception as e:
            self.logger.error(f"Shutdown failed: {e}")
            return False
    
    def get_status(self) -> Dict[str, Any]:
        """Get service status"""
        return {
            "name": self.service_name,
            "version": self.version,
            "initialized": self.initialized,
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "uptime_seconds": (datetime.now() - self.start_time).total_seconds() if self.start_time else 0
        }
    
    @abstractmethod
    def _on_initialize(self):
        """Service-specific initialization logic"""
        pass
    
    @abstractmethod
    def _on_shutdown(self):
        """Service-specific shutdown logic"""
        pass
    
    @abstractmethod
    def process(self, data: Any) -> Any:
        """
        Main service processing method
        
        Args:
            data: Input data
            
        Returns:
            Processed result
        """
        pass
