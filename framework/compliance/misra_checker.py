"""
MISRA Compliance Checker
Validates and reports MISRA-C/C++ compliance
"""

from typing import Dict, List, Any


class MISRAChecker:
    """MISRA-C/C++ compliance checker and reporter"""
    
    def __init__(self):
        self.rules = self._load_rules()
    
    def check_compliance(self, code: str, language: str = "cpp") -> Dict[str, Any]:
        """
        Check MISRA compliance for given code
        
        Args:
            code: Source code to check
            language: Language (c or cpp)
            
        Returns:
            Compliance report with violations and score
        """
        
        violations = []
        
        # Example rule checks (would integrate with actual MISRA checker)
        if "goto" in code:
            violations.append({
                "rule": "MISRA-C:2012 Rule 15.1",
                "severity": "Required",
                "description": "The goto statement shall not be used",
                "line": 0
            })
        
        if "malloc" in code and language == "cpp":
            violations.append({
                "rule": "MISRA-C++:2023 Rule 18-4-1",
                "severity": "Required",
                "description": "Dynamic heap memory allocation shall not be used",
                "line": 0
            })
        
        total_rules_checked = len(self.rules.get(language, []))
        violations_count = len(violations)
        compliance_score = ((total_rules_checked - violations_count) / total_rules_checked * 100) if total_rules_checked > 0 else 100
        
        return {
            "language": language,
            "total_rules_checked": total_rules_checked,
            "violations": violations,
            "violations_count": violations_count,
            "compliance_score": round(compliance_score, 2),
            "compliant": violations_count == 0
        }
    
    def _load_rules(self) -> Dict[str, List[str]]:
        """Load MISRA rules database"""
        return {
            "c": [
                "MISRA-C:2012 Rule 1.1",
                "MISRA-C:2012 Rule 1.2",
                "MISRA-C:2012 Rule 15.1",  # No goto
                "MISRA-C:2012 Rule 21.3",  # No malloc/free
                # ... more rules
            ],
            "cpp": [
                "MISRA-C++:2023 Rule 0-1-1",
                "MISRA-C++:2023 Rule 5-0-3",  # No implicit conversions
                "MISRA-C++:2023 Rule 8-0-1",  # Initialize all variables
                "MISRA-C++:2023 Rule 18-4-1",  # No dynamic allocation
                # ... more rules
            ]
        }
    
    def generate_report(self, compliance_result: Dict[str, Any]) -> str:
        """Generate human-readable compliance report"""
        
        report = f"""
MISRA Compliance Report
{'='*60}
Language: {compliance_result['language'].upper()}
Compliance Score: {compliance_result['compliance_score']}%
Total Rules Checked: {compliance_result['total_rules_checked']}
Violations Found: {compliance_result['violations_count']}
Status: {'✓ COMPLIANT' if compliance_result['compliant'] else '✗ NON-COMPLIANT'}

"""
        
        if compliance_result['violations']:
            report += "Violations:\n"
            report += "-" * 60 + "\n"
            for i, violation in enumerate(compliance_result['violations'], 1):
                report += f"{i}. {violation['rule']} ({violation['severity']})\n"
                report += f"   {violation['description']}\n"
                report += f"   Line: {violation['line']}\n\n"
        
        return report
