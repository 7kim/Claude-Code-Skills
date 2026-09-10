# PhD Research Proposal

## Title: Suppressing Semantic Hallucinations in Autonomous AI Agents through Bi-Hemispheric Cognitive Rehearsal Gates

### Candidate: [Your Name / Candidate]
### Proposed Field: Computational Cognitive Architectures & AI Safety
### Target Venue: NeurIPS / ICML / Journal of Artificial Intelligence Research

---

## Abstract
Autonomous AI agents powered by Large Language Models (LLMs) suffer from a critical flaw: their autoregressive generation process is linear and unbuffered, committing to and executing token sequences in real time without pre-vocalization verification. This structural limitation manifests as semantic hallucinations, logical inconsistencies, and rapid contextual drift. This research proposes **Anatomically-Partitioned Cognitive Architectures (APCA)**, a novel design paradigm modeled on the functional divisions of the human cerebral cortex. By distributing execution tasks, state monitoring, and RAG retrieval across specialized computational "lobes" working in conjunction within a synchronized, bi-hemispheric system, we introduce a formal pre-execution **Cognitive Rehearsal Gate**. This proposal outlines the empirical methodology to test whether internal simulation, logical auditing, and stylistic compliance loops significantly suppress hallucinations in autonomous code-generation and long-horizon planning tasks.

---

## 1. Introduction & Theoretical Foundation
Modern LLM agents operate primarily on reactive, linear loops (e.g., Act-Sense-Plan cycles). In these architectures, the model's "inner monologue" is exposed directly to the execution channel (such as a terminal sandbox or API router) as it is generated. If the model generates a factually incorrect token, it must either commit to the error or execute costly, external trial-and-error corrections.

In contrast, the human brain mitigates motor and speech errors before they are physically executed. Neurological studies demonstrate that the human cerebral cortex is structurally divided into specialized lobes working in conjunction [1]:
*   The **frontal lobe** manages high-level executive control, planning, and voluntary motor coordination [1].
*   The **parietal lobe** integrates somatosensory feedback (such as pressure and pain) to monitor state changes [1].
*   The **temporal lobe** processes linguistic context and coordinates memory consolidation [1].
*   The **occipital lobe** manages visual and structural spatial recognition [1].

Crucially, the brain utilizes **motor imagery and cognitive rehearsal** (localized in prefrontal and supplementary motor systems) to run silent, internal simulations of planned movements or speech. This allows the brain to evaluate, audit, and refine actions before sending neural impulses down the primary motor cortex to execute physical movement [1].

This research implements this bio-inspired paradigm computationally as a **Bi-Hemispheric Cognitive Rehearsal Gate** inside an integrated agent engine, exploring whether formal internal auditing can transition AI systems from *probabilistic token-generators* to *reflective cognitive agents*.

```
                            ┌────────────────────────┐
                            │    Incoming Prompt     │
                            └───────────┬────────────┘
                                        │
                                        ▼
                  ┌────────────────────────────────────────────┐
                  │          Processing Hemispheres            │
                  │   ┌────────────────────┬───────────────┐   │
                  │   │   Left Pipeline    │Right Pipeline │   │
                  │   └─────────┬──────────┴───────┬───────┘   │
                  │             │                  │           │
                  │             ▼                  ▼           │
                  │         [Drafting]         [Drafting]      │
                  └─────────────┬──────────────────┬───────────┘
                                │                  │
                                └─────────┬────────┘
                                          │ (Consensus Check)
                                          ▼
                            ┌────────────────────────┐
                            │     Rehearsal Gate     │
                            │  (Internal Simulation) │
                            ├────────────────────────┤
                            │ - Logical Auditor      │
                            │ - Persona Tone Aligner │
                            └───────────┬────────────┘
                                        │
                                        ▼ (Passed Audit)
                            ┌────────────────────────┐
                            │   Physical Execution   │
                            │   (Motor Output / CLI) │
                            └────────────────────────┘
```

---

## 2. Research Questions & Hypotheses

*   **Primary Research Question (RQ1):** Does the introduction of a bi-hemispheric cognitive rehearsal loop (simulating, auditing, and aligning draft outputs prior to execution) significantly reduce semantic and syntactic hallucinations in autonomous code generation compared to standard linear, single-pass agent loops?
*   **Secondary Research Question (RQ2):** How do varying levels of critical judgement (`level_of_judgement`) and factual grounding constraints (`honesty_threshold`) affect the latency, token economy, and success rate of long-horizon software engineering tasks?
*   **Tertiary Research Question (RQ3):** Can a three-tier stratified memory model (L1 Sensory Cache, L2 Episodic Buffer, L3 Semantic RAG) managed by integer-based context-count limits suppress contextual memory drift in multi-hour autonomous development sessions?

### Hypotheses
*   **Hypothesis 1 ($H_1$):** AI agents utilizing a pre-execution rehearsal gate will show a minimum **35% reduction** in executed syntax errors and database schema violations compared to baseline agents without rehearsal.
*   **Null Hypothesis 1 ($H_0$):** There will be no statistically significant difference in hallucination rates or execution failures between agents with and without cognitive rehearsal gates.

---

## 3. Computational Architecture (`Agent_Brain` Framework)
The experimental platform is built upon the **`Agent_Brain` (v18_pass)** codebase, translating biological subdivisions into functional object-oriented classes:

### 3.1. The Frontal Lobe (`CognitiveFunctions`)
Acts as the executive orchestrator. It manages:
*   **`optimize_prompt(prompt_optimization_passes)`**: A pre-execution gate that refines user inputs. It runs either `0` (disabled), `1` (single pass), or `3` (recursive loop-and-optimize) times.
*   **`rehearse()`**: The central rehearsal gate. It intercepts planned outputs and cascades them through:
    1.  `audit_logical_errors_and_hallucinations()`: Analyzes draft code for syntax bugs, invalid library dependencies, and logical flaws.
    2.  `align_persona_and_tone_compliance()`: Strips sycophantic fluff and verifies tone according to the active `personality_style`.

### 3.2. The Parietal Lobe (`ProcessMonitor`)
The somatosensory feedback hub. It monitors system health telemetry and calculates state drift:
*   **`two_point_discrimination(log_discrimination)`**: Distinguishes between critical, blocking exceptions (requiring code changes) and benign, non-blocking warning logs.
*   **`measure_state_drift_distance()`**: Calculates the mathematical distance (L1-norm) between the current runtime state and the target execution plan, triggering a "pain-withdrawal reflex" (emergency halt) if drift limits are exceeded.

### 3.3. The Temporal Lobe (`KnowledgeRetriever`)
Coordinates language validation and a stratified, multi-tier memory system to prevent attention drift:
*   **`l1()` (Sensory Cache):** Immediate working memory. Stores active token streams up to a 1,000,000-token `l1_context_count_limit`.
*   **`l2()` (Episodic Buffer):** Short-term session memory. Receives consolidated, compressed overflows from L1 once the context count limit is breached.
*   **`l3()` (Semantic RAG):** Long-term persistent vector storage, holding project documentation and historical sessions, queried using `retrieval_similarity_threshold`.

---

## 4. Experimental Methodology & Evaluation Design

To empirically evaluate the architecture, we will execute a randomized, controlled trial comparing our bio-inspired APCA engine against standard agent designs.

### 4.1. Variables Matrix
| Variable Type | Metric / Parameter | Values / Settings | Operational Definition |
| :--- | :--- | :--- | :--- |
| **Independent** | Rehearsal Mode | `Enabled` vs. `Disabled` | Toggles the active pre-execution `rehearse()` loop. |
| | Cognitive Depth | `iq_reasoning_depth` | Scaled from `1` to `200` logical planning passes. |
| | Stance Bias | `level_of_judgement` | Scaled from `0.0` (agreeable) to `1.0` (highly critical). |
| | Memory Mode | `Stratified` vs. `Flat` | Toggles L1/L2/L3 context cascading vs. flat context window. |
| **Dependent** | Hallucination Rate | Syntactic & Semantic | \% of generated scripts containing syntax errors or hallucinated API routes. |
| | Task Success Rate | Pass@k | \% of tasks passing unit tests within $k$ execution loops. |
| | Token Economy | Token Consumption | Total tokens consumed per successful task completion. |
| | Execution Latency | Time-to-Success | Wall-clock time (seconds) taken to reach terminal objective. |

### 4.2. Benchmarking Tasks & Datasets
We will evaluate the agent across three high-complexity, long-horizon domains:
1.  **SWE-bench Lite:** Resolving real-world software engineering issues in large, multi-file Python repositories. This directly tests the temporal lobe's ability to navigate directory trees and the frontal lobe's ability to debug code.
2.  **Custom Database Migration (RAG-intensive):** Re-architecting database schemas and migrating data under strict, multi-source compliance constraints. This evaluates the temporal lobe's `l3()` retrieval accuracy and the frontal lobe's logical grounding checking (`honesty_threshold`).
3.  **Adversarial Debugging (Hostile Sandboxes):** Repairing broken systems where standard library files are intentionally corrupted. This forces the parietal lobe's `ProcessMonitor` to discriminate system "pain" metrics and triggers the frontal lobe's rehearsal critic.

### 4.3. Test Configurations
*   **Control Group (Baseline A - Reactive Agent):** Standard ReAct loop with a flat, unmanaged context window.
*   **Treatment Group A (Single Lobe APCA):** Rehearsal gate enabled (`rehearse()`), but utilizing a flat context window.
*   **Treatment Group B (Dual Hemisphere APCA):** Symmetrical Left and Right `ProcessingPipeline` engines running with synchronized `cross_pipeline_link = True` and stratified L1/L2/L3 memory context cascades.

---

## 5. Expected Research Contributions
By establishing empirical proof that anatomically-partitioned agent loops outperform linear models, this PhD research expects to deliver:
1.  **The APCA Paradigm:** A formal, open-source mathematical framework for partitioning AI agent pipelines into specialized, bio-inspired modules.
2.  **Pre-Execution Auditing Standards:** Quantifiable metrics demonstrating that internal cognitive simulation reduces executed syntax errors and database hallucinations, saving enterprise computational costs.
3.  **Context-Cascade Algorithms:** A validated token-management model showing that stratified, integer-bounded memory layers preserve long-horizon session integrity far better than massive, unmanaged flat context windows.

---

## 6. References
[1] University of Queensland, Queensland Brain Institute. *Lobes of the brain*. Educational Resource on Structural and Functional Cerebral Divisions.
