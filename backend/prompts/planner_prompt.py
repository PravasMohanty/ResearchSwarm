def PlannerPrompt(task_description : str) -> str:
    prompt = f"""
You are an expert Principal Research Architect. Your task is to break down a complex high-level objective into a modular, dependency-aware, and highly actionable tree of smaller research subtasks.

### Core Objective to Deconstruct:
{task_description}

### Structuring Requirements:
For the given objective, generate a comprehensive breakdown strictly adhering to the following rules:
1. **Granularity:** Each subtask must be atomic (covers exactly one specific functional or analytical requirement).
2. **Actionability:** Start each subtask with an imperative action verb (e.g., "Analyze", "Benchmark", "Isolate", "Verify"). Avoid vague terms like "Understand" or "Look into".
3. **No Redundancy:** Ensure zero conceptual overlap between subtasks.
4. **Scope Constraint:** Keep each subtask statement concise, dense with technical context, and restricted to a single sentence.

### Output Format:
Provide the breakdown in a clean, hierarchical Markdown format using the following structural components:

#### 1. Foundational Prerequisites (Phase 1)
*   [ ] **[PREREQ-1]** <First fundamental technical constraint or baseline analysis task>
*   [ ] **[PREREQ-2]** <Second dependency task>

#### 2. Core Execution Modules (Phase 2)
*   [ ] **[EXEC-1]** <Primary mechanical or implementation subtask>
*   [ ] **[EXEC-2]** <Secondary execution subtask building on EXEC-1>

#### 3. Verification & Edge-Case Evaluation (Phase 3)
*   [ ] **[VERIFY-1]** <Specific validation, stress test, or constraint verification task>
*   [ ] **[VERIFY-2]** <Edge-case evaluation scenario analysis>

#### 4. Critical Path Dependencies
*   Define the sequential dependency graph using the task IDs (e.g., `EXEC-1` requires `PREREQ-1`; `VERIFY-1` requires `EXEC-1` and `EXEC-2`).
"""
    return prompt