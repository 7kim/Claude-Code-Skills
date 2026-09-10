# Agent_Brain: Bio-Inspired AI Orchestration Framework
## Functional Neuroanatomy of the AI Agent (v18_pass)

Welcome to **Agent_Brain**, a highly modular, biologically-grounded AI agent skeleton framework. This architecture translates the functional neuroanatomy of the human cerebral cortex [1] into parallel execution pipelines for agentic systems. By dividing cognitive responsibilities into specialized functional components (representing the cerebral lobes) working in conjunction, the framework provides a clean, predictable, and robust blueprint for advanced AI workflows.

Unlike traditional, simple reactive agents, this framework implements a dual-hemisphere execution model, pre-execution prompt optimization, real-time telemetry-driven "pain" watchdog reflexes, pre-speech rehearsal gates to prevent sycophancy, and a three-tier stratified memory architecture (L1 Sensory Cache, L2 Episodic Session Storage, L3 Persistent RAG Database). 

To keep this blueprint clean and highly actionable, only programmatically implemented classes, attributes, and methods are covered. Unimplemented anatomical terms (such as *gyri*, *sulci*, or *cortical folds*) are excluded.

---

## 🧠 Core Architectural Philosophy

Our design relies on the biological principle that complex, adaptive behaviors emerge when distinct specialized lobes work in conjunction to process information:

1. **`Agent_Brain` (The Cerebrum)**: The master controller. It instantiates the parallel execution pipelines and coordinates hemispheric collaboration via the Corpus Callosum bridge (`cross_pipeline_link`).
2. **`ProcessingPipeline` (Cerebral Hemispheres)**: Symmetrical dual-execution pipelines (Left and Right) running in parallel to process inputs, audit thoughts, and validate logic independently or cooperatively.
3. **`Vision_and_hearing` (Occipital Lobe)**: The sensory intake center. Analyzes primary multimodal visual feeds (images, logs, prompts), evaluates token/time compute budgets, and structures task maps.
4. **`ProcessMonitor` (Parietal Lobe)**: The somatic watchdog. Monitors active telemetry, exception rates, API velocities, and user interrupts. Uses a "pain reflex" to halt runaway infinite loops and employs **two-point discrimination** to categorize critical errors vs. benign warnings.
5. **`KnowledgeRetriever` (Temporal Lobe)**: The semantic memory vault. Manages auditory token streams, syntax parsing, workspace layouts, and a three-tier memory architecture (L1, L2, L3) with context-based cascade overflow triggers.
6. **`CognitiveFunctions` (Frontal Lobe)**: The prefrontal executive center. Drives strategic planning, logic reasoning, and problem solving. Governs behavioral dials (honesty, deception, judgment), prompt optimization, pre-speech response rehearsal, and voluntary terminal actions.

---

## 🚀 Quick Start & Customization

The framework is fully configurable at boot time. You can instantiate an `Agent_Brain` with tailored cognitive capacity and alignment profiles:

```python
from brain_anatomy import Agent_Brain

# Instantiate a highly critical, hyper-logical "Auditor" Brain Profile
auditor_brain = Agent_Brain(
    cross_pipeline_link=True,             # Synchronized parallel validation (Corpus Callosum)
    iq_reasoning_depth=160,               # Deep logical reasoning passes
    level_of_judgement=1.0,               # Delivering bitter, honest truth (no sycophancy)
    honesty_threshold=1.0,                # Maximum factual grounding, zero hallucinations
    deception=0.0,                        # Zero tactical obfuscation
    personality_style="Strict Inspector", # Precise, formal, and analytical tone
    log_discrimination=0.9,               # Hyper-sensitive warning/error discrimination
    retrieval_similarity_threshold=0.85,  # High precision memory recall
    linguistic_syntax_precision=0.95,     # Strict schema and code validation
    prompt_optimization_passes=3,         # Triple recursive prompt optimization passes
    l1_context_count_limit=1000000,       # Keep up to 1M tokens entirely in fast L1 cache
    l2_context_count_limit=5000000,       # Retain up to 5M tokens in L2 episodic memory
    l3_context_count_limit=50000000       # Move overflow to persistent L3 vector RAG
)
```

---

## 🎨 Complete UML & Architecture Diagrams

This section contains 10 comprehensive Mermaid UML diagrams tracing every facet of **Agent_Brain (v18_pass)**, from static classes to dynamic data streams, memory lifecycles, and use cases.

### 1. Class Diagram
The static class structure, parameterized constructors, associations, and variable bindings within the coordinating parent methods of our codebase.

```mermaid
classDiagram
    class Agent_Brain {
        +cross_pipeline_link : bool
        +left_pipeline : ProcessingPipeline
        +right_pipeline : ProcessingPipeline
        +__init__(cross_pipeline_link: bool, iq_reasoning_depth: int, level_of_judgement: float, honesty_threshold: float, deception: float, personality_style: str, log_discrimination: float, retrieval_similarity_threshold: float, linguistic_syntax_precision: float, prompt_optimization_passes: int, l1_context_count_limit: int, l2_context_count_limit: int, l3_context_count_limit: int)
        +integrate_whole_brain_function()
    }
    class ProcessingPipeline {
        +side : str
        +cognitive_functions : CognitiveFunctions
        +process_monitor : ProcessMonitor
        +knowledge_retriever : KnowledgeRetriever
        +vision_and_hearing : Vision_and_hearing
        +__init__(side: str, ...)
    }
    class CognitiveFunctions {
        +iq_reasoning_depth : int
        +level_of_judgement : float
        +honesty_threshold : float
        +deception : float
        +personality_style : str
        +prompt_optimization_passes : int
        +__init__(...)
        +planning()
        +reasoning()
        +problem_solving()
        +optimize_prompt()
        +high_level_executive_functions()
        +emotional_control()
        +honesty()
        +deception()
        +level_of_judgement()
        +personality()
        +social_behavior()
        +emotional_regulation()
        +align_persona_and_tone_compliance()
        +audit_logical_errors_and_hallucinations()
        +rehearse()
        +plan_motor_sequence()
        +trigger_primary_motor_cortex()
        +voluntary_movement()
    }
    class ProcessMonitor {
        +log_discrimination : float
        +__init__(log_discrimination: float)
        +monitor_generation_temperature()
        +monitor_user_feedback_signals()
        +evaluate_error_and_exception_rates()
        +monitor_token_velocity_and_rate_limits()
        +detect_execution_loops_and_bloat()
        +evaluate_mcp_tool_telemetry()
        +consolidate_runtime_telemetry()
        +measure_state_drift_distance()
        +evaluate_error_receptive_fields()
        +two_point_discrimination()
    }
    class KnowledgeRetriever {
        +retrieval_similarity_threshold : float
        +linguistic_syntax_precision : float
        +l1_context_count_limit : int
        +l2_context_count_limit : int
        +l3_context_count_limit : int
        +__init__(retrieval_similarity_threshold: float, linguistic_syntax_precision: float, ...)
        +poll_realtime_text_streams()
        +detect_stream_patterns_and_triggers()
        +recognize_stream_context()
        +lexical_syntax_parsing()
        +resolve_semantic_meaning()
        +recognize_language()
        +recognize_prompt_topic_and_intent()
        +map_topic_vector_coordinates()
        +extract_context_anchors()
        +identify_user_profile_and_persona()
        +analyze_directory_context()
        +recognize_visual_context()
        +encode_session_experience()
        +retrieve_long_term_memory()
        +evaluate_agent_objective_alignment()
        +l1()
        +l2()
        +l3()
        +memory_and_learning()
    }
    class Vision_and_hearing {
        +ingest_multimodal_inputs()
        +calculate_optimal_execution_path()
        +receive_visual_data()
        +estimate_token_and_time_budget()
        +generate_workspace_dependency_mindmap()
        +classify_task_entities_and_constraints()
        +process_visual_attributes()
    }
    Agent_Brain *-- ProcessingPipeline : Symmetrical Hemispheres
    ProcessingPipeline *-- CognitiveFunctions : Frontal Lobe
    ProcessingPipeline *-- ProcessMonitor : Parietal Lobe
    ProcessingPipeline *-- KnowledgeRetriever : Temporal Lobe
    ProcessingPipeline *-- Vision_and_hearing : Occipital Lobe
```

---

### 2. Sequence Diagram
The sequential lifecycle of a user prompt, detailing sensory intake, telemetry check, memory tier evaluation, executive reasoning, pre-speech rehearsal, and voluntary movement execution.

```mermaid
sequenceDiagram
    autonumber
    actor User as User Prompt
    participant AB as Agent_Brain (Brain)
    participant VH as Vision_and_hearing (Occipital)
    participant PM as ProcessMonitor (Parietal)
    participant KR as KnowledgeRetriever (Temporal)
    participant CF as CognitiveFunctions (Frontal)

    User->>AB: Send Prompt (e.g., Run test suite)
    AB->>VH: receive_visual_data() & process_visual_attributes()
    VH-->>AB: Resource & Path Blueprint
    AB->>PM: consolidate_runtime_telemetry() & two_point_discrimination()
    PM-->>AB: Health Baseline & Exception discrimination (Benign vs Critical)
    AB->>KR: recognize_visual_context()
    KR-->>AB: Situational Workspace Awareness
    AB->>KR: memory_and_learning()
    Note over KR: Active check on L1 -> L2 -> L3
    KR->>KR: l1() (Sensory Cache check)
    KR->>KR: l2() (Episodic retrieval if L1 overflowed)
    KR->>KR: l3() (Semantic RAG search if L2 overflowed)
    KR-->>AB: Consolidated Memory Context
    AB->>CF: high_level_executive_functions()
    CF->>CF: optimize_prompt()
    CF->>CF: planning() & reasoning() & problem_solving()
    CF-->>AB: Structured Executive Strategy
    AB->>CF: emotional_regulation()
    CF-->>AB: Behavioral Alignments (honesty, deception, judgement dials)
    AB->>CF: rehearse() (Cognitive Rehearsal Gate)
    CF->>CF: align_persona_and_tone_compliance() (Strips sycophancy)
    CF->>CF: audit_logical_errors_and_hallucinations() (Factual Critic)
    CF-->>AB: Rehearsed Response Approved
    AB->>CF: voluntary_movement() (Physical Action)
    CF->>CF: plan_motor_sequence() & trigger_primary_motor_cortex()
    CF-->>AB: Action Executed (Subprocess launch in terminal)
    AB-->>User: Output Delivered
```

---

### 3. Context Diagram
The highest-level system boundaries (Level 0), showing how the Agent_Brain sits between user queries, database stores, and OS terminal environments.

```mermaid
graph TD
    User[User / Developer] -->|Configuration Parameters| AB[Agent_Brain (v18_pass)]
    User -->|Natural Language Prompt / Multimodal Inputs| AB
    AB -->|Status Telemetry & Alerts| User
    AB -->|Voluntary Action Subprocess Commands| Shell[Host Environment / Terminal Sandbox]
    Shell -->|stdout / stderr Logs / Exit Codes| AB
    AB -->|Semantic Vector Queries| VectorDB[Persistent RAG Knowledge Base]
    VectorDB -->|Retrieved Context Passages| AB
    AB -->|Final Audited Response| User
```

---

### 4. Component/Architecture Diagram
The functional partitioning of the cerebrum into symmetrical execution hemispheres (Cerebral Hemispheres) collaborating via the Corpus Callosum bridge.

```mermaid
graph TB
    subgraph Agent_Brain_Orchestrator [Agent_Brain]
        CCL[Corpus Callosum Bridge: cross_pipeline_link]
        
        subgraph Left_Pipeline [Left ProcessingPipeline]
            L_CF[CognitiveFunctions / Frontal Lobe]
            L_PM[ProcessMonitor / Parietal Lobe]
            L_KR[KnowledgeRetriever / Temporal Lobe]
            L_VH[Vision_and_hearing / Occipital Lobe]
        end

        subgraph Right_Pipeline [Right ProcessingPipeline]
            R_CF[CognitiveFunctions / Frontal Lobe]
            R_PM[ProcessMonitor / Parietal Lobe]
            R_KR[KnowledgeRetriever / Temporal Lobe]
            R_VH[Vision_and_hearing / Occipital Lobe]
        end

        Left_Pipeline <-->|Hemispheric Collaboration| CCL
        Right_Pipeline <-->|Hemispheric Collaboration| CCL
    end
    
    Inputs[Prompts, Files, Images] --> L_VH & R_VH
    L_CF & R_CF --> Actions[Code Writing, Shell Run, API Call]
```

---

### 5. Activity Diagram
The detailed operational workflow representing how memory layers are evaluated, how prompt optimization passes are routed, and how the rehearsal gate audits draft text.

```mermaid
stateDiagram-v2
    [*] --> IngestInputs
    IngestInputs --> ParseResourceLimits
    ParseResourceLimits --> ConsolidateTelemetry
    ConsolidateTelemetry --> EvaluateMemoryTier
    
    state EvaluateMemoryTier {
        [*] --> CheckL1
        CheckL1 --> WithinL1Limit : context_size < limit
        CheckL1 --> ExceedsL1Limit : context_size >= limit
        WithinL1Limit --> RetrieveFromL1
        ExceedsL1Limit --> MigrateToL2
        MigrateToL2 --> CheckL2Limit
        CheckL2Limit --> WithinL2Limit : context_size < limit
        CheckL2Limit --> ExceedsL2Limit : context_size >= limit
        WithinL2Limit --> RetrieveFromL2
        ExceedsL2Limit --> MigrateToL3
        MigrateToL3 --> RetrieveFromL3
    }

    EvaluateMemoryTier --> OptimizePromptPasses
    
    state OptimizePromptPasses {
        [*] --> CheckPassConfig
        CheckPassConfig --> 0_Passes : passes == 0
        CheckPassConfig --> 1_Pass : passes == 1
        CheckPassConfig --> 3_Passes : passes == 3
        0_Passes --> UseRawPrompt
        1_Pass --> OptimizeOnce
        3_Passes --> RecursiveOptimizationLoop
    }

    OptimizePromptPasses --> ExecutivePlanning
    ExecutivePlanning --> RunRehearsalGate
    
    state RunRehearsalGate {
        [*] --> ComplianceCheck
        ComplianceCheck --> LogicalSafetyCheck
        LogicalSafetyCheck --> StripSycophancy
    }

    RunRehearsalGate --> ExecuteVoluntaryAction
    ExecuteVoluntaryAction --> [*]
```

---

### 6. Data Flow Diagram (DFD Level 0)
The simplified system context flow diagram representing the boundary inputs and terminal outputs of the execution pipeline.

```mermaid
graph LR
    User((User)) -->|Prompt & Configurations| System[Agent_Brain Engine]
    System -->|Final Structured Output| User
    System -->|Execution Payload| OS((Terminal / OS Sandbox))
    OS -->|Execution Logs & Exit Status| System
```

---

### 7. Data Flow Diagram (DFD Level 1)
The detailed process-by-process data flow of our codebase, mapping the path of text data as it is stored across the cascading memory store (L1/L2/L3) and evaluated by the critic.

```mermaid
graph TD
    User((User)) -->|Input Prompt| P1[Occipital Lobe: Receive & Ingest Inputs]
    User -->|Variables & Rules| P4[Frontal Lobe: Executive Control]
    P1 -->|Raw Text & Paths| P2[Parietal Lobe: Telemetry & Loop Watchdog]
    P2 -->|System Health & Logs| P3[Temporal Lobe: Language Recognition & Memory Retrieve]
    
    subgraph Memory_Cycle [Cascading Memory Store]
        P3 -->|Store Active Token Buffer| M1[(L1 Sensory Cache)]
        M1 -->|Overflow Compression| M2[(L2 Episodic Session Store)]
        M2 -->|Long Term Vector Write| M3[(L3 Persistent RAG DB)]
        M3 -->|Vector Retrieval Match| P3
    end

    P3 -->|Situational Context & Memories| P4
    P4 -->|Pre-speech Response Draft| P5[Frontal Lobe: Rehearsal Gate]
    P5 -->|Persona Aligned & Audited Draft| P6[Frontal Lobe: Motor Sequence Execution]
    P6 -->|Shell Payloads| OS((Terminal OS Sandbox))
    OS -->|CLI stdout/stderr| P2
    P6 -->|Audited Deliverables| User
```

---

### 8. Entity-Relationship Diagram (ERD)
The logical mapping of system components, configuration entities, and the active variables within our tiered memory models.

```mermaid
erDiagram
    AGENT-BRAIN ||--|| CONFIGURATION-PROFILE : holds
    AGENT-BRAIN ||--o| PROCESSING-PIPELINE : runs
    PROCESSING-PIPELINE ||--|| COGNITIVE-FUNCTIONS : contains
    PROCESSING-PIPELINE ||--|| PROCESS-MONITOR : contains
    PROCESSING-PIPELINE ||--|| KNOWLEDGE-RETRIEVER : contains
    PROCESSING-PIPELINE ||--|| VISION-AND-HEARING : contains
    KNOWLEDGE-RETRIEVER ||--o| L1-SENSORY-CACHE : manages
    KNOWLEDGE-RETRIEVER ||--o| L2-EPISODIC-BUFFER : manages
    KNOWLEDGE-RETRIEVER ||--o| L3-SEMANTIC-RAG : manages

    CONFIGURATION-PROFILE {
        bool cross_pipeline_link
        int iq_reasoning_depth
        float level_of_judgement
        float honesty_threshold
        float deception
        string personality_style
        float log_discrimination
        int prompt_optimization_passes
        int l1_context_count_limit
        int l2_context_count_limit
        int l3_context_count_limit
    }
    L1-SENSORY-CACHE {
        int active_tokens
        string current_prompt_focus
    }
    L2-EPISODIC-BUFFER {
        int session_history_size
        string session_dialogue_records
    }
    L3-SEMANTIC-RAG {
        int persistent_token_count
        string vector_embeddings
    }
```

---

### 9. Use Case Diagram
Developer-facing and sandbox environment interaction boundaries representing how the system ingests, optimizes, retrieves, plans, and executes goals.

```mermaid
leftToRightDirection
rect Lobe_Engine [Agent_Brain v18_pass System Boundaries]
    usecase UC_Init [Configure Brain Parameters]
    usecase UC_Ingest [Process Multimodal Prompts]
    usecase UC_Opt [Optimize Ingestion Prompts]
    usecase UC_Mem [Retrieve Tiered Memories L1/L2/L3]
    usecase UC_Plan [Generate Executive Strategy]
    usecase UC_Reh [Rehearse & Audit Output]
    usecase UC_Exec [Execute Voluntary Subprocess Commands]
    usecase UC_Mon [Monitor Loop Telemetry & Pain Levels]
end

actor User as User/Developer
actor OS as Sandbox Environment / Shell

User --> UC_Init
User --> UC_Ingest
UC_Ingest --> UC_Opt : "includes"
UC_Opt --> UC_Mem : "includes"
UC_Mem --> UC_Plan : "includes"
UC_Plan --> UC_Reh : "includes"
UC_Reh --> UC_Exec : "includes"

UC_Exec --> OS
OS --> UC_Mon
UC_Mon --> UC_Plan : "triggers adjustment"
```

---

### 10. State Machine Diagram
The high-level states of the core engine, illustrating how it transitions from idle execution through telemetry monitoring, cascading memory lookups, and ethical self-correction before physical action.

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Ingestion : Receive Prompt
    Ingestion --> Telemetry_Check : Ingest Sensory Inputs
    Telemetry_Check --> Memory_Retrieval : Telemetry Clear
    Telemetry_Check --> Recovery_Reflex : High Pain / Loop Detected
    Recovery_Reflex --> Idle : Reset / Adjust Temp
    
    state Memory_Retrieval {
        [*] --> L1_Query
        L1_Query --> L2_Retrieve : Exceeds L1 Context Limit
        L2_Retrieve --> L3_Query : Exceeds L2 Context Limit
    }
    
    Memory_Retrieval --> Prompt_Optimization
    
    state Prompt_Optimization {
        [*] --> Count_Check
        Count_Check --> Standard_Pass : Passes == 1
        Count_Check --> Recursive_Passes : Passes == 3
        Count_Check --> Bypass : Passes == 0
    }
    
    Prompt_Optimization --> Executive_Reasoning
    Executive_Reasoning --> Rehearsal_Gate
    
    state Rehearsal_Gate {
        [*] --> Aligner : Run Compliance Check
        Aligner --> Critic : Run Logical Safety Check
    }
    
    Rehearsal_Gate --> Action_Execution : Rehearsal Passed
    Action_Execution --> Idle : Subprocess Run Completed
```

---

## 🧬 Reference Materials & Grounding

*   [1] **"Lobes of the brain - Queensland Brain Institute - University of Queensland"**: Outlines the anatomical divisions of the cerebral cortex, and details how the frontal lobe manages executive control and personality, the parietal lobe integrates touch, pain, and sensory inputs, the temporal lobe orchestrates hearing, language, and memory, and the occipital lobe processes vision.

For a detailed code reference or design log, refer to the accompanying manuals:
*   `comments.md`: Line-by-line API code block explanations.
*   `terminologies.md`: Symmetrical biological-to-programmatic translation glossary.
*   `evolution.md`: Narrative logs detailing our chronological design iterations.
