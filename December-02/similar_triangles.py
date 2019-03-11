side1=input("Enter the  dim of triangle1:")
side1=sorted(side1.split())
angle1=input("Enter the angles of triangle1:")
angle1=sorted(angle1.split())
side2=input("Enter the  dim of triangle2:")
side2=sorted(side2.split())
angle2=input("Enter the angles of triangle2:")
angle2=sorted(angle2.split())

AB=int(side1[0])
BC=int(side1[1])
CA=int(side1[2])

PQ=int(side2[0])
QR=int(side2[1])
RP=int(side2[2])

CAB=int(angle1[0])
ABC=int(angle1[1])
BCA=int(angle1[2])

RPQ=int(angle2[0])
PQR=int(angle2[1])
QRP=int(angle2[2])

prop=[]
if(int(AB/PQ) == int(BC/QR) == int(CA/RP)):
    prop.append("SSS")
if(int(AB/PQ) == int(BC/QR) and (int(ABC) == int(PQR))):
    prop.append("SAS")
if(int(ABC) == int(PQR) or int(CAB)==int(RPQ) or int(BCA) == int(QRP)):
    prop.append("AAA")
print(prop)
