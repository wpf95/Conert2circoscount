# Conert2circoscount.py
   

`usage:`python Conert2circoscount.py [input.file] step(mb) > [out.file]

`example:` When i want to count in bins of 5mb ,the unit of step is mb.  
python Conert2circoscount.py [input.file] 5 > [out.file]

Input file format is below：(no header or header startwith "#")(split by space or "\t"),The column1 must chrom column2 and column3 is position. 
Input file must be sorted by chrom
 
1       206868  206885  
1       209407  209431  
1       209552  209572  
2       206868  206885
