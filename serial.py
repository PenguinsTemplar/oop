"""Python serial number generator."""



class SerialGenerator:
    def __init__(self, start=0):
        self.start = self.current = start
        
    def generate(self):
        self.current += 1
        return self.current
       
    def reset(self):
       self.current = self.start

# Test Cases
serial = SerialGenerator(start=100)
print("First Generation", serial.generate())
print("Second Generation", serial.generate())
print("Third Generation", serial.generate())
serial.reset()
print("After Reset", serial.generate())