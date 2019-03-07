import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import BasicAer, execute
from qiskit.quantum_info import Pauli, state_fidelity, basis_state, process_fidelity

q = QuantumRegister(3)
c = ClassicalRegister(3)

circ = QuantumCircuit(q, c)

circ.h(q[0])
circ.h(q[1])
circ.x(q[2])
circ.cx(q[1], q[2])
circ.cx(q[0], q[2])
circ.h(q)
circ.barrier(q)
circ.measure(q, c)

print(circ.draw())

backend_sim = BasicAer.get_backend('statevector_simulator')
result = execute(circ, backend_sim).result()
state = result.get_statevector(circ)
print(state)
