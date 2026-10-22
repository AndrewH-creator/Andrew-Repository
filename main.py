#!/usr/bin/env python3
"""
Hissong Technology Services - Phase 1 Security Assessment
Author: Andrew Hissong

Fictional business and simulated risk scenarios.
No real network scans are performed.
"""

import csv
import json
from datetime import date
from pathlib import Path

OUTPUT = Path("output")

# PHASE 1: ASSET INVENTORY

ASSETS = [
    {
        "id": "A-001",
        "name": "Business File Server",
        "type": "Server",
        "location": "Server VLAN",
        "owner": "IT Administrator",
        "data": "Business documents and customer records",
        "criticality": "Critical",
        "protection": "Access controls, encryption, tested backups",
    },
    {
        "id": "A-002",
        "name": "Employee Workstations",
        "type": "Endpoints",
        "location": "Employee VLAN",
        "owner": "Department Managers",
        "data": "Email and business applications",
        "criticality": "High",
        "protection": "Endpoint protection, patching, MFA",
    },
    {
        "id": "A-003",
        "name": "Business Router and Firewall",
        "type": "Network Device",
        "location": "Network Boundary",
        "owner": "IT Administrator",
        "data": "Network traffic and security rules",
        "criticality": "Critical",
        "protection": "Firewall reviews, firmware updates, MFA",
    },
    {
        "id": "A-004",
        "name": "Employee Email",
        "type": "Cloud Service",
        "location": "Cloud",
        "owner": "Business Manager",
        "data": "Business communications",
        "criticality": "High",
        "protection": "MFA, spam filtering, sign-in monitoring",
    },
    {
        "id": "A-005",
        "name": "Customer Database",
        "type": "Database",
        "location": "Server VLAN",
        "owner": "Business Manager",
        "data": "Customer contact and service information",
        "criticality": "Critical",
        "protection": "Least privilege, encryption, audit logs",
    },
    {
        "id": "A-006",
        "name": "Backup Storage",
        "type": "Backup System",
        "location": "Restricted Backup Network",
        "owner": "IT Administrator",
        "data": "Copies of business data",
        "criticality": "Critical",
        "protection": "Isolated backups and recovery testing",
    },
    {
        "id": "A-007",
        "name": "Employee Wi-Fi",
        "type": "Wireless Network",
        "location": "Wireless VLAN",
        "owner": "IT Administrator",
        "data": "Wireless network connectivity",
        "criticality": "Medium",
        "protection": "Strong authentication and segmentation",
    },
    {
        "id": "A-008",
        "name": "IT Administrator Account",
        "type": "Privileged Account",
        "location": "Identity Systems",
        "owner": "IT Administrator",
        "data": "Administrative system access",
        "criticality": "Critical",
        "protection": "MFA, separate admin account, audit logging",
    },
]

# PHASE 1: RISK REGISTER
# Likelihood and impact are rated from 1 to 5.
# These ratings are preliminary simulated estimates.

RISKS = [
    {
        "id": "R-001",
        "title": "Phishing and email compromise",
        "asset": "A-004",
        "likelihood": 4,
        "impact": 4,
        "finding": "Phishing could compromise employee email accounts.",
        "recommendation": (
            "Enforce MFA, email filtering, employee training, "
            "and sign-in monitoring."
        ),
    },
    {
        "id": "R-002",
        "title": "Ransomware affecting business files",
        "asset": "A-001",
        "likelihood": 3,
        "impact": 5,
        "finding": "Ransomware could interrupt access to business documents.",
        "recommendation": (
            "Maintain isolated backups, test recovery, patch systems, "
            "and deploy endpoint protection."
        ),
    },
    {
        "id": "R-003",
        "title": "Excessive privileged access",
        "asset": "A-008",
        "likelihood": 3,
        "impact": 5,
        "finding": (
            "A compromised administrator account could expose "
            "multiple systems."
        ),
        "recommendation": (
            "Require MFA, review permissions, separate admin accounts, "
            "and enable audit logs."
        ),
    },
    {
        "id": "R-004",
        "title": "Unpatched workstation or server",
        "asset": "A-002",
        "likelihood": 3,
        "impact": 4,
        "finding": (
            "Missing security updates could expose systems "
            "to known vulnerabilities."
        ),
        "recommendation": (
            "Establish a patch schedule and verify updates "
            "through approved assessments."
        ),
    },
    {
        "id": "R-005",
        "title": "Customer data exposure",
        "asset": "A-005",
        "likelihood": 3,
        "impact": 5,
        "finding": (
            "Unauthorized database access could expose "
            "customer information."
        ),
        "recommendation": (
            "Apply least privilege, encryption, database auditing, "
            "and permission reviews."
        ),
    },
    {
        "id": "R-006",
        "title": "Wireless access to internal systems",
        "asset": "A-007",
        "likelihood": 3,
        "impact": 3,
        "finding": (
            "Insufficient wireless segmentation could expose "
            "internal resources."
        ),
        "recommendation": (
            "Use strong wireless authentication and isolate guest Wi-Fi."
        ),
    },
    {
        "id": "R-007",
        "title": "Backup failure or compromise",
        "asset": "A-006",
        "likelihood": 3,
        "impact": 5,
        "finding": (
            "Unavailable or compromised backups could prevent recovery."
        ),
        "recommendation": (
            "Restrict backup access, maintain isolated copies, "
            "and test restoration."
        ),
    },
    {
        "id": "R-008",
        "title": "Firewall misconfiguration",
        "asset": "A-003",
        "likelihood": 2,
        "impact": 5,
        "finding": (
            "Overly permissive firewall rules could expose internal services."
        ),
        "recommendation": (
            "Review firewall rules, update firmware, "
            "and restrict administrative access."
        ),
    },
]


# RISK CALCULATION FUNCTIONS

def risk_level(score):
    if score >= 20:
        return "Critical"
    if score >= 12:
        return "High"
    if score >= 6:
        return "Medium"
    return "Low"


def build_risks():
    results = []

    for risk in RISKS:
        item = dict(risk)
        item["score"] = item["likelihood"] * item["impact"]
        item["level"] = risk_level(item["score"])
        results.append(item)

    return sorted(
        results,
        key=lambda item: item["score"],
        reverse=True,
    )


# FILE GENERATION FUNCTIONS

def write_csv(path, rows):
    if not rows:
        return

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=list(rows[0].keys()),
        )
        writer.writeheader()
        writer.writerows(rows)


def markdown_table(headers, rows):
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]

    for row in rows:
        cells = [
            str(value).replace("|", "\\|").replace("\n", " ")
            for value in row
        ]
        lines.append("| " + " | ".join(cells) + " |")

    return "\n".join(lines)
  # NETWORK DIAGRAM

def create_network_diagram():
    return """flowchart TB
    Internet((Internet))
    FW["Business Router / Firewall"]
    SW["Managed Network Switch"]
    EMP["Employee Workstations"]
    WIFI["Employee Wi-Fi"]
    GUEST["Guest Wi-Fi"]
    FILE["Business File Server"]
    DB[("Customer Database")]
    BACKUP["Restricted Backup Storage"]
    CLOUD["Cloud Email and Identity"]

    Internet --> FW
    FW --> SW
    SW --> EMP
    SW --> WIFI
    SW --> FILE
    FILE --> DB
    FILE --> BACKUP
    EMP -. "Email access" .-> CLOUD
    GUEST -. "Internet access only" .-> FW
"""


# SECURITY ASSESSMENT REPORT

def create_report(risks):
    asset_rows = [
        [a["id"], a["name"], a["type"], a["criticality"]]
        for a in ASSETS
    ]

    risk_rows = [
        [
            r["id"],
            r["title"],
            r["likelihood"],
            r["impact"],
            r["score"],
            r["level"],
            r["recommendation"],
        ]
        for r in risks
    ]

    high_count = sum(
        r["level"] in ("High", "Critical")
        for r in risks
    )

    return f"""# Security Assessment Report
## Hissong Technology Services

**Prepared by:** Andrew Hissong

**Assessment Date:** {date.today().isoformat()}

**Project Phase:** Phase 1

**Assessment Type:** Simulated Small Business Security Assessment

## 1. Executive Summary

This report evaluates the fictional small business Hissong Technology
Services. The purpose is to identify important assets, analyze potential
cybersecurity threats, rank risks, and recommend appropriate security controls.

The assessment identifies {len(ASSETS)} assets and {len(risks)} risk scenarios.
Of these risks, {high_count} have a calculated High or Critical rating.

Priority areas include phishing, ransomware, privileged access, customer
data protection, patch management, and backup recovery.

All findings are simulated scenarios. No real company network was scanned
or inspected, and no vulnerabilities have been confirmed.

## 2. Scope and Methodology

The assessment covers employee workstations, a file server, a customer
database, network equipment, wireless networking, cloud email, administrator
accounts, and backup storage.

The methodology includes asset identification, threat analysis, qualitative
risk scoring, and recommended security controls.

Risk score = Likelihood multiplied by Impact.

Likelihood and impact use a scale from 1 to 5. The resulting score is a
planning aid, not a statistical probability.

## 3. Business Environment

Hissong Technology Services is a fictional small business that depends on
email, customer information, shared files, employee computers, and reliable
network access.

The proposed environment contains a business firewall, managed switch,
employee wireless network, servers, cloud email, and backup storage.

Actual configurations and security controls would need to be verified
before conducting a real assessment.

## 4. Asset Inventory

{markdown_table(
    ["ID", "Asset", "Type", "Criticality"],
    asset_rows
)}

The complete inventory is available in `asset_inventory.csv`.

## 5. Threats and Potential Vulnerabilities

The scenarios considered include:

- Phishing and stolen email credentials.
- Ransomware and business file loss.
- Compromised administrator accounts.
- Unpatched workstations and servers.
- Unauthorized access to customer data.
- Inadequate wireless network segmentation.
- Backup failure or compromise.
- Firewall misconfiguration.

These are potential risks, not confirmed security weaknesses. Validation
would require authorized configuration reviews, interviews, or controlled
testing in a lab environment.

## 6. Risk Assessment

{markdown_table(
    ["ID", "Risk", "Likelihood", "Impact", "Score", "Rating", "Recommendation"],
    risk_rows
)}

### Risk Matrix

| Likelihood / Impact | 1 Minimal | 2 Low | 3 Moderate | 4 Major | 5 Severe |
|---|---:|---:|---:|---:|---:|
| 5 Almost certain | 5 | 10 | 15 | 20 | 25 |
| 4 Likely | 4 | 8 | 12 | 16 | 20 |
| 3 Possible | 3 | 6 | 9 | 12 | 15 |
| 2 Unlikely | 2 | 4 | 6 | 8 | 10 |
| 1 Rare | 1 | 2 | 3 | 4 | 5 |

Risk ratings:

- 1-5: Low
- 6-11: Medium
- 12-19: High
- 20-25: Critical

## 7. Recommended Security Improvements

### Immediate Priorities

1. Require MFA for email and administrative accounts.
2. Verify backups and test data restoration.
3. Review administrator permissions.
4. Establish a regular patch management process.

### Near-Term Priorities

5. Review firewall rules and unnecessary network exposure.
6. Separate guest wireless access from business systems.
7. Protect customer data through encryption and least privilege.
8. Improve endpoint monitoring and phishing reporting.

### Ongoing Activities

- Review user access regularly.
- Document remediation tasks and responsible personnel.
- Test backup recovery.
- Maintain security logs.
- Review incident-response procedures.

## 8. Incident Response Plan

If a suspected cybersecurity incident occurs:

1. Identify and document the alert and affected assets.
2. Notify the designated incident-response contact.
3. Preserve relevant logs and evidence.
4. Contain affected systems when appropriate.
5. Investigate the cause and remove the threat.
6. Recover systems using known-good backups.
7. Verify recovery and document lessons learned.

Evidence should be handled according to organizational policy and applicable
legal requirements.

## 9. Limitations

This assessment uses a fictional business and simulated findings.
No real systems, logs, packet captures, or vulnerability scan results were
examined.

Risk ratings are preliminary and should be updated when evidence becomes
available.

## 10. Conclusion

This project demonstrates how cybersecurity professionals can identify
important business assets, evaluate potential threats, prioritize risks,
and recommend security improvements.

Future phases will introduce authorized lab testing, simulated incident
evidence, network traffic analysis, and a more detailed incident-response
investigation.

## 11. Research and Project Differentiation

CSCC cybersecurity coursework connects directly to this project through
networking, Linux, information security, network security, ethical hacking,
and computer forensics and incident response.

Comparable portfolio projects include SIEM labs using Wazuh and security
operations projects involving log analysis and incident detection.

This project differs by connecting the asset inventory, network diagram,
risk assessment, mitigation recommendations, and planned incident-response
exercises into one continuous fictional business scenario.

### Research Sources

- CSCC Cybersecurity AAS:
  https://explore.cscc.edu/programs/CSCI.CYBER.AAS/computer-science-cybersecurity-major-aas

- CSCC Cybersecurity Curriculum:
  https://www.cscc.edu/academics/departments/computer-it/cybersecurity/curriculum.shtml

- Wazuh Lab Portfolio:
  https://jseverino.com/portfolio/deploying-a-wazuh-siem-lab/

- SOC Detection Lab:
  https://github.com/HarryKlrr/soc-detection-lab
"""


# README DOCUMENTATION

def create_readme():
    return """# Hissong Technology Services - Phase 1

**Author:** Andrew Hissong

## Project Overview

This project simulates a cybersecurity assessment for a fictional small
business. It documents assets, risks, a proposed network, and recommendations.

## Requirements

- Python 3.10 or newer
- No additional Python packages required

## How to Run

Open a terminal in the project folder and execute:

    python main.py

If necessary, use:

    python3 main.py

## Generated Files

The program creates an output folder containing:

- security_assessment_report.md
- asset_inventory.csv
- risk_register.csv
- network_diagram.mmd
- assessment_summary.json
- README.md

## Risk Scoring

Risk score = likelihood multiplied by impact.

Both values use a scale from 1 to 5.

## Safety Notice

This project uses fictional assets and simulated findings. It does not
scan real networks or prove the existence of vulnerabilities.

## Future Phases

- Perform authorized testing in an isolated lab.
- Analyze simulated security logs.
- Examine sample packet captures with Wireshark.
- Create an incident timeline.
- Document response and remediation recommendations.
"""


# MAIN PROGRAM

def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)

    risks = build_risks()

    # Generate the asset inventory.
    write_csv(
        OUTPUT / "asset_inventory.csv",
        ASSETS,
    )

    # Generate the risk register.
    write_csv(
        OUTPUT / "risk_register.csv",
        risks,
    )

    # Generate the network diagram.
    (OUTPUT / "network_diagram.mmd").write_text(
        create_network_diagram(),
        encoding="utf-8",
    )

    # Generate the assessment report.
    (OUTPUT / "security_assessment_report.md").write_text(
        create_report(risks),
        encoding="utf-8",
    )

    # Generate README documentation.
    (OUTPUT / "README.md").write_text(
        create_readme(),
        encoding="utf-8",
    )

    # Generate a machine-readable summary.
    summary = {
        "project": "Hissong Technology Services",
        "author": "Andrew Hissong",
        "assessment_date": date.today().isoformat(),
        "assessment_type": "Simulated",
        "assets_count": len(ASSETS),
        "risks_count": len(risks),
        "risk_counts": {
            level: sum(
                r["level"] == level
                for r in risks
            )
            for level in ("Critical", "High", "Medium", "Low")
        },
        "important_note": (
            "Fictional scenario. No real network scans were performed."
        ),
    }

    (OUTPUT / "assessment_summary.json").write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )

    # Display the results.
    print("=" * 55)
    print("HISSONG TECHNOLOGY SERVICES - PHASE 1")
    print("=" * 55)

    print(f"Assets inventoried: {len(ASSETS)}")
    print(f"Risks assessed:     {len(risks)}")

    print("\nRisk overview:")

    for level, count in summary["risk_counts"].items():
        print(f"  {level:8}: {count}")

    print(f"\nDeliverables saved to: {OUTPUT.resolve()}")
    print("Assessment completed successfully.")
    print("No network scans were performed.")


if __name__ == "__main__":
    main()
