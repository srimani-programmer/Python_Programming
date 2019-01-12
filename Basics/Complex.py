# Working with Complex DataTypes

simpleComplex = 34+14j

print(simpleComplex)

simpleComplex1 = 12

print(complex(simpleComplex1))

simpleComplex2 = -13j

print(complex(simpleComplex2))

simpleComplex3 = 34j + 14

print(simpleComplex3)

# Complex values can contain Integer and floating values

simpleFloatComplex = 1223.2344 + 5432.343235j

print(simpleFloatComplex)

simpleBinaryComplex = 0b110011100011 + 12.234j

simpleOctalComplex = 0o3215342 + 23452j

simpleHexaDecimalComplex = 0x263432AFBC + 23151343j

#Printing the complex DataTypes
print(simpleBinaryComplex)

print(simpleOctalComplex)

print(simpleHexaDecimalComplex)

# Printing the real and imaginary parts separately

print(simpleHexaDecimalComplex.real)

print(simpleHexaDecimalComplex.imag)

# Operations on Complex Numbers

# 1. Conjugate of a number

print(simpleOctalComplex.conjugate())


