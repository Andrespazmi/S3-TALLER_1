class Cargo:
    secuencia=0
    def __init__(self,des="sin cargo") :
        Cargo.secuencia=Cargo.secuencia+1
        self.codigo=Cargo.secuencia
        self.descripcion=des


cargo1 = Cargo()
print(cargo1.codigo,cargo1.descripcion)
cargo2 = Cargo()
cargo2.descripcion="Director"
print(cargo2.codigo,cargo2.descripcion)
cargo3 = Cargo("Analista")
print(cargo3.codigo,cargo3.descripcion)
#print (cargo.secuencia)
#print(cargo1.secuencia)
#print(cargo2.secuencia)
#print(cargo3.secuencia)