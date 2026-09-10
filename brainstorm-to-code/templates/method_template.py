"""
Template: Real-World Methods Pattern

These are the actual business logic methods - the things your object can DO.
All start with 'pass' statements as placeholders for real implementation.

Method categories:
1. Lifecycle: power_on(), start(), initialize()
2. Actions: accelerate(), brake(), turn()
3. State Management: charge(), refuel(), update()
4. Queries: is_running(), get_status(), calculate()
5. Operations: transform(), process(), execute()
"""

class ExampleClass:
    def __init__(self):
        pass
    
    # ============ LIFECYCLE METHODS ============
    
    def power_on(self):
        """Initialize and turn on the device"""
        pass
    
    def power_off(self):
        """Shut down the device"""
        pass
    
    def initialize(self):
        """Set up initial state"""
        pass
    
    # ============ ACTION METHODS ============
    
    def accelerate(self, speed):
        """Increase speed or intensity"""
        pass
    
    def brake(self, force):
        """Decrease speed or stop"""
        pass
    
    def turn(self, direction):
        """Change direction"""
        pass
    
    def execute_action(self, action_name, params):
        """Perform a specific action"""
        pass
    
    # ============ STATE MANAGEMENT METHODS ============
    
    def charge(self, amount):
        """Add power/energy"""
        pass
    
    def refuel(self, amount):
        """Add fuel"""
        pass
    
    def update(self, new_value):
        """Update state or version"""
        pass
    
    def reset(self):
        """Return to default state"""
        pass
    
    # ============ QUERY/CALCULATION METHODS ============
    
    def is_running(self):
        """Check if device is active"""
        pass
    
    def get_status(self):
        """Return current status"""
        pass
    
    def calculate_efficiency(self):
        """Compute performance metric"""
        pass
    
    def check_availability(self):
        """Determine if resource is available"""
        pass
    
    # ============ OPERATION METHODS ============
    
    def transform(self, input_data):
        """Process and convert data"""
        pass
    
    def process(self, data):
        """Handle/process information"""
        pass
    
    def execute(self, command):
        """Run a command or task"""
        pass
    
    # ============ SPECIFIC DOMAIN EXAMPLES ============
    
    # Car-related methods
    def start_engine(self):
        pass
    
    def change_tire(self, position, new_tire):
        pass
    
    def open_door(self, door_position):
        pass
    
    # Brain-related methods
    def think(self, problem):
        pass
    
    def remember(self, data):
        pass
    
    def recall(self, memory_type):
        pass
    
    # Phone-related methods
    def install_app(self, app_name):
        pass
    
    def take_photo(self, camera_type):
        pass
    
    def make_call(self, contact):
        pass


# ============ METHOD NAMING CONVENTIONS ============
"""
Method Naming Rules:

1. Action Methods (things the object DOES):
   - Use verb names: accelerate(), brake(), turn(), charge()
   - Format: verb_object() like refuel(), change_tire(), open_door()

2. Query Methods (things we ASK the object):
   - Start with: is_, get_, check_, calculate_
   - Examples: is_running(), get_status(), check_availability()

3. State Change Methods:
   - Use descriptive verbs: update(), reset(), initialize(), shutdown()

4. Internal Methods:
   - Use underscore prefix for private: _helper_method()

Examples from Brainstorm-to-Code:

Car methods:
- start_engine()
- accelerate(speed)
- brake(force)
- refuel(amount)
- change_tire(position, new_tire)
- calculate_max_speed()

Brain methods:
- think(problem)
- remember(data)
- recall(memory_type)
- learn(subject, complexity)
- process_emotion(emotion)
- calculate_processing_speed()

Phone methods:
- power_on()
- install_app(app_name)
- take_photo(camera_type)
- make_call(contact)
- toggle_airplane_mode()

Pattern: Most verbs make good method names!
"""
