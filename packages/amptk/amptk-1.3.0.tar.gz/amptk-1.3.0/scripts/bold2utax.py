#!/usr/bin/env python

from __future__ import print_function
from builtins import str
import sys
import re
import argparse
import os
import subprocess
import shutil
import io
from natsort import natsorted
from Bio import pairwise2
from Bio.SeqIO.FastaIO import FastaIterator
from amptk import amptklib

def main():
    #setup menu with argparse
    class MyFormatter(argparse.ArgumentDefaultsHelpFormatter):
        def __init__(self,prog):
            super(MyFormatter,self).__init__(prog,max_help_position=48)
    parser=argparse.ArgumentParser(prog='bold2utax.py',
        description='''Parse BOLD DB TSV data dump into FASTA with UTAX compatible labels.''',
        epilog="""Written by Jon Palmer (2016) nextgenusfs@gmail.com""",
        formatter_class = MyFormatter)
    parser.add_argument('-i','--input', required=True, help='Bold data dump TSV format')
    parser.add_argument('-o','--out', required=True, help='UTAX formated FASTA output')
    parser.add_argument('--require_genbank', action='store_true', help='Require output to have GenBank Accessions')
    args=parser.parse_args()

    Total = -1
    nonCOI = 0
    noBIN = 0
    count = 0
    #create tmpdirectory
    pid = os.getpid()
    tmp = 'boldutax_'+str(pid)
    if not os.path.exists(tmp):
        os.makedirs(tmp)

    #store taxonomy in dictionary
    BINtax = {}
    with open(os.path.join(tmp, 'first-pass.fa'), 'w') as output:
        with io.open(args.input, encoding="latin", errors='ignore') as input:
            for line in input:
                Total += 1
                line = line.replace('\n', '')
                if line.startswith('processid'):
                    header = line.split('\t')
                    pid = header.index('phylum_name')
                    cid = header.index('class_name')
                    oid = header.index('order_name')
                    fid = header.index('family_name')
                    gid = header.index('genus_name')
                    sid = header.index('species_name')
                    seqid = header.index('nucleotides')
                    boldid = header.index('sequenceID')
                    gbid = header.index('genbank_accession')
                    bin = header.index('bin_uri')
                    idby = header.index('identification_provided_by')
                    marker = header.index('marker_codes')
                    continue
                #split each line at tabs
                col = line.split('\t')

                #apparently there are other genes in here, so ignore anything not COI
                if not 'COI' in col[marker]:
                    nonCOI += 1
                    continue

                #check for BIN, if none, then move on
                BIN = col[bin].strip()
                if BIN == '':
                    noBIN += 1
                    continue

                #some idiots have collector names in these places in the DB, this DB is kind of a mess, doing the best I can....
                bd = col[idby].strip()
                badnames = bd.split(' ')
                badfiltered = ['1','2','3','4','5','6','7','8','9','0']
                for y in badnames:
                    if len(y) > 2:
                        if y != 'Art':
                            if y != 'Eric':
                                badfiltered.append(y)
                K = 'k:Animalia'
                P = 'p:'+col[pid].strip()
                C = 'c:'+col[cid].strip()
                O = 'o:'+col[oid].strip()
                F = 'f:'+col[fid].strip()
                G = 'g:'+col[gid].strip()
                S = 's:'+col[sid].strip().replace('.', '')
                if ' sp ' in S: #remove those that have sp. in them
                    S = ''
                if S.endswith(' sp'):
                    S = ''
                if badfiltered:
                    if any(bad in G for bad in badfiltered):
                        G = ''
                    if any(bad in S for bad in badfiltered):
                        S = ''
                ID = col[boldid].strip()
                GB = col[gbid].strip()
                if args.require_genbank:
                    if GB: #if there is a GB accession
                        if 'Pending' in GB:
                            continue
                        else:
                            pass
                    else:
                        continue
                #clean up sequence, remove any gaps, remove terminal N's
                Seq = col[seqid].replace('-', '')
                Seq = Seq.strip('N')
                #if still N's in sequence, just drop it
                if 'N' in Seq:
                    continue
                #get taxonomy information
                tax = []
                for i in [K,P,C,O,F,G,S]:
                    if not i.endswith(':'):
                        tax.append(i)
                tax_fmt = ','.join(tax)
                tax_fmt = tax_fmt.rstrip()
                if tax_fmt.endswith(','):
                    tax_fmt = tax_fmt.rsplit(',',1)[0]
                if not BIN in BINtax:
                    BINtax[BIN] = tax_fmt
                else:
                    oldtax = BINtax.get(BIN)
                    oldtax_count = oldtax.count(',')
                    newtax_count = tax_fmt.count(',')
                    if newtax_count > oldtax_count:
                        BINtax[BIN] = tax_fmt
                #just write to fasta file first
                count += 1
                if GB:
                    output.write('>{:}_{:};tax={:}\n{:}\n'.format(BIN, GB, tax_fmt, amptklib.softwrap(Seq)))
                else:
                    output.write('>{:}_NA;tax={:}\n{:}\n'.format(BIN, tax_fmt, amptklib.softwrap(Seq)))
                    
    print("%i total records processed" % Total)
    print("%i non COI records dropped" % nonCOI)
    print("%i records without a BIN dropped" % noBIN)
    print("%i records written to BINs" % count)
    print("Now looping through BINs and clustering with VSEARCH @ 99%")
    FNULL = open(os.devnull, 'w')
    cluster_out = os.path.join(tmp, 'consensus.fa')
    subprocess.call(['vsearch', '--cluster_fast', os.path.join(tmp, 'first-pass.fa'), 
    				'--id', '0.99', '--consout', cluster_out, '--notrunclabels'], stdout = FNULL, stderr = FNULL)

    print("Updating taxonomy")
    #finally loop through centroids and get taxonomy from dictionary 
    finalcount = 0
    with open(args.out, 'w') as outputfile:
        for record in FastaIterator(open(cluster_out)):
            record.id = record.id.replace('consensus=', '')
            finalcount += 1
            fullname = record.id.split(';')[0]
            ID = fullname.split('_')[0]
            if ID in BINtax:
            	tax = BINtax.get(ID)
            else:
            	print('{:} not found in taxonomy dictionary'.format(ID))
            	continue
            outputfile.write('>{:};tax={:}\n{:}\n'.format(ID, tax, amptklib.softwrap(str(record.seq))))

    print("Wrote %i consensus seqs for each BIN to %s" % (finalcount, args.out))
    shutil.rmtree(tmp)

if __name__ == "__main__":
    main()
