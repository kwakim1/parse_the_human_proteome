# parse_the_human_proteome
A Python script to parse the human proteome by molecular size and visualize results

## Steps Performed
1. Set parameters
2. Define helper functions
  - make_dict
  - identify_bin
  - cumilitive_sum
3. Generate dictionary containing (protein name) : (protein length)
4. Calculate number of proteins and relative frequency of proteins in each bin
5. Calculate cumilitive frequency of proteins
6. Generate new dictionary based on binned data: (cur bin) : [ (protein length) , (relative frequency of occurance in the human proteome), (cumilitive frequency) ]
7. Display output in commend window
8. Write output to CSV
9. Plot and save histograms for data visualization
