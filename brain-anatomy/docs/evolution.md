# The Design Evolution & Prompt History: From Skeleton to Cerebral Agent (v18_pass)

This document preserves the development history and audit trail of the **`Agent_Brain`** framework. It traces the design concept, outlines the progression across eighteen code versions, and archives the prompt history that guided our engineering process.

---

## 💡 The Core Idea: Why a Bio-Inspired AI Agent?

Most AI agents operate using a linear loop: *Input ➔ Plan ➔ Tool Execution ➔ Output*. While functional, this simple cycle fails when dealing with high-complexity scenarios, such as debugging code, handling API rate limits, or matching subtle tone adjustments like avoiding sycophantic praise.

This project introduces a **Biologically-Inspired AI Orchestration Framework**. By mapping an agent's subsystems to the human **cerebral cortex** [1]:
1. **Parallel Execution pipelines** act as dual hemispheres. Under standard operation, they collaborate to verify thoughts (`cross_pipeline_link = True`). Under a "split-brain" state, they can diagnose logical errors independently.
2. **Sensory Telemetry (`ProcessMonitor`)** acts as the parietal lobe's sensory integration system, monitoring exceptions and adjusting temperature or executing emergency halts.
3. **Cognitive Rehearsal (`rehearse()`)** acts as motor imagery, allowing the agent to simulate, critique, and style its output before committing to physical execution or displaying the output.
4. **Stratified Memory (`l1`, `l2`, `l3`)** acts as the medial temporal lobe, segregating immediate working memory from episodic session logs and permanent long-term vector (RAG) repositories.

This design moves AI from a simple *reactive chatbot* to a *reflective, self-correcting cognitive agent*.

---

## 📈 "How We Got Here": Chronological Version History

### 1. The Early Skeletal Blueprints (`v1` to `v5`)
* **Focus**: Setting up structural layout and class structures.
* **Leap**: Designed classes mapping to the four lobes (`FrontalLobe`, `ParietalLobe`, `TemporalLobe`, `OccipitalLobe`) with descriptive biological docstrings.

### 2. The Pure Skeleton Phase (`v6` to `v7`)
* **Focus**: Standardizing the interface.
* **Leap**: Cleaned up all early placeholder logic, converting every method into pure, non-implemented Python `pass` blocks, ensuring maximum template purity (`brain_anatomy-v6_pass.py`).

### 3. Personality & The "Bitter Truth" (`v8` to `v10`)
* **Focus**: Controlling alignment, truthfulness, and compliance.
* **Leap**: 
  * Incorporated a `personality` function inside `CognitiveFunctions` to adjust honesty, truthfulness, and prevent lying.
  * Added the **\"bitter honest truth\"** requirement for business queries—preventing sycophancy (always agreeing with the user's premise).
  * Split this into three distinct functions: `honesty()`, `deception()`, and `level_of_judgement()`, while retaining the high-level `personality()` coordinator (`v10_pass`).

### 4. The Cognitive Rehearsal Gate (`v11` to `v12`)
* **Focus**: Pre-speech self-correction and simulation.
* **Leap**: 
  * Implemented `rehearse()`, which simulates a response before it runs tools or replies to the user.
  * Split the rehearsal loop into two specialized functions: **`audit_logical_errors_and_hallucinations()`** (The Internal Critic) and **`align_persona_and_tone_compliance()`** (The Tone Aligner).

### 5. Restoring Variable Bindings (`v13`)
* **Focus**: Exposing the architectural data flow.
* **Leap**: Wrote back descriptive variable bindings into all coordinating parent methods (e.g., binding `plan`, `logic_eval`, and `wbs_gantt` inside `high_level_executive_functions`). This preserved a pure skeleton style while showing exactly how data flows across methods.

### 6. Parameterization & Prompt Optimization (`v14` to `v15`)
* **Focus**: Dynamic configuration and pre-execution optimization.
* **Leap**:\n  * Added a fully parameterized constructor (`__init__`) to `Agent_Brain`, cascading variables like `iq_reasoning_depth`, `level_of_judgement`, `honesty_threshold`, `deception`, and `personality_style` down to the active lobes on initialization.
  * Introduced **`optimize_prompt()`** to pre-process user prompts. Configured a control variable allowing `0` (no optimization), `1` (single optimization pass), or `3` (triple recursive optimization loops).

### 7. Explicit Variable Comments & Safe Boundaries (`v16`)
* **Focus**: Technical self-documentation.
* **Leap**: Added comprehensive, line-by-line developer comments inside constructors, defining explicit data types and safe operational boundaries (e.g., `0.0` to `1.0` for float dials) for all constructor arguments.

### 8. Introduction of Memory Layers (`v17`)
* **Focus**: Layered context management.
* **Leap**: Introduced the concept of three distinct memory tiers (L1 Sensory Cache, L2 Episodic Buffer, L3 Semantic RAG) to optimize token costs and mitigate contextual drift. Managed via turn-count threshold variables in `KnowledgeRetriever`.

### 9. Functional Refinement & Integer Context Windows (`v18_pass`)
* **Focus**: Direct execution paths and token-based boundaries.
* **Leap**: 
  * Replaced high-level memory handlers with explicit, clean **`l1()`**, **`l2()`**, and **`l3()`** functions inside the `KnowledgeRetriever` class.
  * Converted the cache boundaries from turn-counts to **integer context count limits** (e.g., `l1_context_count_limit` of `1,000,000` tokens). This enables a pure cascading overflow model: information is stored entirely in L1 working memory until it ticks past the threshold, at which point it is compressed and migrated down to L2, and eventually L3.

---

## 📋 The Reconstructed Prompt Registry

Here are the primary prompt directives provided to shape the code iterations:

1. **Prompt 1 (Anatomy Setup)**:
   * *\"Create a skeletal Python architecture representing the functional lobes of the human brain as coordinating execution blocks for an AI agent.\"*
2. **Prompt 2 (Ethical Alignment & Bitter Truth)**:
   * *\"Add in personality comments that we can control lying, honesty, and being Judgmental. Sometimes AI agents lie or always agree with the user. If I am asking for business advice, it should be judgmental and tell me the bitter honest truth instead. Append this to the personality comments.\"*
3. **Prompt 3 (Refining Ethics)**:
   * *\"I changed my mind. Let's create different functions for honesty, deception, and level of judgment.\"*
4. **Prompt 4 (Keeping the Coordinator)**:
   * *\"Why did you remove personality? I want you to keep that function too alongside the new distinct ethical functions.\"*
5. **Prompt 5 (Cognitive Rehearsal)**:
   * *\"Let's add a rehearsal function. After Step 4, if the rehearsal boolean is enabled, it should rehearse what response it is about to give to the user. Split this into two tasks: catching mistakes/logical glitches, and aligning the persona and tone compliance.\"*
6. **Prompt 6 (Naming Variables in Rehearsal)**:
   * *\"Update rehearse to store the results of compliance and logic audit into local variables, then interpolate and return them in a formatted string representation.\"*
7. **Prompt 7 (Restoring Parent-Child Variable Bindings)**:
   * *\"Why were the early variable bindings removed during skeleton cleanup? Let's restore those variable bindings inside all major coordinating functions so the logical data flow is clear, while keeping the child leaf functions as pass blocks.\"*
8. **Prompt 8 (Parameterizing the Constructors)**:
   * *\"Let's add constructors and parameters to the classes. Let's configure variables like IQ/reasoning depth, level of judgment, honesty threshold, deception, personality style, log discrimination, retrieval similarity threshold, linguistic syntax precision, and the cross-pipeline link.\"*
9. **Prompt 9 (Prompt Optimization Pass)**:
   * *\"Let's add a prompt optimization function. Set a variable where if 1, it optimizes once; if 3, it optimizes and loops iteratively; if 0, it doesn't optimize. Keep this logic documented as a comment.\"*
10. **Prompt 10 (Adding Memory Layers)**:
    * *\"For v17. Let's make some changes. Let's add memory layers... something like L1 memory layer, L2 memory layer, L3 memory layer...\"*
11. **Prompt 11 (Refining Memory Layer Implementation)**:
    * *\"Why don't we have def functions for L1, L2, L3? And let's keep its variable as context count meaning its an integer. And if I keep it as 1 million context window for L1 then in that case for 1 million context window that information will stay in L1. After that will go to L2. And so on.\"*
