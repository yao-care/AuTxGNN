---
layout: default
title: Phenoxymethylpenicillin
parent: 僅模型預測 (L5)
nav_order: 532
evidence_level: L5
indication_count: 10
---

# Phenoxymethylpenicillin
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

# Phenoxymethylpenicillin: From [Data Gap] to Epiglottitis

## One-Sentence Summary

Phenoxymethylpenicillin (Penicillin V, DB00417) is a long-established penicillin-class antibiotic; its original approved indication is not recorded in this evidence pack, and the drug is not currently marketed in Australia. The TxGNN model predicts a possible new application in **Epiglottitis** with a very high confidence score, but **no clinical trials or published literature currently support this specific prediction** — it is a model-only signal at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established in this evidence pack (no ARTG-approved indication text available; original_indications field empty) |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for phenoxymethylpenicillin in this evidence pack. Based on known information, phenoxymethylpenicillin is a member of the penicillin (beta-lactam) antibiotic class — its identity as "Penicillin V" is embedded in the INN itself — and its established efficacy is in bacterial infections generally. The specific TGA-approved indication text could not be extracted here because the drug has no active ARTG entries.

Epiglottitis is typically an acute bacterial infection of the supraglottic larynx, historically associated with *Haemophilus influenzae* type b and other pyogenic organisms, so a beta-lactam mechanism is broadly plausible in principle. However, phenoxymethylpenicillin's antibacterial spectrum is narrow and it is not a drug conventionally used for epiglottitis (which typically requires broader-spectrum, often IV, antibiotic coverage) — this prediction currently has no supporting trial or literature evidence to confirm the mechanistic link is clinically meaningful.

It is worth noting that the underlying evidence pack contains substantially more literature on other TxGNN-ranked candidates for this drug — laryngitis (rank 2, 19 PubMed records), urinary tract infection (rank 3, 20 records), and gonococcal urethritis (rank 4, 7 records) — though several of those studies report **negative or historical findings** (see Literature Evidence below is specific to epiglottitis; those other candidates are outside the scope of this report per the top-ranked prediction).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*(For context only — not part of the epiglottitis evidence base: TxGNN's second-ranked candidate, laryngitis, has 19 associated PubMed records, several of which — e.g. PMID [3918495](https://pubmed.ncbi.nlm.nih.gov/3918495/) "Inefficacy of penicillin V in acute laryngitis in adults" and the repeated Cochrane reviews on antibiotics for acute laryngitis — report that penicillin V/antibiotics did **not** demonstrate clinical benefit in that condition. This underscores that a high TxGNN score does not by itself indicate positive clinical evidence.)*

---

## Australia Market Information

No ARTG entries found — phenoxymethylpenicillin is not currently listed as marketed in Australia under this evidence pack.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Key warnings, contraindications, and drug-interaction data were not found in this evidence pack (source: DrugBank/TFDA queries returned no results — see data gap DG001, classified as Blocking).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (epiglottitis, TxGNN score 99.90%) has no supporting clinical trial or literature evidence (Evidence Level L5), the drug's original indication and mechanism of action are undocumented in this pack, and it is not currently marketed in Australia (0 ARTG entries), which blocks the standard safety pre-screen (data gap DG001).

**To proceed, the following is needed:**
- TGA-approved Product Information (PI) — warnings, contraindications, drug interactions (blocking gap DG001)
- Mechanism of action data from DrugBank (gap DG002)
- Original approved indication documentation
- Targeted literature/clinical search specifically for phenoxymethylpenicillin in epiglottitis, since current PubMed evidence clusters around other candidate indications (laryngitis, UTI, gonococcal urethritis) rather than epiglottitis itself, and some of that adjacent evidence is negative
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

