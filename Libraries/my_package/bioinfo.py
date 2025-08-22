def gc_content(seq):
    g= seq.count("G")
    c = seq.count("C")
    return (g+c)/len(seq)*100