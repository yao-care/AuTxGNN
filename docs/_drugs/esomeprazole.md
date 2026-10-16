---
layout: default
title: Esomeprazole
parent: Moderate Evidence (L3-L4)
nav_order: 269
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Esomeprazole: predicted new indication Duodenogastric reflux (evidence level L4). Approved use: Peptic ulcer disease, GORD, reflux oesophagitis…"
monitor_inn: "Esomeprazole"
predicted_indications: ["duodenogastric reflux", "duodenal obstruction", "duodenal ulcer (disease)", "active peptic ulcer disease", "abnormality of glucagon secretion", "gastrojejunal ulcer", "peptic ulcer perforation", "Smouldering systemic mastocytosis", "multiple endocrine neoplasia", "acne (disease)"]
---

# Esomeprazole
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Esomeprazole: From Peptic Ulcer Disease to Duodenogastric Reflux

## One-Sentence Summary

Esomeprazole is a proton pump inhibitor (PPI) originally used for peptic ulcer disease, gastro-oesophageal reflux disease (GORD), reflux oesophagitis and Zollinger-Ellison syndrome.
The TxGNN model predicts it may be effective for **Duodenogastric Reflux**, but the supporting evidence is thin: **no clinical trials** and **1 publication** (a general PPI review) are currently available for this indication.

Note: the strongest evidence in the data compiled for this report relates to **duodenal ulcer** (rank 3) and **active peptic ulcer disease** (rank 4). These fall within or very close to the existing labelled use. They are discussed in the conclusion as the better-supported findings.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease, GORD, reflux oesophagitis, Zollinger-Ellison syndrome (the Australian ARTG entries carry no indication text) |
| Predicted New Indication | Duodenogastric reflux |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L4 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Esomeprazole is the S-isomer of omeprazole and, as a class, PPIs irreversibly block the gastric H+/K+ ATPase (the "proton pump"), suppressing gastric acid secretion.

Duodenogastric (bile) reflux is only partly acid-driven. Esomeprazole may ease acid-related symptoms or mucosal injury in these patients, but it does not stop bile reflux itself. The only supporting publication is a general review of PPI use, so the support is indirect. The high TxGNN score therefore reflects a plausible acid-related overlap rather than demonstrated benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for duodenogastric reflux.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | Eur J Clin Pharmacol | General update on PPI clinical use and pharmacokinetics; PPIs are first-choice drugs for peptic ulcer, H. pylori infection, GORD, NSAID-related lesions and Zollinger-Ellison syndrome. Does not address bile reflux directly. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10295W | Noxicid Caps | Enteric capsule 20 mg (as magnesium) | Not listed in the data compiled |
| ARTG 10759G | ESOMEPRAZOLE SANDOZ Hp7 | Co-pack: 14 enteric-coated esomeprazole 20 mg tablets, 14 clarithromycin 500 mg tablets and 28 amoxicillin 500 mg capsules (H. pylori eradication pack) | Not listed in the data compiled |

---

## Safety Considerations

- **Contraindication signals from a knowledge graph (not label text)**: liver failure, osteoporosis, postmenopausal osteoporosis, bone fracture, chronic atrophic gastritis. These should be verified against the Product Information.
- **Drug Interactions**: 100 interactions were identified in total. Examples from the first 20 reviewed:
  - **Major**: acalabrutinib, atazanavir
  - **Moderate**: hydrochlorothiazide, amphotericin B, amikacin, amphetamine, fenofibrate, apalutamide, armodafinil, atorvastatin, bendamustine, bosutinib, bumetanide
  - **Minor**: acetylsalicylic acid, axitinib, bortezomib, brivaracetam, cyanocobalamin
- CYP2C19-related interactions are of particular relevance for this class.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For duodenogastric reflux, there are no trials and only one indirect review. Esomeprazole does not treat bile reflux itself, so the prediction rests on a model score and a plausible acid-related symptom benefit.

**Better-supported findings from the same analysis (for context):**
- **Duodenal ulcer (L1, Proceed with Guardrails):** multiple completed Phase 3 RCTs (for example NCT00633932, NCT00633672, NCT00542789, NCT01069939, NCT01142245) and RCTs of esomeprazole-based triple therapy (PMIDs 11742194, 11121908). This is effectively on-label or a close extension of the labelled use.
- **Active peptic ulcer disease (L2, Proceed with Guardrails):** a completed Phase 2 active-controlled trial and a Phase 4 triple-therapy study. This is already within the labelled indication, so it supports continued use rather than a new repurposing claim.
- **Gastrojejunal ulcer** is a reasonable research question (L4), while the remaining top-10 predictions (duodenal obstruction, abnormality of glucagon secretion, peptic ulcer perforation, smouldering systemic mastocytosis, multiple endocrine neoplasia and acne) have no supporting evidence or only indirect evidence and should be held.

**To proceed, the following is needed:**
- Mechanism of action data (currently missing) and the TGA Product Information warnings and contraindications (a blocking data gap for safety screening)
- Targeted studies of esomeprazole in duodenogastric reflux with defined bile-reflux endpoints
- For the ulcer indications: confirmation of the labelled indication scope, H. pylori testing and eradication where relevant, and a DDI management plan, including CYP2C19-related interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

