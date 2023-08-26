from qiskit import QuantumCircuit, Aer, transpile
from qiskit.visualization import plot_histogram
from qiskit.providers.aer import AerSimulator
from qiskit import assemble

# Step 1: Create a Quantum Circuit
# Create a quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Step 2: Prepare the Bell State
# Apply a Hadamard gate to the first qubit
qc.h(0)

# Apply a Controlled-NOT (CNOT) gate between the first and second qubit
qc.cx(0, 1)

# Step 3: Add Measurement
# Measure the qubits and store the result in classical bits
qc.measure([0, 1], [0, 1])

# Step 4: Simulate the Circuit
# Use Aer's qasm_simulator
simulator = AerSimulator()

# Transpile and assemble the circuit for simulation
t_qc = transpile(qc, simulator)
qobj = assemble(t_qc)

# Run the simulation
result = simulator.run(qobj).result()

# Step 5: Get and Display Results
# Extract and display the counts (results)
counts = result.get_counts()
plot_histogram(counts)
