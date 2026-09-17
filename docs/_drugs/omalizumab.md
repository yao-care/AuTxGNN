---
layout: default
title: Omalizumab
parent: Moderate Evidence (L3-L4)
nav_order: 491
evidence_level: L3
indication_count: 10
---

# Omalizumab
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Omalizumab: From Allergic Asthma to Bronchitis

## One-Sentence Summary

Omalizumab (DB00043) is a humanised anti-IgE monoclonal antibody originally developed for moderate-to-severe persistent allergic asthma.
The TxGNN model predicts it may also be useful for **bronchitis**, but the supporting evidence pack currently consists of **2 clinical trials** and **8 publications**, most of which are actually asthma studies rather than bronchitis-specific trials.
Evidence strength is currently low (**L3**), and a key regulatory data gap (TFDA/TGA product information) blocks formal safety assessment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Moderate-to-severe persistent allergic asthma (internationally approved indication; not derived from a local ARTG entry — see Market Information below) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.9992% |
| Evidence Level | L3 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack. Based on known pharmacology, omalizumab is a humanised monoclonal antibody that binds the constant (Cε3) region of free immunoglobulin E (IgE), lowering circulating free IgE and down-regulating FcεRI receptor expression on mast cells and basophils. This interrupts the Type I hypersensitivity cascade that drives airway inflammation, and its efficacy in moderate-to-severe allergic asthma is well established internationally.

Bronchitis and allergic asthma share overlapping airway inflammation pathways, and in principle an IgE-mediated (allergic/eosinophilic) subtype of bronchitis could respond to the same mechanism. However, the evidence pack's own relevance grading flags this link as indirect: the two registered trials are graded "C" because they are, in substance, asthma or chronic urticaria dose-finding studies that share an ontology label with "bronchitis" rather than trials that enrolled and treated a bronchitis-specific population. No trial in this pack tested omalizumab in bronchitis as a primary, well-defined clinical endpoint.

In short, the mechanistic rationale is plausible, but the current clinical evidence is an artefact of knowledge-graph label overlap with asthma rather than a direct, dedicated evidence base for bronchitis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2 | Completed | 382 | Dose-finding study of QGE031 (ligelizumab, an anti-IgE antibody related to omalizumab) as add-on therapy in Chronic Spontaneous Urticaria — not a bronchitis-specific trial; relevance graded C (indirect ontology overlap). |
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | Completed | 11 | Investigated whether add-on omalizumab allows steroid dose reduction in patients with asthma and eosinophilic bronchitis; very small sample (n=11), population is primarily asthma; relevance graded C. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Review | Clinical Reviews in Allergy & Immunology | Overview of omalizumab's approval and post-approval experience in asthma; describes reduced airway inflammation via IgE/FcεRI blockade. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opinion on Pharmacotherapy | Discusses treatment challenges in smoking-related airway disease (including chronic bronchitis) overlapping with asthma; notes these patients are often excluded from trials. |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Review | Allergologia et Immunopathologia | General update on monoclonal antibody use in paediatrics, including allergic disease; not bronchitis-specific. |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Review | Masui (Japanese Journal of Anesthesiology) | Preoperative management review for bronchial asthma/chronic bronchitis patients; mentions omalizumab as an option for severe allergic asthma. |
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Cohort/Review | Postępy Dermatologii i Alergologii | Omalizumab in older patients with severe allergic asthma-COPD overlap; supports biologic use in overlap phenotypes but not bronchitis specifically. |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Pooled Analysis | Current Medical Research and Opinion | Pooled safety analysis of omalizumab in children with allergic (IgE-mediated) asthma. |
| [21163396](https://pubmed.ncbi.nlm.nih.gov/21163396/) | 2010 | Review | Revue des Maladies Respiratoires | French expert review on definitions and treatment of adult asthma exacerbations; general asthma context. |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Case Report | Journal of Investigational Allergology & Clinical Immunology | Rare case of plastic bronchitis following bronchial thermoplasty; not an omalizumab efficacy report. |

---

## Australia Market Information

Omalizumab is **not currently registered in the ARTG** (Australian Register of Therapeutic Goods) according to this evidence pack (0 entries, market status "Not Marketed"). No local product, dosage form, or approved indication text is available to summarise.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. This evidence pack contains no verified warnings, contraindications, or drug interaction data for omalizumab — notably, the TFDA/product-label warning data gap (DG001) is flagged as **Blocking**, meaning a formal safety pre-assessment cannot be completed until this is resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis signal is driven mainly by a high TxGNN embedding score, but the underlying clinical trials and literature are substantially asthma- or urticaria-focused rather than bronchitis-specific (relevance grade C), placing true evidence strength at L3. A Blocking data gap in TFDA/PI safety information also prevents any S1 safety pre-assessment, and the drug is not currently marketed in Australia.

**To proceed, the following is needed:**
- TFDA/TGA-approved Product Information (warnings, contraindications) to resolve the Blocking data gap (DG001)
- Confirmed mechanism-of-action documentation (DG002)
- A dedicated, prospectively defined bronchitis (ideally allergic/eosinophilic subtype) clinical trial, rather than asthma trials sharing an ontology label
- Clarification of ARTG registration pathway, since the drug is not currently marketed in Australia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

