
#### EXAMPLE 3

"""  CASE 1 - SIMPLY SUPPORTED BEAM :TWO POINT LOAD : Equivalent UDL  = (3)*P/L            Page 19 """
"""  CASE 2  - SIMPLY SUPPORTED BEAM: TWO POINT LOAD : Equivalent Double Point Load = 2*P    Page 20"""

"""  all examples based on the book: Structural Engineering Art and Approximation by Hugh Morrison-Manchester UK"""

class EquivalentUDL():      ####CASE 1
    ### CONNECTORS
    def __init__(self,span,pointLoad,youngModulus,momentOfInertia):
        self.span  = span             ####Span in meters
        self.pointLoad =pointLoad     ###point load in kN
        self.youngModulus = youngModulus     #### E in N/mm^2
        self.momentOfInertia = momentOfInertia    ## I in mm^4

    ### METHODOLOGY

    def MaxShearLoad(self):
        return (3/2)*self.pointLoad
    def MaxBendingMoment(self):
        return (3/8)*(self.span*self.pointLoad)
    def MaxDeflection(self):
        return (1e12)*(15/384)*(self.pointLoad*self.span**3)/(self.youngModulus*self.momentOfInertia)

class EquivDoublePointLoad():          # CASE 2
        ### CONNECTORS
    def __init__(self, span, pointLoad, youngModulus, momentOfInertia):
        self.span = span  ####Span in meters
        self.pointLoad = pointLoad  ###point load in kN
        self.youngModulus = youngModulus  #### E in N/mm^2
        self.momentOfInertia = momentOfInertia  ## I in mm^4

        ### METHODOLOGY

    def MaxShearLoad(self):
       return self.pointLoad

    def MaxBendingMoment(self):
        return (1 / 2) * (self.span * self.pointLoad)

    def MaxDeflection(self):
        return (1e12) * (1 / 24) * (self.pointLoad * self.span ** 3) / (self.youngModulus * self.momentOfInertia)



class ActualTwoPointLoad():          ### ACTUAL LOADING CONDITIONS

    ### CONNECTORS
    def __init__(self, span, pointLoad, youngModulus, momentOfInertia):
        self.span = span  ####Span in meters
        self.pointLoad = pointLoad  ###point load in kN
        self.youngModulus = youngModulus  #### E in N/mm^2
        self.momentOfInertia = momentOfInertia  ## I in mm^4

    ### METHODOLOGY

    def MaxShearLoad(self):
        return self.pointLoad

    def MaxBendingMoment(self):
        return (1 / 3) * (self.span * self.pointLoad)

    def MaxDeflection(self):
        return (1e12) * (23 / 648) * (self.pointLoad * self.span ** 3) / (self.youngModulus * self.momentOfInertia)

    ### OUTPUT


x =EquivalentUDL(3,4,210000,667000000)

x.span = 10                           ### in m.
x.pointLoad = 10                   ### in kN
print(x.MaxShearLoad())              #### in kN
print(x.MaxBendingMoment())          ### kN.m
print(x.MaxDeflection())             ### in mm


y =EquivDoublePointLoad(3,4,210000,667000000)

y.span = 10                          ### in m.
y.pointLoad = 10                     ### in kN
print(y.MaxShearLoad())              #### in kN
print(y.MaxBendingMoment())          ### kN.m
print(y.MaxDeflection())             #### in mm


z =ActualTwoPointLoad(3,4,210000,667000000)

z.span = 10                           ### in m.
z.pointLoad = 10                     ### in kN
print(z.MaxShearLoad())              #### in kN
print(z.MaxBendingMoment())          ### kN.m
print(z.MaxDeflection())             #### in mm