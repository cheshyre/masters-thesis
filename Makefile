PROPOSAL_DOCS = \
								proposal/doc/00_abschlussarbeit_erklaerung.tex \
								proposal/doc/00_abstract.tex \
								proposal/doc/00_acknowledgements.tex \
								proposal/doc/01_introduction.tex \
								proposal/doc/02_nuclear_hamiltonian.tex \
								proposal/doc/03_wavefunction_expansion_methods.tex \
								proposal/doc/04_imsrg_for_nuclear_structure.tex \
								proposal/doc/05_results.tex \
								proposal/doc/06_outlook.tex
PROPOSAL_PLOTS = \
								 proposal/doc/images/he4_imsrg2_energies.pdf \
								 proposal/doc/images/he4_imsrg2_flow.pdf \
								 proposal/doc/images/pairing_ham_imsrg3.pdf \
								 proposal/doc/images/vnn_srg_emn500_n3lo.pdf

PROPOSAL_TALK_PLOTS = \
											proposal/talk/images/he4_imsrg2_energies.pdf \
											proposal/talk/images/he4_imsrg2_flow.pdf \
											proposal/talk/images/pairing_ham_imsrg3.pdf \
											proposal/talk/images/pairing_ham_imsrg3_relative.pdf \
											proposal/talk/images/vnn_srg_emn500_n3lo.pdf

all: proposal/doc/doc.pdf proposal/talk/talk.pdf

clean:
	rm -r latex.out/
	rm -r proposal/doc/*.pdf
	rm -r proposal/doc/images/*.pdf
	rm -r proposal/talk/*.pdf
	rm -r proposal/talk/images/*.pdf

# --------------------- Main document rules --------------------------------

proposal/doc/doc.pdf: proposal/doc/doc.tex macros.tex sources.bib $(PROPOSAL_DOCS) $(PROPOSAL_PLOTS)
	./latexrun proposal/doc/doc.tex -o proposal/doc/doc.pdf

proposal/talk/talk.pdf: proposal/talk/talk.tex macros.tex proposal/talk/talk_macros.tex $(PROPOSAL_TALK_PLOTS)
	./latexrun proposal/talk/talk.tex -o proposal/talk/talk.pdf

# --------------------- Proposal plots -------------------------------------

proposal/doc/images/he4_imsrg2_energies.pdf: proposal/doc/images/he4_imsrg2_energies.py proposal/doc/images/data/kai_results.json
	python3 proposal/doc/images/he4_imsrg2_energies.py

proposal/doc/images/he4_imsrg2_flow.pdf: proposal/doc/images/he4_imsrg2_flow.py proposal/doc/images/data/evolve_data.json
	python3 proposal/doc/images/he4_imsrg2_flow.py

proposal/doc/images/pairing_ham_imsrg3.pdf: proposal/doc/images/pairing_ham_imsrg3.py proposal/doc/images/data/pairing_ham_data.json
	python3 proposal/doc/images/pairing_ham_imsrg3.py

proposal/doc/images/vnn_srg_emn500_n3lo.pdf: proposal/doc/images/vnn_srg_emn500_n3lo.py proposal/doc/images/data/EM500new_data.json
	python3 proposal/doc/images/vnn_srg_emn500_n3lo.py

# --------------------- Proposal talk plots ----------------------------------
#
proposal/talk/images/he4_imsrg2_energies.pdf: proposal/talk/images/he4_imsrg2_energies.py proposal/talk/images/data/kai_results.json
	python3 proposal/talk/images/he4_imsrg2_energies.py

proposal/talk/images/he4_imsrg2_flow.pdf: proposal/talk/images/he4_imsrg2_flow.py proposal/talk/images/data/evolve_data.json
	python3 proposal/talk/images/he4_imsrg2_flow.py

proposal/talk/images/pairing_ham_imsrg3.pdf: proposal/talk/images/pairing_ham_imsrg3.py proposal/talk/images/data/pairing_ham_data.json
	python3 proposal/talk/images/pairing_ham_imsrg3.py

proposal/talk/images/pairing_ham_imsrg3_relative.pdf: proposal/talk/images/pairing_ham_imsrg3_relative.py proposal/talk/images/data/pairing_ham_data.json
	python3 proposal/talk/images/pairing_ham_imsrg3_relative.py

proposal/talk/images/vnn_srg_emn500_n3lo.pdf: proposal/talk/images/vnn_srg_emn500_n3lo.py proposal/talk/images/data/EM500new_data.json
	python3 proposal/talk/images/vnn_srg_emn500_n3lo.py
