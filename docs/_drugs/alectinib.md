---
layout: default
title: Alectinib
parent: 僅模型預測 (L5)
nav_order: 28
evidence_level: L5
indication_count: 10
---

# Alectinib
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

# Alectinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Alectinib is a second-generation, highly selective ALK (Anaplastic Lymphoma Kinase) tyrosine kinase inhibitor, with established global clinical use in ALK-positive non-small cell lung cancer (NSCLC), though it is not currently registered with the TGA in Australia.
The TxGNN model predicts it may be effective for **Gingival Fibromatosis (Fibromatosis, Gingival)**,
however, **no clinical trials or supporting publications** currently exist for this specific indication, and the biological rationale is assessed as **extremely low** — this prediction is most likely a knowledge graph artefact rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK-positive non-small cell lung cancer (NSCLC) |
| Predicted New Indication | Fibromatosis, Gingival (Gingival Fibromatosis) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed (0 ARTG entries) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this Evidence Pack. Based on published clinical pharmacology, Alectinib is a second-generation, ATP-competitive inhibitor of ALK, with additional activity against RET and ROS1 kinases. It works by blocking the constitutively active EML4-ALK fusion protein found in approximately 3–5% of NSCLC patients, preventing downstream tumour cell proliferation and survival signalling. Its clinical efficacy in ALK-positive NSCLC has been robustly established across multiple global Phase 3 trials (ALEX, J-ALEX, ALESIA) and is supported by a substantial body of peer-reviewed literature — though none of this evidence relates to the predicted indication assessed here.

Gingival fibromatosis (GF) is a rare, typically hereditary condition characterised by progressive fibrous overgrowth of gingival tissue. Its primary known genetic drivers are mutations in the **SOS1** gene (GINGF1 locus) and related hereditary loci, governing fibroblast proliferation through RAS pathway signalling. There is no established or proposed intersection between SOS1/GINGF-driven fibrotic pathology and the ALK/RET/ROS1 kinase axis that Alectinib targets.

The TxGNN model's high score for this indication most likely arises from indirect multi-hop connections within the biomedical knowledge graph — for example, pathways connecting "fibroproliferative lesion → kinase activation → ALK" — rather than any direct mechanistic relationship. The biological plausibility of applying an ALK inhibitor to a benign, non-kinase-driven, hereditary fibrotic condition is assessed as **extremely low**. This result is considered a probable false positive driven by graph topology rather than genuine pharmacological rationale, and should not be acted upon without substantial preclinical validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Alectinib in gingival fibromatosis.

---

## Literature Evidence

Currently no related literature available for Alectinib in gingival fibromatosis.

---

## Cytotoxicity

Alectinib is an antineoplastic agent indicated for the treatment of ALK-positive NSCLC; the following cytotoxicity assessment applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted Therapy — Second-generation ALK/RET/ROS1 tyrosine kinase inhibitor (not conventional cytotoxic) |
| Myelosuppression Risk | Low — haematological toxicities are uncommon; anaemia reported in Phase 3 trials at low frequency; not myelosuppressive in the traditional cytotoxic sense |
| Emetogenicity Classification | Low |
| Monitoring Items | Full blood count (FBC), liver function tests (LFTs), renal function, serum creatine phosphokinase (CPK/CK), blood pressure, resting heart rate (bradycardia risk), and ECG |
| Handling Protection | Standard oral targeted therapy precautions apply; cytotoxic handling procedures per institutional policy are recommended given the antineoplastic classification |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> **Important note for Australian clinicians:** Alectinib is **not currently registered with the TGA** in Australia (0 ARTG entries). Safety information should be sourced from international regulatory agency product information (e.g., FDA [Alecensa®] or EMA-approved PI), the DrugBank record (DB11363), or published Phase 3 trial safety data. Key adverse effects documented in published trials include: constipation, myalgia, peripheral oedema, elevated CPK, anaemia, elevated liver transaminases, bradycardia, and photosensitivity. Weight gain (up to ~10% of patients) has also been reported in real-world cohorts.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical, preclinical, or mechanistic evidence linking Alectinib to gingival fibromatosis. The condition is driven by SOS1/GINGF gene mutations affecting fibroblast proliferation — a pathway with no established relationship to ALK, RET, or ROS1 kinase signalling — making this TxGNN prediction a likely knowledge graph false positive with negligible translational value in its current form.

**To proceed, the following would be needed:**

- **Preclinical validation:** Demonstrate ALK pathway activity (e.g., ALK expression, phosphorylation, or rearrangement) in gingival fibromatosis cell lines or patient-derived tissue specimens
- **Molecular profiling:** Screen GF tissue for any incidental ALK/RET rearrangements that might create a targetable niche subpopulation
- **MOA data acquisition:** Retrieve full kinase inhibition and pharmacodynamic profile from DrugBank (DB11363) to identify any off-target mechanisms that could be relevant to fibrotic pathology
- **TGA registration pathway assessment:** If biological rationale is subsequently established, determine whether compassionate access, TGA Special Access Scheme (SAS), or a clinical trial pathway would be appropriate for Australian patients
- **Safety baseline:** Obtain full TGA-equivalent Product Information from FDA or EMA sources prior to any clinical consideration

---

> ⚠️ **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All TxGNN predictions are model-generated hypotheses and must be interpreted in the context of available biological and clinical evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

