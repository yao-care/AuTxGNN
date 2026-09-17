---
layout: default
title: Rivaroxaban
parent: Moderate Evidence (L3-L4)
nav_order: 602
evidence_level: L4
indication_count: 10
---

# Rivaroxaban
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

# Rivaroxaban: From Anticoagulation (Unspecified Original Indication) to Rheumatoid Arthritis

## One-Sentence Summary

Rivaroxaban is an oral Factor Xa (FXa) inhibitor; this evidence pack does not contain a Taiwan/Australia-sourced original indication text, so the drug's established anticoagulant use (e.g. stroke prevention in atrial fibrillation, VTE treatment/prevention) is noted here only as general background, not as sourced data. The TxGNN model's top-ranked prediction for this drug is **Rheumatoid Arthritis**, but currently only **3 supporting publications** and **0 clinical trials** are available, and none of the literature directly evaluates rivaroxaban's therapeutic effect in RA.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in this evidence pack (`original_indications` and `taiwan_regulatory.licenses` are both empty) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L4 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (`original_moa` is flagged as a data gap, DG002). Based on general pharmacological knowledge, rivaroxaban is a direct Factor Xa inhibitor used clinically as an anticoagulant — this is background context, not data drawn from the evidence pack.

The rationale linking rivaroxaban to rheumatoid arthritis (RA) is indirect: RA patients are known to have increased thrombin generation and elevated thromboembolic risk, so FXa inhibition is theoretically plausible as a way to reduce RA-associated vascular/thrombotic complications. However, none of the three supporting publications directly assess rivaroxaban's effect on RA disease activity or joint damage — one is a general review of lower-extremity VTE, one is a methodology paper on thrombin generation assays in autoimmune disease, and one is a cohort study comparing rivaroxaban/apixaban adherence in atrial fibrillation. The prediction should be treated as a hypothesis-generating signal from the knowledge graph rather than as evidence of therapeutic efficacy in RA.

It is worth noting that of the 10 candidates in this evidence pack, the **HIV infectious disease** candidate (rank 3) reached a more advanced decision stage (S1, "Research Question") on the strength of one completed Phase 2 trial and seven publications — though that evidence also concerns anticoagulant drug-drug interaction/bleeding risk in HIV patients rather than an antiviral effect. Several lower-ranked candidates (feline AIDS, simian immunodeficiency virus infection) likely reflect knowledge-graph proximity to the HIV node rather than genuine pharmacological relevance, and two candidates (brachydactyly-syndactyly syndrome, colobomatous microphthalmia-rhizomelic dysplasia syndrome) have no supporting evidence at all.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the Rheumatoid Arthritis indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohort | PloS one | Compared medication adherence to rivaroxaban vs. apixaban in non-valvular atrial fibrillation patients; not RA-related, included for background on anticoagulant use patterns. |
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | General review of diagnosis/treatment of lower-extremity venous thromboembolism; no RA-specific content. |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Review | La Revue de médecine interne | Reviews thrombin generation assay (TGA) methodology for assessing hypercoagulability in autoimmune disease, including antiphospholipid syndrome; does not evaluate rivaroxaban treatment of RA. |

---

## Australia Market Information

No ARTG entries are recorded for Rivaroxaban in this evidence pack (`total_licenses: 0`, `market_status: Not marketed` / Not Marketed).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. (Key warnings, contraindications, and drug interaction data are all marked as data gaps in this evidence pack — DG001, Blocking severity.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The TxGNN score is high, but no clinical trial and no literature directly evaluates rivaroxaban's therapeutic effect in RA — the supporting literature is background/indirect only (VTE review, TGA methodology, unrelated AF adherence study). This does not meet the bar to proceed.

**To proceed, the following is needed:**
- TFDA/TGA product information (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action data (DG002)
- A study or trial that directly measures rivaroxaban's effect on RA disease activity, joint damage, or a relevant clinical endpoint
- Given the data gaps above, consider whether the HIV infectious disease candidate (rank 3, decision_stage S1) — despite also being an indirect/DDI-safety signal rather than an antiviral mechanism — merits separate evaluation as a comparatively more advanced candidate in this same evidence pack.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

