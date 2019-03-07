from qiskit.tools.visualization import plot_histogram
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, BasicAer

q = QuantumRegister(2)
c = ClassicalRegister(2)

# quantum circuit to make a Bell state
bell = QuantumCircuit(q,c)
bell.h(q[0])
bell.cx(q[0],q[1])

meas = QuantumCircuit(q,c)
meas.measure(q, c)

# execute the quantum circuit
backend = BasicAer.get_backend('qasm_simulator') # the device to run on
circ = bell+meas
result = execute(circ, backend, shots=1000).result()
counts  = result.get_counts(circ)
print(counts)

plot_histogram(counts)

second_result = execute(circ, backend, shots=1000).result()
second_counts  = second_result.get_counts(circ)
# Plot results with legend
legend = ['First execution', 'Second execution']
plot_histogram([counts, second_counts], legend=legend)
