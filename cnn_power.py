#!/usr/bin/python

from os import argv

def calc_power(entropy, dataset_size, design_power, frequency, calculation_clocks):
    
    ddr_power_per_bit = 180e-3 / 1

    if entropy > 8:
        print("Entropy is bigger then 8. compression is useless!!!")

    bytes_to_transfer = (1.0 * dataset_size) / 8 * entropy
    design_energy = (1.0 * design_power) / frequency * calculation_clocks






print os.argv
# calc_power()