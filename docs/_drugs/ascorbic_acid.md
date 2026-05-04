---
layout: default
title: Ascorbic Acid
parent: 僅模型預測 (L5)
nav_order: 57
evidence_level: L5
indication_count: 10
---

# Ascorbic Acid
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

# Ascorbic Acid: From Vitamin C Deficiency to Non-Syndromic Esophageal Malformation

## One-Sentence Summary

Ascorbic acid (Vitamin C) is an essential water-soluble nutrient, globally recognised for the prevention and treatment of Vitamin C deficiency (scurvy) and as a nutritional supplement across a broad range of clinical settings.
The TxGNN model ranks **Non-Syndromic Esophageal Malformation** as its top predicted new indication with a score of 99.96%, however there are **no supporting clinical trials or published literature** for this specific indication, and the model's own rationale flags this prediction as likely arising from **knowledge graph topology bias** rather than a genuine therapeutic signal.
Clinicians reviewing this report should be aware that more evidence-supported TxGNN predictions exist for Ascorbic acid, particularly for **Vitamin Deficiency Disorder** (Rank 10, L1 evidence, Proceed with Guardrails) and **Injury** (Rank 4, L3 evidence), which represent far more actionable drug-repurposing opportunities.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formal ARTG registration identified; globally recognised for Vitamin C deficiency and scurvy prevention/treatment |
| Predicted New Indication | Non-Syndromic Esophageal Malformation |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ascorbic acid functions as an essential cofactor for prolyl and lysyl hydroxylase enzymes, which are required for collagen cross-linking and biosynthesis. This role in connective tissue formation theoretically places Ascorbic acid in pathways adjacent to structural development — including oesophageal tissue integrity. Additionally, Ascorbic acid is involved in collagen-dependent basement membrane assembly, which is required for normal organ morphogenesis during embryonic development.

However, non-syndromic oesophageal malformation is a congenital structural anomaly primarily driven by genetic and embryological factors, with causative variants reported in genes governing foregut patterning and tracheo-oesophageal separation. There is no established or proposed mechanism by which postnatal Ascorbic acid supplementation could prevent or correct such developmental defects. The evidence package explicitly acknowledges this disconnect and flags the TxGNN score of 0.9996 as **probable model bias** — the most likely cause being over-connectivity of pan-gastrointestinal anatomical nodes within the TxGNN knowledge graph, producing spuriously high-confidence predictions for structural and developmental conditions that share only anatomical neighbourhood with pharmacologically better-supported drug-disease relationships. This is a recognised limitation of graph topology-based prediction models.

It is important to note that several other TxGNN predictions for Ascorbic acid carry substantially stronger mechanistic and clinical support. **Vitamin Deficiency Disorder** (Rank 10, L1) is essentially the existing, well-validated indication — Ascorbic acid is the definitive treatment for scurvy. **Injury** (Rank 4, L3) is supported by multiple completed Phase 1–4 trials in burn, spinal cord injury, and critical care populations. **Perinatal Disease** (Rank 7, L2) is supported by several large Phase 3 RCTs in antenatal micronutrient supplementation. Clinicians should prioritise these findings when assessing the overall repurposing landscape for this drug.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ascorbic acid in Non-Syndromic Esophageal Malformation.

---

## Literature Evidence

Currently no related literature available for Ascorbic acid in Non-Syndromic Esophageal Malformation.

---

## Australia Market Information

Ascorbic acid is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)**. The TGA database search conducted on 9 March 2026 identified zero licence entries for this drug.

> **Note for clinicians:** Vitamin C formulations (tablets, powders, and injection solutions) may be available in Australia as listed complementary medicines, via compounding pharmacy, or through TGA-authorised importation pathways. Current availability and regulatory status should be verified directly at [www.tga.gov.au](https://www.tga.gov.au).

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Where an Australian PI is not available due to the absence of ARTG registration, clinicians should consult product labelling from comparable regulatory jurisdictions (e.g. US FDA, EMA) or the relevant DrugBank monograph (DB00126).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction for Non-Syndromic Esophageal Malformation has no clinical trial or published literature support whatsoever, and the model's own evidence package identifies the high TxGNN score (99.96%) as a probable artefact of gastrointestinal node over-connectivity in the knowledge graph. There is no plausible or established mechanistic pathway by which Ascorbic acid supplementation could treat or prevent a congenital oesophageal structural malformation. Pursuing this indication would not represent an appropriate use of research resources at this stage.

**To proceed with this specific indication, the following would be needed:**
- Independent validation that the TxGNN rank 1 prediction reflects a genuine biological signal rather than a graph topology artefact
- Identification of a plausible mechanistic hypothesis linking Ascorbic acid to prevention or correction of oesophageal structural malformation in humans
- At minimum, preclinical evidence (animal models or organoid studies) demonstrating a relevant morphogenetic effect

---

**Higher-priority predictions from the same TxGNN analysis that warrant separate evaluation:**

| Rank | Disease | Evidence Level | Recommendation | Key Supporting Evidence |
|------|---------|---------------|----------------|-------------------------|
| 10 | Vitamin Deficiency Disorder | **L1** | **Proceed with Guardrails** | RCTs confirming Ascorbic acid as definitive scurvy/hypovitaminosis C treatment; large observational study ([NCT02422901](https://clinicaltrials.gov/study/NCT02422901), n=5,000); PMID [37795755](https://pubmed.ncbi.nlm.nih.gov/37795755/); Australian paediatric scurvy case series PMID [39031615](https://pubmed.ncbi.nlm.nih.gov/39031615/) |
| 7 | Perinatal Disease | **L2** | Research Question | Phase 3 Bangladesh antenatal RCT ([NCT00860470](https://clinicaltrials.gov/study/NCT00860470), n=44,567); Guinea-Bissau Phase 1 RCT ([NCT00168688](https://clinicaltrials.gov/study/NCT00168688), n=2,100); preeclampsia Phase 1 trial ([NCT03451266](https://clinicaltrials.gov/study/NCT03451266), n=34) |
| 4 | Injury | **L3** | Research Question | Phase 3 burn trial VICToRY ([NCT04138394](https://clinicaltrials.gov/study/NCT04138394), n=666); Phase 1 burn micronutrient study ([NCT00879723](https://clinicaltrials.gov/study/NCT00879723), n=28); spinal cord injury Vitamin C + iron study ([NCT00881803](https://clinicaltrials.gov/study/NCT00881803), n=60); PMID [27852613](https://pubmed.ncbi.nlm.nih.gov/27852613/) RCT on collagen synthesis |
| 2 | Esophageal Disease | **L3** | Research Question | Linxian nutritional intervention trial ([NCT00342654](https://clinicaltrials.gov/study/NCT00342654), n=32,902); dose-response meta-analyses on dietary Vitamin C and oesophageal cancer risk (PMID [26355388](https://pubmed.ncbi.nlm.nih.gov/26355388/); PMID [35703897](https://pubmed.ncbi.nlm.nih.gov/35703897/)) — ⚠️ **Safety caveat:** animal studies (PMID [17953708](https://pubmed.ncbi.nlm.nih.gov/17953708/)) suggest potential pro-carcinogenic signal under acid reflux conditions with sodium nitrite co-exposure; dual-direction risk assessment required before clinical development |

> **Research note:** This report covers only the results for Ascorbic acid as currently registered in the Australian TGA database (no ARTG entries). Investigators wishing to pursue any of the above indications should first confirm the most appropriate regulatory pathway for Ascorbic acid formulation(s) in Australia, given the current absence of ARTG registration.

---

*⚠️ This report is intended for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

