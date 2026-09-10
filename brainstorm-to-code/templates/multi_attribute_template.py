"""
Template: Multiple Attributes Pattern (Arrays)

Use this template when you have MULTIPLE of something.
Examples: tyres, seats, doors, students, courses, buildings, sensors

Pattern:
- Public array: self.attribute_name = [...]
- Getter method: get_attribute_name()
- Setter method: set_attribute_name(items)
- List items descriptively: "left_front", "passenger_rear", etc.
"""

class ExampleClass:
    def __init__(self):
        # Multiple attributes - MANY of each (as arrays)
        # Use PUBLIC names for collections (no underscore prefix)
        
        # Example 1: Tyres on a car
        self.tyres = [
            "left_front",
            "right_front",
            "left_rear",
            "right_rear"
        ]
        
        # Example 2: Seats in a car
        self.seats = [
            "driver",
            "passenger_front",
            "passenger_rear_left",
            "passenger_rear_middle",
            "passenger_rear_right"
        ]
        
        # Example 3: Doors on a car
        self.doors = [
            "front_left",
            "front_right",
            "rear_left",
            "rear_right"
        ]
        
        # Example 4: Installed apps on a phone
        self.installed_apps = [
            "Maps",
            "Calendar",
            "Camera",
            "Messages",
            "Phone"
        ]
        
        # Example 5: Students at a university
        self.students = [
            "student_1",
            "student_2",
            "student_3"
        ]
        
        # Example 6: Brain lobes
        self.lobes = [
            "frontal",
            "parietal",
            "temporal",
            "occipital"
        ]
    
    # ============ MULTIPLE ATTRIBUTES PATTERN ============
    
    def get_tyres(self):
        """Retrieve all tyres"""
        pass
    
    def set_tyres(self, tyres):
        """Set all tyres (replaces entire list)"""
        pass
    
    def get_seats(self):
        """Retrieve all seats"""
        pass
    
    def set_seats(self, seats):
        """Set all seats (replaces entire list)"""
        pass
    
    def get_doors(self):
        """Retrieve all doors"""
        pass
    
    def set_doors(self, doors):
        """Set all doors (replaces entire list)"""
        pass
    
    def get_installed_apps(self):
        """Retrieve all installed apps"""
        pass
    
    def set_installed_apps(self, apps):
        """Set all installed apps (replaces entire list)"""
        pass
    
    def get_students(self):
        """Retrieve all students"""
        pass
    
    def set_students(self, students):
        """Set all students (replaces entire list)"""
        pass
    
    def get_lobes(self):
        """Retrieve all brain lobes"""
        pass
    
    def set_lobes(self, lobes):
        """Set all brain lobes (replaces entire list)"""
        pass


# ============ NAMING CONVENTIONS ============
"""
Multiple Attributes Naming:
- Variable names: use_snake_case (plural or collection name)
- Getter: get_attribute_name()
- Setter: set_attribute_name(items)
- List items: specific, descriptive names

Examples:
✅ Good:
  self.tyres = ["left_front", "right_front", "left_rear", "right_rear"]
  self.seats = ["driver", "passenger_front", "passenger_rear_left"]
  self.sensors = ["camera", "accelerometer", "gps", "microphone"]
  
❌ Don't:
  self.tyre_list = ["tyre1", "tyre2", "tyre3"]  # Use "tyres" not "tyre_list"
  self.items = ["item1", "item2"]  # Be specific: "seats", "doors", etc.

List Item Naming:
- Be specific and descriptive
- Use position/location when applicable: "left_front", "rear_left"
- Use role/type when applicable: "driver", "passenger_front"
- Use underscore_case for multi-word items
"""
