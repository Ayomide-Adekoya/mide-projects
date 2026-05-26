# OWASP Vulnerability Analysis
**Course:** Introduction to Cybersecurity and Strategies (CYB 206)

## Vulnerabilities Covered
- SQL Injection
- Cross-Site Scripting (XSS)

## SQL Injection
**Definition:** A critical security vulnerability where untrusted user-supplied data is sent to an interpreter as part of a command or query.

**How it occurs:** Attacker finds an input point → tests with special characters → crafts a malicious payload → application executes it as a legitimate command.

**Impact:** Data breach, data manipulation, authentication bypass, Denial of Service (DoS).

## Cross-Site Scripting (XSS)
**Definition:** A client-side code injection attack where an attacker inserts malicious scripts into a trusted website, targeting the users browser.

**How it occurs:** Application includes untrusted data in a web page without proper validation, causing the browser to execute the attacker's script.

**Impact:** Account hijacking, data theft, page defacement.

## Mitigation Strategies
**SQL Injection:** Parameterized queries, input validation, generic error messages.

**XSS:** Escape and sanitize output, Content Security Policy (CSP), server-side input validation.
