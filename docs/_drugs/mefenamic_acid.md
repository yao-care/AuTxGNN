---
layout: default
title: Mefenamic Acid
parent: 僅模型預測 (L5)
nav_order: 421
evidence_level: L5
indication_count: 10
---

# Mefenamic Acid
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

# Mefenamic Acid: From NSAID (Fenamate) Analgesic Use to Rheumatoid Arthritis

## One-Sentence Summary

Mefenamic acid is a fenamate-class NSAID; the evidence pack does not capture its originally registered indication (no Australian licence on file), but its established pharmacology is COX-1/COX-2 inhibition for pain and inflammation.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, with **0 registered clinical trials** but **20 supporting publications**, mostly historical (1960s–80s) comparative and double-blind trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack — drug is not currently marketed in Australia and no ARTG licence text is available |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this drug record is not available (data gap). Based on the evidence pack's own classification, mefenamic acid belongs to the fenamate class of NSAIDs, acting through inhibition of COX-1/COX-2 and reduction of prostaglandin synthesis — a class effect shared with diclofenac, ibuprofen, sulindac, and flurbiprofen.

Rheumatoid arthritis is a chronic synovial inflammatory disease driven substantially by prostaglandin-mediated pain and inflammation, which is directly addressed by NSAID pharmacology. This is not a novel repositioning hypothesis so much as a re-confirmation of a historically used indication: multiple double-blind and comparative trials from the 1960s–1980s directly tested mefenamic acid in RA populations against other NSAIDs (ibuprofen, sulindac, flurbiprofen, phenylbutazone, aspirin), generally reporting comparable efficacy.

The main caveat is evidence currency — all supporting trials predate modern RA outcome measures (e.g., ACR/EULAR response criteria) and none are registered on ClinicalTrials.gov or ICTRP. The prediction is mechanistically sound but rests on dated clinical evidence rather than contemporary registration trials. It is also worth noting that other TxGNN candidates in this pack for the same drug — osteoarthritis (rank 10) and migraine/headache disorder (ranks 3, 7) — reflect the same underlying NSAID/prostaglandin mechanism and are supported by similar literature, reinforcing overall biological plausibility. In contrast, several lower-ranked candidates (rare congenital syndromes, an "osteoarthritis susceptibility" ontology term) have no supporting evidence and are flagged in the pack itself as likely knowledge-graph noise.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [373989](https://pubmed.ncbi.nlm.nih.gov/373989/) | 1979 | RCT (double-blind crossover) | Current Medical Research and Opinion | Mefenamic acid, sulindac and flurbiprofen all significantly superior to placebo for pain, tenderness, and morning stiffness in RA |
| [796645](https://pubmed.ncbi.nlm.nih.gov/796645/) | 1976 | Comparative clinical trial (vs ibuprofen) | The Medical Journal of Australia | Double-blind crossover in RA on background salicylate; mefenamic acid compared favourably with ibuprofen, mild GI-predominant side effects |
| [330287](https://pubmed.ncbi.nlm.nih.gov/330287/) | 1977 | RCT (vs ibuprofen) | Journal of International Medical Research | Randomised double-blind within-patient study in 40 RA patients; analgesic/anti-inflammatory effect not significantly different from ibuprofen |
| [4294443](https://pubmed.ncbi.nlm.nih.gov/4294443/) | 1967 | Early clinical study | Annals of the Rheumatic Diseases | Early clinical evaluation of mefenamic acid specifically in rheumatoid arthritis |
| [5920657](https://pubmed.ncbi.nlm.nih.gov/5920657/) | 1966 | Comparative trial (vs aspirin/phenylbutazone) | British Medical Journal | Mefenamic acid and flufenamic acid compared with aspirin and phenylbutazone in RA |
| [10439](https://pubmed.ncbi.nlm.nih.gov/10439/) | 1976 | Comparative study (10 drugs, 684 patients) | The Journal of Rheumatology | Single-blind non-crossover method assessing 10 antirheumatic drugs including mefenamic acid; pain-chart based efficacy assessment |
| [6039589](https://pubmed.ncbi.nlm.nih.gov/6039589/) | 1967 | Comparative study (vs phenylbutazone/aspirin) | Annals of the Rheumatic Diseases | Evaluation of mefenamic and flufenamic acids vs phenylbutazone and aspirin in RA out-patients |
| [306128](https://pubmed.ncbi.nlm.nih.gov/306128/) | 1978 | Review | Scottish Medical Journal | Review of the place of mefenamic acid in RA treatment |
| [29548675](https://pubmed.ncbi.nlm.nih.gov/29548675/) | 2018 | Observational (case-crossover) | The American Journal of Cardiology | Nonselective NSAIDs, including mefenamic acid class, evaluated for transient stroke/AMI risk in RA patients (5,921 cases) |
| [335681](https://pubmed.ncbi.nlm.nih.gov/335681/) | 1977 | Review | Zeitschrift für die gesamte innere Medizin | General review of non-steroidal antirheumatic agents including mefenamic acid, covering efficacy, side effects, indications/contraindications |

---

## Australia Market Information

Mefenamic acid currently has 0 ARTG entries and is not marketed in Australia; no product listing is available to summarise.

---

## Safety Considerations

Mefenamic acid is not currently registered in Australia (0 ARTG entries), so no local Product Information could be sourced. The DrugBank drug-interaction query for this record returned no results, and TFDA warning/contraindication text has not yet been obtained (flagged as a blocking data gap). As a fenamate-class NSAID, the standard NSAID safety profile — gastrointestinal, renal, cardiovascular, and hypersensitivity risk — should be assumed as a baseline until formal Product Information/safety review is completed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple historical double-blind and comparative trials support mefenamic acid's efficacy in rheumatoid arthritis via a well-established NSAID mechanism, but the evidence base is decades old, has no modern trial registration, and critical safety documentation (TFDA warnings/contraindications) is missing — this is a blocking gap for any safety sign-off.

**To proceed, the following is needed:**
- TFDA/TGA-equivalent Product Information (warnings and contraindications) — currently a Blocking data gap
- Detailed mechanism-of-action confirmation from DrugBank — currently a High-severity data gap
- Contemporary drug-drug interaction data (current DDI query returned no results)
- Confirmation of Australian registration pathway, given 0 current ARTG entries
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

