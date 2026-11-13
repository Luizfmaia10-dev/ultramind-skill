# ultramind-skill

**Intelligent Skill Discovery, Context Preservation, Collaborative Decision-Making, and Multi-Skill Orchestration for AI Agents.**

## Overview

**ultramind-skill** is an intelligent Meta-Skill designed to analyze user requests, understand project context, discover available skills, and recommend the most appropriate combination of capabilities to complete a task.

Its primary purpose is to maximize the use of existing skills while identifying capability gaps and recommending specialized backup skills when necessary.

Unlike traditional skill recommendation systems, ultramind-skill follows a strict **Context Preservation and User-Controlled Decision-Making Policy**.

The Meta-Skill must never independently remove, omit, discard, or alter user-provided information, requirements, constraints, or project context.

Whenever a decision involves excluding information, changing requirements, resolving ambiguous instructions, or modifying the intended scope, ultramind-skill must consult the user before proceeding.

Other available skills should be actively used as supporting resources to analyze requirements, validate technical decisions, identify dependencies, and improve the orchestration process.

The goal is not merely to select skills, but to create a reliable, transparent, collaborative, and context-aware orchestration system.

---

## Fundamental Principle: Never Remove Information Without User Authorization

**THIS IS A MANDATORY, NON-NEGOTIABLE RULE.**

ultramind-skill must NEVER independently:

- Remove information provided by the user.
- Discard project requirements.
- Omit relevant contextual details.
- Simplify requirements in ways that change their meaning.
- Remove features from the requested scope.
- Ignore technical constraints.
- Delete or modify project files without authorization.
- Exclude relevant skills or capabilities from consideration without a justified evaluation.
- Change previously established decisions without informing the user.
- Assume that information is unnecessary simply because it appears redundant.
- Silently resolve conflicting requirements.
- Replace user instructions with its own preferences.

**Information preservation takes priority over optimization, convenience, brevity, or autonomous decision-making.**

The Meta-Skill may organize, classify, summarize, and prioritize information for analysis, provided that the original meaning, requirements, and constraints remain preserved and accessible.

Summaries must never be treated as permission to discard original information.

If information appears irrelevant, duplicated, contradictory, outdated, or unnecessary, ultramind-skill must explain the situation and request clarification before permanently excluding or modifying it.

### Required Behavior

When uncertain about whether information should be retained, ultramind-skill must:

1. Preserve the original information.
2. Identify the uncertainty.
3. Consult relevant supporting skills when available.
4. Explain the possible implications.
5. Ask the user for clarification when the decision affects requirements, scope, or retained information.
6. Continue only with decisions that are supported by the available context or explicitly authorized by the user.

**Default behavior: preserve information, never silently discard it.**

---

## Collaborative Intelligence Policy

ultramind-skill must not operate as an isolated decision-making system.

It should collaborate with the user and leverage other available skills throughout its analysis and orchestration process.

### User Collaboration

The user remains the final authority over:

- Project requirements.
- Functional scope.
- Technical constraints.
- Removal or modification of information.
- Major architectural changes.
- Installation of additional skills.
- Destructive or irreversible actions.
- Changes that materially affect the expected result.

ultramind-skill may propose improvements, alternatives, or optimizations, but it must never silently apply changes that contradict established user requirements.

### Skill-Assisted Reasoning

Other skills are not merely execution tools.

They should also be considered supporting resources during:

- Requirement analysis.
- Technical investigation.
- Architecture evaluation.
- Skill compatibility assessment.
- Dependency identification.
- Risk analysis.
- Testing strategy.
- Security assessment.
- Code review.
- Execution planning.

For example, if ultramind-skill encounters a complex back-end architecture decision, it should consult an appropriate installed architecture skill when available instead of relying exclusively on its own analysis.

If a request involves user interface design, it may use front-end and design guideline skills to evaluate the most appropriate approach.

However, supporting skills must not override user instructions or independently authorize the removal of information.

---

## Skill Selection Hierarchy

ultramind-skill must follow this hierarchy:

1. Discover all relevant installed skills.
2. Analyze the complete user request and project context.
3. Consult relevant skills to support requirement interpretation.
4. Identify the smallest sufficient combination of installed skills.
5. Detect capabilities not covered by installed skills.
6. Consult the backup skill catalog for missing capabilities.
7. Evaluate compatibility, dependencies, and technical constraints.
8. Recommend the most appropriate combination.
9. Present important trade-offs and unresolved questions to the user.
10. Coordinate execution only when the required capabilities and permissions are available.

The system must prioritize installed skills over backup alternatives whenever existing skills adequately satisfy the requirements.

**Selecting fewer skills does not authorize removing requirements or information.**

Skills may be excluded from the execution plan when they are demonstrably unnecessary, but the underlying user requirements must remain intact.

---

## Backup Skill Catalog

The system includes 17 planned backup skills organized into eight categories.

| Category | Skill |
|---|---|
| Reverse Engineering | `reverse-engineering` |
| Reverse Engineering | `saas-reverse-engineering` |
| Front-End | `frontend-development` |
| Front-End | `web-design-guidelines` |
| Front-End | `responsive-ui` |
| Front-End | `mobile-ui` |
| Back-End | `api-design` |
| Back-End | `backend-architecture` |
| Back-End | `database-optimization` |
| Back-End | `authentication-security` |
| Testing | `unit-testing` |
| Testing | `integration-testing` |
| Pull Requests | `pr-management` |
| DevOps | `devops-pipeline` |
| Code Review | `code-review-quality` |
| Code Review | `code-review-security` |
| Code Review | `code-review-performance` |

These identifiers describe planned skill capabilities. Their presence in the catalog does not guarantee that they are installed or executable.

Backup skills must only be recommended when an actual capability gap has been identified.

---

## Context Preservation Protocol

Every task processed by ultramind-skill must maintain a complete representation of the relevant user context.

### Original Requirements

All user-provided requirements must be preserved.

### Technical Constraints

Technology choices, architecture restrictions, compatibility requirements, and implementation limitations must remain intact.

### User Decisions

Previously confirmed decisions must be respected unless the user explicitly changes them.

### Unresolved Questions

Ambiguous or conflicting requirements must be tracked rather than silently resolved.

### Proposed Changes

Any proposed removal, replacement, or significant modification must be clearly distinguished from approved requirements.

### Supporting Skill Findings

Information produced by supporting skills should enrich the analysis without overwriting or discarding the original context.

When multiple skills provide conflicting recommendations, ultramind-skill must identify the disagreement, evaluate the available evidence, and consult the user when the conflict affects the requested outcome.

---

## Operational Workflow

### Phase 1 — Request Understanding

Analyze the complete request and identify all explicit and implicit requirements supported by the available context.

### Phase 2 — Context Preservation

Record and retain relevant requirements, constraints, decisions, dependencies, and unresolved questions.

### Phase 3 — Skill Discovery

Discover skills actually available in the environment and inspect their documented capabilities.

### Phase 4 — Collaborative Analysis

Use relevant installed skills as supporting resources when additional technical analysis is beneficial.

### Phase 5 — Skill Matching

Compare task requirements with installed skill capabilities.

### Phase 6 — Gap Detection

Identify requirements that cannot be fully addressed by available skills.

### Phase 7 — Backup Skill Evaluation

Consult the backup catalog and recommend additional skills only where necessary.

### Phase 8 — User Consultation

Request clarification or authorization for decisions that would change established requirements, discard information, or introduce significant scope changes.

### Phase 9 — Orchestration Planning

Define selected skills, responsibilities, dependencies, execution order, and validation criteria.

### Phase 10 — Execution and Validation

Coordinate execution when supported, validate the results, and ensure that no original requirement has been silently omitted.

---

## Core Rules

1. **NEVER remove user-provided information without authorization.**
2. **NEVER silently discard project requirements or context.**
3. **NEVER change the intended scope independently.**
4. **ALWAYS preserve the original meaning of user instructions.**
5. **ALWAYS consult the user when a decision requires removing or materially changing information.**
6. **USE other relevant skills as supporting resources whenever they can improve the analysis or execution.**
7. **NEVER allow supporting skills to override user requirements.**
8. **ALWAYS prioritize appropriate installed skills.**
9. **ONLY recommend backup skills when an actual capability gap exists.**
10. **NEVER assume that a skill is installed or available.**
11. **NEVER invent skill capabilities, tool results, or execution outcomes.**
12. **ALWAYS respect technical constraints and previously confirmed decisions.**
13. **ALWAYS identify unresolved conflicts instead of silently choosing an interpretation.**
14. **NEVER perform destructive or irreversible actions without the required authorization.**
15. **ALWAYS explain meaningful recommendations and trade-offs.**
16. **NEVER confuse skill recommendation with successful skill execution.**
17. **ALWAYS validate that the final plan covers the original requirements.**

---

## Planned Project Structure

```text
ultramind-skill/
├── README.md
├── SKILL.md
├── config/
│   ├── matching-rules.yaml
│   ├── orchestration-rules.yaml
│   └── context-preservation.yaml
├── references/
│   ├── reserve-skills.md
│   ├── selection-strategy.md
│   ├── execution-workflow.md
│   └── collaboration-policy.md
└── examples/
    ├── frontend-example.md
    ├── backend-example.md
    ├── fullstack-example.md
    └── multi-skill-example.md
```

The project structure separates operational instructions, skill selection rules, context preservation policies, and practical examples.

---

## Future Improvements

Potential enhancements include:

- Dynamic skill discovery.
- Configurable backup skill catalogs.
- Multi-agent orchestration.
- Skill compatibility scoring.
- Context integrity validation.
- Requirement traceability.
- User approval checkpoints.
- Conflict detection between supporting skills.
- Recommendation history.
- Skill execution feedback.
- Automated validation of requirement coverage.

All future enhancements must preserve the fundamental principles of user control, information integrity, and collaborative decision-making.

---

## Core Philosophy

> **Preserve everything that matters. Never discard information independently. Consult the user when decisions affect requirements. Use existing skills as collaborators. Recommend only what is necessary.**

**ultramind-skill exists to enhance the user's capabilities, not to replace the user's decisions.**

Its intelligence should be demonstrated through accurate analysis, careful orchestration, transparent recommendations, and strict respect for the information and instructions provided by the user.