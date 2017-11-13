#!/usr/bin/env python3
# -*- coding: utf-8 -*-

 #   This software was developed by Zanoni Dias, Ulisses Dias and João
 #   C. Setubal
 #
 #   It should not be redistributed or used for any commercial purpose
 #   without written permission from authors
 #
 #   release date: nov 15, 2011
 #
 # This software is experimental in nature and is
 # supplied "AS IS", without obligation by the authors to provide
 # accompanying services or support.  The entire risk as to the quality
 # and performance of the Software is with you. The authors
 # EXPRESSLY DISCLAIM ANY AND ALL WARRANTIES REGARDING THE SOFTWARE,
 # WHETHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO WARRANTIES
 # PERTAINING TO MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.
 #

import sys
import re

def parse_sis(sis_filename) :
    sis_file = open(sis_filename)
    scaffolds     = []
    line_count    = 0

    for line in sis_file :
        line_count = line_count + 1
        if line.rstrip() :
            match = re.match("^>(.*?)$", line)
            if match :
                scaffolds.append([match.group(1).rstrip().lstrip(),
                                 []])
            else :
                match = re.match("^(.*) ([01])$", line)
                if match :
                    scaffolds[-1][1].append([match.group(1),
                                            int(match.group(2))]
                                            )
                else :
                    print("Warning: ignoring line %s:\n %s" % (line_count,
                                                               line))

    return scaffolds

# Read the draft genome and create a contig dictionary
def contig_dictionary(genome_array) :
    contig_dict  = {}
    last_contig = ""
    last_count  = 0

    i = 0

    for i in range(len(genome_array)) :
        line = genome_array[i]
        match = re.match("^>(.*?)( .*)?$", line)
        if match :
            if last_contig :
                contig_dict[last_contig].append(i)
                contig_dict[last_contig].append(last_count)

            last_contig = match.group(1)
            last_count  = 0
            if not last_contig in contig_dict :
                contig_dict[last_contig] = [match.group(2), i+1]
            else :
                print("Two contigs with the same name")
                sys.exit()
        else :
            last_count = last_count + len(line.rstrip().lstrip())
    contig_dict[last_contig].append(len(genome_array))
    contig_dict[last_contig].append(last_count)
    return contig_dict

def reverse_string(input_sequence) :
    output_sequence = ""
    for el in input_sequence.rstrip() :
        new_el = ""
        if el == "A" :
            new_el = "T"
        elif el == "T" :
            new_el = "A"
        elif el == "G" :
            new_el = "C"
        elif el == "C" :
            new_el = "G"
        elif el == "N" :
            new_el = "N"
        elif el == "S" :
            new_el = "S"
        elif el == "W" :
            new_el = "W"
        elif el == "M" :
            new_el = "K"
        elif el == "K" :
            new_el = "M"
        elif el == "R" :
            new_el = "Y"
        elif el == "Y" :
            new_el = "R"
        else :
#            print("ERRO: Caracter nao permitido no genoma '%s'" % el)
            new_el = ""
        output_sequence = "%s%s" % (new_el,output_sequence)
    return "%s\n" % output_sequence


####################################################
#################### MAIN ##########################
################## FUNCTION ########################
####################################################
def main(args=None):
    if args is None:
        args = sys.argv
    ## Reading SIS file
    try:
        scaffolds = parse_sis(args[1])

        ## Reading Draft Genome
        draft       = open(args[2])
        draft_array = draft.readlines()
        contig_dict = contig_dictionary(draft_array)

        for scaffold  in scaffolds :
            scaffold_file = open("%s.fna" % scaffold[0],"w")

            for contig in scaffold[1] :
                scaffold_file.write(">%s \n" % contig[0])

                contig_range = list(range(contig_dict[contig[0]][1],
                                          contig_dict[contig[0]][2])
                )

                if contig[1] :
                    contig_range.reverse()
                    for j in contig_range :
                        scaffold_file.write(reverse_string(draft_array[j]))
                else :
                    for j in contig_range :
                        scaffold_file.write(draft_array[j])
    except :
        print("Usage: %s <sis> <multifasta>" % args[0])
        print("   <sis> is the output file of sis.py")
        print("   <multifasta> contigs.fasta")
