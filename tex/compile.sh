
for p in page*.tex 
do
	cat template_top.tex $p template_bottom.tex > badges_$p
	pdflatex badges_$p
done
