---
layout: default
title: Iron Sucrose
parent: 僅模型預測 (L5)
nav_order: 275
evidence_level: L5
indication_count: 10
---

# Iron Sucrose
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

# Iron Sucrose: From Iron Deficiency Anaemia to Primary Hyperoxaluria

## One-Sentence Summary

Iron sucrose is an intravenous iron complex used to treat iron deficiency anaemia, particularly in patients with chronic kidney disease (CKD) on dialysis or peritoneal dialysis.
The TxGNN model predicts it may be effective for **Primary Hyperoxaluria**, however there are currently **0 clinical trials** and **0 publications** directly supporting this repurposing direction.
This prediction is based entirely on knowledge graph topology and should be interpreted with caution.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Iron deficiency anaemia in CKD/dialysis patients |
| Predicted New Indication | Primary Hyperoxaluria |
| TxGNN Prediction Score | 98.82% |
| Evidence Level | L5 |
| Australia Market Status | Not registered in Australia |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this evidence pack. Based on established pharmacological knowledge, iron sucrose (Venofer® and generics) is a polynuclear iron(III)-hydroxide complex stabilised with sucrose, administered intravenously. Its primary action is to replenish iron stores via uptake by the reticuloendothelial system — macrophages in the liver, spleen, and bone marrow — with subsequent controlled release to transferrin and erythropoietic precursors. Importantly, iron sucrose also transiently and markedly elevates intact serum FGF23 (fibroblast growth factor 23), which suppresses renal phosphate reabsorption and modulates the calcium–phosphate–PTH axis. This FGF23 effect is thought to underpin several of the TxGNN predictions in this candidate set.

Primary hyperoxaluria (PH) is a group of rare autosomal-recessive inborn errors of hepatic metabolism caused by mutations in *AGXT* (PH Type 1), *GRHPR* (PH Type 2), or *HOGA1* (PH Type 3). These mutations impair enzymes involved in glyoxylate detoxification, resulting in excessive hepatic oxalate production, massive urinary oxalate excretion, calcium oxalate crystal deposition in the kidneys and systemic organs, and ultimately renal failure and systemic oxalosis.

There is no established biological plausibility for iron sucrose in primary hyperoxaluria. Iron supplementation and FGF23 modulation — the known pharmacological actions of iron sucrose — have no known intersection with glyoxylate or oxalate biosynthetic pathways (AGXT, GRHPR, HOGA1 enzyme functions). The high TxGNN score (0.9882) most likely reflects a non-specific knowledge graph jump from the "chronic kidney disease – iron deficiency" node cluster to "primary hyperoxaluria" (which also causes renal failure), rather than a genuine mechanistic therapeutic link. This is a recognised limitation of graph-based repurposing models when rare renal diseases share node proximity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Iron sucrose is **not currently registered** with the Therapeutic Goods Administration (TGA) and has **no entries** in the Australian Register of Therapeutic Goods (ARTG). Healthcare professionals wishing to access iron sucrose for Australian patients would need to apply via the Special Access Scheme (SAS Category B or C) or the Authorised Prescriber pathway.

Internationally, iron sucrose products (e.g., Venofer®) are registered in the EU, UK, USA, and many Asia-Pacific markets for iron deficiency anaemia in CKD. Australian clinicians should refer to the relevant overseas Product Information and seek guidance from TGA's Access to Unapproved Therapeutic Goods team.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> **Clinical note for Australian practitioners:** Although no PI is currently available via TGA, iron sucrose is known internationally to carry risks of acute hypersensitivity reactions (including anaphylaxis), hypotension, and iron overload — particularly in patients with haemochromatosis or pre-existing iron excess. Intravenous iron preparations should only be administered where resuscitation facilities are immediately available. Detailed safety information can be obtained from the EMA-approved Venofer® Summary of Product Characteristics or the US FDA prescribing information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial evidence and no published literature supporting iron sucrose as a treatment for primary hyperoxaluria. The TxGNN prediction score of 98.82% reflects knowledge graph proximity between renal failure phenotypes rather than a mechanistically justified repurposing hypothesis — the drug's known actions (iron replacement, FGF23 elevation) have no plausible downstream effect on oxalate overproduction.

**To proceed, the following is needed:**

- Preclinical mechanistic studies investigating whether iron status, FGF23 signalling, or reactive oxygen species from iron infusion affect AGXT/GRHPR/HOGA1 enzyme activity or glyoxylate flux
- Structured literature review across oxalate metabolism and iron biology to identify any indirect pathway overlap
- Clinical pharmacologist and rare disease specialist consultation before any compassionate use consideration
- TGA Special Access Scheme application and ethics review if a pilot clinical assessment is deemed warranted
- Full safety workup specific to PH patients, who are often already in advanced renal impairment and may be at elevated risk from intravenous iron

---

> **Disclaimer:** This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require formal clinical validation before therapeutic application. All use must comply with applicable Australian regulations and institutional ethics requirements.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

