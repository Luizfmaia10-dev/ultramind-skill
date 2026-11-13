# Backup capabilities — 17 slots

**Purpose:** recommend missing skills after checking installed capabilities. The identifiers below are **capability aliases**, not proof of a real installed skill. Public GitHub examples are **potential alternatives**, not exact equivalents or automatically trusted dependencies. Confirm the repository, license, contents, compatibility, maintenance, and user authorization before installing anything. Do not fetch or execute third-party code automatically.

| Slot | Capability needed | Public GitHub candidates / notes |
|---|---|---|
| `reverse-engineering` | Understand authorized source/code architecture, behavior, dependencies | `wshobson/agents` lists protocol/binary reverse-engineering skills (narrower than general code reconstruction). For general architecture extraction, search currently installed project/codebase analysis skills first. |
| `saas-reverse-engineering` | Authorized SaaS journey, features, model, UX and behavior mapping | [alextnetto/res — `reverse-engineering-saas`](https://github.com/alextnetto/res/blob/main/skills/reverse-engineering-saas/SKILL.md) (name differs from alias). |
| `frontend-development` | Implement web UI/components | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) (`vercel-react-best-practices`, React-focused); [wshobson/agents](https://github.com/wshobson/agents) has complementary front-end skills. |
| `web-design-guidelines` | Review accessible, consistent web UX | [vercel-labs/agent-skills — `web-design-guidelines`](https://github.com/vercel-labs/agent-skills); [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill). |
| `responsive-ui` | Adaptive layouts, breakpoints, containers | [wshobson/agents](https://github.com/wshobson/agents) lists `responsive-design`; Vercel design guidelines may be complementary. |
| `mobile-ui` | Mobile-first and native interaction guidance | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) (`vercel-react-native-skills`); [wshobson/agents](https://github.com/wshobson/agents) lists mobile iOS/Android design skills. |
| `api-design` | REST/GraphQL API contracts, errors, schemas | [wshobson/agents](https://github.com/wshobson/agents) lists `api-design-principles`. |
| `backend-architecture` | Clean/hexagonal architecture, modular services | [wshobson/agents](https://github.com/wshobson/agents) lists `architecture-patterns`. |
| `database-optimization` | SQL performance, indexes, pagination, N+1 | [wshobson/agents](https://github.com/wshobson/agents) lists `postgresql-table-design` and related data skills, **not a verified drop-in generic query optimizer**. |
| `authentication-security` | Authentication, authorization, access policy | [wshobson/agents](https://github.com/wshobson/agents) lists threat-analysis and security-requirement skills; check for exact implementation capability before substituting. |
| `unit-testing` | Unit tests, mocks, regression | [obra/superpowers](https://github.com/obra/superpowers) lists `test-driven-development`; it is a workflow skill, not a framework-specific unit-test generator. |
| `integration-testing` | DB/API/service integration tests | [wshobson/agents](https://github.com/wshobson/agents) lists `temporal-python-testing` (Temporal-specific, **not generic**); seek a matching stack-specific integration skill. |
| `pr-management` | PR description, review, merge readiness | [obra/superpowers](https://github.com/obra/superpowers) lists `requesting-code-review` and `finishing-a-development-branch`. |
| `devops-pipeline` | CI/CD, containers, deploy and rollback | [wshobson/agents](https://github.com/wshobson/agents) lists `gitops-workflow`, `helm-chart-scaffolding`; [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills) lists `deploy-to-vercel`. These cover distinct stacks, not every DevOps platform. |
| `code-review-quality` | Maintainability, complexity, correctness | [obra/superpowers](https://github.com/obra/superpowers) (`requesting-code-review`, `receiving-code-review`); [wshobson/agents](https://github.com/wshobson/agents) (`multi-reviewer-patterns`). |
| `code-review-security` | Vulnerabilities, access flaws, secret exposure | [wshobson/agents](https://github.com/wshobson/agents) lists `sast-configuration` and `stride-analysis-patterns`. |
| `code-review-performance` | Hot paths, latency, CPU/memory, query bottlenecks | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) (`vercel-react-best-practices`, front-end specific); for back-end, seek a stack-matched profiler/reviewer. |

## Required fallback sequence

1. Search *installed* skills in the one-pass inventory; match capabilities, not just names.
2. If an installed skill covers the requirement, use it; no backup needed.
3. Otherwise identify the missing capability slot and relevant GitHub candidate.
4. Mark the candidate `unverified` until its exact identity, availability and contents are checked.
5. Recommend optional installation to the user if beneficial; don't install or execute automatically.
6. If no suitable skill is available, clearly report the gap or use ordinary available tools only when authorized and adequate.

## Reverse engineering safety

Operate only on systems/data the user is authorized to examine. Respect provider terms and security boundaries. Do not bypass authentication, impersonate users, exfiltrate data, or copy protected assets. Prefer clean-room functional descriptions and evidence over cloning proprietary implementations.
