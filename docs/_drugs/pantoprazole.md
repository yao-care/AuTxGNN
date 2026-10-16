---
layout: default
title: Pantoprazole
parent: High Evidence (L1-L2)
nav_order: 546
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-13
description: "Pantoprazole: predicted new indication Active peptic ulcer disease (evidence level L1). Approved use: Peptic ulcer disease, gastro-oesophageal reflux disease, oesophagitis…"
---

# Pantoprazole
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Pantoprazole: From Peptic Ulcer Disease to Active Peptic Ulcer Disease

## One-Sentence Summary

Pantoprazole is a proton pump inhibitor originally used for peptic ulcer disease, gastro-oesophageal reflux disease, oesophagitis and Zollinger-Ellison syndrome.
The TxGNN model predicts it may be effective for **active peptic ulcer disease**, but this is effectively an on-label use rather than true repurposing.
The data compiled for this report include **1 clinical trial** (a completed Phase 3 RCT) and **19 publications** for this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease, gastro-oesophageal reflux disease, oesophagitis, Zollinger-Ellison syndrome (the Australian licence record carries no indication text) |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L1 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the compiled data. From the literature, pantoprazole irreversibly inhibits the gastric H+/K+ ATPase (proton pump) in parietal cells. This suppresses gastric acid secretion and allows ulcers to heal.

Active peptic ulcer disease is closely related to pantoprazole's original indications. The prediction is therefore mechanistically sound, but it largely restates an established use.

The model's other predictions fall into three groups:
- **Established acid-related uses:** duodenal ulcer (rank 6) and gastric ulcer (rank 8) are on-label and supported by Phase 3 evidence (both L1, Proceed with Guardrails).
- **Plausible adjunct or indirect uses:** peptic ulcer perforation, gastrojejunal ulcer and duodenogastric reflux have limited or indirect evidence (L3–L4, Research Question).
- **Unsupported predictions:** duodenal obstruction, acne, smouldering systemic mastocytosis and lymphoadenopathic mastocytosis with eosinophilia have no credible mechanistic link or evidence (L5, Hold). The high scores for acne and duodenal obstruction appear to be model artefacts.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Completed | 323 | Multicentre, randomised, double-blind trial of ilaprazole vs pantoprazole triple therapy for 7 days in H. pylori-positive gastric and/or duodenal ulcer patients |

For the related indications of duodenal and gastric ulcer, further trials are listed in the model output. They include NCT00374101 (Phase 3, n=450, high vs standard dose PPI in bleeding peptic ulcer) and NCT00843063 (Phase 4, n=161, famotidine vs pantoprazole for preventing recurrent aspirin-induced ulcer).

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38384180](https://pubmed.ncbi.nlm.nih.gov/38384180/) | 2024 | RCT | Gut and Liver | Tegoprazan (a potassium-competitive acid blocker) in endoscopic resection-induced artificial ulcers; pantoprazole is not the study drug |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Systematic review / network meta-analysis | Am J Gastroenterol | P-CAB vs PPI for grade C/D oesophagitis |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Review | Clin Drug Investig | Pantoprazole binds irreversibly to the proton pump; short-term efficacy in reflux disease; no drug interactions identified in numerous studies |
| [21534455](https://pubmed.ncbi.nlm.nih.gov/21534455/) | 2011 | Review | Med Arh | PPIs in the management of GERD |
| [10638560](https://pubmed.ncbi.nlm.nih.gov/10638560/) | 2000 | Clinical trial | Am J Gastroenterol | Pantoprazole vs ranitidine in duodenal ulcer (Brazilian multicentre study) |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | Clinical trial | Hepatogastroenterology | Lansoprazole vs pantoprazole in active duodenal ulcer and H. pylori eradication |
| [15989651](https://pubmed.ncbi.nlm.nih.gov/15989651/) | 1997 | Review | Expert Opin Investig Drugs | Pantoprazole gives faster pain relief and ulcer healing than H2 antagonists |
| [38652367](https://pubmed.ncbi.nlm.nih.gov/38652367/) | 2024 | Preclinical (rat) | Inflammopharmacology | Pantoprazole plus mesenchymal stem cells in experimental gastric ulcer |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 11678P | Somac | Sachet containing granules 40 mg (as sodium sesquihydrate) | Not recorded in the compiled data |

## Safety Considerations

- **Contraindications recorded in the knowledge graph (not label text):** osteoporosis, postmenopausal osteoporosis, bone fracture and pernicious anaemia. These are consistent with concerns about long-term PPI use affecting bone health and vitamin B12 absorption.
- **Drug interactions:** 100 interactions were identified. Examples include:
  - **Major:** acalabrutinib, atazanavir.
  - **Moderate:** alpelisib, amphotericin B, amikacin, amphetamine, apalutamide, armodafinil, atorvastatin, bosutinib, bumetanide, fenofibrate, hydrochlorothiazide.
  - **Minor:** acetylsalicylic acid, axitinib, bortezomib, brivaracetam, cyanocobalamin.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Active peptic ulcer disease is an established acid-related use of pantoprazole. It is supported by a completed Phase 3 RCT and by Phase 3 evidence in duodenal and gastric ulcer, so efficacy is not in doubt. The "guardrails" reflect missing Australian label and safety data, not uncertainty about benefit. The unsupported predictions (acne, mastocytosis, duodenal obstruction) should not be pursued.

**To proceed, the following is needed:**
- Review of the TGA Product Information for Somac, including approved indications, warnings and contraindications, which are not in the compiled data
- Detailed mechanism of action data from DrugBank
- Confirmation that the approved indications and the sachet granule formulation suit the intended ulcer use
- A review of the major interactions (acalabrutinib, atazanavir) and of long-term risks (bone health, vitamin B12 status)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

