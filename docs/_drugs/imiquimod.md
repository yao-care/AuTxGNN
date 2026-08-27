---
layout: default
title: Imiquimod
parent: 僅模型預測 (L5)
nav_order: 346
evidence_level: L5
indication_count: 10
---

# Imiquimod
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

# Imiquimod: From Unregistered Status in Australia to a Candidate for Pre-Malignant Neoplasms

## One-Sentence Summary

Imiquimod is a topical toll-like receptor 7 (TLR7) agonist that is **not currently registered in Australia** (0 ARTG entries), so it has no locally approved indication on file.
The TxGNN model predicts it may be effective for **pre-malignant neoplasms** (e.g. actinic keratosis, cervical/vulvar intraepithelial neoplasia),
with **19 clinical trials** and **9 publications** currently identified as supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not applicable — no Australian registration on file (product not marketed here) |
| Predicted New Indication | Pre-malignant neoplasm |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L1 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action documentation was not retrievable from this evidence pack (DrugBank query returned no MOA text). Based on the evidence pack's mechanistic rationale, imiquimod is a **TLR7 agonist** that, when applied topically, induces local production of interferon-α, TNF-α and other cytokines, activating innate and adaptive immune responses that clear abnormally proliferating keratinocytes.

This mechanism is already the established basis for imiquimod's overseas use in **actinic keratosis** and **superficial basal cell carcinoma** — both premalignant/early-malignant epidermal lesions. The predicted indication, "pre-malignant neoplasm," largely captures HPV-driven intraepithelial lesions (cervical, vulvar and anal intraepithelial neoplasia, Bowenoid papulosis) that share the same underlying biology: localized abnormal epithelial proliferation accessible to a topically applied immune modulator.

In other words, this prediction is best understood as an **extension of an already-established mechanism and use pattern** to closely related premalignant epithelial/mucosal conditions, rather than a novel pharmacological hypothesis. The main gap for Australian practice is regulatory: imiquimod is not currently on the ARTG, so none of this overseas experience is yet reflected in a local Product Information (PI) document.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | Completed | 20 | Duration of effect of imiquimod 5% cream applied 3 days/week for actinic keratoses of the head |
| [NCT03233412](https://clinicaltrials.gov/study/NCT03233412) | Phase 2 | Completed | 90 | RCT of topical imiquimod for high-grade cervical intraepithelial lesions (CIN) |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Terminated | 9 | RCT of topical imiquimod vs. LLETZ for high-grade cervical intraepithelial neoplasia (CIN 2-3) |
| [NCT01720407](https://clinicaltrials.gov/study/NCT01720407) | Phase 3 | Completed | 259 | Neo-adjuvant imiquimod to reduce excision size/margins in lentigo maligna (premalignant melanocytic lesion) of the face |
| [NCT00941811](https://clinicaltrials.gov/study/NCT00941811) | Phase 2 | Completed | 5 | Immune mechanisms and efficacy of imiquimod for vulvar intraepithelial neoplasia (VIN 2/3) and anogenital warts |
| [NCT02242929](https://clinicaltrials.gov/study/NCT02242929) | Phase 3 | Unknown | 145 | Non-inferiority RCT: surgical excision vs. curettage + imiquimod for nodular basal cell carcinoma |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Phase 1 | Terminated | 49 | Comparison of 5% imiquimod, 0.05% imiquimod, and nanoencapsulated imiquimod gel for actinic cheilitis |
| [NCT01229319](https://clinicaltrials.gov/study/NCT01229319) | Phase 4 | Unknown | 20 | Imiquimod 3.75% cream after cryotherapy for hypertrophic actinic keratoses on hands/forearms |
| [NCT04883645](https://clinicaltrials.gov/study/NCT04883645) | Early Phase 1 | Completed | 16 | Neoadjuvant topical imiquimod (TLR7 agonist) in early-stage oral squamous cell carcinoma |

*Note: several additional trials in the evidence pack use imiquimod solely as a vaccine adjuvant in advanced/metastatic cancers (e.g. melanoma, glioma, lung, prostate) — these were excluded as not directly relevant to a pre-malignant-lesion indication.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Interventions, including imiquimod, for anal canal intraepithelial neoplasia (AIN), a premalignant HPV-associated condition |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Medical interventions, including imiquimod, for high-grade vulval intraepithelial neoplasia (VIN) |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | Int J Mol Sci | Combined treatments (incl. topical agents) for non-melanoma skin cancer |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Semin Cutan Med Surg | Topical treatment strategies, including imiquimod, for non-melanoma skin cancer and precursor lesions |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Review | Skin Therapy Lett | Current management of actinic keratoses, a premalignant cutaneous lesion |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclinical (PK/PD) | Urol Oncol | Pharmacokinetics of TLR7 agonists (imiquimod-related compounds) for premalignant/malignant urothelial lesions in a rat model |
| [18931984](https://pubmed.ncbi.nlm.nih.gov/18931984/) | 2008 | Imaging case study | Hautarzt | OCT imaging of actinic porokeratosis, including cases with coexisting actinic keratoses treated topically |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Case report | Int J STD AIDS | Successful treatment of high-grade vulval intraepithelial neoplasia with imiquimod 5% in a renal transplant recipient |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Case report | Int J STD AIDS | Bowenoid papulosis of the penis successfully treated with topical imiquimod 5% cream |

---

## Australia Market Information

Imiquimod currently has **no entries on the Australian Register of Therapeutic Goods (ARTG)** and is not marketed in Australia. No approved local Product Information exists to draw indication or dosage-form details from.

---

## Safety Considerations

No warnings, contraindications, or drug-interaction data were retrievable for this evidence pack, and imiquimod has no Australian-approved Product Information to reference (product not registered here). Prescribers/researchers should consult overseas regulatory PI (e.g. from jurisdictions where imiquimod is marketed) as an interim reference pending local registration.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link is strong and the supporting evidence includes multiple completed Phase 2/3 trials (AK, CIN, VIN, lentigo maligna) directly targeting premalignant epithelial/mucosal lesions, giving an L1 evidence level for this indication. However, imiquimod is not registered in Australia and safety/PI documentation is a **Blocking** data gap (DG001), so this cannot proceed without further regulatory groundwork.

**To proceed, the following is needed:**
- TGA-equivalent Product Information (warnings, contraindications) obtained from a jurisdiction where imiquimod is marketed (resolves DG001, Blocking)
- Confirmed detailed mechanism-of-action documentation from DrugBank (resolves DG002, High)
- Assessment of the regulatory pathway for ARTG registration, since the drug currently has zero Australian licences
- Clarification of which specific premalignant condition(s) (AK, CIN, VIN, AIN) to prioritise for a formal evidence review, as "pre-malignant neoplasm" spans several distinct clinical entities

*Note: This evidence pack also scored nine additional candidate indications for imiquimod (ranks 2–10), all rated L4–L5 evidence with a "Hold" recommendation (e.g. weak/indirect literature links, anatomically inaccessible sites for a topical drug, or likely knowledge-graph noise). These were not pursued further in this report.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

