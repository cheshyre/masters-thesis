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

THESIS_DOCS = \
								thesis/doc/00_titlepage.tex \
								thesis/doc/00_meta_information.tex \
								thesis/doc/00_abschlussarbeit_erklaerung.tex \
								thesis/doc/00_abstract.tex \
								thesis/doc/00_acknowledgements.tex \
								thesis/doc/01_introduction.tex \
								thesis/doc/02_nuclear_hamiltonian.tex \
								thesis/doc/03_wavefunction_expansion_methods.tex \
								thesis/doc/04_imsrg_for_nuclear_structure.tex \
								thesis/doc/05_angular_momentum_coupling.tex \
								thesis/doc/06_jscheme_results.tex \
								thesis/doc/07_conclusions.tex \
								thesis/doc/a01_mscheme_fundamental_commutators.tex \
								thesis/doc/a02_jscheme_simplification_strategies.tex \
								thesis/doc/a03_pairing_hamiltonian_imsrg3.tex

THESIS_PLOTS = \
								thesis/doc/images/he4_imsrg2_energies.pdf \
								thesis/doc/images/he4_imsrg2_flow.pdf \
								thesis/doc/images/pairing_ham_imsrg3.pdf \
								thesis/doc/images/vnn_srg_emn500_n3lo.pdf \
								thesis/doc/images/he4_imsrg2_results.pdf \
								thesis/doc/images/he4_NAT_results.pdf \
								thesis/doc/images/he4_HF_results.pdf \
								thesis/doc/images/term_by_term_o16_plot.pdf

all: proposal_doc.pdf proposal_talk.pdf thesis_doc.pdf

clean:
	rm -rf latex.out/
	rm -rf proposal/doc/*.pdf
	rm -rf proposal/doc/images/*.pdf
	rm -rf proposal/talk/*.pdf
	rm -rf proposal/talk/images/*.pdf
	rm -rf thesis/doc/*.pdf
	rm -rf thesis/doc/images/*.pdf
	rm -rf *.pdf

# --------------------- Main document rules --------------------------------

proposal_doc.pdf: proposal_doc.tex macros.tex sources.bib $(PROPOSAL_DOCS) $(PROPOSAL_PLOTS)
	rm -rf latex.out/
	poetry run python3 latexrun proposal_doc.tex -o proposal_doc.pdf

proposal_talk.pdf: proposal_talk.tex macros.tex proposal/talk/talk_macros.tex $(PROPOSAL_TALK_PLOTS)
	rm -rf latex.out/
	poetry run python3 latexrun proposal_talk.tex -o proposal_talk.pdf

thesis_doc.pdf: thesis_doc.tex macros.tex sources.bib $(THESIS_DOCS) $(THESIS_PLOTS) apsrev4-1-mh-mod.bst
	rm -rf latex.out/
	poetry run python3 latexrun thesis_doc.tex -o thesis_doc.pdf

# --------------------- Thesis plots -------------------------------------

thesis/doc/images/he4_imsrg2_energies.pdf: thesis/doc/images/he4_imsrg2_energies.py thesis/doc/images/data/kai_results.json
	poetry run python3 thesis/doc/images/he4_imsrg2_energies.py

thesis/doc/images/he4_imsrg2_flow.pdf: thesis/doc/images/he4_imsrg2_flow.py thesis/doc/images/data/evolve_data.json
	poetry run python3 thesis/doc/images/he4_imsrg2_flow.py

thesis/doc/images/pairing_ham_imsrg3.pdf: thesis/doc/images/pairing_ham_imsrg3.py thesis/doc/images/data/pairing_ham_data.json
	poetry run python3 thesis/doc/images/pairing_ham_imsrg3.py

thesis/doc/images/vnn_srg_emn500_n3lo.pdf: thesis/doc/images/vnn_srg_emn500_n3lo.py thesis/doc/images/data/EM500new_data.json
	poetry run python3 thesis/doc/images/vnn_srg_emn500_n3lo.py

thesis/doc/images/he4_NAT_results.pdf: thesis/doc/images/he4_NAT_results.py thesis/doc/images/data/he4/imsrg2/data.json thesis/doc/images/data/he4/imsrg3/data.json
	poetry run python3 thesis/doc/images/he4_NAT_results.py

thesis/doc/images/he4_HF_results.pdf: thesis/doc/images/he4_HF_results.py thesis/doc/images/data/he4/imsrg2/data.json thesis/doc/images/data/he4/imsrg3/data.json
	poetry run python3 thesis/doc/images/he4_HF_results.py

thesis/doc/images/he4_imsrg2_results.pdf: thesis/doc/images/he4_imsrg2_results.py thesis/doc/images/data/he4/imsrg2/data.json
	poetry run python3 thesis/doc/images/he4_imsrg2_results.py

thesis/doc/images/term_by_term_o16_plot.pdf: thesis/doc/images/term_by_term_o16_plot.py thesis/doc/images/data/o16/costs.json
	poetry run python3 thesis/doc/images/term_by_term_o16_plot.py

# --------------------- Proposal plots -------------------------------------

proposal/doc/images/he4_imsrg2_energies.pdf: proposal/doc/images/he4_imsrg2_energies.py proposal/doc/images/data/kai_results.json
	poetry run python3 proposal/doc/images/he4_imsrg2_energies.py

proposal/doc/images/he4_imsrg2_flow.pdf: proposal/doc/images/he4_imsrg2_flow.py proposal/doc/images/data/evolve_data.json
	poetry run python3 proposal/doc/images/he4_imsrg2_flow.py

proposal/doc/images/pairing_ham_imsrg3.pdf: proposal/doc/images/pairing_ham_imsrg3.py proposal/doc/images/data/pairing_ham_data.json
	poetry run python3 proposal/doc/images/pairing_ham_imsrg3.py

proposal/doc/images/vnn_srg_emn500_n3lo.pdf: proposal/doc/images/vnn_srg_emn500_n3lo.py proposal/doc/images/data/EM500new_data.json
	poetry run python3 proposal/doc/images/vnn_srg_emn500_n3lo.py

# --------------------- Proposal talk plots ----------------------------------

proposal/talk/images/he4_imsrg2_energies.pdf: proposal/talk/images/he4_imsrg2_energies.py proposal/talk/images/data/kai_results.json
	poetry run python3 proposal/talk/images/he4_imsrg2_energies.py

proposal/talk/images/he4_imsrg2_flow.pdf: proposal/talk/images/he4_imsrg2_flow.py proposal/talk/images/data/evolve_data.json
	poetry run python3 proposal/talk/images/he4_imsrg2_flow.py

proposal/talk/images/pairing_ham_imsrg3.pdf: proposal/talk/images/pairing_ham_imsrg3.py proposal/talk/images/data/pairing_ham_data.json
	poetry run python3 proposal/talk/images/pairing_ham_imsrg3.py

proposal/talk/images/pairing_ham_imsrg3_relative.pdf: proposal/talk/images/pairing_ham_imsrg3_relative.py proposal/talk/images/data/pairing_ham_data.json
	poetry run python3 proposal/talk/images/pairing_ham_imsrg3_relative.py

proposal/talk/images/vnn_srg_emn500_n3lo.pdf: proposal/talk/images/vnn_srg_emn500_n3lo.py proposal/talk/images/data/EM500new_data.json
	poetry run python3 proposal/talk/images/vnn_srg_emn500_n3lo.py
