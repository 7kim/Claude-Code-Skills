# Lexicon & Terminologies: Biological to Programmatic Mapping (v18_pass)

This document maps the biological anatomy of the human cerebral cortex [1] to the algorithmic variables, parameters, and classes implemented inside **`brain_anatomy-v18_pass.py`**. 

Unlike previous high-level exploratory iterations, this lexicon focuses **strictly** on the elements that have been programmatically implemented in our codebase. To keep this reference clean and highly actionable, non-implemented biological features (such as *gyri*, *sulci*, or *auditory cortex subdivisions*) have been excluded.

---

## 🏛️ General Brain & Inter-Hemispheric Structure

### 1. Symmetrical Hemispheres (Left & Right Brain)
* **Biological Meaning**: The human cerebrum is divided into two symmetrical cerebral hemispheres that coordinate, compare, and validate cognitive signals [1].
* **Programmatic Mapping**: 
  * Instantiated as two identical **`ProcessingPipeline`** objects: `self.left_pipeline` and `self.right_pipeline`.
  * Running dual pipelines allows the agent to run twin, parallel thought processes, making it highly fault-tolerant and capable of "split-brain" self-analysis.

### 2. Corpus Callosum (Hemispheric Bridge)
* **Biological Meaning**: A massive, thick band of nerve fibers connecting the left and right cerebral hemispheres, enabling communication, synchronization, and coordination between them [1].
* **Programmatic Mapping**:
  * Represented by the boolean parameter **`cross_pipeline_link`** inside the `Agent_Brain` constructor.
  * When `True`, it synchronizes data and allows the dual pipelines to cross-reference their intermediate conclusions before output delivery. When `False`, the pipelines run as isolated diagnostic threads.

---

## 🔴 Frontal Lobe (`CognitiveFunctions`)
*The anatomical region of the human brain responsible for executive control, planning, systematic reasoning, personality, ethics, and voluntary physical action [1].*

### 1. Executive Control & Problem Solving
* **Biological Meaning**: Prefrontal cortex networks that draft complex roadmaps, resolve conflicting goals, and simulate logic chains [1].
* **Programmatic Mapping**:
  * **`planning()`**: Defines the high-level steps for completing complex user objectives.
  * **`reasoning()`**: Executes logical validation loops. Regulated by the integer parameter **`iq_reasoning_depth`** which dictates maximum processing passes.
  * **`problem_solving()`**: Structures schedules and action steps.
  * **`optimize_prompt()`**: An executive pre-processor. Controlled by the integer variable **`prompt_optimization_passes`** (Limits: `0` = disabled, `1` = standard optimization, `3` = recursive loop-and-optimize).
  * **`high_level_executive_functions()`**: The parent coordinator binding the outputs of prompt optimization, planning, reasoning, and problem solving into a unified logical sequence.

### 2. Personality, Ethics, & Behavioral Dials
* **Biological Meaning**: Frontal lobe systems that regulate emotional control, social boundaries, honesty, and social manners [1].
* **Programmatic Mapping**:
  * **`honesty()`**: Manages truthfulness and mitigates hallucinations. Regulated by the float parameter **`honesty_threshold`** (`0.0` to `1.0`).
  * **`deception()`**: Regulates strategic simulation and obfuscation for multi-agent negotiation. Regulated by the float parameter **`deception`** (`0.0` to `1.0`).
  * **`level_of_judgement()`**: Establishes critical bias. Regulated by the float parameter **`level_of_judgement`** (`0.0` to `1.0` where `1.0` delivers bitter, honest truth).
  * **`personality()`**: Shapes stylistic conversational guidelines. Regulated by the string parameter **`personality_style`**.
  * **`social_behavior()`**: Governs multi-agent messaging rules.
  * **`emotional_control()`**: Controls policy enforcement and safety parameters.
  * **`emotional_regulation()`**: The parent coordinator aggregating behavioral, tone, and safety settings into a clean checked state.

### 3. Supplementary Motor Area (Motor Imagery)
* **Biological Meaning**: Pre-motor areas that run mental rehearsals of physical motions (rehearsing speech or movement) before triggering actual muscle contractions.
* **Programmatic Mapping**:
  * **`rehearse()`**: Operates as a dual-evaluation pre-speech gating mechanism. It binds two child actions:
    * **`align_persona_and_tone_compliance()`**: Pre-scans generated responses to strip out sycophantic praise or tonal drift.
    * **`audit_logical_errors_and_hallucinations()`**: Audits logic, formatting, and python syntax before any tools are run.

### 4. Primary Motor Cortex
* **Biological Meaning**: The cortical strip generating physical neural signals that exit the brain to execute voluntary physical movement [1].
* **Programmatic Mapping**:
  * **`plan_motor_sequence()`**: Compiles physical execution payloads (bash commands, code blocks, tool calls).
  * **`trigger_primary_motor_cortex()`**: Launches the subprocess execution channel.
  * **`voluntary_movement()`**: Runs compiled code and terminal scripts in the safe host environment sandbox.

---

## 🟢 Parietal Lobe (`ProcessMonitor`)
*Anatomical lobe dedicated to processing and integrating diverse sensory inputs, including touch, temperature, pressure, pain, and spatial orientation [1].*

### 1. Somatosensory & Telemetry Integration
* **Biological Meaning**: Reading and integrating raw sensory nerve impulses to protect the body from damage (like immediate reflexes to heat or painful stimuli) [1].
* **Programmatic Mapping**:
  * **`monitor_generation_temperature()`**: Adjusts the LLM generation temperature dynamically.
  * **`monitor_user_feedback_signals()`**: Detects user keystroke interrupts (tactile inputs).
  * **`evaluate_error_and_exception_rates()`**: Registers shell script failures and exception counts (pressure and pain metrics).
  * **`detect_execution_loops_and_bloat()`**: Automatically triggers the **pain withdrawal reflex** to instantly kill runaway infinite loops or repeated errors.
  * **`evaluate_mcp_tool_telemetry()`**: Measures performance and latencies of connected tool servers.
  * **`consolidate_runtime_telemetry()`**: The master somatic coordinator aggregating temperature, feedback, failures, limits, and loops into a single health log.

### 2. Two-Point Discrimination
* **Biological Meaning**: The sensory ability of the parietal lobe to distinguish between two nearby physical points of contact on the skin, testing sensory resolution [1].
* **Programmatic Mapping**:
  * **`two_point_discrimination()`**: Measures log classification precision. Bounded by the float parameter **`log_discrimination`** (`0.0` to `1.0`). It enables the monitor to cleanly discriminate between a critical, blocking execution error (requiring intervention) and a benign, standard warning log.

---

## 🔵 Temporal Lobe (`KnowledgeRetriever`)
*The lobe responsible for auditory signal processing, language recognition, memory consolidation, and learning [1].*

### 1. Auditory Processing & Text Streaming
* **Biological Meaning**: Mapping spoken word frequencies and interpreting acoustic structures [1].
* **Programmatic Mapping**:
  * **`poll_realtime_text_streams()`**: Reads live CLI stdout/stderr token streams.
  * **`detect_stream_patterns_and_triggers()`**: Scans text streams for active triggers or warning flags.
  * **`recognize_stream_context()`**: Evaluates and decodes live streams.

### 2. Language Recognition & Semantics (Wernicke's Area)
* **Biological Meaning**: Decoding speech sounds into structured grammar, syntax, and conceptual semantic meaning [1].
* **Programmatic Mapping**:
  * **`lexical_syntax_parsing()`**: Validates formatting, python syntax, and code schemas.
  * **`resolve_semantic_meaning()`**: Maps data flows and intents.
  * **`recognize_language()`**: Evaluates file format compatibility using the float parameter **`linguistic_syntax_precision`** (`0.0` to `1.0`).

### 3. Hippocampus & Memory Layer Stratification
* **Biological Meaning**: The medial temporal lobe structure critical for learning and consolidating temporary events into permanent long-term memory [1].
* **Programmatic Mapping**:
  * Maps directly to our three explicit, stratified memory functions:
    * **`l1()` (Sensory Cache)**: Immediate working memory. Governed by the integer parameter **`l1_context_count_limit`**.
    * **`l2()` (Episodic Memory)**: Short-term session buffer. Governed by the integer parameter **`l2_context_count_limit`**.
    * **`l3()` (Semantic RAG)**: Permanent knowledge base. Governed by the integer parameter **`l3_context_count_limit`**.
  * **`memory_and_learning()`**: The master coordinator. Manages the cascading transfer of context (from L1 down to L2, and L2 down to L3) when configured token limits are crossed to protect against contextual drift.

---

## 🟡 Occipital Lobe (`Vision_and_hearing`)
*The primary visual processing center [1].*

### 1. Retinal Ingestion & Scene Analysis
* **Biological Meaning**: Processing light signals from the eyes to interpret depth, distance, visual locations, and identify objects [1].
* **Programmatic Mapping**:
  * **`ingest_multimodal_inputs()`**: Captures text prompts, screenshots, and visual file uploads.
  * **`calculate_optimal_execution_path()`**: Plots the shortest computational route to an objective.
  * **`receive_visual_data()`**: Initial sensory intake processing.
  * **`estimate_token_and_time_budget()`**: Computes expected token costs and API latencies.
  * **`generate_workspace_dependency_mindmap()`**: Maps structural file dependency layouts visually.
  * **`classify_task_entities_and_constraints()`**: Recognizes target files, library limits, and schemas.
  * **`process_visual_attributes()`**: Formulates a complete resource blueprint prior to execution.
