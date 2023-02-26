# parse_the_human_proteome
A Python script to parse and bin proteins in the human proteome by molecular size and visualize results.

![alt_text](https://i.ibb.co/fYqPRfV/Num-Prot-0-1650-binwidth-50.png)

## Notes
To challenge myself, this project was coded using the Python base package only (no libraries). However, to visualize results, matplotlib.pyplot was used to generate plots.

## Requirements
1. Python 3
2. Any text editor
3. The file called "uniprot-9606-reviewed.fasta" which is included in this repository

## How to Run This Program
1. Download this repository
2. Run the script "human_proteome_parser.py" from inside the folder called "run_from_this_dict"

## Steps Performed
1. Set parameters
    - User is prompted to enter the following:
        1. Desired lower bound of protein lengths: (e.g. 0 residues)
        2. Desired upper bound of protein lengths: (e.g. 1500 residues)
        3. Desired bin width: (e.g. 50 residues)
            - *Note*: Please enter only the integer, not the string "residues"
3. Define helper functions
    - make_dict
        - Parses the .fasta file, isolating the protein name from the molecular sequence
    - identify_bin
        - Based on user-specified input (bin width, range of protein sizes to consider), bin proteins based on number of residues
    - cumilative_sum
        - Creates running sum of elements in a list. For example, the list [1,2,3,4,5] becomes [1,3,6,10,15].
4. Generate dictionary by calling make_dict
    - (protein name) : (protein length)
5. Calculate number of proteins and relative frequency of proteins in each bin by calling identify_bin
6. Calculate cumilitive frequency of proteins by calling cumilative_sum
7. Generate new dictionary based on binned data
    - (cur bin) : [ (protein length) , (relative frequency of occurance in the human proteome), (cumilitive frequency) ]
9. Display output in commend window
10. Write output to CSV
11. Plot and save histograms for data visualization
