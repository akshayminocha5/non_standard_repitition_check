##########Author Akshay Minocha ( ksnmi | minocha )#####################
##########mailto: akshayminocha5@gmail.com##############################


Our main aim is to standardise the words with repititive characters
The script works for english now since the list of english words as a python dictionary object is available in the folder by the name of english_dic
The wordlist can be changed according to any language as necessary

sample is given as below -> 

> > Input program 1:
> >
> > Nossssaaa
> > !!
> > Ta
> > muito
> > chique
> > hein
> > !!!!!
> >
> > Output program 1 / input program 2:
> >
> > ^Nossssaaa/nossaa/nossa/nosa/nosaa$
> > ^!!/!!$
> > ^Ta/está/tá/ta$
> > ^muito/muito$
> > ^chique/chique$
> > ^hein/hein$
> > ^!!!!!/!!!!!$
> >
> > Output program 2:
> >
> > ^Nossssaaa/nossa$
> > ^!!/!!$
> > ^Ta/ta$
> > ^muito/muito$
> > ^chique/chique$
> > ^hein/hein$
> > ^!!!!!/!!!!!$

Here the sample file where the sentence in tokenized (one token each line) format is in the "sample" file

The bash script run.sh will use the input in "sample" and generate the output on the terminal
