from array_stack import ArrayStack as AS

Original = AS()
Fidelity = AS()
Helper = AS()

Original.push('JAMFX') # Non-Fidelity funds
Original.push('FSELX')
Original.push('FOCPX')
Original.push('AFOIX') #
Original.push('TEFQX') #
Original.push('FSRPX')
Original.push('MSSMX') #
Original.push('FSCSX')
Original.push('FSPTX')
Original.push('FCPGX')
Original.push('MACGX') #
Original.push('JMCGX') #
Original.push('FCVSX')
Original.push('NEXTX') #
Original.push('BFOCX') #
Original.push('BFGFX') #
Original.push('ADNPX') #
Original.push('FDSVX')
Original.push('FSAVX')
Original.push('FHKCX')
Original.push('SAGAX') #
Original.push('FSEAX')
Original.push('CPOAX') #
Original.push('FDCPX')
Original.push('FTRNX')
Original.push('FNCMX')
Original.push('FBGRX')
Original.push('FSMEX') 

for fidelityFunds in range(5):
  Helper.push(Original.pop())
Fidelity.push(Original.pop())
Helper.push(Original.pop())
Fidelity.push(Original.pop())

for fidelityFunds in range(3):
  Helper.push(Original.pop())
  
for normalFunds in range(4):
  Fidelity.push(Original.pop())
Helper.push(Original.pop())

for normalFunds in range(2):
  Fidelity.push(Original.pop())

for fidelityFunds in range(3):
  Helper.push(Original.pop())
Fidelity.push(Original.pop())
Helper.push(Original.pop())

for normalFunds in range(2):
  Fidelity.push(Original.pop())

for fidelityFunds in range(2):
  Helper.push(Original.pop())
Fidelity.push(Original.pop())

for normalFunds in range(len(Fidelity)):
  Original.push(Fidelity.pop())
for fidelityFunds in range(len(Helper)):
  Fidelity.push(Helper.pop())

print(Original.top()) # To check what's at the top of each stack
print(Fidelity.top())

""" Runtime of the program: O(n), the function is linear."""