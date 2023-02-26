# parse_the_human_proteome
A Python script to parse the human proteome by molecular size and visualize results.

![alt_text](https://i.ibb.co/fYqPRfV/Num-Prot-0-1650-binwidth-50.png)


## Steps Performed
1. Set parameters
2. Define helper functions
    - make_dict
    - identify_bin
    - cumilitive_sum
3. Generate dictionary
    - (protein name) : (protein length)
5. Calculate number of proteins and relative frequency of proteins in each bin
6. Calculate cumilitive frequency of proteins
7. Generate new dictionary based on binned data
    - (cur bin) : [ (protein length) , (relative frequency of occurance in the human proteome), (cumilitive frequency) ]
9. Display output in commend window
10. Write output to CSV
11. Plot and save histograms for data visualization
