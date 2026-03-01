# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.0.x   | Yes       |
| < 1.0   | No        |

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it responsibly.

**Do NOT open a public GitHub Issue for security vulnerabilities.**

Instead, email: **security@eduardpetraeus.dev**

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

## Response Timeline

- **Acknowledgment:** Within 48 hours
- **Initial assessment:** Within 1 week
- **Fix and disclosure:** Within 30 days for confirmed vulnerabilities

## Scope

This scaffolder generates project structures. Security concerns include:
- Template injection via project names or config values
- Path traversal in --output-dir or --name arguments
- Overwriting existing files or directories
- Symlink attacks

## Security Measures in Place

- `create_project()` refuses to overwrite existing directories
- No shell execution of user input
- No network calls during scaffolding
- AGENTS.md symlink uses relative path (no absolute path symlink attacks)
