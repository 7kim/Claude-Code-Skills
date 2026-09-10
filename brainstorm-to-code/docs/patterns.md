# Brainstorm-to-Code Patterns & Conventions

## Overview
This document explains the code patterns and naming conventions used by the Brainstorm-to-Code skill.

---

## 1. Class Structure

### Basic Template
```python
class MyClass:
    def __init__(self):
        # Single attributes (private)
        self._attribute_1 = None
        self._attribute_2 = None
        
        # Multiple attributes (public arrays)
        self.collection_1 = [...]
        self.collection_2 = [...]
    
    # Getter/setter methods
    # Real-world methods
```

---

## 2. Single Attributes (One of Each)

### When to Use
- Engine (one engine per car)
- Battery (one battery per phone)
- Age (one age per person)
- Processor (one CPU per computer)
- IQ (one IQ value per person)

### Pattern
```python
def __init__(self):
    self._attribute_name = None

def get_attribute_name(self):
    pass

def set_attribute_name(self, value):
    pass
```

### Naming Rules
- Variable: `_snake_case` (lowercase with underscores)
- Getter: `get_snake_case()`
- Setter: `set_snake_case(value)`
- Private indicator: Use `_` prefix

### Examples
```python
self._engine = None
def get_engine(self):
    pass
def set_engine(self, engine):
    pass

self._battery_level = None
def get_battery_level(self):
    pass
def set_battery_level(self, level):
    pass

self._iq = None
def get_iq(self):
    pass
def set_iq(self, iq):
    pass
```

---

## 3. Multiple Attributes (Arrays)

### When to Use
- Tyres (4 tyres on a car)
- Seats (5+ seats in a car)
- Doors (4 doors on a car)
- Students (many students in a university)
- Sensors (multiple sensors on a phone)
- Brain lobes (4 lobes in the brain)
- Buildings (multiple buildings on campus)

### Pattern
```python
def __init__(self):
    self.attribute_name = [
        "specific_item_1",
        "specific_item_2",
        "specific_item_3"
    ]

def get_attribute_name(self):
    pass

def set_attribute_name(self, items):
    pass
```

### Naming Rules
- Variable: `snake_case` (NO underscore - public)
- Use plural or collection names
- Getter: `get_attribute_name()`
- Setter: `set_attribute_name(items)`
- Array items: Specific, descriptive names

### Good vs. Bad Examples

✅ **GOOD:**
```python
self.tyres = [
    "left_front",
    "right_front",
    "left_rear",
    "right_rear"
]

self.seats = [
    "driver",
    "passenger_front",
    "passenger_rear_left",
    "passenger_rear_middle",
    "passenger_rear_right"
]

self.sensors = [
    "camera",
    "accelerometer",
    "gps",
    "microphone"
]

self.lobes = [
    "frontal",
    "parietal",
    "temporal",
    "occipital"
]
```

❌ **BAD:**
```python
self._tyres = [...]           # Don't use underscore for public collections
self.tyre_list = [...]        # Use "tyres", not "tyre_list"
self.tyres = [
    "tyre1",                  # Don't use generic "tyre1", be specific
    "tyre2",
    "tyre3"
]
self.items = ["item1", ...]   # Be specific about what items these are
self.things = [...]           # Avoid vague collection names
```

### Array Item Naming

**Position-based (physical location):**
```python
["left_front", "right_front", "left_rear", "right_rear"]
["front_left", "front_right", "rear_left", "rear_right"]
["top", "middle", "bottom"]
["north", "south", "east", "west"]
```

**Role-based (function/responsibility):**
```python
["driver", "passenger_front", "passenger_rear"]
["captain", "crew_member", "engineer"]
["manager", "developer", "designer"]
```

**Category-based (type/class):**
```python
["camera", "accelerometer", "gps", "microphone"]
["frontal", "parietal", "temporal", "occipital"]
["Maps", "Calendar", "Camera", "Messages"]
```

---

## 4. Real-World Methods

### Method Categories

#### 1. Lifecycle Methods
Powers on/off, starts/stops
```python
def power_on(self):
    pass

def power_off(self):
    pass

def start_engine(self):
    pass

def shutdown(self):
    pass
```

#### 2. Action Methods
Things the object actively does
```python
def accelerate(self, speed):
    pass

def brake(self, force):
    pass

def turn(self, direction):
    pass

def install_app(self, app_name):
    pass
```

#### 3. State Management
Changing or updating state
```python
def charge_battery(self, amount):
    pass

def refuel(self, amount):
    pass

def update(self, new_version):
    pass

def reset(self):
    pass
```

#### 4. Query/Calculation Methods
Asking for information or computing values
```python
def is_running(self):
    pass

def get_status(self):
    pass

def calculate_efficiency(self):
    pass

def check_availability(self):
    pass
```

#### 5. Complex Operations
Multi-step processes
```python
def process_data(self, data):
    pass

def transform(self, input_data):
    pass

def execute_task(self, task):
    pass
```

### Method Naming Conventions

| Category | Pattern | Examples |
|----------|---------|----------|
| Action | `verb()` | `accelerate()`, `brake()`, `turn()` |
| Lifecycle | `verb()` | `power_on()`, `shutdown()` |
| State change | `verb_object()` | `refuel()`, `charge_battery()`, `update_version()` |
| Query (boolean) | `is_*()`, `has_*()` | `is_running()`, `has_battery()` |
| Query (get value) | `get_*()`, `calculate_*()` | `get_status()`, `calculate_max_speed()` |
| Specific action | `object_action()` | `change_tire()`, `open_door()`, `install_app()` |

### Real-World Examples

**Car Class Methods:**
```python
def start_engine(self):
    pass

def accelerate(self, speed):
    pass

def brake(self, force):
    pass

def refuel(self, amount):
    pass

def change_tire(self, position, new_tire):
    pass

def open_door(self, door_position):
    pass

def shift_gear(self, gear):
    pass

def calculate_max_speed(self):
    pass
```

**Brain Class Methods:**
```python
def think(self, problem):
    pass

def remember(self, data):
    pass

def recall(self, memory_type):
    pass

def focus(self, duration):
    pass

def learn(self, subject, complexity):
    pass

def process_emotion(self, emotion):
    pass

def create_neural_pathway(self):
    pass
```

**Phone Class Methods:**
```python
def power_on(self):
    pass

def install_app(self, app_name):
    pass

def uninstall_app(self, app_name):
    pass

def take_photo(self, camera_type):
    pass

def make_call(self, contact):
    pass

def send_message(self, contact, message):
    pass

def toggle_airplane_mode(self):
    pass
```

---

## 5. Complete Example: Car Class

```python
class Car:
    def __init__(self):
        # Single Attributes
        self._engine = None
        self._transmission = None
        self._weight = None
        self._car_type = None
        self._speed_limit = None
        self._acceleration = None
        
        # Multiple Attributes
        self.tyres = [
            "left_front",
            "right_front",
            "left_rear",
            "right_rear"
        ]
        
        self.seats = [
            "driver",
            "passenger_front",
            "passenger_rear_left",
            "passenger_rear_middle",
            "passenger_rear_right"
        ]
        
        self.doors = [
            "front_left",
            "front_right",
            "rear_left",
            "rear_right"
        ]
    
    # Single Attribute: Engine
    def get_engine(self):
        pass
    
    def set_engine(self, engine):
        pass
    
    # Multiple Attribute: Tyres
    def get_tyres(self):
        pass
    
    def set_tyres(self, tyres):
        pass
    
    # Real-World Methods
    def start_engine(self):
        pass
    
    def accelerate(self, speed):
        pass
    
    def brake(self, force):
        pass
    
    def change_tire(self, position, new_tire):
        pass
```

---

## 6. Best Practices

### ✅ DO:
- Use descriptive, specific names for array items
- Use `_` prefix for private single attributes
- Use plural/collection names for arrays (without `_`)
- Name methods after actions/verbs
- Group related getters/setters
- Comment method sections for clarity
- Keep methods focused on one task

### ❌ DON'T:
- Use generic names like "item1", "thing2"
- Mix single and multiple with same naming
- Use underscore for public collections
- Make method names too vague
- Have methods do multiple unrelated things
- Forget to provide both getter and setter
- Use confusing abbreviations

---

## 7. Progressive Enhancement

The skeleton code is just the START. After generation, you can:

1. **Add implementation** to method bodies (replace `pass`)
2. **Add docstrings** for documentation
3. **Add type hints** for clarity (Python 3.5+)
4. **Add properties** (use `@property` decorator)
5. **Add error handling** (try/except blocks)
6. **Add validation** (input checking)

Example:
```python
def set_speed_limit(self, speed_limit: int) -> None:
    """Set the speed limit in km/h.
    
    Args:
        speed_limit: Speed limit value (positive integer)
        
    Raises:
        ValueError: If speed_limit is negative
    """
    if speed_limit < 0:
        raise ValueError("Speed limit cannot be negative")
    self._speed_limit = speed_limit
```

---

## 8. When to Use Single vs. Multiple

| Scenario | Use | Example |
|----------|-----|---------|
| ONE per object | Single | Engine, Battery, Brain, Processor |
| MANY per object | Multiple | Tyres, Seats, Students, Sensors |
| Unclear? | Ask! | "Are there usually many of these?" |
| 0 or 1 | Single | `_manager = None` |
| 1 or more (list) | Multiple | `team = ["member1", ...]` |

---

## References
- See `examples/` for complete working skeletons
- See `templates/` for detailed pattern templates
- See `SKILL.md` for workflow guidance
