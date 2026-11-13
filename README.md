# Skill ultramind

**Orquestração inteligente, descoberta e recomendação de skills para agentes de IA.**

## Visão geral

O **Skill ultramind** é uma Meta-Skill desenvolvida para analisar solicitações, compreender o contexto de um projeto e selecionar as skills mais adequadas para realizar uma tarefa.

Seu principal objetivo é aproveitar ao máximo as skills já disponíveis no ambiente, evitando recomendações desnecessárias e identificando possíveis lacunas de capacidade.

Quando uma tarefa exige uma competência que não está coberta pelas skills instaladas, o Skill ultramind consulta um catálogo de **17 skills de reserva**, organizadas por especialidade.

A Meta-Skill não substitui as demais skills. Sua função é atuar como uma camada de inteligência responsável pela descoberta, seleção, recomendação e organização das skills utilizadas durante a execução.

## Objetivos

- Identificar automaticamente as skills disponíveis no ambiente.
- Interpretar a solicitação e o contexto fornecido pelo usuário.
- Selecionar as skills mais adequadas para cada tarefa.
- Priorizar skills já instaladas.
- Evitar skills redundantes ou incompatíveis.
- Identificar competências ausentes.
- Recomendar skills de reserva quando necessário.
- Definir a ordem lógica de utilização das skills.
- Considerar tecnologias, arquitetura, dependências e restrições do projeto.
- Explicar por que cada skill foi selecionada.
- Evitar recomendar skills sem relação direta com a tarefa.

## Arquitetura de funcionamento

O Skill ultramind utiliza uma arquitetura baseada em cinco componentes principais.

### 1. Skill Discovery Engine

Responsável pela descoberta das skills disponíveis.

Deve identificar:

- Nome e descrição da skill.
- Capacidades e responsabilidades.
- Instruções de utilização.
- Requisitos e dependências.
- Ferramentas necessárias.
- Limitações conhecidas.

A descoberta deve utilizar os mecanismos disponibilizados pelo ambiente, sem presumir que uma skill está instalada apenas porque seu nome aparece no catálogo de reserva.

### 2. Context Analysis Engine

Responsável por compreender a solicitação do usuário.

Analisa:

- Objetivo principal.
- Requisitos funcionais e não funcionais.
- Tecnologias utilizadas.
- Estrutura e arquitetura do projeto.
- Restrições técnicas.
- Critérios de qualidade.
- Resultados esperados.

O sistema deve utilizar o contexto disponível e solicitar esclarecimentos somente quando informações essenciais estiverem ausentes.

### 3. Skill Matching Engine

Responsável por comparar os requisitos da tarefa com as capacidades das skills descobertas.

Os principais critérios de seleção são:

| Critério | Peso sugerido |
|---|---|
| Compatibilidade com a tarefa | 35% |
| Compatibilidade com o contexto técnico | 25% |
| Cobertura dos requisitos | 20% |
| Compatibilidade com dependências | 10% |
| Especialização e adequação | 10% |

Os pesos são parâmetros iniciais e podem ser ajustados.

A pontuação serve para comparar candidatas, mas não substitui a verificação de requisitos obrigatórios, permissões e disponibilidade real.

### 4. Skill Fallback Engine

Responsável por identificar lacunas e consultar o catálogo de skills de reserva.

Seu funcionamento segue três princípios:

**Prioridade:** uma skill instalada e adequada deve ser escolhida antes de uma alternativa de reserva.

**Complementaridade:** uma skill de reserva pode ser recomendada quando acrescentar uma competência necessária que não está coberta.

**Disponibilidade:** uma skill de reserva não pode ser considerada executável até que sua implementação e suas dependências estejam acessíveis.

O sistema deve distinguir claramente:

- Skill instalada e disponível.
- Skill de reserva disponível.
- Skill de reserva recomendada, mas não instalada.
- Competência não atendida pelo catálogo.

### 5. Skill Orchestration Engine

Responsável por organizar a utilização das skills selecionadas.

Define:

- Ordem de execução.
- Dependências entre etapas.
- Entradas necessárias.
- Saídas esperadas.
- Critérios de conclusão.
- Pontos de validação.

Quando houver suporte no ambiente, a Meta-Skill poderá orientar a execução sequencial ou paralela de skills independentes.

Caso contrário, deverá apresentar um plano de execução, sem afirmar que executou ações que não foram realizadas.

---

## Catálogo de skills de reserva

O catálogo inicial contém **17 skills**, distribuídas em oito categorias.

Os identificadores abaixo representam capacidades planejadas. Cada skill deverá ter uma implementação própria ou uma referência verificável antes de ser utilizada.

### 1. Engenharia reversa

**`reverse-engineering`**

Responsável pela análise e compreensão de sistemas existentes.

Capacidades:

- Analisar código-fonte e dependências.
- Identificar arquitetura e padrões de projeto.
- Reconstruir fluxos e regras de negócio.
- Mapear componentes e integrações.
- Documentar comportamentos existentes.
- Identificar oportunidades de refatoração.

**`saas-reverse-engineering`**

Especializada na análise estrutural e funcional de aplicações SaaS.

Capacidades:

- Analisar funcionalidades e módulos de produtos SaaS.
- Identificar jornadas de usuário.
- Mapear fluxos de autenticação e permissões.
- Analisar modelos de assinatura e cobrança.
- Reconstruir requisitos e arquitetura conceitual.
- Identificar funcionalidades necessárias para desenvolver soluções semelhantes.

A análise deve respeitar autorizações, licenças, privacidade e limites de acesso.

### 2. Front-end e experiência do usuário

**`frontend-development`**

- Desenvolvimento de componentes e interfaces.
- Integração com APIs.
- Gerenciamento de estados.
- Organização de projetos front-end.
- Reutilização e manutenção de componentes.

**`web-design-guidelines`**

- Avaliação de usabilidade.
- Acessibilidade.
- Hierarquia visual.
- Consistência de componentes.
- Padrões de navegação e formulários.

**`responsive-ui`**

- Layouts responsivos.
- Breakpoints.
- Flexbox e CSS Grid.
- Adaptação de componentes.
- Compatibilidade entre tamanhos de tela.

**`mobile-ui`**

- Interfaces mobile-first.
- Navegação mobile.
- Componentes adequados para toque.
- Ergonomia e legibilidade.
- Adaptação para diferentes dispositivos móveis.

### 3. Back-end

**`api-design`**

- Arquitetura de APIs REST.
- Contratos de entrada e saída.
- Validação de requisições.
- Tratamento de erros.
- Versionamento.
- Documentação OpenAPI.

**`backend-architecture`**

- Organização de camadas.
- Separação de responsabilidades.
- Arquitetura modular.
- Padrões de projeto.
- Serviços e regras de negócio.
- Escalabilidade e manutenção.

**`database-optimization`**

- Otimização de consultas SQL.
- Análise de índices.
- Identificação de gargalos.
- Estratégias de paginação.
- Problemas de consultas N+1.
- Transações e desempenho de persistência.

**`authentication-security`**

- Autenticação e autorização.
- JWT, sessões e OAuth 2.0.
- Controle de acesso baseado em papéis.
- Proteção de endpoints.
- Gerenciamento seguro de credenciais.
- Práticas de segurança para APIs.

### 4. Testes

**`unit-testing`**

- Criação de testes unitários.
- Testes de regras de negócio.
- Uso de mocks e stubs.
- Validação de cenários de erro.
- Testes de regressão.
- Análise de cobertura.

**`integration-testing`**

- Testes de integração entre componentes.
- Validação de endpoints.
- Testes com banco de dados.
- Integração com serviços externos.
- Verificação de contratos.
- Testes de fluxos completos entre camadas.

### 5. Pull Requests

**`pr-management`**

- Preparação e organização de Pull Requests.
- Análise das alterações propostas.
- Elaboração de descrições.
- Verificação de critérios de aceite.
- Checklists de revisão.
- Identificação de riscos e impactos.
- Orientação para resolução de conflitos.

### 6. DevOps

**`devops-pipeline`**

- Configuração de pipelines CI/CD.
- Automação de builds.
- Execução automatizada de testes.
- Docker e conteinerização.
- Configuração de ambientes.
- Deploy e rollback.
- Gerenciamento de variáveis e segredos.
- Monitoramento básico de aplicações.

### 7. Code Review

**`code-review-quality`**

Focada na qualidade e manutenção do código.

- Legibilidade.
- Complexidade.
- Duplicação.
- Organização e modularidade.
- Princípios SOLID.
- Code smells.
- Possíveis refatorações.

**`code-review-security`**

Focada em vulnerabilidades e riscos.

- Falhas de autenticação e autorização.
- Injeção SQL.
- XSS e CSRF.
- Exposição de informações sensíveis.
- Dependências vulneráveis.
- Configurações inseguras.
- Validação de entradas.

**`code-review-performance`**

Focada em eficiência e escalabilidade.

- Gargalos de processamento.
- Consultas ineficientes.
- Consumo excessivo de memória.
- Operações bloqueantes.
- Concorrência.
- Estratégias de cache.
- Escalabilidade e uso de recursos.

---

## Estratégia de seleção

O Skill ultramind deve seguir a seguinte hierarquia:

1. Skills instaladas que atendam integralmente à tarefa.
2. Combinações de skills instaladas que atendam aos requisitos.
3. Skills instaladas complementadas por skills de reserva disponíveis.
4. Recomendações de skills de reserva ainda não instaladas.
5. Identificação explícita de lacunas não atendidas.

A Meta-Skill deve selecionar o menor conjunto suficiente de skills, sem sacrificar requisitos importantes.

Uma skill altamente especializada deve ser priorizada quando sua especialização for relevante. Entretanto, uma skill mais abrangente poderá ser escolhida quando cobrir adequadamente todos os requisitos com menos dependências.

## Fluxo operacional

**Etapa 1 — Receber a solicitação**

Interpretar a tarefa e identificar o resultado esperado.

**Etapa 2 — Analisar o contexto**

Identificar tecnologias, restrições, requisitos e informações do projeto.

**Etapa 3 — Descobrir skills**

Consultar as skills realmente disponíveis no ambiente.

**Etapa 4 — Avaliar compatibilidade**

Comparar as capacidades encontradas com os requisitos da tarefa.

**Etapa 5 — Identificar lacunas**

Determinar quais requisitos não são atendidos pelas skills instaladas.

**Etapa 6 — Consultar reservas**

Buscar alternativas no catálogo de reserva apenas para as lacunas identificadas.

**Etapa 7 — Construir o plano**

Definir skills selecionadas, justificativas, dependências e ordem de utilização.

**Etapa 8 — Validar a recomendação**

Verificar cobertura, compatibilidade, disponibilidade e possíveis redundâncias.

**Etapa 9 — Apresentar ou executar**

Entregar o plano de utilização ou encaminhar a execução quando o ambiente permitir.

---

## Exemplo de utilização

### Solicitação

> Desenvolva um sistema SaaS de gerenciamento financeiro utilizando React, Spring Boot e PostgreSQL. A aplicação precisa ser responsiva, possuir autenticação e ter testes automatizados.

### Análise do ultramind-skill

**Contexto identificado:**

- Aplicação SaaS.
- Front-end em React.
- Back-end em Spring Boot.
- Banco de dados PostgreSQL.
- Autenticação.
- Responsividade.
- Testes automatizados.

### Resultado esperado

| Skill | Responsabilidade | Prioridade |
|---|---|---|
| `frontend-development` | Desenvolver interface React | Alta |
| `responsive-ui` | Garantir responsividade | Alta |
| `backend-architecture` | Estruturar o back-end | Alta |
| `api-design` | Definir contratos REST | Alta |
| `authentication-security` | Implementar autenticação | Alta |
| `unit-testing` | Validar regras de negócio | Alta |
| `integration-testing` | Validar integrações | Alta |
| `code-review-security` | Revisar segurança | Complementar |

As skills serão classificadas como instaladas ou de reserva conforme a descoberta realizada no ambiente.

### Ordem recomendada

1. Análise dos requisitos e arquitetura.
2. Definição dos contratos da API.
3. Implementação de autenticação e back-end.
4. Desenvolvimento da interface.
5. Adaptação responsiva.
6. Testes unitários e de integração.
7. Revisão de segurança.

A ordem poderá ser modificada quando houver dependências ou atividades que possam ocorrer em paralelo.

---

## Formato de resposta da Meta-Skill

Sempre que uma seleção de skills for solicitada, o ultramind skill deverá apresentar:

**Resumo da tarefa:** interpretação objetiva do pedido.

**Contexto identificado:** stack, arquitetura, restrições e requisitos relevantes.

**Skills selecionadas:** nome, responsabilidade e justificativa.

**Origem:** instalada, reserva disponível ou reserva não instalada.

**Skills complementares:** somente quando agregarem valor real.

**Ordem de execução:** sequência recomendada e dependências.

**Lacunas:** requisitos que ainda não podem ser atendidos.

**Observações:** riscos, limitações ou informações pendentes.

O formato deve ser proporcional à complexidade da solicitação. Tarefas simples não devem produzir relatórios excessivamente longos.

---

## Regras fundamentais

1. Nunca presumir que uma skill está instalada.
2. Nunca inventar capacidades ou ferramentas.
3. Priorizar skills existentes e adequadas.
4. Utilizar reservas somente quando houver necessidade.
5. Não recomendar todas as skills de uma categoria automaticamente.
6. Evitar sobreposição desnecessária de responsabilidades.
7. Respeitar as restrições técnicas do projeto.
8. Considerar dependências e compatibilidade.
9. Explicar a seleção de maneira objetiva.
10. Não afirmar que uma skill foi executada quando apenas foi recomendada.
11. Não instalar, modificar ou remover skills sem autorização.
12. Não executar ações destrutivas sem as confirmações necessárias.
13. Reavaliar a seleção quando o contexto ou os requisitos mudarem.
14. Não tratar a pontuação de compatibilidade como garantia de qualidade.
15. Preservar as instruções e limites de segurança do ambiente.

---

## Estrutura planejada do projeto

```text
ultramind-skill/
├── README.md
├── SKILL.md
├── config/
│   ├── matching-rules.yaml
│   └── orchestration-rules.yaml
├── references/
│   ├── reserve-skills.md
│   ├── selection-strategy.md
│   └── execution-workflow.md
└── examples/
    ├── frontend-example.md
    ├── backend-example.md
    └── fullstack-example.md
```

**README.md:** documentação geral do projeto.

**SKILL.md:** instruções operacionais da Meta-Skill.

**config/:** parâmetros de seleção, compatibilidade e orquestração.

**references/:** catálogo de reserva e regras detalhadas.

**examples/:** demonstrações práticas de utilização.

Essa estrutura é uma proposta inicial e poderá ser adaptada ao formato de skills suportado pelo ambiente de instalação.

---

## Evolução futura

O Skill ultramind foi pensado para permitir a expansão gradual do catálogo e dos mecanismos de recomendação.

Possíveis melhorias incluem:

- Catálogo configurável de skills.
- Descoberta de novas skills em fontes autorizadas.
- Detecção de conflitos entre skills.
- Histórico de recomendações e resultados.
- Avaliação da eficácia das seleções.
- Perfis de seleção por tipo de projeto.
- Suporte a fluxos com múltiplos agentes.
- Reavaliação automática após mudanças no contexto.

## Princípio central

> **Use o que já existe. Identifique o que falta. Recomende apenas o necessário. Organize a execução com base no contexto.**

O Skill ultramind deve funcionar como uma camada de decisão inteligente, garantindo que cada tarefa utilize as competências mais adequadas disponíveis no ambiente, com o mínimo de redundância e o máximo de coerência técnica.