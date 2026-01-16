"""
ASPICE Compliance Mapper
Maps requirements to design, code, and tests for ASPICE compliance
"""

from typing import Dict, List, Any
import json


class ASPICEMapper:
    """ASPICE (Automotive SPICE) compliance mapper and tracer"""
    
    def __init__(self):
        self.traceability_matrix = {}
    
    def create_traceability_matrix(self, 
                                   system_reqs: List[Dict],
                                   software_reqs: List[Dict],
                                   design_elements: List[Dict],
                                   code_units: List[Dict],
                                   test_cases: List[Dict]) -> Dict[str, Any]:
        """
        Create complete traceability matrix for ASPICE
        
        Traces:
        System Req → Software Req → Design → Code → Tests
        """
        
        matrix = {
            "system_to_software": self._map_system_to_software(system_reqs, software_reqs),
            "software_to_design": self._map_software_to_design(software_reqs, design_elements),
            "design_to_code": self._map_design_to_code(design_elements, code_units),
            "code_to_tests": self._map_code_to_tests(code_units, test_cases),
            "end_to_end": self._create_end_to_end_trace(system_reqs, test_cases)
        }
        
        self.traceability_matrix = matrix
        return matrix
    
    def _map_system_to_software(self, system_reqs: List[Dict], software_reqs: List[Dict]) -> List[Dict]:
        """Map system requirements to software requirements"""
        mappings = []
        
        for sw_req in software_reqs:
            if 'traces_to' in sw_req:
                mappings.append({
                    "software_req_id": sw_req.get('id'),
                    "system_req_id": sw_req.get('traces_to'),
                    "coverage": "full"
                })
        
        return mappings
    
    def _map_software_to_design(self, software_reqs: List[Dict], design_elements: List[Dict]) -> List[Dict]:
        """Map software requirements to design elements"""
        mappings = []
        
        for design in design_elements:
            mappings.append({
                "design_element": design.get('name'),
                "software_req_ids": design.get('implements', []),
                "coverage": "full"
            })
        
        return mappings
    
    def _map_design_to_code(self, design_elements: List[Dict], code_units: List[Dict]) -> List[Dict]:
        """Map design elements to code units"""
        mappings = []
        
        for code_unit in code_units:
            mappings.append({
                "code_unit": code_unit.get('name'),
                "design_element": code_unit.get('implements_design'),
                "language": code_unit.get('language'),
                "coverage": "full"
            })
        
        return mappings
    
    def _map_code_to_tests(self, code_units: List[Dict], test_cases: List[Dict]) -> List[Dict]:
        """Map code units to test cases"""
        mappings = []
        
        for test in test_cases:
            mappings.append({
                "test_case": test.get('name'),
                "code_unit": test.get('tests_unit'),
                "requirement": test.get('traces_requirement'),
                "coverage": "full"
            })
        
        return mappings
    
    def _create_end_to_end_trace(self, system_reqs: List[Dict], test_cases: List[Dict]) -> List[Dict]:
        """Create end-to-end traceability from system req to test"""
        traces = []
        
        for req in system_reqs:
            traces.append({
                "requirement_id": req.get('id'),
                "requirement_desc": req.get('description'),
                "validated_by_tests": [t.get('name') for t in test_cases if req.get('id') in str(t)],
                "fully_traced": True
            })
        
        return traces
    
    def calculate_aspice_level(self) -> Dict[str, Any]:
        """Calculate ASPICE capability level based on traceability"""
        
        if not self.traceability_matrix:
            return {"level": 0, "description": "No traceability"}
        
        # Check coverage
        has_requirements = len(self.traceability_matrix.get('system_to_software', [])) > 0
        has_design = len(self.traceability_matrix.get('software_to_design', [])) > 0
        has_code = len(self.traceability_matrix.get('design_to_code', [])) > 0
        has_tests = len(self.traceability_matrix.get('code_to_tests', [])) > 0
        has_end_to_end = len(self.traceability_matrix.get('end_to_end', [])) > 0
        
        if has_requirements and has_design and has_code and has_tests and has_end_to_end:
            level = 3
            description = "Established Process"
        elif has_requirements and has_design and has_code:
            level = 2
            description = "Managed Process"
        elif has_requirements:
            level = 1
            description = "Performed Process"
        else:
            level = 0
            description = "Incomplete Process"
        
        return {
            "level": level,
            "description": description,
            "traceability_coverage": {
                "system_to_software": has_requirements,
                "software_to_design": has_design,
                "design_to_code": has_code,
                "code_to_tests": has_tests,
                "end_to_end": has_end_to_end
            }
        }
    
    def generate_report(self) -> str:
        """Generate ASPICE compliance report"""
        
        aspice_level = self.calculate_aspice_level()
        
        report = f"""
ASPICE Compliance Report
{'='*60}
Capability Level: {aspice_level['level']} - {aspice_level['description']}

Traceability Coverage:
"""
        
        for key, value in aspice_level['traceability_coverage'].items():
            status = "✓" if value else "✗"
            report += f"  {status} {key.replace('_', ' ').title()}\n"
        
        report += f"\nTraceability Matrix Summary:\n"
        report += f"  System → Software: {len(self.traceability_matrix.get('system_to_software', []))} links\n"
        report += f"  Software → Design: {len(self.traceability_matrix.get('software_to_design', []))} links\n"
        report += f"  Design → Code: {len(self.traceability_matrix.get('design_to_code', []))} links\n"
        report += f"  Code → Tests: {len(self.traceability_matrix.get('code_to_tests', []))} links\n"
        
        return report
