# Technical Reference & API Documentation (v18_pass)

This document provides a class-by-class, variable-by-variable, and function-by-function technical reference of the **`brain_anatomy-v18_pass.py`** codebase.

---

## 🏛️ Class: `Agent_Brain`
The main coordinator of the AI agent, orchestrating dual parallel processing pipelines to process inputs, manage runtime safety, and execute tasks.

```python
class Agent_Brain:
    def __init__(
        self, 
        cross_pipeline_link: bool = True, 
        iq_reasoning_depth: int = 120, 
        level_of_judgement: float = 0.5, 
        honesty_threshold: float = 0.9, 
        deception: float = 0.1, 
        personality_style: str = "Balanced Brainstormer", 
        log_discrimination: float = 0.5, 
        retrieval_similarity_threshold: float = 0.75, 
        linguistic_syntax_precision: float = 0.85,
        prompt_optimization_passes: int = 0,
        l1_context_count_limit: int = 100000,
        l2_context_count_limit: int = 1000000,
        l3_context_count_limit: int = 10000000
    ):
```

### Constructor Parameters (`__init__`)
* **`cross_pipeline_link` (bool)**:
  * *Description*: Connects or disconnects the left and right processing pipelines (simulating the Corpus Callosum).
  * *Type*: `bool`
  * *Operational Boundaries*: `True` (enabled - dual cooperative pipelines run parallel validations) or `False` (disabled - isolated diagnostic threads).
* **`iq_reasoning_depth` (int)**:
  * *Description*: Governs maximum reasoning loops/planning steps inside executive control.
  * *Type*: `int`
  * *Operational Boundaries*: `1` to `200+` (lower settings yield fast/simple runs; higher settings enable deep analytical checks).
* **`level_of_judgement` (float)**:
  * *Description*: Sets the critical evaluation stance and tone.
  * *Type*: `float`
  * *Operational Boundaries*: `0.0` (highly agreeable, sycophantic) to `1.0` (unbiased, bitter, blunt analytical criticism).
* **`honesty_threshold` (float)**:
  * *Description*: Controls the strictness of grounding checks to avoid logical hallucinations.
  * *Type*: `float`
  * *Operational Boundaries*: `0.0` (allows creative extrapolation) to `1.0` (strict factual grounding constraint).
* **`deception` (float)**:
  * *Description*: Manages strategic simulation and private logic boundaries for multi-agent game-theory interactions.
  * *Type*: `float`
  * *Operational Boundaries*: `0.0` (complete transparency) to `1.0` (high strategic simulation).
* **`personality_style` (str)**:
  * *Description*: The active behavioral voice and style profile (e.g., "Pragmatic Architect", "Socratic Guide").
  * *Type*: `str`
  * *Operational Boundaries*: Any non-empty string.
* **`log_discrimination` (float)**:
  * *Description*: Controls the parietal two-point discrimination sensory resolution for telemetry warnings vs errors.
  * *Type*: `float`
  * *Operational Boundaries*: `0.0` (group logs broadly) to `1.0` (fine-grained individual error tracking).
* **`retrieval_similarity_threshold` (float)**:
  * *Description*: Cutoff similarity score for retrieving semantic memories during standard memory tasks.
  * *Type*: `float`
  * *Operational Boundaries*: `0.0` (highly permissive analogies) to `1.0` (strict exact semantic matching).
* **`linguistic_syntax_precision` (float)**:
  * *Description*: Regulates parser strictness and syntax-conformance audits.
  * *Type*: `float`
  * *Operational Boundaries*: `0.0` (lenient compliance) to `1.0` (strict syntax and formatting enforcement).
* **`prompt_optimization_passes` (int)**:
  * *Description*: Configures the number of pre-execution prompt rewriting iterations.
  * *Type*: `int`
  * *Operational Boundaries*: `0` (disabled), `1` (single pass), or `3` (triple recursive loop-and-optimize).
* **`l1_context_count_limit` (int)**:
  * *Description*: Size threshold in tokens for the volatile L1 immediate working memory cache.
  * *Type*: `int`
  * *Operational Boundaries*: `1,000` to `1,000,000+` (e.g., set to `1,000,000` to retain all active dialogue in L1).
* **`l2_context_count_limit` (int)**:
  * *Description*: Size threshold in tokens for L2 episodic session history storage.
  * *Type*: `int`
  * *Operational Boundaries*: `10,000` to `10,000,000+`.
* **`l3_context_count_limit` (int)**:
  * *Description*: Size threshold in tokens for persistent L3 semantic storage.
  * *Type*: `int`
  * *Operational Boundaries*: `100,000` to infinite.

### Functions
* **`integrate_whole_brain_function(self)`**:
  * *Description*: Coordinates complex cooperative behaviors requiring multiple lobes working in conjunction across both parallel pipelines.
  * *Code Block*:
    ```python
    def integrate_whole_brain_function(self):
        pass
    ```

---

## 🔄 Class: `ProcessingPipeline`
Represents one of the dual parallel execution pipelines (Left and Right hemispheres) of the agent engine.

```python
class ProcessingPipeline:
    def __init__(self, side: str, ...):
```

### Instance Attributes
* **`self.side` (str)**: Indicates which hemisphere this pipeline belongs to (`"Left"` or `"Right"`).
* **`self.cognitive_functions`**: Instance of `CognitiveFunctions`.
* **`self.process_monitor`**: Instance of `ProcessMonitor`.
* **`self.knowledge_retriever`**: Instance of `KnowledgeRetriever`.
* **`self.vision_and_hearing`**: Instance of `Vision_and_hearing`.

---

## 🔴 Class: `CognitiveFunctions` (Frontal Lobe)
Coordinates executive control, goal planning, logic reasoning, tone alignment, prompt optimization, pre-speech rehearsal, and voluntary movement execution.

```python
class CognitiveFunctions:
    def __init__(
        self, 
        iq_reasoning_depth: int = 120, 
        level_of_judgement: float = 0.5, 
        honesty_threshold: float = 0.9, 
        deception: float = 0.1, 
        personality_style: str = "Balanced Brainstormer",
        prompt_optimization_passes: int = 0
    ):
```

### Functions

#### 📋 Executive Cluster
* **`planning(self)`**: Drafts structured goals for task execution.
* **`reasoning(self)`**: Executes logic evaluation loops using `self.iq_reasoning_depth`.
* **`problem_solving(self)`**: Devises schedules and action plans.
* **`optimize_prompt(self)`**:
  * *Description*: Refines raw prompt inputs prior to planning or execution. Under `1`, optimizes once. Under `3`, optimizes and recursively loops to evaluate. Under `0`, no optimization is performed.
* **`high_level_executive_functions(self)`**:
  * *Description*: Coordinates the executive cluster, binding the outputs of `optimize_prompt`, `planning`, `reasoning`, and `problem_solving` to establish a strategy.
  * *Code Block*:
    ```python
    def high_level_executive_functions(self):
        prompt_opt = self.optimize_prompt()
        plan = self.planning()
        logic_eval = self.reasoning()
        wbs_gantt = self.problem_solving()
        return f"Prompt Optimization: {prompt_opt} | Executive Plan: {plan} | Logic Evaluation: {logic_eval} | Solutions: {wbs_gantt}"
    ```

#### ⚖️ Behavioral & Ethical Cluster
* **`emotional_control(self)`**: Maintains system policy boundaries and output safety.
* **`honesty(self)`**: Configures truthfulness checks using `self.honesty_threshold` to avoid hallucinations.
* **`deception(self)`**: Governs game-theory negotiation capabilities using `self.deception`.
* **`level_of_judgement(self)`**: Establishes critical bias using `self.level_of_judgement` (avoiding sycophancy).
* **`personality(self)`**: Directs stylistic language using `self.personality_style`.
* **`social_behavior(self)`**: Orchestrates multi-agent etiquette and collaboration rules.
* **`emotional_regulation(self)`**:
  * *Description*: Coordinates safety, honesty, deception, judgment, style, and social protocol settings.
  * *Code Block*:
    ```python
    def emotional_regulation(self):
        safety = self.emotional_control()
        truth = self.honesty()
        simulation = self.deception()
        bias = self.level_of_judgement()
        style = self.personality()
        collab = self.social_behavior()
        return f"Alignment Check: Safety={safety}, Honesty={truth}, Strategy={simulation}, Judgement={bias}, Style={style}, Protocol={collab}"
    ```

#### 🛡️ Cognitive Rehearsal Gate
* **`align_persona_and_tone_compliance(self)`**: Reviews draft text to verify style guidelines and strip sycophantic fluff.
* **`audit_logical_errors_and_hallucinations(self)`**: Inspects drafts for logic errors, formatting issues, or schema bugs.
* **`rehearse(self)`**:
  * *Description*: Pre-speech simulation gate that binds persona compliance and logical safety checks to refine draft responses prior to terminal execution or output delivery.
  * *Code Block*:
    ```python
    def rehearse(self):
        persona_compliance = self.align_persona_and_tone_compliance()
        logical_safety = self.audit_logical_errors_and_hallucinations()
        return f"Rehearsing: {persona_compliance} and {logical_safety}"
    ```

#### ⚙️ Physical Action Channel
* **`plan_motor_sequence(self)`**: Formulates bash payloads and code execution scripts.
* **`trigger_primary_motor_cortex(self)`**: Launches communication pathways to pass instructions to the host environment.
* **`voluntary_movement(self)`**:
  * *Description*: Executes compiled code blocks and bash payloads within the shell environment sandbox.
  * *Code Block*:
    ```python
    def voluntary_movement(self):
        payload = self.plan_motor_sequence()
        execution_trigger = self.trigger_primary_motor_cortex()
        return f"Action executed: {payload} via channel {execution_trigger}"
    ```

---

## 🟢 Class: `ProcessMonitor` (Parietal Lobe)
System monitor tracking live execution telemetry, exceptions, temperature, loops, and user interrupts.

```python
class ProcessMonitor:
    def __init__(self, log_discrimination: float = 0.5):
```

### Functions
* **`monitor_generation_temperature(self)`**: Governs temperature adjustments (cooling down for math; warming up for brainstorming).
* **`monitor_user_feedback_signals(self)`**: Scans for user stop keystrokes or cancellation interrupts.
* **`evaluate_error_and_exception_rates(self)`**: Evaluates active shell exit codes and exception velocities.
* **`monitor_token_velocity_and_rate_limits(self)`**: Adapts execution speeds to avoid API throttling.
* **`detect_execution_loops_and_bloat(self)`**: Immediately aborts infinite execution loops or repeated errors (pain reflex).
* **`evaluate_mcp_tool_telemetry(self)`**: Monitors latency and health of connected tool servers.
* **`consolidate_runtime_telemetry(self)`**:
  * *Description*: Aggregates system temperature, feedback, errors, velocity limits, loop detections, and tool telemetry into a single health baseline.
  * *Code Block*:
    ```python
    def consolidate_runtime_telemetry(self):
        temp = self.monitor_generation_temperature()
        user_signals = self.monitor_user_feedback_signals()
        exceptions = self.evaluate_error_and_exception_rates()
        rate_limits = self.monitor_token_velocity_and_rate_limits()
        loops = self.detect_execution_loops_and_bloat()
        mcp_health = self.evaluate_mcp_tool_telemetry()
        return (
            f"Telemetry State: Temp={temp}, Interruption={user_signals}, "
            f"Exception Rate={exceptions}, Rate adaptation={rate_limits}, "
            f"Emergency Halt={loops}, Tool Health={mcp_health}"
        )
    ```
* **`measure_state_drift_distance(self)`**: Measures mathematical divergence between current output and target guidelines.
* **`evaluate_error_receptive_fields(self)`**: Maps clustered exception regions inside terminal logs.
* **`two_point_discrimination(self)`**:
  * *Description*: Evaluates and discriminates between critical, blocking exceptions and benign logs using `self.log_discrimination`.
  * *Code Block*:
    ```python
    def two_point_discrimination(self):
        drift = self.measure_state_drift_distance()
        error_fields = self.evaluate_error_receptive_fields()
        return f"Log discrimination computed with drift margin={drift} and error density={error_fields}"
    ```

---

## 🔵 Class: `KnowledgeRetriever` (Temporal Lobe)
Manages semantic search, syntax validation, file system directory structures, and active memory layering (L1, L2, L3).

```python
class KnowledgeRetriever:
    def __init__(
        self, 
        retrieval_similarity_threshold: float = 0.75, 
        linguistic_syntax_precision: float = 0.85,
        l1_context_count_limit: int = 100000,
        l2_context_count_limit: int = 1000000,
        l3_context_count_limit: int = 10000000
    ):
```

### Functions
* **`poll_realtime_text_streams(self)`**: Polls live terminal stdout/stderr chunks.
* **`detect_stream_patterns_and_triggers(self)`**: Scans text streams for specific success/warning triggers.
* **`recognize_stream_context(self)`**:
  * *Description*: Decodes active text streams to maintain real-time execution context.
  * *Code Block*:
    ```python
    def recognize_stream_context(self):
        raw_stream = self.poll_realtime_text_streams()
        patterns = self.detect_stream_patterns_and_triggers()
        return f"Active stream context parsed: Raw={raw_stream}, Patterns={patterns}"
    ```
* **`lexical_syntax_parsing(self)`**: Validates correctness of code grammar and schemas.
* **`resolve_semantic_meaning(self)`**: Maps structural data flows and concepts.
* **`recognize_language(self)`**:
  * *Description*: Assesses linguistic and programming language syntaxes using `self.linguistic_syntax_precision`.
  * *Code Block*:
    ```python
    def recognize_language(self):
        grammar = self.lexical_syntax_parsing()
        semantics = self.resolve_semantic_meaning()
        return f"Language matching: Syntax={grammar}, Semantics={semantics}"
    ```
* **`recognize_prompt_topic_and_intent(self)`**: Pinpoints high-level prompt topics.
* **`map_topic_vector_coordinates(self)`**: Resolves multidimensional topic vector coordinates.
* **`extract_context_anchors(self)`**: Locks onto named entity anchors (like path, library, and variable names).
* **`identify_user_profile_and_persona(self)`**: Evaluates user coding preferences and persona styles.
* **`analyze_directory_context(self)`**: Scans directory layouts and folder trees.
* **`recognize_visual_context(self)`**:
  * *Description*: Integrates directory layouts, prompt topics, context anchors, and user profile guidelines to establish complete situational awareness.
  * *Code Block*:
    ```python
    def recognize_visual_context(self):
        topic = self.recognize_prompt_topic_and_intent()
        coords = self.map_topic_vector_coordinates()
        anchors = self.extract_context_anchors()
        persona = self.identify_user_profile_and_persona()
        scene = self.analyze_directory_context()
        return (
            f"Situational Awareness: Topic={topic}, Coordinates={coords}, "
            f"Anchors={anchors}, Persona={persona}, Scene={scene}"
        )
    ```
* **`encode_session_experience(self)`**: Backs up conversational turns into short-term arrays.
* **`retrieve_long_term_memory(self)`**: Queries persistent vector documentation databases.
* **`evaluate_agent_objective_alignment(self)`**: Assesses intermediate alignment with safety guidelines.
* **`l1(self)`**:
  * *Description*: Manages L1 Sensory Cache (Immediate Working Memory). Keeps all active tokens entirely in L1 for zero-latency execution if under the `self.l1_context_count_limit` boundary.
* **`l2(self)`**:
  * *Description*: Manages L2 Episodic Memory (Short-Term Session Storage). Receives consolidated overflow from L1 up to the `self.l2_context_count_limit` boundary.
* **`l3(self)`**:
  * *Description*: Manages L3 Semantic Memory (Long-Term Knowledge Base / RAG). Receives compressed, synthesized context overflow from L2 up to the `self.l3_context_count_limit` boundary.
* **`memory_and_learning(self)`**:
  * *Description*: Coordinates L1, L2, and L3 memory layers along with objective alignment vectors to optimize retrieval while preventing token bloat and context drift.
  * *Code Block*:
    ```python
    def memory_and_learning(self):
        l1_cache = self.manage_l1_sensory_cache() if hasattr(self, 'manage_l1_sensory_cache') else self.l1()
        l2_episodic = self.manage_l2_episodic_memory() if hasattr(self, 'manage_l2_episodic_memory') else self.l2()
        l3_semantic = self.manage_l3_semantic_memory() if hasattr(self, 'manage_l3_semantic_memory') else self.l3()
        alignment = self.evaluate_agent_objective_alignment()
        return f"Memory State: L1 Volatile={l1_cache}, L2 Episodic={l2_episodic}, L3 Semantic RAG={l3_semantic}, Alignment={alignment}"
    ```

---

## 🟡 Class: `Vision_and_hearing` (Occipital Lobe)
Stateless sensory intake processing visual file uploads, multimodal prompts, and token resource budgets.

```python
class Vision_and_hearing:
    # Stateless sensor parser, no constructor variables.
```

### Functions
* **`ingest_multimodal_inputs(self)`**: Captures text prompts, screenshots, and visual file uploads.
* **`calculate_optimal_execution_path(self)`**: Computes the shortest execution roadmap to reach the user's objective.
* **`receive_visual_data(self)`**:
  * *Description*: Performs initial analysis on visual and prompt inputs.
  * *Code Block*:
    ```python
    def receive_visual_data(self):
        retina_input = self.ingest_multimodal_inputs()
        execution_path = self.calculate_optimal_execution_path()
        return f"Intake completed: Raw input={retina_input}, Path={execution_path}"
    ```
* **`estimate_token_and_time_budget(self)`**: Estimates prompt tokens, expected context window ceilings, and API latency limits.
* **`generate_workspace_dependency_mindmap(self)`**: Builds visual structural mindmaps of file relationships.
* **`classify_task_entities_and_constraints(self)`**: Classifies schemas, variable boundaries, and file parameters.
* **`process_visual_attributes(self)`**:
  * *Description*: Generates a comprehensive resource blueprint prior to execution.
  * *Code Block*:
    ```python
    def process_visual_attributes(self):
        budget = self.estimate_token_and_time_budget()
        mindmap = self.generate_workspace_dependency_mindmap()
        entities = self.classify_task_entities_and_constraints()
        return f"Resource blueprint: Budget={budget}, Mindmap={mindmap}, Entities={entities}"
    ```
