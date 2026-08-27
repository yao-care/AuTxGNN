---
layout: default
title: Flucloxacillin
parent: 僅模型預測 (L5)
nav_order: 280
evidence_level: L5
indication_count: 10
---

# Flucloxacillin
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

# Flucloxacillin: From Staphylococcal Infections to Conjunctivitis

## One-Sentence Summary

Flucloxacillin is a narrow-spectrum, penicillinase-resistant penicillin conventionally used to treat infections caused by *Staphylococcus aureus* and other penicillinase-producing organisms. The TxGNN model predicts it may be effective for **conjunctivitis**, but this is supported by **0 clinical trials** and only **2 tangentially related publications**, neither of which demonstrates therapeutic benefit for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (no ARTG entries returned); internationally recognised as an antistaphylococcal penicillin |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed (per this evidence pack) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, flucloxacillin is a narrow-spectrum, penicillinase-resistant beta-lactam antibiotic in the penicillin class. Its efficacy against penicillinase-producing *Staphylococcus aureus* is well established, and mechanistically it could be applicable to bacterial conjunctivitis when *S. aureus* is the causative organism — this species is a recognised cause of bacterial conjunctivitis and blepharoconjunctivitis.

However, the two retrieved publications do not actually test this hypothesis. Both mention conjunctivitis only as an incidental symptom of unrelated conditions — one on staphylococcal scalded skin syndrome (where conjunctivitis appears as part of a prodrome, not as a treated endpoint), and one on atypical herpes simplex presentations with no abstract available. Neither evaluates flucloxacillin's efficacy against conjunctivitis. In addition, flucloxacillin is conventionally administered orally or intravenously for systemic infection, whereas conjunctivitis is typically managed with topical ophthalmic anti-infectives — raising a route-of-administration question this evidence pack does not resolve.

This caution is reinforced by the wider candidate set in this evidence pack: several other TxGNN-ranked candidates for flucloxacillin (e.g. rheumatoid arthritis, leprosy, thrombotic disease) were independently reviewed and flagged as likely infection-comorbidity confounds or embedding-level noise rather than genuine repurposing signals. All candidates in this pack sit at TxGNN ranks beyond 2,600, i.e. well outside the model's top predictions. Taken together, the conjunctivitis signal should be treated as a hypothesis-generating lead rather than an evidence-backed candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12627992](https://pubmed.ncbi.nlm.nih.gov/12627992/) | 2003 | Pending classification | American Journal of Clinical Dermatology | Describes staphylococcal scalded skin syndrome (SSSS); notes conjunctivitis can occur as part of the prodrome. Does not evaluate flucloxacillin efficacy for conjunctivitis itself. |
| [1286123](https://pubmed.ncbi.nlm.nih.gov/1286123/) | 1992 | Pending classification | International Journal of STD & AIDS | Abstract not available in this evidence pack. Title concerns atypical herpes simplex virus presentations; relevance to a flucloxacillin–conjunctivitis link is unclear from available data. |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. This evidence pack flags TGA warnings/contraindications data as a **blocking data gap** — without it, this candidate cannot proceed to safety pre-assessment (S1).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high in isolation, but the underlying rank (2,630) is far outside the model's top predictions, no clinical trials exist, and the only two literature hits mention conjunctivitis incidentally rather than as evidence of therapeutic effect. Mechanism of action, Australian market authorisation, and safety data are all unavailable, and the missing PI safety data is a blocking gap.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank API query)
- TGA Product Information — warnings, contraindications, DDI (blocking gap, DG001)
- Verification of ARTG/market status — 0 entries is worth re-confirming given flucloxacillin's well-established global availability
- Mechanistic or preclinical evidence specifically linking flucloxacillin to conjunctivitis (ideally isolating *S. aureus*-driven cases) rather than incidental symptom co-mention
- Clarification of intended route of administration, since systemic dosing does not match conventional topical treatment of conjunctivitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

