---
layout: default
title: Lanthanum Carbonate
parent: 僅模型預測 (L5)
nav_order: 384
evidence_level: L5
indication_count: 10
---

# Lanthanum Carbonate
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

# Lanthanum Carbonate: From Hyperphosphataemia (CKD) to Dyspepsia

## One-Sentence Summary

Lanthanum carbonate is a non-absorbed phosphate binder used to control **hyperphosphataemia in chronic kidney disease (CKD)** patients, particularly those on dialysis. The TxGNN model predicts it may be relevant to **Dyspepsia**, but the only supporting literature (4 publications, 0 clinical trials) describes dyspepsia and gastric lanthanum deposition as **adverse effects of the original indication**, not as a treatment target — meaning the evidence base points in the opposite direction to the prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperphosphataemia in chronic kidney disease (CKD) patients on dialysis *(based on known drug use; no TGA/ARTG licence text available — see Australia Market Information)* |
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 95.11% |
| Evidence Level | L4 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for lanthanum carbonate in this evidence pack. Based on known information, lanthanum carbonate is a non-calcium, non-absorbed phosphate binder that acts locally in the gastrointestinal tract to reduce phosphate absorption; its efficacy in hyperphosphataemia associated with CKD is well established and forms the basis of its approved use in other jurisdictions.

However, the relationship between the original indication and the predicted new indication (dyspepsia) is not supportive of a therapeutic link. All four available publications relate to the original CKD/hyperphosphataemia indication, and dyspepsia appears in this literature as a **symptom associated with drug exposure** — most notably a case report (PMID 30902374) describing lanthanum deposits found in gastric mucosa biopsied *because of* dyspepsia in a patient on long-term lanthanum carbonate therapy.

This suggests the TxGNN model's high score most likely reflects a drug–symptom **co-occurrence pattern typical of an adverse effect**, rather than a genuine treatment signal. In other words, the model may have picked up that lanthanum carbonate is associated with dyspepsia because it can *cause* it, not because it *treats* it. No mechanistic pathway supports a therapeutic effect of a phosphate binder on dyspepsia, and no clinical trials have tested this direction of use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34602015](https://pubmed.ncbi.nlm.nih.gov/34602015/) | 2021 | Meta-analysis/Review | Renal Failure | Meta-analysis of lanthanum carbonate vs. calcium salts/sevelamer/placebo for hyperphosphataemia in CKD; summarises safety and efficacy for the *original* indication only. |
| [21069570](https://pubmed.ncbi.nlm.nih.gov/21069570/) | 2012 | Cohort | International Urology and Nephrology | Observational study of lanthanum carbonate for serum phosphate control in difficult-to-control hyperphosphataemic dialysis patients; no mention of dyspepsia as a treatment outcome. |
| [20613851](https://pubmed.ncbi.nlm.nih.gov/20613851/) | 2010 | Cohort/Survey | Nefrología | Survey of haemodialysis patients' preferences among phosphate binders and impact on adherence/phosphorus control; not related to dyspepsia treatment. |
| [30902374](https://pubmed.ncbi.nlm.nih.gov/30902374/) | 2019 | Case Report | Revista Española de Patología | Case of a CKD patient on 3 years of lanthanum carbonate found to have lanthanum deposits in gastric mucosa, biopsied **due to dyspepsia** — indicates dyspepsia as a possible adverse effect, not a treatable target. |

---

## Australia Market Information

Lanthanum carbonate is **not currently marketed in Australia** and has no ARTG entries on record. No Australian Product Information is available to reference for approved indications, dosage forms, or brand names.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only available evidence for the dyspepsia prediction consists of literature describing the original CKD/hyperphosphataemia indication, where dyspepsia and gastric lanthanum deposition appear as **possible adverse effects of the drug rather than a treatment response**. There are no clinical trials, no ANZCTR/ICTRP registrations, and no mechanistic basis for a therapeutic effect on dyspepsia. Combined with the drug's non-marketed status in Australia and the missing MOA and TGA safety data, the evidence does not support progressing this candidate at this time.

**To proceed, the following is needed:**
- TGA-equivalent Product Information / warnings and contraindications (currently a blocking data gap, DG001)
- Confirmed mechanism of action data from DrugBank or primary literature (DG002)
- Clarification of directionality — targeted studies or case-control data assessing whether lanthanum carbonate causes or relieves dyspepsia
- Any dedicated clinical or preclinical study directly testing lanthanum carbonate in dyspepsia, rather than incidental mentions in CKD-focused literature

**Note on other predicted indications:** Ranks 2–10 (various otitis media–related conditions, otosalpingitis, pharyngitis) all carry Evidence Level L5 with zero clinical trials or literature support and no plausible mechanistic link to a phosphate binder's local GI action. These are assessed as likely knowledge-graph embedding artefacts rather than credible repurposing candidates and are not recommended for further review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

