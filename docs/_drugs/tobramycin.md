---
layout: default
title: Tobramycin
parent: 僅模型預測 (L5)
nav_order: 681
evidence_level: L5
indication_count: 10
---

# Tobramycin
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

# Tobramycin: From Bacterial Infections to Exposure Keratitis

## One-Sentence Summary

> Tobramycin is an aminoglycoside antibiotic conventionally used to treat bacterial infections, particularly those caused by *Pseudomonas aeruginosa* and other Gram-negative organisms.
> The TxGNN model predicts it may be effective for **Exposure Keratitis**,
> but this direction is currently supported by only **2 clinical trials** (neither testing tobramycin directly) and **7 publications**, mostly case reports and in vitro toxicity data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (aminoglycoside antibiotic class) — no specific approved indication text available; drug is not currently marketed in Australia |
| Predicted New Indication | Exposure Keratitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, tobramycin is an aminoglycoside antibiotic that inhibits bacterial protein synthesis at the 30S ribosomal subunit, with strong bactericidal activity against Gram-negative organisms including *Pseudomonas aeruginosa*. Its efficacy in bacterial infections (systemic and topical/ophthalmic) is well established.

However, the mechanistic link to exposure keratitis is weak. Exposure keratitis is primarily caused by incomplete eyelid closure leading to corneal drying and epithelial breakdown — it is **not a primary infectious disease**. Tobramycin, as an antibiotic, could only address a *secondary* bacterial infection complicating exposure keratitis, not the underlying cause. Furthermore, in vitro data (PMID 2707046) suggest aminoglycosides, including tobramycin, may be corneal-epithelium-toxic, which could theoretically delay epithelial healing — a relevant safety concern for a condition where epithelial recovery is the therapeutic goal.

Given this, the high TxGNN score should be interpreted cautiously: it likely reflects tobramycin's general association with ocular/keratitis-related knowledge graph nodes rather than a mechanistically validated new indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06200727](https://clinicaltrials.gov/study/NCT06200727) | N/A | Unknown | 170 | Evaluates platelet-rich fibrin (PRF) membrane across four ophthalmic conditions (macular hole, pterygium, corneal ulcer, post-trabeculectomy); does not test tobramycin directly |
| [NCT05313828](https://clinicaltrials.gov/study/NCT05313828) | N/A | Unknown | 40 | Compares treatment modalities for dendritic (herpetic) corneal ulcer; viral, not exposure-related keratitis, and does not test tobramycin directly |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2707046](https://pubmed.ncbi.nlm.nih.gov/2707046/) | 1989 | In vitro toxicity study | Current Eye Research | Aminoglycosides including tobramycin show corneal epithelial cytotoxicity in rabbit cell culture model |
| [34987857](https://pubmed.ncbi.nlm.nih.gov/34987857/) | 2021 | Case report | Oxford Medical Case Reports | Bacterial keratitis (MDR *Shewanella algae*) in a vegetative-state patient unable to close eyes voluntarily — an exposure keratitis context |
| [12861116](https://pubmed.ncbi.nlm.nih.gov/12861116/) | 2003 | Case report | Eye & Contact Lens | Bilateral MRSA keratitis following photorefractive keratectomy |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Case report | Ophthalmology | *Bacillus cereus* keratitis associated with contact lens wear |
| [17228760](https://pubmed.ncbi.nlm.nih.gov/17228760/) | 2006 | Susceptibility study | Nippon Ganka Gakkai Zasshi | MIC and post-antibiotic effect of antibiotic eye drops against infectious keratitis isolates in Japan |
| [33847093](https://pubmed.ncbi.nlm.nih.gov/33847093/) | 2021 | Case series (veterinary) | Polish Journal of Veterinary Sciences | Feline ocular toxoplasmosis case series; limited human translational relevance |
| [14574976](https://pubmed.ncbi.nlm.nih.gov/14574976/) | 2003 | Case report | Yan Ke Xue Bao | Paracentral corneal dellen (a form of localised exposure) in Graves ophthalmopathy; does not address tobramycin treatment |

---

## Australia Market Information

Tobramycin is currently **not marketed** in Australia and has **0 ARTG entries** in this evidence pack, so no product-specific formulation or approved-indication data is available.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No product is currently registered on the ARTG for this drug, and no drug interaction data were identified in this evidence pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (exposure keratitis) lacks direct clinical trial or literature support — no identified trial or publication tests tobramycin specifically for this condition. The proposed mechanism is also questionable, since exposure keratitis is a non-infectious, mechanical disorder, and available in vitro data raise a corneal-toxicity concern rather than supporting benefit.

**To proceed, the following is needed:**
- TGA/TFDA product information (warnings, contraindications) — currently a blocking data gap (DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Clinical evidence directly evaluating tobramycin (topical or otherwise) specifically in exposure keratitis, ideally addressing epithelial toxicity risk
- Confirmation of Australian marketing status/ARTG registration before any repurposing pathway can be pursued

**Note:** Within the same evidence pack, *otitis externa* (rank 3) shows substantially stronger evidence (L3, multiple relevant publications including long-term safety data, "Proceed with Guardrails") and may warrant separate evaluation as a more actionable candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

