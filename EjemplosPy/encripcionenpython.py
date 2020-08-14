import base64
cartita = b"""
Hola me gustas
dhduasgugpjaojohusczj
gcsufihoshfuagsojohdajscl
hwaudygaishnosagugoadjskvuas
"""
secreto = base64.b85encode(cartita)
print(secreto)