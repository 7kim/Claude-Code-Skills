"""
Template: Single Attribute Pattern

Use this template when you have ONE of something (not multiple).
Examples: engine, battery, processor, name, iq, age, weight

Pattern:
- Private variable: self._attribute_name = None
- Getter method: get_attribute_name()
- Setter method: set_attribute_name(value)
"""

class ExampleClass:
    def __init__(self):
        # Single attributes - ONE of each
        # Use underscore prefix to indicate private
        self._engine = None
        self._battery = None
        self._processor = None
        self._brand_name = None
        self._iq = None
        self._weight = None
    
    # ============ SINGLE ATTRIBUTE PATTERN ============
    
    def get_engine(self):
        """Retrieve the engine attribute"""
        pass
    
    def set_engine(self, engine):
        """Set the engine attribute"""
        pass
    
    def get_battery(self):
        """Retrieve the battery attribute"""
        pass
    
    def set_battery(self, battery):
        """Set the battery attribute"""
        pass
    
    def get_processor(self):
        """Retrieve the processor attribute"""
        pass
    
    def set_processor(self, processor):
        """Set the processor attribute"""
        pass
    
    def get_brand_name(self):
        """Retrieve the brand name attribute"""
        pass
    
    def set_brand_name(self, brand_name):
        """Set the brand name attribute"""
        pass
    
    def get_iq(self):
        """Retrieve the IQ attribute"""
        pass
    
    def set_iq(self, iq):
        """Set the IQ attribute"""
        pass
    
    def get_weight(self):
        """Retrieve the weight attribute"""
        pass
    
    def set_weight(self, weight):
        """Set the weight attribute"""
        pass


# ============ NAMING CONVENTIONS ============
"""
Single Attribute Naming:
- Variable names: use_snake_case
- Getter: get_attribute_name()
- Setter: set_attribute_name(value)

Examples:
- self._battery_level -> get_battery_level() / set_battery_level()
- self._car_type -> get_car_type() / set_car_type()
- self._processing_speed -> get_processing_speed() / set_processing_speed()
"""
