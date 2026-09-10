---
name: brainstorm-to-code
description: Brainstorm a topic to generate Python class skeletons with real-world functions. Use this skill whenever a user wants to design a class structure, architect an object-oriented system, or generate Python skeleton code with attributes and methods. Trigger on phrases like "generate a skeleton for X", "create a class structure", "design this as a class", "let's brainstorm X", or any request to turn a concept into Python code with getter/setter methods and business logic functions.
---

# Brainstorm-to-Code Skill

This skill helps you iteratively brainstorm a topic and convert it into a well-structured Python class skeleton with:
- **Single attributes** with private variables, getters, and setters
- **Multiple attributes** as arrays with getters and setters
- **Real-world methods** with business logic (all with `pass` statements)

## Workflow

### 1. Start Simple
Ask the user for their topic and create an empty class:
```python
class TopicName:
    pass
```

### 2. Brainstorm Components
Identify what the class needs:
- **Single items** (like an engine in a car, or IQ in a brain) → private variable + getter/setter
- **Multiple items** (like tyres, seats, lobes) → array with all specific items

Ask guiding questions like:
- "What are the main components?"
- "Are there things that come in multiples?"
- "Should we track any measurements or properties?"

### 3. Brainstorm Methods
Think about real-world behaviors and actions:
- What can this object do?
- What operations would a user perform on it?
- What calculations or processes should it handle?

Ask questions like:
- "What actions can be performed on this?"
- "What real-world functions would this need?"
- "Should it track state changes?"

### 4. Generate Python Skeleton

Once you've brainstormed both components and methods, generate the complete skeleton:

**Pattern for single attributes:**
```python
def get_attribute_name(self):
    pass

def set_attribute_name(self, value):
    pass
```

**Pattern for array attributes:**
```python
self.attribute_name = [
    "item_1",
    "item_2",
    "item_3"
]

def get_attribute_name(self):
    pass

def set_attribute_name(self, items):
    pass
```

**Pattern for methods:**
```python
def method_name(self, param1, param2):
    pass

def another_method(self):
    pass
```

## Tips

- **Ask clarifying questions** before generating to ensure you're capturing the user's vision
- **Group related attributes** logically in `__init__`
- **Use descriptive method names** that reflect real-world actions
- **If unsure about a component, suggest it** but ask for confirmation
- **Iterate** - if the user says "let's add X" or "remove Y", regenerate the skeleton with updates

## Example Topics
- Vehicles (car, truck, bike)
- Living things (human, animal, plant)
- Systems (school, hospital, library)
- Technology (smartphone, computer, game)
- Organizations (company, team, club)
