class MotorElectrico:
    Potencia= None 

    def encender (self):
        print ("Encendido motor electrico")

    def __init__(self):
        pass

motor1= MotorElectrico()
motor1.potencia= 1000
motor1.encender()    
