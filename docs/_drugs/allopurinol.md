---
layout: default
title: Allopurinol
parent: 僅模型預測 (L5)
nav_order: 32
evidence_level: L5
indication_count: 10
---

# Allopurinol
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

# Allopurinol: From Gout & Hyperuricaemia to Hepatic Porphyria

---

## One-Sentence Summary

Allopurinol is a well-established xanthine oxidase (XO) inhibitor widely used internationally to manage gout and hyperuricaemia, though no TGA-registered products were identified in this evidence pack.
The TxGNN model predicts it may have potential for **Hepatic Porphyria**, with **0 clinical trials** and **2 publications** currently supporting this direction.
The existing evidence is limited to a single hypothesis paper and one indirect animal study, placing this firmly at the research question stage rather than clinical translation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gout / Hyperuricaemia (established international use; no ARTG entries identified in this evidence pack — see note below) |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| Australia Market Status | Not Marketed (per data retrieved) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

> **Data quality note:** Allopurinol is understood to be available as a generic medicine in Australia. The absence of ARTG entries may reflect a data retrieval gap rather than true market absence. Manual verification via the TGA ARTG public portal is recommended before drawing conclusions about regulatory status.

---

## Why is This Prediction Reasonable?

Formal mechanism of action data was not retrieved in this evidence pack. Based on well-established pharmacology, Allopurinol and its active metabolite oxypurinol competitively inhibit xanthine oxidase (XO), the enzyme that converts hypoxanthine → xanthine → uric acid. This reduces uric acid synthesis and lowers serum urate levels. Beyond urate lowering, XO inhibition also curbs reactive oxygen species (ROS) generation, providing a secondary antioxidant effect that may be relevant to conditions involving hepatic oxidative stress.

The proposed link to hepatic porphyria rests on a specific metabolic hypothesis: Allopurinol may indirectly suppress hepatic 5-aminolevulinate synthase (ALAS), the rate-limiting enzyme of haem biosynthesis. In acute porphyrias, an inherited enzymatic deficiency causes over-induction of ALAS, resulting in toxic accumulation of porphyrin precursors (δ-aminolevulinic acid and porphobilinogen). A portion of hepatic haem is consumed by tryptophan 2,3-dioxygenase (TDO); if XO inhibition alters the hepatic haem regulatory pool, reduced haem utilisation by TDO could provide negative feedback on ALAS induction, thereby attenuating porphyrin precursor overproduction. PMID 31443750 advances this concept as a formal hypothesis and specifically notes XO inhibitor relevance. PMID 1567472 provides supportive mechanistic context via carbamazepine's haem metabolism effects in rat liver, though it is not a direct Allopurinol study.

It is critical to emphasise that this mechanistic chain remains entirely hypothetical. No clinical trials in hepatic porphyria have been conducted, and the evidence does not yet support clinical translation. The TxGNN high prediction score likely reflects the model's knowledge graph capturing shared metabolic pathway nodes (haem biosynthesis, oxidative stress) between Allopurinol and porphyria biology, rather than observed clinical efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothesis/Perspective | Medical Hypotheses | Proposes metabolic targeting of hepatic ALAS via inhibition of haem utilisation by tryptophan 2,3-dioxygenase (TDO) as therapy for acute hepatic porphyrias; notes that xanthine oxidase inhibitors may be relevant to ALAS suppression through modulation of the hepatic regulatory haem pool |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Animal Study (In Vivo) | Biochemical Pharmacology | Examines carbamazepine's acute effects on haem metabolism in rat liver using a validated screening model for porphyria exacerbation; demonstrates that drug-induced haem depletion potentiates ALAS induction — provides indirect mechanistic context for haem pathway manipulation, but is not a direct Allopurinol study |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for complete safety information, as formal safety data was not retrieved in this evidence pack.

**Important clinical alert (general knowledge):** Allopurinol is internationally recognised for a risk of severe cutaneous adverse reactions (SCARs), including Stevens-Johnson Syndrome (SJS) and toxic epidermal necrolysis (TEN). The HLA-B\*58:01 allele is a strong pharmacogenomic risk factor, with high carrier frequency in East Asian and South-East Asian populations (approximately 6–8% in Han Chinese). Australian prescribers should consider pharmacogenomic screening before initiating therapy in patients of relevant ancestry. This risk is particularly important if Allopurinol is being considered for a new indication in a population that may not have been screened.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN prediction score is very high (99.95%) and a plausible mechanistic hypothesis exists connecting Allopurinol's XO inhibition to ALAS suppression in hepatic porphyria, the current evidence base comprises only one hypothesis paper and one indirect animal study — no human clinical data, no dedicated preclinical porphyria studies, and no clinical trials. An L4 evidence level does not support progression to clinical use or trial design at this stage.

**To proceed, the following is needed:**

- **Preclinical validation:** Dedicated studies in established acute porphyria animal models (e.g., phenobarbital-induced AIP mouse model) measuring urinary ALA and porphobilinogen excretion following Allopurinol administration
- **Targeted literature review:** Systematic search for case reports, case series, or off-label use of Allopurinol in acute intermittent porphyria or related porphyrias
- **Formal MOA documentation:** Retrieve complete DrugBank pharmacology record including enzyme targets, carriers, and transporters relevant to haem metabolism
- **Full safety profile:** Download and parse the TGA-approved Product Information for Allopurinol; document all warnings, contraindications, and drug interactions (particularly interactions with azathioprine, mercaptopurine, and warfarin — interactions clinically relevant to porphyria management)
- **ARTG verification:** Manually confirm Australian market status via the TGA ARTG public search portal, as the evidence pack returned 0 entries (likely a data retrieval gap for this well-known generic)
- **Expert consultation:** Engage a clinical haematologist or porphyria specialist (e.g., through the Australian Porphyria Network) to assess biological plausibility and feasibility of a future proof-of-concept study

> *This report is intended for research purposes only and does not constitute medical advice. Any repurposing candidate requires prospective clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

