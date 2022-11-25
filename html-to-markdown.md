The Genetic Codes
=================

Compiled by Andrzej (Anjay) Elzanowski and Jim Ostell at National Center for Biotechnology Information (NCBI), Bethesda, Maryland, U.S.A.

Last update of the Genetic Codes: Jan. 7, 2019

NCBI takes great care to ensure that the translation for each coding sequence (CDS) present in GenBank records is correct. Central to this effort is careful checking on the taxonomy of each record and assignment of the correct genetic code (shown as a /transl\_table qualifier on the CDS in the flat files) for each organism and record. This page summarizes and references this work.

The synopsis presented below is based primarily on the reviews by [Osawa et al.](https://www.ncbi.nlm.nih.gov/pubmed/1579111?dopt=Abstract) (1992) and [Jukes and Osawa](https://www.ncbi.nlm.nih.gov/pubmed/8281749?dopt=Abstract) (1993). Listed in square brackets \[\] (under **Systematic Range**) are tentative assignments of a particular code based on sequence homology and/or phylogenetic relationships.

The print-form ASN.1 version of this document, which includes all the genetic codes outlined below, is also available [here](ftp://ftp.ncbi.nih.gov/entrez/misc/data/gc.prt). Detailed information on codon usage can be found at the [Codon Usage Database](http://www.kazusa.or.jp/codon).

GenBank format by historical convention displays mRNA sequences using the DNA alphabet. Thus, for the convenience of people reading GenBank records, the genetic code tables shown here use T instead of U. The initiator codon - whether it is AUG, CTG, TTG or something else, - is by default translated as methionine (Met, M). The possible intiator codons are marked as 'M' in the second ('Starts') row of the translation tables.

Currently, genetic codes can be set independently for nucleus, mitochondria, plastids and hydrogenosomes. The current settings for each of these on the taxonomic tree can be viewed by the four buttons directly underneath the following code list.

The following genetic codes are described here:  

*   [1\. The Standard Code](#SG1)
*   [2\. The Vertebrate Mitochondrial Code](#SG2)
*   [3\. The Yeast Mitochondrial Code](#SG3)
*   [4\. The Mold, Protozoan, and Coelenterate Mitochondrial Code and the Mycoplasma/Spiroplasma Code](#SG4)
*   [5\. The Invertebrate Mitochondrial Code](#SG5)
*   [6\. The Ciliate, Dasycladacean and Hexamita Nuclear Code](#SG6)
*   [9\. The Echinoderm and Flatworm Mitochondrial Code](#SG9)
*   [10\. The Euplotid Nuclear Code](#SG10)
*   [11\. The Bacterial, Archaeal and Plant Plastid Code](#SG11)
*   [12\. The Alternative Yeast Nuclear Code](#SG12)
*   [13\. The Ascidian Mitochondrial Code](#SG13)
*   [14\. The Alternative Flatworm Mitochondrial Code](#SG14)
*   [16\. Chlorophycean Mitochondrial Code](#SG16)
*   [21\. Trematode Mitochondrial Code](#SG21)
*   [22\. Scenedesmus obliquus Mitochondrial Code](#SG22)
*   [23\. Thraustochytrium Mitochondrial Code](#SG23)
*   [24\. Rhabdopleuridae Mitochondrial Code](#SG24)
*   [25\. Candidate Division SR1 and Gracilibacteria Code](#SG25)
*   [26\. Pachysolen tannophilus Nuclear Code](#SG26)
*   [27\. Karyorelict Nuclear Code](#SG27)
*   [28\. Condylostoma Nuclear Code](#SG28)
*   [29\. Mesodinium Nuclear Code](#SG29)
*   [30\. Peritrich Nuclear Code](#SG30)
*   [31\. Blastocrithidia Nuclear Code](#SG31)
*   [33\. Cephalodiscidae Mitochondrial UAA-Tyr Code](#SG33)

 

 

 

 

* * *

1\. The Standard Code (transl\_table=1)
---------------------------------------

By default all transl\_table in GenBank flatfiles are equal to id 1, and this is **not** shown. When transl\_table is not equal to id 1, it is shown as a qualifier on the CDS feature.

    AAs  = FFLLSSSSYY\*\*CC\*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = ---M------\*\*--\*----M---------------M----------------------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG1)

#### Initiation Codon:

AUG

#### Alternative Initiation Codons:

In rare cases, translation in eukaryotes can be initiated from codons other than AUG. A well documented case (including direct protein sequencing) is the GUG start of a ribosomal P protein of the fungus

[Candida albicans](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?name=Candida+albicans) ([Abramczyk et al.](https://www.ncbi.nlm.nih.gov/pubmed/12961752?dopt=Abstract)) and the GUG initiation in mammalian NAT1 ([Takahashi et al. 2005](https://www.ncbi.nlm.nih.gov/pubmed/15718103?dopt=Abstract)).

Other examples can be found in the following references: [Peabody 1989](https://www.ncbi.nlm.nih.gov/pubmed/2538469?dopt=Abstract); [Prats et al. 1989](https://www.ncbi.nlm.nih.gov/pubmed/2538817?dopt=Abstract); [Hann et al. 1992](https://www.ncbi.nlm.nih.gov/pubmed/3277717?dopt=Abstract); [Sugihara et al. 1990](https://www.ncbi.nlm.nih.gov/pubmed/2123874?dopt=Abstract). The standard code currently allows initiation from UUG and CUG in addition to AUG.  
[Back to top](#top)

* * *

2\. The Vertebrate Mitochondrial Code (transl\_table=2)
-------------------------------------------------------

    AAs  = FFLLSSSSYY\*\*CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSS\*\*VVVVAAAADDEEGGGG
  Starts = ----------\*\*--------------------MMMM----------\*\*---M------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG2)

#### Differences from the Standard Code:

        Code 2          Standard

 AGA    Ter  \*          Arg  R
 AGG    Ter  \*          Arg  R
 AUA    Met  M          Ile  I
 UGA    Trp  W          Ter  \*

#### Alternative Initiation Codons:

Bos: AUA

Homo: AUA, AUU

Mus: AUA, AUU, AUC

Coturnix, Gallus: also GUG ([Desjardins and Morais, 1991](https://www.ncbi.nlm.nih.gov/pubmed/1706782?dopt=Abstract))

#### Systematic Range:

Vertebrata

#### Comments:

AGA and AGG were thought to have become mitochondrial stop codons early in vertebrate evolution ([Osawa, Ohama, Jukes & Watanabe 1989](https://www.ncbi.nlm.nih.gov/pubmed/2506356?dopt=Abstract)). However, at least in humans it has now been shown that AGA and AGG sequences are not recognized as termination codons. A -1 mitoribosome frameshift occurs at the AGA and AGG codons predicted to terminate the CO1 and ND6 ORFs, and consequently both ORFs terminate in the standard UAG codon ([Temperley et al. 2010](https://www.ncbi.nlm.nih.gov/pubmed/20075246?dopt=Abstract)).

Mitochondrial genes in some vertebrate (including humans) have incomplete stop codons ending in U or UA, which become complete termination codons (UAA) upon subsequent polyadenylation ([Hou et al. 2006](https://www.ncbi.nlm.nih.gov/pubmed/17205108?dopt=Abstract); [Oh et al. 2007](https://www.ncbi.nlm.nih.gov/pubmed/17541835?dopt=Abstract); [Ki et al. 2010](https://www.ncbi.nlm.nih.gov/pubmed/19757186?dopt=Abstract); [Temperley R J et al 2010](https://www.ncbi.nlm.nih.gov/pubmed/20211597?dopt=Abstract)).  
[Back to top](#top)

* * *

3\. The Yeast Mitochondrial Code (transl\_table=3)
--------------------------------------------------

    AAs  = FFLLSSSSYY\*\*CCWWTTTTPPPPHHQQRRRRIIMMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = ----------\*\*----------------------MM---------------M------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG3)

#### Differences from the Standard Code:

        Code 3          Standard

 AUA    Met  M          Ile  I
 CUU    Thr  T          Leu  L
 CUC    Thr  T          Leu  L
 CUA    Thr  T          Leu  L
 CUG    Thr  T          Leu  L
 UGA    Trp  W          Ter  \*

#### Systematic Range:

_Saccharomyces cerevisiae_, _Candida glabrata_, _Hansenula saturnus_, and _Kluyveromyces thermotolerans_ ([Clark-Walker and Weiller, 1994](https://www.ncbi.nlm.nih.gov/pubmed/8083884?dopt=Abstract))

#### Comments:

GUG (GTG) is used as a start codon for a few proteins in some _Saccharomyces_ species ([Sulo et al. 2017](https://www.ncbi.nlm.nih.gov/pubmed/28992063?dopt=Abstract)). The remaining CGN codons are rare in _Saccharomyces cerevisiae_ and absent in _Candida glabrata_ (= _Torulopsis glabrata_).

The AUA codon is common in the gene var1 coding for the single mitochondrial ribosomal protein, but rare in genes encoding the enzymes.

The coding assignments of the AUA (Met or Ile) and CUU (possibly Leu, not Thr) are uncertain in _Hansenula saturnus_.

The coding assignment of Thr to CUN is uncertain in _Kluyveromyces thermotolerans_ ([Clark-Walker and Weiller, 1994](https://www.ncbi.nlm.nih.gov/pubmed/8083884?dopt=Abstract)).  
[Back to top](#top)

* * *

4\. The Mold, Protozoan, and Coelenterate Mitochondrial Code and the Mycoplasma/Spiroplasma Code (transl\_table=4)
------------------------------------------------------------------------------------------------------------------

    AAs  = FFLLSSSSYY\*\*CCWWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = --MM------\*\*-------M------------MMMM---------------M------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG4)

#### 

Differences from the Standard Code:

        Code 4         Standard

 UGA    Trp  W          Ter  \*

#### Alternative Initiation Codons:

**Trypanosoma**: UUA, UUG, CUG

**Leishmania**: AUU, AUA

**Tertrahymena**: AUU, AUA, AUG

**Paramecium**: AUU, AUA, AUG, AUC, GUG, GUA(?)

([Pritchard et al., 1990](https://www.ncbi.nlm.nih.gov/pubmed/2137906?dopt=Abstract))

#### Systematic Range:

**Bacteria**: The code is used in _Entomoplasmatales_ and _Mycoplasmatales_ ([Bove et al. 1989](https://www.ncbi.nlm.nih.gov/pubmed/7691196?dopt=Abstract)). The situation in the _Acholeplasmatales_ is unclear. Based on a study of ribosomal protein genes, it had been concluded that UGA does not code for tryptophan in plant-pathogenic mycoplasma-like organisms (MLO) and the _Acholeplasmataceae_ ([Lim and Sears, 1992](https://www.ncbi.nlm.nih.gov/pubmed/1556079?dopt=Abstract)) and there seems to be only a single tRNA-CCA for tryptophan in _Acholeplasma laidlawii_ ([Tanaka et al. 1989](https://www.ncbi.nlm.nih.gov/pubmed/2762159?dopt=Abstract)). In contrast, in a study of codon usage in _Phytoplasmas_, it was found that 30 out of 78 ORFs analyzed translated better with code 4 (UGA for tryptophan) than with code 11 while the remainder showed no differences between the two codes ([Melamed et al. 2003](https://www.ncbi.nlm.nih.gov/pubmed/14594823?dopt=Abstract)). In addition, the coding reassignment of UGA Stop --> Trp can be found in an alpha-proteobacterial symbiont of cicadas: _Candidatus Hodgkinia cicadicola_ ([McCutcheon et al. 2009](https://www.ncbi.nlm.nih.gov/pubmed/19609354?dopt=Abstract)).

**Fungi**: _Emericella nidulans_, _Neurospora crassa_, _Podospora anserina_, _Acremonium_ ([Fox, 1987](https://www.ncbi.nlm.nih.gov/pubmed/3327473?dopt=Abstract)), _Candida parapsilosis_ ([Guelin et al., 1991](https://www.ncbi.nlm.nih.gov/pubmed/1826652?dopt=Abstract)), _Trichophyton rubrum_ ([de Bievre and Dujon, 1992](https://www.ncbi.nlm.nih.gov/pubmed/1326416?dopt=Abstract)), _Dekkera/Brettanomyces, Eeniella_ ([Hoeben et al., 1993](https://www.ncbi.nlm.nih.gov/pubmed/8387113?dopt=Abstract)), and probably _Ascobolus immersus_, _Aspergillus amstelodami_, _Claviceps purpurea_, and _Cochliobolus heterostrophus_.

**Other Eukaryotes**: _Gigartinales_ among the red algae ([Boyen et al. 1994](https://www.ncbi.nlm.nih.gov/pubmed/8190631?dopt=Abstract)), and the protozoa _Trypanosoma brucei_, _Leishmania tarentolae_, _Paramecium tetraurelia_, _Tetrahymena pyriformis_ and probably _Plasmodium gallinaceum_ ([Aldritt et al., 1989](https://www.ncbi.nlm.nih.gov/pubmed/2779560?dopt=Abstract)).

**Metazoa**: _Coelenterata_ (Ctenophora and Cnidaria)

#### Comments:

This code is also used for the kinetoplast DNA (maxicircles, minicircles). Kinetoplasts are modified mitochondria (or their parts).  
[Back to top](#top)

* * *

5\. The Invertebrate Mitochondrial Code (transl\_table=5)
---------------------------------------------------------

    AAs  = FFLLSSSSYY\*\*CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSSSSVVVVAAAADDEEGGGG
  Starts = ---M------\*\*--------------------MMMM---------------M------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG5)

#### Comment:

The codon AGG is absent in Drosophila.

#### Differences from the Standard Code:

        Code 5          Standard

 AGA    Ser  S          Arg  R
 AGG    Ser  S          Arg  R
 AUA    Met  M          Ile  I
 UGA    Trp  W          Ter  \*

#### Alternative Initiation Codons:

AUA, AUU

AUC: Apis ([Crozier and Crozier, 1993](https://www.ncbi.nlm.nih.gov/pubmed/8417993?dopt=Abstract))

GUG: Polyplacophora ([Boore and Brown, 1994](https://www.ncbi.nlm.nih.gov/pubmed/7828825?dopt=Abstract) GenBank Accession Number:

[U09810](http://www.ncbi.nlm.nih.gov/nuccore/557273?report=GenBank))

UUG: Ascaris, Caenorhabditis

#### Systematic Range:

**Nematoda**: Ascaris, Caenorhabditis;

**Mollusca**: Bivalvia ([Hoffmann et al., 1992](https://www.ncbi.nlm.nih.gov/pubmed/1386586?dopt=Abstract)); Polyplacophora ([Boore and Brown, 1994](https://www.ncbi.nlm.nih.gov/pubmed/7828825?dopt=Abstract))

**Arthropoda/Crustacea**: Artemia ([Batuecas et al., 1988](https://www.ncbi.nlm.nih.gov/pubmed/3135541?dopt=Abstract));

**Arthropoda/Insecta**: Drosophila \[Locusta migratoria (migratory locust), Apis mellifera (honeybee)\]

#### Comments:

Several arthropods translate the codon AGG as lysine instead of serine (as in the invertebrate mitochondrial genetic code) or arginine (as in the standard genetic code) ([Abascal et al., 2006](https://www.ncbi.nlm.nih.gov/pubmed/16620150?dopt=Abstract)).

GUG may possibly function as an initiator in Drosophila ([Clary and Wolstenholme, 1985](https://www.ncbi.nlm.nih.gov/pubmed/3001325?dopt=Abstract); [Gadaleta et al., 1988](https://www.ncbi.nlm.nih.gov/pubmed/3399396?dopt=Abstract)). AUU is not used as an initiator in Mytilus ([Hoffmann et al., 1992](https://www.ncbi.nlm.nih.gov/pubmed/1386586?dopt=Abstract)).

"An exceptional mechanism must operate for initiation of translation of the cytochrome oxidase subunit I mRNA in both D. melanogaster ([de Bruijn, 1983](https://www.ncbi.nlm.nih.gov/pubmed/6408489?dopt=Abstract)) and D. yakuba ([Clary and Wolstenholme 1983](https://www.ncbi.nlm.nih.gov/pubmed/6314262?dopt=Abstract)), since its only plausible initiation codon, AUA, is out of frame with the rest of the gene. Initiation appears to require the "reading" of of an AUAA quadruplet, which would be equivalent to initiation at AUA followed immediately by a specific ribosomal frameshift. Another possible mechanism ... is that the mRNA is "edited" to bring the AUA initiation into frame." ([Fox, 1987](https://www.ncbi.nlm.nih.gov/pubmed/3327473?dopt=Abstract))  
[Back to top](#top)

* * *

6\. The Ciliate, Dasycladacean and Hexamita Nuclear Code (transl\_table=6)
--------------------------------------------------------------------------

    AAs  = FFLLSSSSYYQQCC\*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = --------------\*--------------------M----------------------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG6)

#### Differences from the Standard Code:

          Code 6       Standard

 UAA      Gln  Q        Ter  \*
 UAG      Gln  Q        Ter  \*

#### Systematic Range:

**Ciliata**: Oxytricha and Stylonychia ([Hoffman et al. 1995](https://www.ncbi.nlm.nih.gov/pubmed/7753617?dopt=Abstract)), Paramecium, Tetrahymena, Oxytrichidae and probably Glaucoma chattoni.

**Dasycladaceae**: Acetabularia ([Schneider et al., 1989](https://www.ncbi.nlm.nih.gov/pubmed/2573818?dopt=Abstract)) and

**Batophora** ([Schneider and de Groot, 1991](https://www.ncbi.nlm.nih.gov/pubmed/1934113?dopt=Abstract)).

**Diplomonadida**:

Scope: Hexamita inflata, Diplomonadida ATCC50330, and ATCC50380.

Ref.: [Keeling, P.J. and Doolittle, W.F. 1996.](https://www.ncbi.nlm.nih.gov/pubmed/8641293?dopt=Abstract). A non-canonical genetic code in an early diverging eukaryotic lineage. The EMBO Journal 15, 2285-2290.

#### Comment:

The ciliate macronuclear code has not been determined completely. The codon UAA is known to code for Gln only in the Oxytrichidae.  
[Back to top](#top)

* * *

9\. The Echinoderm and Flatworm Mitochondrial Code (transl\_table=9)
--------------------------------------------------------------------

    AAs  = FFLLSSSSYY\*\*CCWWLLLLPPPPHHQQRRRRIIIMTTTTNNNKSSSSVVVVAAAADDEEGGGG
  Starts = ----------\*\*-----------------------M---------------M------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG9)

#### Differences from the Standard Code:

          Code 9        Standard

 AAA      Asn  N        Lys K
 AGA      Ser  S        Arg R
 AGG      Ser  S        Arg R
 UGA      Trp  W        Ter \*

#### Systematic Range:

**Asterozoa** (starfishes) ([Himeno et al., 1987](https://www.ncbi.nlm.nih.gov/pubmed/3678836?dopt=Abstract))

**Echinozoa** (sea urchins) ([Jacobs et al., 1988](https://www.ncbi.nlm.nih.gov/pubmed/3172215?dopt=Abstract); [Cantatore et al., 1989](https://www.ncbi.nlm.nih.gov/pubmed/2544576?dopt=Abstract))

**Rhabditophora** among the Platyhelminthes ([Telford et al. 2000](https://www.ncbi.nlm.nih.gov/pubmed/11027335?dopt=Abstract))  
[Back to top](#top)

* * *

10\. The Euplotid Nuclear Code (transl\_table=10)
-------------------------------------------------

    AAs  = FFLLSSSSYY\*\*CCCWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = ----------\*\*-----------------------M----------------------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG10)

#### Differences from the Standard Code:

          Code 10     Standard

 UGA      Cys  C        Ter  \*

#### Systematic Range:

**Ciliata**: Euplotidae ([Hoffman et al. 1995](https://www.ncbi.nlm.nih.gov/pubmed/7753617?dopt=Abstract)).  
[Back to top](#top)

* * *

11\. The Bacterial, Archaeal and Plant Plastid Code (transl\_table=11)
----------------------------------------------------------------------

    AAs  = FFLLSSSSYY\*\*CC\*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = ---M------\*\*--\*----M------------MMMM---------------M------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG11)

#### Systematic Range and Comments:

Table 11 is used for Bacteria, Archaea, prokaryotic viruses and chloroplast proteins. As in the standard code, initiation is most efficient at AUG. In addition, GUG and UUG starts are documented in Archaea and Bacteria ([Kozak 1983](https://www.ncbi.nlm.nih.gov/pubmed/6343825?dopt=Abstract), [Fotheringham et al. 1986](https://www.ncbi.nlm.nih.gov/pubmed/3521591?dopt=Abstract), [Golderer et al. 1995](https://www.ncbi.nlm.nih.gov/pubmed/7592355?dopt=Abstract), [Nolling et al. 1995](https://www.ncbi.nlm.nih.gov/pubmed/7730278?dopt=Abstract), [Sazuka & Ohara 1996](https://www.ncbi.nlm.nih.gov/pubmed/8946162?dopt=Abstract), [Genser et al. 1998](https://www.ncbi.nlm.nih.gov/pubmed/9821671?dopt=Abstract), [Wang et al. 2003](https://www.ncbi.nlm.nih.gov/pubmed/14633098?dopt=Abstract)). In E. coli, UUG is estimated to serve as initiator for about 3% of the bacterium's proteins ([Blattner et al. 1997](https://www.ncbi.nlm.nih.gov/pubmed/9278503?dopt=Abstract)). CUG is known to function as an initiator for one plasmid-encoded protein (RepA) in Escherichia coli ([Spiers and Bergquist, 1992](https://www.ncbi.nlm.nih.gov/pubmed/1447126?dopt=Abstract)). In addition to the NUG initiations, in rare cases Bacteria can initiate translation from an AUU codon as e.g. in the case of poly(A) polymerase PcnB and the InfC gene that codes for translation initiation factor IF3 ([Polard et al. 1991](https://www.ncbi.nlm.nih.gov/pubmed/1660923?dopt=Abstract), [Liveris et al. 1993](https://www.ncbi.nlm.nih.gov/pubmed/8405963?dopt=Abstract), [Sazuka & Ohara 1996](https://www.ncbi.nlm.nih.gov/pubmed/8946162?dopt=Abstract), [Binns & Masters 2002](https://www.ncbi.nlm.nih.gov/pubmed/12068810?dopt=Abstract)). The internal assignments are the same as in the standard code though UGA codes at low efficiency for Trp in Bacillus subtilis and, presumably, in Escherichia coli ([Hatfiled and Diamond, 1993](https://www.ncbi.nlm.nih.gov/pubmed/8488562?dopt=Abstract)).  
[Back to top](#top)

* * *

12\. The Alternative Yeast Nuclear Code (transl\_table=12)
----------------------------------------------------------

    AAs  = FFLLSSSSYY\*\*CC\*WLLLSPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = ----------\*\*--\*----M---------------M----------------------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG12)

#### Differences from the Standard Code:

           Code 12      Standard

 CUG       Ser          Leu
       

#### Alternative Initiation Codons:

CAG may be used in Candida albicans ([Santos et al., 1993](https://www.ncbi.nlm.nih.gov/pubmed/8440250?dopt=Abstract)).

#### Systematic Range and Comments:

In code 12 the CUG codon has been reassigned from Leu to Ser ([Santos et al., 2011](https://www.ncbi.nlm.nih.gov/pubmed/21819941?dopt=Abstract), [Mateus et al., 2013](https://www.ncbi.nlm.nih.gov/pubmed/23619021?dopt=Abstract), [Krassowski et al., 2018](https://www.ncbi.nlm.nih.gov/pubmed/29760453?dopt=Abstract)). This code is used by the fungal CUG-Ser1 and CUG-Ser2 clades that represent separate monophyletic lineages of the Saccharomycotina ([Li et al., 2021](https://www.ncbi.nlm.nih.gov/pubmed/33607033?dopt=Abstract)). In the NCBI taxonomy, CUG-Ser1 currently comprises the three families Cephaloascaceae, Debaryomycetaceae and Metschnikowiaceae and the genus Babjeviella. The CUG-Ser1 clade includes important human pathogens like Candida albicans and the multidrug-resistant Candida auris. The CUG-Ser2 clade represents a parallel reassignment of CUG and includes species in the families Ascoideaceae and Saccharomycopsidaceae. Most other true yeasts (Saccharomycotina) use the standard code however.  
[Back to top](#top)

* * *

13\. The Ascidian Mitochondrial Code (transl\_table=13)
-------------------------------------------------------

    AAs  = FFLLSSSSYY\*\*CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSSGGVVVVAAAADDEEGGGG
  Starts = ---M------\*\*----------------------MM---------------M------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG13)

#### Differences from the Standard Code:

          Code 13     Standard

 AGA      Gly  G        Arg  R
 AGG      Gly  G        Arg  R
 AUA      Met  M        Ile  I
 UGA      Trp  W        Ter  \*

#### Systematic range and Comments:

There is evidence from a phylogenetically diverse sample of tunicates (Urochordata) that AGA and AGG code for glycine. In other organisms, AGA/AGG code for either arginine or serine and in vertebrate mitochondria they code a STOP. Evidence for glycine translation of AGA/AGG has been found in Pyura stolonifera ([Durrheim et al. 1993](https://www.ncbi.nlm.nih.gov/pubmed/8393993?dopt=Abstract)), Halocynthia roretzi ([Kondow et al. 1999](https://www.ncbi.nlm.nih.gov/pubmed/10352185?dopt=Abstract),[Yokobori et al., 1993](https://www.ncbi.nlm.nih.gov/pubmed/8381878?dopt=Abstract), [Yokobori et al. 1999](https://www.ncbi.nlm.nih.gov/pubmed/10581290?dopt=Abstract)) and Ciona savignyi ([Yokobori et al. 2003](https://www.ncbi.nlm.nih.gov/pubmed/14738316?dopt=Abstract)).

In addition, the Halocynthia roretzi mitochondrial genome encodes an additional tRNA gene with the anticodon U\*CU that is thought to enable the use of AGA or AGG codons for glycine and the gene has been shown to be transcribed in vivo ([Kondow et al. 1999](https://www.ncbi.nlm.nih.gov/pubmed/10352185?dopt=Abstract), [Yokobori et al. 1999](https://www.ncbi.nlm.nih.gov/pubmed/10581290?dopt=Abstract)).

#### Alternative initiation codons:

ATA, GTG and TTG ([Yokobori et al. 1999](https://www.ncbi.nlm.nih.gov/pubmed/10581290?dopt=Abstract)). ATT is the start codon for the CytB gene in _Halocynthia roretzi_ ([Gissi and Pesole, 2003](http://www.pubmedcentral.nih.gov/articlerender.fcgi?tool=pubmed&pubmedid=12915488)).  
[Back to top](#top)

* * *

14\. The Alternative Flatworm Mitochondrial Code (transl\_table=14)
-------------------------------------------------------------------

    AAs  = FFLLSSSSYYY\*CCWWLLLLPPPPHHQQRRRRIIIMTTTTNNNKSSSSVVVVAAAADDEEGGGG
  Starts = -----------\*-----------------------M----------------------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG14)

#### Differences from the Standard Code:

          Code 14      Standard

 AAA      Asn  N       Lys  K
 AGA      Ser  S       Arg  R
 AGG      Ser  S       Arg  R
 UAA      Tyr  Y       Ter  \*
 UGA      Trp  W       Ter  \*

#### Systematic Range:

**Platyhelminthes (flatworms) and Nematoda (roundworms)**

#### Comments:

Code 14 differs from code 9 only by translating UAA to Tyr rather than STOP. A recent study ([Telford et al. 2000](https://www.ncbi.nlm.nih.gov/pubmed/11027335?dopt=Abstract)) has found no evidence that the codon UAA codes for Tyr in the flatworms but other opinions exist. There are very few GenBank records that are translated with code 14 but a test translation shows that retranslating these records with code 9 can cause premature terminations. More recently, UAA has been found to code for tyrosine in the nematodes Radopholus similis and Radopholus arabocoffeae ([Jacob et al. 2009](https://www.ncbi.nlm.nih.gov/pubmed/19778425?dopt=Abstract)).  
[Back to top](#top)

* * *

16\. Chlorophycean Mitochondrial Code (transl\_table=16)
--------------------------------------------------------

    AAs  = FFLLSSSSYY\*LCC\*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = ----------\*---\*--------------------M----------------------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG16)

#### Differences from the Standard Code:

          Code 16       Standard

TAG       Leu  L        STOP

#### Systematic Range:

**Chlorophyceae** ([Hayashi-Ishimaru et al. 1996](https://www.ncbi.nlm.nih.gov/pubmed/8662206?dopt=Abstract). UAG is a sense codon in several chlorophycean mitochondria) and the chytridiomycete fungus **Spizellomyces punctatus** ([Laforest et al. 1997](https://www.ncbi.nlm.nih.gov/pubmed/9016605?dopt=Abstract). Mitochondrial tRNAs in the lower fungus Spizellomyces punctatus: tRNA editing and UAG 'stop' codons recognized as leucine).  
[Back to top](#top)

* * *

21\. Trematode Mitochondrial Code (transl\_table=21)
----------------------------------------------------

    AAs  = FFLLSSSSYY\*\*CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNNKSSSSVVVVAAAADDEEGGGG
  Starts = ----------\*\*-----------------------M---------------M------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG21)

#### Differences from the Standard Code:

          Code 21       Standard

TGA       Trp  W        STOP
ATA       Met  M        Ile
AGA       Ser  S        Arg
AGG       Ser  S        Arg
AAA       Asn  N        Lys 

#### Systematic Range:

**Trematoda**: [Ohama, T, S. Osawa, K. Watanabe, T.H. Jukes, 1990. J. Molec Evol. 30](https://www.ncbi.nlm.nih.gov/pubmed/2111847?dopt=Abstract)

[Garey, J.R. and D.R. Wolstenholme, 1989. J. Molec. Evol. 28: 374-387 329-332.](https://www.ncbi.nlm.nih.gov/pubmed/2545889?dopt=Abstract)  
[Back to top](#top)

* * *

22\. Scenedesmus obliquus Mitochondrial Code (transl\_table=22)
---------------------------------------------------------------

    AAs  = FFLLSS\*SYY\*LCC\*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = ------\*---\*---\*--------------------M----------------------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG22)

#### Differences from the Standard Code:

          Code 22       Standard

TCA       STOP \*        Ser
TAG       Leu  L        STOP

#### Systematic Range:

**Scenedesmus obliquus**: [Nedelcu A, Lee RW, Lemieux C, Gray MW and Burger G. "The complete mitochondrial DNA sequence of Scenedesmus obliquus reflects an intermediate stage in the evolution of the green algal mitochondrial genome."](https://www.ncbi.nlm.nih.gov/pubmed/10854413?dopt=Abstract) Genome Res. 2000 Jun;10(6):819-31.  
[Back to top](#top)

* * *

23\. Thraustochytrium Mitochondrial Code (transl\_table=23)
-----------------------------------------------------------

    AAs  = FF\*LSSSSYY\*\*CC\*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = --\*-------\*\*--\*-----------------M--M---------------M------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG23)

This code has been created for the mitochondrial genome of the labyrinthulid Thraustochytrium aureum sequenced by The Organelle Genome Megasequencing Program ([OGMP](http://megasun.bch.umontreal.ca/ogmpproj.html)).

It is the similar to the bacterial code ([transl\_table 11](#11)) but it contains an additional stop codon (TTA) and also has a different set of start codons.  
[Back to top](#top)

* * *

24\. Rhabdopleuridae Mitochondrial Code (transl\_table=24)
----------------------------------------------------------

    AAs  = FFLLSSSSYY\*\*CCWWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSSKVVVVAAAADDEEGGGG
  Starts = ---M------\*\*-------M---------------M---------------M------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG24)

#### Differences from the Standard Code:

          Code 24        Standard

AGA       Ser S          Arg  R
AGG       Lys K          Arg  R
UGA       Trp W          STOP \*

Code 24 has been created for the mitochondrial genome of Rhabdopleura compacta (Pterobranchia). The Pterobranchia are one of the two groups in the Hemichordata which together with the Echinodermata and Chordata form the three major lineages of deuterostomes. AUA translates to isoleucine in Rhabdopleura as it does in the Echinodermata and Enteropneusta while AUA encodes methionine in the Chordata. The assignment of AGG to Lys is not found elsewhere in deuterostome mitochondria but it occurs in some taxa of Arthropoda ([Perseke et al. 2011](https://www.ncbi.nlm.nih.gov/pubmed/21599892?dopt=Abstract)). Code 24 shares with many other mitochondrial codes the reassignment of the UGA STOP to Trp, and AGG and AGA to an amino acid other than Arg. The initiation codons in Rhabdopleura compacta are ATG and GTG ([Perseke et al. 2011](https://www.ncbi.nlm.nih.gov/pubmed/21599892?dopt=Abstract)).  
[Back to top](#top)

* * *

25\. Candidate Division SR1 and Gracilibacteria Code (transl\_table=25)
-----------------------------------------------------------------------

    AAs  = FFLLSSSSYY\*\*CCGWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = ---M------\*\*-----------------------M---------------M------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG25)

#### Differences from the Standard Code:

          Code 25        Standard

UGA       Gly            STOP

#### Initiation Codons:

AUG, GUG, UUG

#### Systematic Range:

**Candidate Division SR1**, **Gracilibacteria**

#### Comments:

Code 25 is used in two groups of (so far) uncultivated Bacteria found in marine and fresh-water environment and in the intestines and oral cavities of mammals among others. The difference to the standard and the bacterial code is that UGA represents an additional glycine codon and does not code for termination ([Campbell et al. 2013](https://www.ncbi.nlm.nih.gov/pubmed/23509275?dopt=Abstract)).  
[Back to top](#top)

* * *

26\. Pachysolen tannophilus Nuclear Code (transl\_table=26)
-----------------------------------------------------------

    AAs  = FFLLSSSSYY\*\*CC\*WLLLAPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = ----------\*\*--\*----M---------------M----------------------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG26)

#### Differences from the Standard Code:

          Code 26        Standard

CUG       Ala            Leu

#### Initiation Codons:

AUG, GUG, UUG

#### Systematic Range:

**species in the genera Nakazawaea, Pachysolen and Peterozyma**

#### Comments:

Code 26 differs from the standard code only the translation of CUG as alanine (as opposed to leucine) ([Muhlhausen et al. 2016](https://www.ncbi.nlm.nih.gov/pubmed/27197221?dopt=Abstract)). It is also similar to code 12 that translates CUG as serine. Code 26 is used by the CUG-Ala clade that include a small number of yeast genera: Nakazawaea, Pachysolen and Peterozyma ([Krassowski et al. 2018](https://www.ncbi.nlm.nih.gov/pubmed/29760453?dopt=Abstract)).  
[Back to top](#top)

* * *

27\. Karyorelict Nuclear Code (transl\_table=27)
------------------------------------------------

    AAs  = FFLLSSSSYYQQCCWWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = --------------\*--------------------M----------------------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG27)

#### Differences from the Standard Code:

          Code 27        Standard

UAG       Gln            STOP
UAA       Gln            STOP
UGA       STOP or Trp    STOP

#### Initiation Codons:

AUG

#### Systematic Range:

**the karyorelictid ciliate Parduczia**

#### Comments:

Code 27 reassigns the UAG and UAA stops to glutamine while UGA can function as either STOP or tryptophan. Code 27 is used for the karyorelictid ciliate Parduczia sp. ([Swart et al. 2016](https://www.ncbi.nlm.nih.gov/pubmed/27426948?dopt=Abstract)).  
[Back to top](#top)

* * *

28\. Condylostoma Nuclear Code (transl\_table=28)
-------------------------------------------------

    AAs  = FFLLSSSSYYQQCCWWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = ----------\*\*--\*--------------------M----------------------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG28)

#### Differences from the Standard Code:

          Code 28          Standard

UAA       Gln or STOP      STOP
UAG       Gln or STOP      STOP
UGA       Trp or STOP      STOP

#### Initiation Codons: AUG

#### Systematic Range:

**Condylostoma magnum**

#### Comments:

Code 28 is used in Condylostoma magnum. The difference to the standard code is that the three stop codons can also be translated as glutamine (UAA, UAG) or tryptophan (UGA), respectively([Swart et al. 2016](https://www.ncbi.nlm.nih.gov/pubmed/%2027426948?dopt=Abstract)[, Heaphy et al. 2016](https://www.ncbi.nlm.nih.gov/pubmed/%2027501944?dopt=Abstract)).  
[Back to top](#top)

* * *

29\. Mesodinium Nuclear Code (transl\_table=29)
-----------------------------------------------

    AAs  = FFLLSSSSYYYYCC\*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = --------------\*--------------------M----------------------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG29)

#### Differences from the Standard Code:

          Code 29        Standard

UAA       Tyr            STOP
UAG       Tyr            STOP

#### Initiation Codons:

AUG

#### Systematic Range:

**the mesodiniid ciliates Mesodinium and Myrionecta**

#### Comments:

Code 29 is used for the haptorid ciliates Mesodinium and Myrionecta. It differs from the standard code in reassigning the stop codons UAA and UAG to Tyrosine. ([Heaphy et al. 2016](https://www.ncbi.nlm.nih.gov/pubmed/27501944?dopt=Abstract)).  
[Back to top](#top)

* * *

30\. Peritrich Nuclear Code (transl\_table=30)
----------------------------------------------

    AAs  = FFLLSSSSYYEECC\*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = --------------\*--------------------M----------------------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG30)

#### Differences from the Standard Code:

          Code 30        Standard

UAA       Glu            STOP
UAG       Glu            STOP

#### Initiation Codons:

AUG

#### Systematic Range:

**the peritrich ciliate Carchesium**

#### Comments:

Code 30 is used in the peritrich ciliate Carchesium. The stop codons UAA and UAG are reassigned to Glutamine. ([Sanchez-Silva et al. 2003](https://www.ncbi.nlm.nih.gov/pubmed/12620196?dopt=Abstract)).  
[Back to top](#top)

* * *

31\. Blastocrithidia Nuclear Code (transl\_table=31)
----------------------------------------------------

    AAs  = FFLLSSSSYYEECCWWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = ----------\*\*-----------------------M----------------------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG31)

#### Differences from the Standard Code:

          Code 31          Standard

UGA       Trp              STOP
UAG       Glu or STOP      STOP
UAA       Glu or STOP      STOP

#### Initiation Codons:

AUG

#### Systematic Range:

**Blastocrithidia sp.**

#### Comments:

Code 31 is used for the trypanosome Blastocrithidia sp. UGA encodes trytophan and UAG and UAA encode glutamate and also serve as termination codons. ([Zahonova et al. 2016](https://www.ncbi.nlm.nih.gov/pubmed/27593378?dopt=Abstract)).  
[Back to top](#top)

* * *

33\. Cephalodiscidae Mitochondrial UAA-Tyr Code (transl\_table=33)
------------------------------------------------------------------

    AAs  = FFLLSSSSYYY\*CCWWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSSKVVVVAAAADDEEGGGG
  Starts = ---M-------\*-------M---------------M---------------M------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG

[Click here to change format](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG33)

#### Differences from the Standard Code:

     Code 33     Standard
UAA  Tyr         STOP
UGA  Trp         STOP
AGA  Ser         Arg
AGG  Lys         Arg

#### Systematic Range:

Cephalodiscidae (Hemichordata)

#### Comments:

Code 33 is very similar to the mitochondrial code 24 for the _Pterobranchia_, which also belong to the _Hemichordata_, except that it uses UAA for tyrosine rather than as a stop codon ([Li Y, Kocot KM, Tassia MG, Cannon JT, Bernt M, Halanych KM. Mitogenomics Reveals a Novel Genetic Code in Hemichordata. Genome Biol Evol. 2019 Jan 1;11(1):29-40.](https://www.ncbi.nlm.nih.gov/pubmed/30476024?dopt=Abstract))

  
[Back to top](#top)