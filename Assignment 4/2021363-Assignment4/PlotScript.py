import matplotlib.pyplot as plt
import pyshark



class plotting:
    def __init__(self, f_path):
        self.c_window_list = []        
        self.t_list = []        
        self.f_path = f_path

    def gather_data(self):

        cap = pyshark.FileCapture(self.f_path)
        

        for packet in cap:

            if 'TCP' in packet:
                try:
                    t = float(packet.sniff_timestamp)
                    c_window = int(packet.tcp.window_size)
                    
                    self.c_window_list.append(c_window)
                    self.t_list.append(t)
                    
                except AttributeError as e:
                    print(f"Attribute error: {e}")

    def plot(self):
        plt.plot(self.t_list, self.c_window_list)
        plt.title('Congestion Window Over Time')

        plt.xlabel('Time (seconds)')
        plt.ylabel('Congestion Window Size')

        plt.show()

if __name__ == "__main__":

    plotting = plotting('vansh.pcap')
    plotting.gather_data()
    plotting.plot()