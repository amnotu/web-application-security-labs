# Methodology

This project follows a PTES-style workflow. Each lab is documented using the same process so the work stays consistent and easy to review.

## 1. Scope and Authorization

Testing is limited to the local VMware lab. No public systems, third-party systems, or production applications are included.

## 2. Intelligence Gathering

The tester identifies reachable hosts, exposed services, application URLs, and basic HTTP behavior.

## 3. Vulnerability Analysis

Application behavior is reviewed through HTTP traffic, input handling, authentication flows, session behavior, access control, and server responses.

## 4. Exploitation Validation

Potential weaknesses are validated only far enough to prove the issue in the local lab. The goal is to confirm impact without unnecessary damage.

## 5. Reporting

Each lab documents the objective, scope, tools, evidence, observed result, security impact, remediation, and lessons learned.

## 6. Remediation

Each finding should explain how the issue can be fixed and why the recommendation addresses the observed weakness.
