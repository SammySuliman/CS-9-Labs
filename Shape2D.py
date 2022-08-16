# Shape2D.py

class Shape2D:
    def __init__(self, color):
        self.color = color
    def setColor(self, color2):
        self.color = color2
    def getColor(self):
        return self.color
    def getShapeProperties(self):
        return ('Shape: {}, Color: {}'.format('N/A', self.color))
        
if __name__ == '__main__':
    blue_shap = Shape2D('blue')
    blue_shap.getShapeProperties()
    blue_shap.setColor('green')
    blue_shap.getShapeProperties()
    print(blue_shap.getColor())
