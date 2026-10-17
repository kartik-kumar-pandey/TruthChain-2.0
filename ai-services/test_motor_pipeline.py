"""
Test script for TruthChain 2.0 Motor Domain Pipeline
"""

import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from graph.motor_graph import app_graph as motor_graph

sample_motor_claim = {
    "claim_id": "CLM-MOTOR-001",
    "domain": "motor",
    "data": {
        "claim_id": "CLM-MOTOR-001",
        "description": "Vehicle collision at traffic intersection while traveling at 35 km/h. Moderate bumper impact and front denting.",
        "image": r"C:\Users\karti\Downloads\image-test3.webp",
        "sensor": {
            "speed": 35.0,
            "accel_x": 0.25,
            "accel_y": 3.80,
            "accel_z": 0.40,
            "speed_change": 18.0,
            "acceleration_change": 3.4,
            "gps_distance": 95.0,
            "gps_speed": 34.2,
            "impact_detected": True,
            "airbag_deployed": False,
            "heading": 142.5
        },
        "policy": {
            "policy_id": "POL-9841",
            "coverage_type": "COMPREHENSIVE",
            "deductible": 500
        }
    }
}

print("=== STARTING MOTOR PIPELINE TEST ===")
result = motor_graph.invoke(sample_motor_claim)

print("\n=== MOTOR PIPELINE COMPLETED ===")
print("Claim ID:", result.get("claim_id"))
print("Domain:", result.get("domain"))
print("Final Verdict:", result.get("final_verdict"))
print("Fraud Score:", result.get("fraud_score"))
print("Pipeline Status:", result.get("pipeline_status"))
print("Blockchain Allowed:", result.get("blockchain_allowed"))

print("\nAgent Reports:")
for agent_name, report in result.get("agent_reports", {}).items():
    print(f"  - {agent_name}: decision={report.get('decision')}, score={report.get('risk_score') or report.get('fraud_score')}")

print("\n=== SUCCESS ===")
