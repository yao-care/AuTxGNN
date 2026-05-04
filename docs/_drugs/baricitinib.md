---
layout: default
title: Baricitinib
parent: 僅模型預測 (L5)
nav_order: 76
evidence_level: L5
indication_count: 10
---

# Baricitinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Baricitinib: From Rheumatoid Arthritis to Myeloid Leukemia

## One-Sentence Summary

Baricitinib (Olumiant) is an oral selective JAK1/JAK2 inhibitor approved in multiple countries for rheumatoid arthritis, atopic dermatitis, and alopecia areata, blocking pro-inflammatory cytokine signalling via the JAK-STAT pathway. The TxGNN model has generated **10 predicted new indications** across this Evidence Pack; the most evidence-supported direction is **myeloid leukemia**, backed by **1 active Phase 2/3 clinical trial** and **4 publications**, though the majority of top-ranked predictions are rare structural congenital disorders likely representing knowledge graph artefacts rather than genuine biological opportunities. Overall evidence across all indications remains at **Level L4 or below**, and no predictions are currently ready for clinical advancement.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid arthritis (globally approved; ⚠️ Australian ARTG data unavailable — see market information section) |
| Top-Ranked Predicted Indication (TxGNN Score) | Colobomatous microphthalmia-rhizomelic dysplasia syndrome (99.94% — likely KG artefact) |
| Best-Evidenced Predicted Indication | Myeloid leukemia (1 Phase 2/3 trial + 4 publications) |
| TxGNN Score (Rank 1) | 99.94% |
| Best Evidence Level | L4 |
| Australia Market Status | ⚠️ System query returned no ARTG entries — probable data collection error; manual ARTG verification strongly recommended |
| Number of ARTG Entries | 0 (data gap suspected — Olumiant is expected to hold TGA registration) |
| Recommended Decision | Hold |

---

## All Predicted Indications at a Glance

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Mechanistic Plausibility |
|------|---------|-------------|----------------|----------------|--------------------------|
| 1 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.94% | L5 | Hold | Very low — structural congenital defect; likely KG artefact |
| 2 | Brachydactyly-syndactyly syndrome | 99.94% | L5 | Hold | Very low — skeletal developmental anomaly |
| 3 | Indolent plasma cell myeloma | 93.31% | L5 | Hold | Moderate (theoretical) — IL-6/JAK/STAT3 axis relevant; no evidence |
| 4 | WHIM syndrome | 93.12% | L5 | Research Question | Moderate (theoretical) — CXCR4→JAK2 cross-talk; no evidence |
| 5 | Plasma cell myeloma | 91.83% | L4 | Research Question | Moderate — IL-6/JAK1/JAK2→STAT3; 1 case report (indirect) |
| 6 | Myeloid leukemia | 91.01% | L4 | Research Question | Moderate — FLT3-ITD/BCR-ABL→JAK-STAT; 1 trial + 4 publications |
| 7 | Meester-Loeys syndrome | 88.21% | L5 | Hold | Very low — connective tissue/aortic structural disorder |
| 8 | Ganglioneuroblastoma | 87.59% | L5 | Hold | Low — neural tumour; no JAK-specific preclinical data |
| 9 | Heparin cofactor 2 deficiency | 86.31% | L5 | Hold | ⚠️ Adverse match — JAK inhibitors increase VTE risk |
| 10 | Vertebral anomalies + T-cell dysfunction | 84.68% | L5 | Research Question | Low-moderate — T-cell JAK-STAT component; structural elements unaddressable |

---

## Why Are These Predictions Reasonable?

Baricitinib selectively and reversibly inhibits JAK1 and JAK2 kinases, blocking downstream STAT1, STAT3, and STAT5 signalling. This dampens cytokine-driven immune responses mediated by IL-6, IL-2, GM-CSF, and interferons — the mechanism underpinning its efficacy in autoimmune conditions. The central question for repurposing is whether JAK-STAT signalling plays a disease-driving role in the predicted new indications.

For **haematological malignancies** — the most biologically credible cluster — the mechanistic rationale is strongest. In acute myeloid leukaemia (AML), FLT3-ITD mutations drive constitutive JAK2/STAT5 activation; in chronic myeloid leukaemia (CML), BCR-ABL trans-activates JAK2. In multiple myeloma, IL-6 signals through JAK1/JAK2→STAT3 to promote malignant plasma cell survival, upregulate anti-apoptotic proteins (BCL-XL, MCL-1), and suppress immune surveillance in the bone marrow microenvironment. The closely related JAK1/2 inhibitor ruxolitinib has already obtained regulatory approval for myelofibrosis and steroid-refractory acute graft-versus-host disease (aGvHD), providing clinical proof-of-concept for JAK inhibition in haematological settings. The single case report in this Evidence Pack (PMID 34856779) shows baricitinib co-administered during active myeloma, though anti-myeloma efficacy was not the study objective.

For the top-ranked structural congenital disorders (Ranks 1–2, 7), the mechanistic basis is essentially absent. Colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachydactyly-syndactyly syndrome, and Meester-Loeys syndrome are developmental structural anomalies driven by mutations in biosynthetic or structural genes (ALDH4A1, HOXD/GDF5 axis, B4GALT7) — not inflammatory or cytokine-mediated processes. Their high TxGNN scores almost certainly reflect shared rare disease node co-neighbourhoods in the knowledge graph rather than genuine biological similarity to baricitinib's mechanism. These predictions should be treated as model artefacts and do not warrant clinical investigation. Additionally, the heparin cofactor 2 deficiency prediction (Rank 9) is actively contraindicated by pharmacology: JAK inhibitors, including baricitinib, carry a known venous thromboembolism risk — making this an adverse pharmacodynamic match.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06475820](https://clinicaltrials.gov/study/NCT06475820) | Phase 2/3 | Active, Not Recruiting | 150 | GvHD prevention using post-transplant cyclophosphamide + abatacept + vedolizumab + baricitinib in children and young adults with haemoblastosis (primarily leukaemia) following myeloablative conditioning and HSCT from unrelated or haploidentical donors. Primary endpoint is GvHD prevention — baricitinib is used as an immunosuppressant in the post-transplant setting, not as direct anti-leukaemia therapy. Provides safety and feasibility data for baricitinib use in leukaemia patients undergoing transplant. |

**Note:** No clinical trials were identified that directly assess baricitinib as anti-tumour therapy for any of the 10 predicted indications. The trial above represents indirect but contextually relevant evidence in the myeloid leukaemia transplant setting.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34856779](https://pubmed.ncbi.nlm.nih.gov/34856779/) | 2021 | Case Report | Minerva Medica | Simultaneous treatment of critical COVID-19 and newly diagnosed high-risk multiple myeloma using thalidomide, methylprednisolone, tocilizumab, and baricitinib. Documents baricitinib co-administration in an active myeloma patient; anti-myeloma efficacy was not the study focus. Demonstrates tolerability in a severely ill myeloma patient. |
| [34730109](https://pubmed.ncbi.nlm.nih.gov/34730109/) | 2021 | Preclinical/Experimental | J Clin Investigation | Antibody-drug conjugate conditioning + JAK inhibition enables MHC-mismatched allogeneic HSCT in preclinical models for acute leukaemia. Supports JAK inhibition as a component of leukaemia treatment conditioning — mechanistically adjacent to the NCT06475820 trial. |
| [36569952](https://pubmed.ncbi.nlm.nih.gov/36569952/) | 2022 | Review | Frontiers in Immunology | BCL-2 and JAK1/2 inhibitor repurposing for HIV and viral infections. Discusses baricitinib's broader immunomodulatory repurposing potential; tangentially relevant to haematological malignancy immune microenvironment context. |
| [35442720](https://pubmed.ncbi.nlm.nih.gov/35442720/) | 2022 | Diagnostic Study | JCO Precision Oncology | Acute leukaemia classification using low-cost nanopore mRNA sequencing. A methodology paper for leukaemia subtype classification; no direct baricitinib relevance. Retrieved due to keyword overlap. |
| [31816725](https://pubmed.ncbi.nlm.nih.gov/31816725/) | 2020 | Analytical Method | Talanta | LC-MS/MS method for therapeutic drug monitoring of 11 kinase inhibitors including ruxolitinib in plasma. Includes ruxolitinib (the structurally related JAK1/2 inhibitor) as a clinical comparator; indirect relevance to baricitinib monitoring in haematological disease. |

**Note:** The literature base is thin. The most clinically relevant publication (PMID 34856779) is a case report of baricitinib used for COVID-19 co-management in a myeloma patient — not as myeloma-directed treatment. No randomised trials, Phase 2 studies, or baricitinib-specific anti-tumour preclinical studies were identified across any of the 10 predicted indications.

---

## Australia Market Information

⚠️ **Data Collection Notice:** The automated ARTG query returned 0 registrations for baricitinib. This is highly likely to be a data collection error. Baricitinib (Olumiant, Eli Lilly) is known to hold TGA approval in Australia. Manual verification against the ARTG is required before this field can be used in regulatory decision-making.

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| *Automated query returned no results — manual ARTG verification required* | — | — | — |

**Expected TGA-registered indications** (to be confirmed against the ARTG — not confirmed from automated data):
- Moderate-to-severe active rheumatoid arthritis in adults with inadequate response or intolerance to DMARDs
- Moderate-to-severe atopic dermatitis (approved ~2022–2023 in Australia)
- Severe alopecia areata (TGA approval confirmed 2023)

---

## Safety Considerations

No local Product Information data was retrieved through the automated query pipeline. Based on internationally available safety information for baricitinib:

- **Key Warnings:** Serious and opportunistic infections (tuberculosis, herpes zoster, invasive fungal infections); increased risk of malignancy (lymphoma, lung cancer — particularly relevant when considering oncology repurposing); **venous thromboembolism** (DVT and pulmonary embolism — this risk is especially pertinent and makes the heparin cofactor 2 deficiency prediction (Rank 9) pharmacologically inappropriate); major adverse cardiovascular events (MACE); potential embryotoxicity and use in pregnancy.
- **Drug Interactions:** Concomitant use with other JAK inhibitors or biologic DMARDs (including tocilizumab, abatacept) is not recommended due to additive immunosuppression — relevant to the combination regimen used in NCT06475820. Baricitinib exposure is increased by OAT1/OAT3 inhibitors (e.g., probenecid), requiring dose adjustment.

Please refer to the TGA-approved Product Information (PI) for baricitinib (Olumiant) for complete and current Australian safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN predictions for baricitinib are predominantly dominated by structurally implausible congenital disorders (Ranks 1–2, 7, 9) that carry no genuine mechanistic connection to JAK-STAT signalling and should be considered knowledge graph noise. The most scientifically credible cluster — myeloid leukaemia and plasma cell myeloma — is supported only by indirect evidence (one case report, one GvHD prevention trial) and sits firmly at the Research Question stage. No direct anti-tumour efficacy data for baricitinib exists across any of the 10 predicted indications, and critical regulatory data (ARTG registration, TGA Product Information) could not be confirmed through the automated pipeline.

**To proceed, the following is needed:**

- **Resolve ARTG data gap:** Manually query the ARTG for Olumiant (baricitinib) and retrieve the approved Australian Product Information PDF to complete safety and regulatory assessment
- **Resolve MOA data gap:** Retrieve the complete DrugBank pharmacology entry for DB11817 to formalise the mechanistic link analysis
- **For myeloid leukaemia (Rank 6) — to upgrade to Proceed with Guardrails:**
  - Commission a systematic literature review of JAK1/2 inhibition (including ruxolitinib as a comparator) in AML and CML
  - Confirm whether NCT06475820 captures any secondary endpoints related to leukaemia response or relapse rates
  - Review in vitro/ex vivo data on baricitinib's direct cytostatic effect on AML/CML cell lines
- **For plasma cell myeloma (Rank 5) — to upgrade from Research Question:**
  - Assess additive potential of IL-6/JAK pathway inhibition alongside IMiD-based and proteasome inhibitor regimens
  - Search for preclinical baricitinib + myeloma cell line datasets in public repositories (e.g., DepMap, PharmacoGx)
- **Knowledge graph quality improvement:**
  - Investigate the structural biases causing congenital disorder nodes (Ranks 1–2, 7) to achieve high TxGNN scores for an anti-inflammatory drug — this likely reflects a known rare disease co-neighbourhood artefact requiring model calibration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

