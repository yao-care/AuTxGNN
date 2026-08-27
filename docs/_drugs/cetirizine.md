---
layout: default
title: Cetirizine
parent: 僅模型預測 (L5)
nav_order: 139
evidence_level: L5
indication_count: 10
---

# Cetirizine
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

# Cetirizine: From Established Antihistamine Use to Allergic Urticaria

## One-Sentence Summary

> Cetirizine is a second-generation H1-antihistamine widely used for allergic conditions; a formal record of its originally approved indication is not present in this evidence pack.
> The TxGNN model's top prediction identifies **Allergic Urticaria** as the strongest candidate indication, with a prediction score of **99.99%**,
> supported by **3 clinical trials** and **18 publications**, including one completed Phase 3 trial and a 2021 systematic review.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available regulatory dataset (`taiwan_regulatory.licenses` and `drug.original_indications` are empty) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Australia Market Status | Not currently marketed (per dataset) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, a formal mechanism-of-action record (DrugBank `original_moa`) is not available in this evidence pack. Based on the pharmacological detail captured in the repurposing evidence itself, cetirizine is a second-generation H1-histamine receptor inverse agonist that directly blocks histamine-driven vasodilation, increased vascular permeability, and pruritus — the core pathophysiological pathway underlying urticaria.

Because `drug.original_indications` was not populated in this extract, the originally approved indication wording cannot be quoted directly. However, the evidence supplied for this candidate is unusual among repurposing predictions: the reviewer-provided rationale notes that allergic urticaria is essentially not a *novel* indication for cetirizine but rather a **reconfirmation of an already well-established, guideline-endorsed use** of second-generation antihistamines (allergic and chronic urticaria).

Mechanistically, this is consistent — H1-receptor blockade is the accepted first-line pharmacological approach to histamine-mediated urticaria, and the same mechanism underlies the lower-ranked, related predictions in this pack (e.g., cold urticaria, angioedema), which show progressively weaker direct evidence as the disease mechanism moves further from classical histamine-driven pathology.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 | Completed | 36 | Multicentre pilot RCT of IV cetirizine 10 mg vs IV diphenhydramine 50 mg for acute urticaria in ED/urgent care settings; feasibility study directly testing cetirizine in this indication. |
| [NCT03296358](https://clinicaltrials.gov/study/NCT03296358) | N/A | Completed | 75 | Randomised, double-blind trial assessing whether adding a short corticosteroid burst to conventional H1-antihistamine treatment improves outcomes in urticaria; antihistamine background therapy, corticosteroid is the primary studied intervention. |
| [NCT01008592](https://clinicaltrials.gov/study/NCT01008592) | N/A | Terminated | 11 | Evaluated levocetirizine (the active enantiomer of cetirizine) effects on skin inflammatory mediators (histamine, proteases, PGE2, LTB4) in dermatographism and chronic idiopathic urticaria; trial terminated early, limiting evidentiary weight. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33030434](https://pubmed.ncbi.nlm.nih.gov/33030434/) | 2021 | Systematic Review | J Investig Allergol Clin Immunol | Systematic review of efficacy/safety of up-dosing second-generation antihistamines (up to 4x licensed dose) in chronic spontaneous urticaria when standard dosing fails. |
| [7645679](https://pubmed.ncbi.nlm.nih.gov/7645679/) | 1995 | Clinical trial review | Allergy | Review of clinical studies specifically evaluating cetirizine in allergic rhinitis and chronic urticaria. |
| [7510611](https://pubmed.ncbi.nlm.nih.gov/7510611/) | 1993 | Review | Drugs | Pharmacological reappraisal of cetirizine; reports it as effective and well-tolerated for seasonal/perennial allergic rhinitis and chronic idiopathic urticaria in adults. |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Review | Drugs | Reviews cetirizine's H1-receptor affinity, lack of CNS depressant effect at standard 10 mg dose, and inhibition of histamine release/eosinophil chemotaxis relevant to allergic urticaria. |
| [8477125](https://pubmed.ncbi.nlm.nih.gov/8477125/) | 1993 | Review | Ann Pharmacother | Introduces cetirizine as a nonsedating antihistamine, covering mechanism of action, clinical/comparative trial data, and adverse effects. |
| [9951950](https://pubmed.ncbi.nlm.nih.gov/9951950/) | 1999 | Review | Drugs | Comparative review of second-generation antihistamines (including cetirizine) evaluating features relevant to clinical choice. |
| [18201439](https://pubmed.ncbi.nlm.nih.gov/18201439/) | 2007 | Review | Allergy Asthma Proc | Reviews levocetirizine (cetirizine's active enantiomer) pharmacology, safety, and effectiveness in allergic rhinitis and chronic idiopathic urticaria. |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | Reviews efficacy and safety of oral antihistamines, including cetirizine, for allergic rhinitis and chronic idiopathic urticaria, with a pharmacy management focus. |
| [7530629](https://pubmed.ncbi.nlm.nih.gov/7530629/) | 1994 | Review | Drugs | Reviews recognition, causes and treatment of urticaria, noting nonsedating antihistamines as mainstay therapy. |
| [41602253](https://pubmed.ncbi.nlm.nih.gov/41602253/) | 2025 | Case Report | Cureus | Case report of rebound pruritus/urticaria following discontinuation of chronic cetirizine use in an Asian patient — relevant safety observation for long-term use. |

---

## Australia Market Information

No ARTG entries are recorded for this product in the currently available dataset (`taiwan_regulatory.total_licenses = 0`). Market status is reported as **not currently marketed** in this data source. This should be independently verified against the current TGA/ARTG register, as it directly affects Blocking Data Gap DG001 (TFDA/TGA product information).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug–drug interaction data are currently available in this evidence pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top-ranked prediction (allergic urticaria) is supported by L1-level evidence, including one completed Phase 3 trial directly testing cetirizine and a 2021 systematic review on antihistamine dosing in chronic urticaria. However, the underlying regulatory (TGA/ARTG) and mechanism-of-action data needed for a full safety evaluation are currently missing, so the recommendation stops short of an unconditional "Go."

**To proceed, the following is needed:**
- TGA-approved Product Information — warnings and contraindications (Blocking gap, DG001)
- Confirmed mechanism-of-action documentation from DrugBank or equivalent source (High priority gap, DG002)
- Verified current ARTG registration status and licensed indication wording for cetirizine in Australia
- Drug–drug interaction data (current query returned no results)
- Clinical evaluation of lower-ranked, mechanistically weaker candidates (cold urticaria, angioedema) only after the above gaps are closed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

