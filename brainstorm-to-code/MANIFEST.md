# Brainstorm-to-Code Skill - Package Contents

## 📦 Package Structure

```
brainstorm-to-code/
├── SKILL.md                          # Main skill definition (required)
├── README.md                         # Comprehensive guide
├── MANIFEST.md                       # This file
├── examples/                         # Example generated code
│   ├── car_example.py               # Car class example
│   ├── human_brain_example.py       # HumanBrain class example
│   └── smartphone_example.py        # Smartphone class example
├── templates/                        # Code templates
│   ├── single_attribute_template.py # Template for single attributes
│   ├── multi_attribute_template.py  # Template for multiple attributes
│   └── method_template.py           # Template for methods
└── docs/                            # Additional documentation
    └── patterns.md                  # Code patterns and conventions
```

## 📄 Files Description

### Core Files (Required)

**SKILL.md**
- Official Claude skill definition
- YAML frontmatter with name and description
- Workflow instructions
- Code patterns and tips
- Triggering conditions

**README.md**
- User-friendly guide
- Example workflows
- Use cases and best practices
- Test results documentation

### Examples

**examples/car_example.py**
- Generated Car class with:
  - Single attributes: engine, transmission, weight, car_type, speed_limit, acceleration
  - Multiple attributes: tyres, seats, doors (as arrays)
  - Real-world methods: start_engine(), accelerate(), brake(), refuel(), etc.

**examples/human_brain_example.py**
- Generated HumanBrain class with:
  - Single attributes: IQ, age, memory_capacity, L1/L2/L3 memory
  - Multiple attributes: lobes, hemispheres (as arrays)
  - Real-world methods: think(), remember(), recall(), learn(), etc.

**examples/smartphone_example.py**
- Generated Smartphone class (similar structure to Car)

### Templates

**templates/single_attribute_template.py**
- Template showing proper pattern for single attributes
- Includes private variable initialization
- Shows getter/setter method structure

**templates/multi_attribute_template.py**
- Template for array-based attributes
- Shows array initialization with items
- Getter/setter methods for collections

**templates/method_template.py**
- Method naming conventions
- Parameter structure
- Docstring templates

### Documentation

**docs/patterns.md**
- Detailed code patterns
- When to use single vs. multiple attributes
- Method naming conventions
- Real-world method examples by category

## 🚀 Getting Started

1. **Read SKILL.md** for the skill definition
2. **Review README.md** for usage guide
3. **Check examples/** for sample generated code
4. **Reference templates/** when creating new classes
5. **Consult docs/patterns.md** for detailed patterns

## 📊 Skill Capabilities

✅ Brainstorms single attributes with getter/setter methods
✅ Brainstorms multiple attributes as arrays
✅ Generates real-world method stubs
✅ Handles simple to complex domains
✅ Iterative refinement support
✅ Production-ready code scaffolding

## 🎯 Trigger Conditions

The skill triggers when users request:
- "Generate a skeleton for X"
- "Create a class structure for X"
- "Design this as a class"
- "Let's brainstorm X" (for code generation)
- "Turn this concept into Python code"
- "Build an OOP structure for X"

## 📝 Version Information

- **Version:** 1.0
- **Created:** August 2026
- **Skill Type:** Brainstorming + Code Generation
- **Target Audience:** Developers, architects, system designers
- **Python Version:** 3.7+

## 🔧 Dependencies

None - this skill uses only standard Python syntax and patterns.

## 📞 Usage Notes

- All generated methods have `pass` statements and are ready for implementation
- Code follows PEP 8 naming conventions
- Private attributes use `_prefix` notation
- Public arrays use descriptive names
- Getter/setter methods follow `get_`/`set_` convention

---

**For more information, see README.md or SKILL.md**
