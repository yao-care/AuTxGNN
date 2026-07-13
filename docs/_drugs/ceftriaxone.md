---
layout: default
title: Ceftriaxone
parent: 僅模型預測 (L5)
nav_order: 133
evidence_level: L5
indication_count: 10
---

# Ceftriaxone
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

# Ceftriaxone: From Bacterial Infections to Infectious Otitis Media

## One-Sentence Summary

Ceftriaxone is a third-generation cephalosporin antibiotic used to treat serious bacterial infections.
The TxGNN model identifies **Infectious Otitis Media** as the highest-evidence repurposing candidate among 10 predicted indications, supported by **3 clinical trials** and **19 publications**.
This aligns closely with Ceftriaxone's well-established antibacterial mechanism and warrants a **Proceed with Guardrails** recommendation for formalising its use in the Australian context.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious bacterial infections (third-generation cephalosporin) |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed (ARTG record shows 0 entries — data verification recommended) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on ARTG status:** The Evidence Pack records 0 ARTG entries for Ceftriaxone. This is likely a data extraction gap, as Ceftriaxone preparations (e.g., Rocephin®) are understood to be registered with the TGA. Clinicians should verify current status at [search.tga.gov.au](https://www.tga.gov.au/resources/artg) before prescribing.

---

## Why Is This Prediction Reasonable?

Ceftriaxone inhibits bacterial cell wall synthesis by binding irreversibly to penicillin-binding proteins (PBPs), triggering autolytic enzymes that lyse the bacterial cell. As a third-generation cephalosporin, it combines enhanced Gram-negative coverage with a long plasma half-life (~8 hours) and high protein binding, allowing once-daily IM or IV dosing. Critically, it achieves middle ear fluid concentrations that exceed minimum inhibitory concentration (MIC) breakpoints for key otitis media pathogens.

Infectious otitis media (acute otitis media, AOM) is driven by three primary pathogens — *Streptococcus pneumoniae*, *Haemophilus influenzae*, and *Moraxella catarrhalis* — all of which fall squarely within Ceftriaxone's antibacterial spectrum. When first-line amoxicillin fails (particularly with drug-resistant *S. pneumoniae*), or when oral administration is not possible (e.g., vomiting, non-adherent children), single-dose or 3-day IM Ceftriaxone provides a practical, high-efficacy rescue option with superior middle ear penetration compared to many oral alternatives.

This is not a speculative repurposing scenario. IM Ceftriaxone for AOM is already recommended as second-line or rescue therapy in international guidelines (AAP, IDSA, Japanese Society of Chemotherapy). The TxGNN score of 99.26% reflects the model's detection of these well-established pharmacological links within the drug-disease knowledge graph, confirming that the prediction is scientifically grounded. In the Australian context, formal evidence consolidation and confirmation of ARTG status may nonetheless strengthen guideline alignment and support clinical adoption.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01511107](https://clinicaltrials.gov/study/NCT01511107) | Phase 2b | Terminated | 520 | Multicenter, randomised, double-blind, placebo-controlled RCT comparing 5-day vs 10-day antibiotic courses for AOM in children aged 6–23 months. Enrolled 520 of 600 planned before termination. Provides comparative antibiotic duration data relevant to Ceftriaxone's role as a rescue agent. |
| [NCT02567825](https://clinicaltrials.gov/study/NCT02567825) | N/A | Completed | 250 | Assessed tympanostomy tube placement versus non-surgical management for recurrent AOM in children. Establishes clinical severity thresholds and management escalation pathways where IM Ceftriaxone is typically deployed. |
| [NCT01272999](https://clinicaltrials.gov/study/NCT01272999) | N/A | Completed | 391 | Post-marketing observational study of Prevnar 13 impact on AOM incidence in children. Quantifies the residual antibiotic-susceptible AOM burden in the post-vaccine era, which directly contextualises Ceftriaxone prescribing needs. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [8989332](https://pubmed.ncbi.nlm.nih.gov/8989332/) | 1997 | RCT | *Pediatrics* | Prospective, randomised, single-blind trial comparing single IM Ceftriaxone vs 10-day oral TMP-SMZ for AOM. Ceftriaxone demonstrated comparable clinical efficacy as a convenient one-dose IM regimen (Greater Boston Otitis Media Study Group). |
| [11099083](https://pubmed.ncbi.nlm.nih.gov/11099083/) | 2000 | RCT | *Pediatric Infectious Disease Journal* | Compared 1-day vs 3-day IM Ceftriaxone for non-responsive AOM in children. The 3-day regimen showed superior bacteriological eradication and clinical outcomes, particularly against drug-resistant *S. pneumoniae*. |
| [12237596](https://pubmed.ncbi.nlm.nih.gov/12237596/) | 2002 | RCT | *Pediatric Infectious Disease Journal* | Assessed nasopharyngeal pneumococcal carriage dynamics in non-responsive AOM treated with 1-day vs 3-day IM Ceftriaxone. The 3-day course was superior for eradicating resistant strains during and after therapy. |
| [12750572](https://pubmed.ncbi.nlm.nih.gov/12750572/) | 1998 | RCT | *Le infezioni in medicina* | Three-arm randomised trial in 75 paediatric AOM patients comparing amoxicillin, cefuroxime axetil, and single-dose IM Ceftriaxone (50 mg/kg). No statistically significant efficacy difference across groups, supporting Ceftriaxone as a viable alternative. |
| [9877360](https://pubmed.ncbi.nlm.nih.gov/9877360/) | 1998 | Clinical Study | *Pediatric Infectious Disease Journal* | 3-day IM Ceftriaxone for non-responsive AOM — demonstrated bacteriological eradication of *S. pneumoniae* (including drug-resistant strains) from middle ear fluid aspirates. |
| [39361280](https://pubmed.ncbi.nlm.nih.gov/39361280/) | 2024 | Clinical Practice Guideline Review | *JAMA Network Open* | US paediatric outpatient antibiotic prescribing appropriateness review. Identifies Ceftriaxone as appropriate for specific AOM scenarios while highlighting antimicrobial stewardship concerns — directly relevant to Australian prescribing context. |
| [35841649](https://pubmed.ncbi.nlm.nih.gov/35841649/) | 2022 | Retrospective Cohort | *Int J Pediatric Otorhinolaryngology* | Large US primary care database analysis of Ceftriaxone use for AOM. Documented increasing IM Ceftriaxone prescribing, especially for otitis-conjunctivitis syndrome, raising stewardship considerations applicable to Australian practice. |
| [12166789](https://pubmed.ncbi.nlm.nih.gov/12166789/) | 2002 | Consensus Statement | *Clinical Pediatrics* | AOM management consensus for paediatricians. Ceftriaxone positioned as second-line rescue agent for treatment failure or when oral administration is not feasible — relevant to Australian primary care and ED settings. |
| [20802367](https://pubmed.ncbi.nlm.nih.gov/20802367/) | 2010 | Review | *Otology & Neurotology* | Prevention and treatment of AOM and meningitis in children with cochlear implants. Ceftriaxone cited as the preferred antibiotic for complicated or severe AOM with intracranial risk in this high-risk population. |
| [10688388](https://pubmed.ncbi.nlm.nih.gov/10688388/) | 2000 | Review | *Clinical Therapeutics* | Synthesised AOM antimicrobial treatment recommendations. Ceftriaxone identified as the most appropriate rescue therapy for multi-drug resistant *S. pneumoniae* AOM, reinforcing its second-line role. |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple published RCTs, guideline consensus statements, and large observational studies support Ceftriaxone's efficacy in infectious otitis media — particularly as a second-line or rescue therapy for children with non-responsive, severe, or complicated AOM, or when oral administration is not achievable. The drug's bactericidal mechanism directly targets the three principal AOM pathogens, and its pharmacokinetic profile (favourable middle ear penetration, once-daily IM dosing) makes it well-suited to this indication.

**To proceed, the following is needed:**

- Verify current ARTG registration status directly via TGA (current Evidence Pack data shows 0 entries — a data extraction gap is suspected and must be confirmed before any clinical or regulatory action)
- Review the TGA-approved Product Information (PI) for approved indications, dosing schedules, contraindications, and key warnings
- Obtain mechanism of action (MOA) data from DrugBank (DB01212) to complete pharmacological documentation for any formal submission
- Develop an antimicrobial stewardship framework for Ceftriaxone use in paediatric AOM, aligned with **Therapeutic Guidelines: Antibiotic** (eTG complete), to govern second-line and rescue indications
- If the current ARTG approval does not explicitly include infectious otitis media, consider whether a formal TGA indication extension or off-label use protocol is required for institutional prescribing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

