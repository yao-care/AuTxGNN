---
layout: default
title: Obeticholic Acid
parent: 僅模型預測 (L5)
nav_order: 481
evidence_level: L5
indication_count: 10
---

# Obeticholic Acid
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

# Obeticholic Acid: From Primary Biliary Cholangitis to Rheumatoid Arthritis

## One-Sentence Summary

Obeticholic acid (OCA) is a farnesoid X receptor (FXR) agonist reported in the literature for the treatment of primary biliary cholangitis (PBC). The TxGNN model predicts a possible new indication in **rheumatoid arthritis**, but **no clinical trials** support this link and the **3 supporting publications** do not actually address rheumatoid arthritis — the evidence pack's own analysis flags this as likely model noise.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Primary biliary cholangitis (PBC) — sourced from literature only; not TGA/ARTG-registered |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this candidate (flagged as a Blocking/High-severity data gap). Based on literature references within this evidence pack, OCA is an FXR agonist used in primary biliary cholangitis, where it modulates bile acid metabolism and has downstream anti-inflammatory and anti-fibrotic effects in the liver.

However, the evidence pack's own mechanistic assessment for this specific prediction is **negative**: none of the three supporting publications discuss rheumatoid arthritis or joint/synovial inflammation. They instead cover PBC diagnosis, autoimmune hepatitis animal models, and FXR-mediated hepatoprotection against herbal-induced liver injury (a drug used to treat RA, not evidence that OCA treats RA). The reviewers assess this as likely embedding-similarity noise, possibly driven by the shared "autoimmune disease" semantic neighbourhood in the model's knowledge graph, rather than a genuine mechanistic link between FXR agonism and rheumatoid joint disease.

**Note for reviewers:** a separate candidate in this pack — OCA repurposed for **heart disease** (rank 7, evidence level L3, decision stage S1, "Research Question") — has substantially stronger and more mechanistically coherent literature support (FXR activation improving NASH-related cardiac dysfunction, cardiovascular risk associated with NAFLD/NASH). That candidate may warrant separate evaluation and is not covered further in this report, which follows the top-ranked candidate as specified.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32299307](https://pubmed.ncbi.nlm.nih.gov/32299307/) | 2020 | Review | United European Gastroenterology Journal | Overview of PBC diagnosis and treatment; does not address rheumatoid arthritis |
| [35903109](https://pubmed.ncbi.nlm.nih.gov/35903109/) | 2022 | Review | Frontiers in Immunology | Animal models for autoimmune liver disease (autoimmune hepatitis, PBC); not RA-related |
| [33704005](https://pubmed.ncbi.nlm.nih.gov/33704005/) | 2021 | Preclinical/Animal | Xenobiotica | FXR activation prevents liver injury from *Tripterygium wilfordii* preparations (a herbal RA treatment); does not test OCA in RA |

---

## Australia Market Information

No ARTG entries were found — obeticholic acid is not currently marketed in Australia (0 registered products).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The rheumatoid arthritis prediction has no clinical trial support and the cited literature does not establish a plausible mechanistic link — the pack's own analysis attributes the high TxGNN score to embedding-similarity noise rather than genuine biological rationale. Combined with the absence of MOA data and the drug's current unmarketed status in Australia, this candidate does not meet the bar for further development at this time.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for obeticholic acid
- Preclinical or mechanistic studies specifically linking FXR agonism to rheumatoid joint inflammation, if such a rationale is to be pursued
- TGA/ARTG regulatory status confirmation, since the drug is not currently marketed in Australia
- Consider evaluating the heart disease candidate (rank 7) separately, as it currently has stronger supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

