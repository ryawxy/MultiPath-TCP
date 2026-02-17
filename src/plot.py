import matplotlib.pyplot as plt
import csv

packets = []
paths = []

try:
    with open('../results/transmission_log.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) 
        for row in reader:
            packets.append(int(row[0]))
            paths.append(int(row[1]))
except FileNotFoundError:
    print("Error: Run client.py first to generate data!")
    exit()

plt.figure(figsize=(10, 5))
plt.step(packets, paths, where='post', linewidth=3, color='blue')

plt.title('MPTCP Failover Simulation', fontsize=16)
plt.xlabel('Packet Sequence Number', fontsize=12)
plt.ylabel('Path Used (1=Primary, 2=Backup)', fontsize=12)
plt.yticks([1, 2], ['Path A (Primary)', 'Path B (Backup)'])
plt.grid(True, linestyle='--', alpha=0.7)
plt.ylim(0.5, 2.5)

plt.axvline(x=10, color='red', linestyle='--')
plt.text(10.5, 1.5, ' Link Failure Event', color='red', fontweight='bold')


output_path = '../results/failover_graph.png'
plt.savefig(output_path)
print(f"Graph saved to {output_path}")