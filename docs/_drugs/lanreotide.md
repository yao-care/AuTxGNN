---
layout: default
title: Lanreotide
parent: 僅模型預測 (L5)
nav_order: 382
evidence_level: L5
indication_count: 10
---

# Lanreotide
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

# Lanreotide: From Neuroendocrine Tumour Management to Polycystic Kidney/Liver Disease (Multi-Candidate TxGNN Screen)

## One-Sentence Summary

Lanreotide is a long-acting somatostatin analogue used to manage neuroendocrine tumour (NET)-associated endocrine syndromes and related hormone-secreting conditions. In this evidence pack, TxGNN generated **10 ranked candidate indications**, but only one — **Polycystic Kidney Disease 3 with or without Polycystic Liver Disease (ADPKD/PLD)** — has any supporting mechanism and literature, backed by **20 publications** (including one lanreotide-specific paper) and **zero drug-specific clinical trials**. The nine higher-scoring candidates (including the top-ranked "hypertrichosis") have no clinical trials, no literature, and no plausible mechanistic link, and should be treated as likely model noise rather than genuine signals.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (drug is not TGA/ARTG registered). Contextual reference within the pack's own trial data describes lanreotide as a somatostatin analogue used for endocrine syndromes associated with neuroendocrine tumours |
| Highest TxGNN-Scored Candidate | Hypertrichosis (disease) — score 99.97%, **no supporting evidence of any kind** |
| Most Clinically Plausible Candidate | Polycystic Kidney Disease 3 with or without Polycystic Liver Disease (ADPKD/PLD) |
| TxGNN Score (ADPKD/PLD) | 98.84% (rank 11,608 of all disease pairs) |
| Evidence Level | L5 for 8 of 10 candidates (model prediction only); **L4** for ADPKD/PLD and thoracic malformation (mechanism/indirect literature, no direct trials) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | **Hold** for 9 of 10 candidates; **Research Question** for ADPKD/PLD only |

---

## Why is This Prediction Reasonable?

Detailed drug-specific mechanism-of-action data was not available in this evidence pack (flagged as a High-severity data gap). However, the pack's own supporting materials — a clinical trial brief summary and a dedicated literature reference — provide enough context to assess plausibility for the two candidates that returned any evidence.

**Polycystic Kidney/Liver Disease (rank 8, the featured candidate):** Somatostatin analogues, including lanreotide and octreotide, act on Gαi-protein-coupled somatostatin receptors (SSTRs) expressed in kidney and liver tissue, inhibiting cAMP production — a signalling pathway implicated in cyst epithelial proliferation and fluid secretion in autosomal dominant polycystic kidney disease (ADPKD) and polycystic liver disease (PLD). This is a recognised pharmacological rationale (see Sun et al., 2015, below), not something inferred from this dataset alone. Critically, one of the 20 literature results returned is *specifically about lanreotide* in this context (PMID 26126910), which distinguishes this candidate from the other nine. That said, the remaining 19 papers are general ADPKD/PLD reviews and guidelines with no mention of lanreotide, and the pack contains **zero clinical trials** of lanreotide in this population — so the mechanistic story is reasonable, but direct clinical evidence for lanreotide itself is currently absent.

**All other candidates (hypertrichosis, Dandy-Walker malformation, odontal/periodontal malformation syndrome, hair shaft abnormality, Ambras-type hypertrichosis, renal-hepatic-pancreatic dysplasia, pulmonary arteriovenous malformation, genetic alopecia, thoracic malformation):** These returned either no evidence at all, or literature/trials that do not reference lanreotide and do not match the predicted disease concept (e.g., 20 general periodontitis papers with no mention of lanreotide for "malformation syndrome with odontal/periodontal component"; a trial of *octreotide*, not lanreotide, in neuroendocrine tumours loosely linked to "thoracic malformation"). These are consistent with the pack's own assessment that they represent knowledge-graph co-occurrence artefacts rather than genuine drug–disease signals, and should not be prioritised despite having nominally higher TxGNN scores than the ADPKD/PLD candidate.

---

## Clinical Trial Evidence

No clinical trials of lanreotide in ADPKD/PLD (the featured candidate) were identified in this evidence pack.

One incidental trial was returned elsewhere in the pack, linked to the "thoracic malformation" candidate. It is included here for completeness, with an important caveat: it tests **octreotide**, not lanreotide, in neuroendocrine tumours — not thoracic malformation.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00990535](https://clinicaltrials.gov/study/NCT00990535) | Phase 2 | Completed | 28 | High-dose octreotide LAR in progressive neuroendocrine tumours; octreotide and lanreotide are both cited as therapy of choice for NET-associated endocrine syndromes. **Relevance grade C** — different drug within the same class, and indication (NET) does not match the predicted disease label (thoracic malformation) |

---

## Literature Evidence

Presented for the featured candidate, ADPKD/PLD (evidence level L4), prioritising the one lanreotide-specific paper followed by the highest-tier reviews and guidelines:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26126910](https://pubmed.ncbi.nlm.nih.gov/26126910/) | 2015 | Review (drug-specific) | Current Topics in Medicinal Chemistry | Lanreotide and related somatostatin analogues block Gαi-coupled SSTR/cAMP signalling implicated in cyst formation and enlargement in polycystic kidney and liver disease — the only paper in this pack that names lanreotide directly |
| [30819518](https://pubmed.ncbi.nlm.nih.gov/30819518/) | 2019 | Review | Lancet | ADPKD is a systemic disorder with renal cysts, hypertension and extrarenal complications including liver cysts; summarises molecular genetics and management advances |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clinics in Liver Disease | PLD is the most common extrarenal manifestation of ADPKD; notes tolvaptan slows renal decline, highlighting the unmet need for liver-directed therapy |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Guideline | Journal of Hepatology | EASL clinical practice guideline covering diagnosis and management of cystic liver diseases, including polycystic liver disease |
| [38958301](https://pubmed.ncbi.nlm.nih.gov/38958301/) | 2024 | Guideline | American Journal of Gastroenterology | ACG guideline on focal liver lesions, including management recommendations for polycystic liver disease |
| [29038287](https://pubmed.ncbi.nlm.nih.gov/29038287/) | 2018 | Review | JASN | Reviews genetic overlap and shared pathogenesis between ADPKD and autosomal dominant polycystic liver disease |
| [34724412](https://pubmed.ncbi.nlm.nih.gov/34724412/) | 2022 | Review | Annual Review of Pathology | Mechanisms of PLD cystogenesis (primary, secondary, tertiary) and treatment advances |
| [36200122](https://pubmed.ncbi.nlm.nih.gov/36200122/) | 2022 | Review | Hepatic Medicine: Evidence and Research | Pathophysiology, diagnosis and treatment overview of polycystic liver disease |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | 2023 | Review | Advances in Kidney Disease and Health | Genetic spectrum of polycystic kidney/liver disease and resulting phenotypes |
| [28317394](https://pubmed.ncbi.nlm.nih.gov/28317394/) | 2017 | Review | Expert Review of Gastroenterology & Hepatology | Update on pathophysiology and management of polycystic liver disease |

Note: A separate search returned 20 general periodontitis papers linked to the "malformation syndrome with odontal/periodontal component" candidate, but none reference lanreotide — these are not reproduced here as they do not support a drug-specific link.

---

## Australia Market Information

Lanreotide has no ARTG entries and is not currently marketed in Australia (0 licences on file). No product, dosage form or approved indication text is therefore available from this evidence pack.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. This evidence pack returned no usable data on warnings, contraindications or drug interactions for lanreotide (all fields marked as data gaps).

---

## Conclusion and Next Steps

**Decision: Hold (9 of 10 candidates) / Research Question (ADPKD/PLD only)**

**Rationale:**
- Nine of the ten TxGNN-predicted indications — including the single highest-scoring one, hypertrichosis — have no clinical trials, no relevant literature and no plausible mechanistic link to lanreotide. High raw TxGNN scores here should not be read as clinical signal; they most likely reflect knowledge-graph co-occurrence rather than a real drug–disease relationship.
- The ADPKD/PLD candidate is the only one with a coherent pharmacological rationale (somatostatin receptor/cAMP-mediated inhibition of cystogenesis) and a lanreotide-specific literature reference, but it still lacks any drug-specific clinical trial evidence within this pack, so it is best framed as a research question rather than a near-term repurposing opportunity.

**To proceed, the following is needed:**
- Confirmed original indication and TGA/international regulatory status for lanreotide (currently absent from this pack)
- DrugBank-sourced mechanism-of-action detail (currently a data gap, DG002)
- TFDA/TGA Product Information for warnings, contraindications and interactions (currently a blocking data gap, DG001)
- A targeted literature/trial search specifically for "lanreotide AND (ADPKD OR polycystic liver disease)" to establish whether direct clinical evidence exists outside this pack
- Re-scoping of the remaining nine candidates to confirm whether they represent genuine signal or should be deprioritised as knowledge-graph artefacts before any further evaluation effort is spent on them
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

