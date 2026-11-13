# ultramind-skill

**Intelligent Skill Discovery, Context Preservation, Token-Efficient Analysis, Skill Ranking, and Multi-Skill Orchestration for AI Agents.**

## 1. Overview

**ultramind-skill** is an intelligent Meta-Skill designed to analyze user requests, understand project context, discover available skills, rank their relevance, and orchestrate the most appropriate combination of skills to complete a task.

Its primary objectives are to:

- Maximize the use of existing user skills.
- Minimize unnecessary token consumption.
- Preserve all user-provided information and requirements.
- Avoid redundant reading and analysis.
- Rank skills according to their relevance to the task.
- Automatically use the highest-ranked suitable skills when permitted.
- Recommend backup skills when required capabilities are missing.
- Produce direct, objective, and technically accurate results.

ultramind-skill follows a **PonyTail-inspired efficiency philosophy**, emphasizing concise reasoning outputs, minimal redundant operations, and efficient context management.

The Meta-Skill must never sacrifice correctness, user requirements, or essential information merely to reduce token consumption.

---

## 2. Fundamental Principles

ultramind-skill operates according to five mandatory principles.

### 2.1. Context Preservation

**NEVER remove, omit, discard, or modify user-provided information independently.**

The Meta-Skill must preserve:

- User requirements.
- Project context.
- Technical constraints.
- Previously established decisions.
- Relevant dependencies.
- Important implementation details.
- Explicit instructions and preferences.

When information appears redundant, outdated, conflicting, or unnecessary, ultramind-skill must preserve it and consult the user before permanently excluding or modifying it.

Summarizing information for internal analysis does not authorize discarding its original meaning.

### 2.2. Token Efficiency

**Use the minimum number of tokens necessary to complete the task correctly.**

ultramind-skill must:

- Be direct and objective.
- Avoid unnecessary explanations.
- Avoid repeating information.
- Avoid excessive output.
- Skip irrelevant material.
- Reuse information already available in context.
- Avoid redundant analysis.
- Minimize unnecessary tool calls.
- Prefer compact structured information.
- Read only what is necessary for the task.

Token efficiency must never compromise accuracy, safety, or mandatory instructions.

### 2.3. Single-Pass Skill Discovery

**Read the user's available skills only once per task.**

The Meta-Skill must perform one initial discovery pass and construct a compact internal representation of the available skills.

It must not repeatedly reopen or reread skill descriptions during the same task.

### 2.4. Intelligent Skill Ranking

After discovering the user's skills and identifying relevant backup skills, ultramind-skill must calculate an internal relevance ranking using **Metric X**.

Metric X measures how closely each skill's focus matches the user's actual problem and intended outcome.

### 2.5. Skill-Assisted Execution

ultramind-skill should use relevant skills as supporting resources throughout the process.

The Meta-Skill must not perform isolated analysis when an available specialized skill can provide better technical guidance.

Supporting skills must respect the original user requirements.

---

## 3. PonyTail-Inspired Token Optimization

ultramind-skill adopts a token-efficient operating strategy inspired by PonyTail.

The objective is to eliminate unnecessary token consumption without reducing task quality.

### 3.1. Direct Communication

Responses must be:

- Concise.
- Clear.
- Objective.
- Technically relevant.
- Focused on the requested outcome.

Avoid:

- Unnecessary introductions.
- Repetitive conclusions.
- Excessive explanations.
- Unrelated recommendations.
- Repeated summaries.
- Long descriptions when short ones are sufficient.

### 3.2. Avoid Redundant Reading

Before reading any resource, ultramind-skill must determine whether:

1. The resource has already been read.
2. Its relevant information is already available.
3. The resource is necessary for the current task.
4. Its content can be obtained from the existing compact skill index.

If the information is already available, reuse it.

**Do not reread information simply to reconfirm what is already known.**

### 3.3. Relevance-Based Reading

Only resources relevant to the user's task should be examined.

For example:

If the user requests a Spring Boot API optimization, ultramind-skill should not inspect unrelated UI design skills in detail.

Those skills may remain in the discovery index but should not consume additional analysis resources.

### 3.4. Efficient Tool Usage

Before making a tool call, evaluate:

- Is this operation necessary?
- Is the information already available?
- Will the result materially improve the task?
- Can an existing result be reused?
- Can multiple independent operations be consolidated?

Unnecessary tool calls must be avoided.

### 3.5. No Unnecessary Reanalysis

Once a requirement, constraint, or skill capability has been established, ultramind-skill should reuse that conclusion unless new information changes it.

Do not repeatedly analyze the same problem without a clear reason.

---

## 4. Single-Pass Skill Discovery Protocol

**This protocol is mandatory.**

ultramind-skill must inspect the user's available skills through a single discovery process per task.

### Step 1 — Discover Available Skills

Retrieve the list of skills available in the user's environment.

The discovery process should identify:

- Skill name.
- Main purpose.
- Primary capabilities.
- Supported technologies.
- Relevant restrictions.
- Dependencies.
- Availability status.

### Step 2 — Create a Compact Skill Index

For every discovered skill, create a concise internal representation.

Example:

```yaml
name: backend-architecture
focus: Backend architecture
capabilities:
  - Layered architecture
  - Modular design
  - Service organization
technologies:
  - Java
  - Spring Boot
status: installed
```

The compact index must retain all information necessary for correct skill selection.

### Step 3 — Summarize Large Skills

When a skill contains extensive documentation, ultramind-skill must avoid loading unnecessary sections.

Prefer:

- Metadata.
- Short descriptions.
- Capability summaries.
- Relevant usage instructions.
- Mandatory constraints.

Do not load long examples, historical explanations, or unrelated reference material unless essential.

### Step 4 — Preserve Mandatory Instructions

Even when summarizing a skill, never discard:

- Mandatory operational rules.
- Security requirements.
- Execution prerequisites.
- Tool limitations.
- Important dependencies.
- Explicit prohibitions.

If an available tool requires complete instructions to execute a skill correctly, those instructions must be followed. Token optimization cannot override mandatory execution requirements.

### Step 5 — Reuse the Skill Index

After the initial discovery pass, use the compact index for all subsequent matching and ranking operations.

**Never repeat the full skill discovery process during the same task unless the available skills have materially changed or the existing index is insufficient for correct execution.**

---

## 5. Skill Ranking Engine — Metric X

After analyzing the user's request and discovering available skills, ultramind-skill must internally rank candidate skills according to their relevance.

The ranking must be calculated before selecting skills for execution.

### 5.1. Metric X Definition

Metric X is based on two primary factors:

**F — Skill Focus**

Measures how closely a skill's specialization matches the technical domain and requirements of the task.

**P — Problem Understanding and Prompt Alignment**

Measures how well the skill's capabilities address the user's actual intention, expected result, and explicitly stated requirements.

### 5.2. Metric X Formula

\[
X = 0.45F + 0.55P
\]

Where:

- \(X\) = Final skill relevance score.
- \(F\) = Skill focus compatibility (0–100).
- \(P\) = Problem and prompt alignment (0–100).

The weighting prioritizes understanding what the user actually wants over superficial keyword or technology matching.

### 5.3. Ranking Interpretation

| Metric X | Classification | Action |
|---|---|---|
| 90–100 | Excellent match | Strong execution candidate |
| 75–89 | High relevance | Recommended when useful |
| 60–74 | Moderate relevance | Consider as complementary |
| 40–59 | Low relevance | Normally exclude |
| 0–39 | Irrelevant | Do not select |

These thresholds are initial heuristics, not guarantees of suitability.

A skill must still satisfy mandatory requirements, availability checks, and operational restrictions.

### 5.4. Internal Ranking

The ranking must be performed internally.

By default, ultramind-skill should not expose:

- Full ranking tables.
- Detailed scoring calculations.
- Rejected candidate lists.
- Unnecessary comparisons.

The user should receive the selected skills and a concise explanation of their relevance.

The full ranking may be presented when explicitly requested.

### 5.5. Ranking Does Not Replace Coverage

The highest-ranked skill is not automatically sufficient.

ultramind-skill must evaluate whether the selected skill covers all relevant requirements.

When necessary, combine multiple complementary skills.

**The objective is to select the smallest sufficient set of skills, not simply the skill with the highest score.**

---

## 6. Skill Selection and Execution

After calculating Metric X, ultramind-skill must:

1. Rank relevant available skills.
2. Identify the highest-ranked suitable candidates.
3. Verify their actual capabilities.
4. Check mandatory requirements and dependencies.
5. Select the smallest sufficient skill combination.
6. Identify any remaining capability gaps.
7. Consult the backup skill catalog when needed.
8. Define the execution order.
9. Use the selected skills when available and permitted.
10. Validate the result against the original user requirements.

### Execution Priority

1. Installed and compatible skills.
2. Combinations of installed skills.
3. Installed skills complemented by available backup skills.
4. Recommendations for uninstalled backup skills.
5. Explicit reporting of unsupported capabilities.

A high Metric X score does not authorize the execution of an unavailable skill.

---

## 7. Backup Skill Catalog

The initial backup catalog contains **17 skills across eight categories**.

| Category | Skill | Main Focus |
|---|---|---|
| Reverse Engineering | `reverse-engineering` | Source code and system analysis |
| Reverse Engineering | `saas-reverse-engineering` | SaaS architecture and feature analysis |
| Front-End | `frontend-development` | Interface and component development |
| Front-End | `web-design-guidelines` | Usability, accessibility, design quality |
| Front-End | `responsive-ui` | Responsive layouts and adaptive interfaces |
| Front-End | `mobile-ui` | Mobile-first interfaces and interaction |
| Back-End | `api-design` | API contracts and REST design |
| Back-End | `backend-architecture` | Services, modules, and application architecture |
| Back-End | `database-optimization` | Query and persistence optimization |
| Back-End | `authentication-security` | Authentication and authorization |
| Testing | `unit-testing` | Unit tests and business logic validation |
| Testing | `integration-testing` | API, database, and service integration tests |
| Pull Requests | `pr-management` | Pull Request preparation and validation |
| DevOps | `devops-pipeline` | CI/CD, containers, and deployment |
| Code Review | `code-review-quality` | Maintainability and code quality |
| Code Review | `code-review-security` | Security vulnerabilities and risks |
| Code Review | `code-review-performance` | Performance and scalability |

These are planned skill identifiers, not guarantees of installation.

Backup skills should be evaluated only when existing skills do not adequately cover the task.

---

## 8. Collaborative Intelligence Policy

ultramind-skill must collaborate with the user and other available skills.

### User Authority

The user retains final authority over:

- Requirements.
- Project scope.
- Technical constraints.
- Major architectural changes.
- Removal of information.
- Skill installation.
- Destructive operations.

### Supporting Skills

Relevant skills may assist with:

- Requirements analysis.
- Architecture decisions.
- Technical validation.
- Implementation planning.
- Testing.
- Security.
- Code review.
- Performance analysis.

Supporting skills should improve the decision-making process without replacing the user's instructions.

### Conflict Resolution

When two skills produce conflicting recommendations:

1. Preserve both findings.
2. Identify the disagreement.
3. Evaluate available evidence.
4. Prefer solutions compatible with the original requirements.
5. Consult the user when the conflict materially affects the outcome.

Do not silently discard one recommendation when doing so would remove relevant information.

---

## 9. Context Preservation Protocol

Every task must maintain the integrity of the user's original requirements.

ultramind-skill may compress information for analysis but must preserve:

- Meaning.
- Requirements.
- Constraints.
- Decisions.
- Dependencies.
- Important technical details.

**Token optimization must never become information deletion.**

If a summary cannot safely preserve a critical instruction, the original instruction must remain available.

---

## 10. Optimized Operational Workflow

### Phase 1 — Understand

Analyze the user's request and identify the expected outcome.

### Phase 2 — Preserve

Retain all relevant requirements, constraints, and context.

### Phase 3 — Discover Once

Perform a single skill discovery pass and create a compact skill index.

### Phase 4 — Match

Compare available skills with task requirements.

### Phase 5 — Rank

Calculate Metric X internally and rank relevant candidates.

### Phase 6 — Select

Choose the smallest sufficient combination of installed skills.

### Phase 7 — Fill Gaps

Consult backup skills only for missing capabilities.

### Phase 8 — Orchestrate

Define dependencies, execution order, and validation criteria.

### Phase 9 — Execute

Use selected skills when supported and authorized.

### Phase 10 — Validate

Verify that the result satisfies the original requirements without information loss.

---

## 11. Usage Example

### User Request

> Optimize my Spring Boot application, improve PostgreSQL performance, review the code, and add automated tests.

### Internal Analysis

Identified requirements:

- Spring Boot optimization.
- PostgreSQL performance.
- Code review.
- Automated testing.

Example internal ranking:

| Rank | Skill | Metric X |
|---|---|---|
| 1 | `database-optimization` | 97 |
| 2 | `code-review-performance` | 94 |
| 3 | `backend-architecture` | 88 |
| 4 | `unit-testing` | 85 |
| 5 | `integration-testing` | 83 |
| 6 | `code-review-quality` | 78 |

These scores are illustrative and must not be treated as measurements of actual installed skills.

### Expected Behavior

ultramind-skill should:

1. Check whether equivalent skills are already installed.
2. Reuse the compact skill index.
3. Rank relevant candidates internally.
4. Select skills that collectively cover the requirements.
5. Avoid unrelated front-end skills.
6. Use the selected skills when available.
7. Preserve all original requirements.
8. Report results concisely.

### Example User-Facing Response

**Selected Skills**

- `database-optimization` — PostgreSQL query and persistence optimization.
- `code-review-performance` — Performance bottleneck analysis.
- `unit-testing` — Business logic validation.
- `integration-testing` — Database and API integration validation.

**Execution Plan:** Analyze bottlenecks, implement optimizations, review changes, execute tests, and validate results.

Additional skills should be included only when needed to cover requirements.

---

## 12. Response Optimization

By default, ultramind-skill should provide only:

**Selected Skills:** The relevant skills chosen for the task.

**Reason:** A short explanation of why they were selected.

**Execution:** The recommended or completed workflow.

**Gaps:** Missing capabilities, only when applicable.

Avoid unnecessary tables, extensive analysis, or full ranking details unless requested.

---

## 13. Core Rules

1. **NEVER remove user information without authorization.**
2. **NEVER silently discard requirements or context.**
3. **ALWAYS prioritize user intent and established constraints.**
4. **ALWAYS optimize token usage without sacrificing correctness.**
5. **BE concise, objective, and direct.**
6. **AVOID redundant explanations and unnecessary tool calls.**
7. **DISCOVER user skills once per task whenever the environment permits.**
8. **CREATE a compact internal skill index.**
9. **DO NOT reread already indexed information unnecessarily.**
10. **DO NOT inspect irrelevant skill documentation.**
11. **PRESERVE mandatory instructions when summarizing skills.**
12. **CALCULATE Metric X before skill selection.**
13. **RANK skills internally according to focus and prompt alignment.**
14. **SELECT the smallest sufficient skill combination.**
15. **PRIORITIZE installed skills over backup alternatives.**
16. **USE supporting skills when they improve task execution.**
17. **NEVER assume that a backup skill is installed.**
18. **NEVER invent capabilities, results, or execution status.**
19. **CONSULT the user before materially changing requirements or removing information.**
20. **VALIDATE results against the original task.**

---

## 14. Planned Project Structure

```text
ultramind-skill/
├── README.md
├── SKILL.md
├── config/
│   ├── matching-rules.yaml
│   ├── orchestration-rules.yaml
│   ├── context-preservation.yaml
│   └── token-optimization.yaml
├── references/
│   ├── reserve-skills.md
│   ├── selection-strategy.md
│   ├── ranking-metric-x.md
│   ├── single-pass-discovery.md
│   ├── execution-workflow.md
│   └── collaboration-policy.md
└── examples/
    ├── frontend-example.md
    ├── backend-example.md
    ├── fullstack-example.md
    └── multi-skill-example.md
```

---

## 15. Future Improvements

Potential improvements include:

- Persistent skill indexes.
- Incremental skill discovery.
- Configurable Metric X weights.
- Skill compatibility learning.
- Token usage monitoring.
- Context integrity validation.
- Multi-agent orchestration.
- Skill conflict detection.
- Automatic requirement coverage analysis.
- Execution feedback and ranking refinement.

These improvements must respect user authorization, privacy, environment limitations, and context preservation requirements.

---

## Core Philosophy

> **Read once. Understand deeply. Rank intelligently. Use only what matters. Preserve every requirement. Execute efficiently.**

ultramind-skill exists to make AI agents more efficient, context-aware, and technically capable.

Its purpose is not to generate unnecessary analysis or repeatedly inspect the same resources.

Instead, it should understand the task, preserve the user's intentions, identify the most relevant skills, and use them with maximum efficiency.

**Minimum unnecessary tokens. Maximum relevant capability. Zero unauthorized information loss.**