<p align="center">
  <img src="../assets/brainstorm-to-code/logo.png" width="120" alt="Brainstorm-to-Code logo" />
</p>

<h1 align="center">💡 Brainstorm-to-Code</h1>

<p align="center">
  <b>Talk through an idea with Claude and walk away with a ready-to-extend Python class skeleton.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/type-Claude%20Skill-blueviolet" />
  <img src="https://img.shields.io/badge/language-Python-3776AB" />
  <img src="https://img.shields.io/badge/workflow-Interactive%20Q%26A-FAB43C" />
</p>

<p align="center">
  <img src="../assets/brainstorm-to-code/screenshot-flow.png" width="850" alt="Brainstorm-to-Code flow: idea in, Python class skeleton out" />
</p>

## 🧩 What problem does it solve?

Staring at a blank file when starting a new class is a small but real friction point — what attributes does this thing need? What should come in a list vs. a single value? What methods make sense? **Brainstorm-to-Code** turns that blank-page problem into a short guided conversation, then generates a clean, consistent Python skeleton (private variables, getters/setters, method stubs) so you can jump straight to filling in logic instead of boilerplate.

## Overview
This skill transforms ideas into well-structured Python class skeletons through iterative brainstorming. It guides you through conceptualizing object-oriented designs and generates production-ready code scaffolding.

## What It Does

**Input:** A topic or concept you want to build as a Python class
**Process:** Interactive brainstorming about:
  - What attributes/components the class needs
  - What methods/behaviors it should have
**Output:** Complete Python skeleton with:
  - Private variables with getter/setter methods (for single items)
  - Public arrays with getter/setter methods (for multiple items)
  - Real-world method stubs with `pass` statements

## Example Workflow

### Step 1: Start with a topic
```
User: "I want to create a Car class"
Claude: Creates empty Car class and starts brainstorming
```

### Step 2: Brainstorm components
```
Claude: "A car needs:
  - Single: engine, transmission, weight, speed_limit
  - Multiple: tyres, seats, doors"
User: "Yes, add fuel_tank too"
```

### Step 3: Brainstorm methods
```
Claude: "Car should be able to:
  - start_engine()
  - accelerate()
  - brake()
  - refuel()
  - change_tire()"
User: "Perfect, generate it"
```

### Step 4: Get complete skeleton
```python
class Car:
    def __init__(self):
        self._engine = None
        self.tyres = ["left_front", "right_front", "left_rear", "right_rear"]
    
    def get_engine(self):
        pass
    
    def set_engine(self, engine):
        pass
    
    def start_engine(self):
        pass
    
    def accelerate(self, speed):
        pass
    # ... and so on
```

## Skill Patterns

### Single Attribute Pattern
For things like `battery`, `processor`, `name`:
```python
self._attribute = None

def get_attribute(self):
    pass

def set_attribute(self, value):
    pass
```

### Multiple Attributes Pattern
For things like `tyres`, `seats`, `departments`:
```python
self.attributes = [
    "item_1",
    "item_2",
    "item_3"
]

def get_attributes(self):
    pass

def set_attributes(self, items):
    pass
```

### Method Pattern
For behaviors like `start()`, `stop()`, `process()`:
```python
def method_name(self, param1, param2):
    pass
```

## Best Use Cases
- ✅ Initial architecture/design phase
- ✅ Object-oriented system planning
- ✅ Class structure scaffolding
- ✅ Complex domain modeling
- ✅ Multiple brainstorming iterations
- ✅ Quickly turning ideas into code

## Topics That Work Well
- 🚗 Vehicles (Car, Bus, Airplane, Bike)
- 👤 Living things (Human, Animal, Plant)
- 🏥 Organizations (Hospital, School, Company, Bank)
- 🎮 Games & Entertainment (Game, Character, Level)
- 💻 Technology (Smartphone, Computer, Robot)
- 🏠 Real-world systems (House, Restaurant, Library)

## Tips for Best Results
1. **Be specific with topics** - "Car" is better than "Vehicle"
2. **Ask clarifying questions** - The skill will ask, but feel free to guide
3. **Iterate freely** - Say "add X" or "remove Y" and it regenerates
4. **Review the skeleton** - Make sure it matches your mental model
5. **Extend later** - The skeleton can always be expanded with real logic

## Test Results
✅ Simple topics (Smartphone) - Clear component identification, good method diversity
✅ Complex topics (University) - Handles multiple arrays, numerous attributes
✅ Domain-specific (Robot) - Captures specialized attributes and operations
✅ Incremental building (Book) - Works well when adding components iteratively

---

**Created:** August 2026  
**Skill Type:** Brainstorming + Code Generation  
**Best for:** Developers, architects, system designers
