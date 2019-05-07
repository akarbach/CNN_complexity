#!/usr/bin/python

from sys import argv

def calc_power(entropy, dataset_size, design_power, fpga_frequency, calculation_clocks):
    
    ddr_datarate = 1066e6
    ddr_power_write_per_16bit = 180e-3 * 1.5
    ddr_power_read_per_16bit  = 220e-3 * 1.5



    if entropy > 8:
        print("Entropy is bigger then 8. compression is useless!!!")

    bits_to_transfer = (1.0 * dataset_size) * entropy
    design_energy = (1.0 * design_power) / fpga_frequency * calculation_clocks
    transfer_read_energy = (1.0 * ddr_power_read_per_16bit ) * (1.0 * bits_to_transfer / 16) * 4 / ddr_datarate
    transfer_write_energy = (1.0 * ddr_power_write_per_16bit ) * (1.0 * bits_to_transfer / 16) * 4 / ddr_datarate
    print("")
    print("Total energy: {:.3E}[J]".format((design_energy + transfer_read_energy + transfer_write_energy)))
    print("Design energy: {:.3E}[J]".format(design_energy))
    print("Transfer read energy {:.3E}[J], Transfer write energy {:.3E}[J]".format(transfer_read_energy, transfer_write_energy))
    # print("Total energy: " +str(design_energy + transfer_energy)+"[J]. Design energy: " + str(design_energy) +"[J], Transfer energy " + str(transfer_energy) + "[J]")



def calc_work():
	conv1 = 112*112*64
	conv2 = 56*56*64
	conv3 = 56*56*64
	conv4 = 56*56*64
	conv5 = 56*56*64
	conv6 = 28*28*128
	conv7 = 28*28*128
	conv8 = 28*28*128
	conv9 = 28*28*128
	conv10 = 14*14*256
	conv11 = 14*14*256
	conv12 = 14*14*256
	conv13 = 14*14*256
	conv14 = 7*7*512
	conv15 = 7*7*512
	conv16 = 7*7*512
	conv17 = 7*7*512

	net = [conv1, conv2, conv3, conv4, conv5, conv6, conv7, conv8, conv9, conv10, conv11, conv12, conv13, conv14, conv15, conv16, conv17]


	sum = 0
	for conv in net:
		sum += conv

	for conv in net:
		print("{:.3E}".format(1.0 * conv / sum))




calc_power(*list(map(float,argv[1:])))

calc_work()