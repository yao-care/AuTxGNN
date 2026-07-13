---
layout: default
title: Interferon Beta-1B
parent: 僅模型預測 (L5)
nav_order: 268
evidence_level: L5
indication_count: 10
---

# Interferon Beta-1B
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

# Interferon Beta-1b: From Multiple Sclerosis to Hairy Cell Leukaemia

## One-Sentence Summary

Interferon beta-1b (IFN-β-1b) is a recombinant Type I interferon internationally established as a disease-modifying therapy for multiple sclerosis (MS), though it is not currently registered in Australia.
The TxGNN model predicts potential efficacy for **Hairy Cell Leukaemia (HCL)** with a prediction score of **99.16%**, supported by **0 registered clinical trials** and **5 publications** — predominantly early pilot clinical studies and case series from 1987–1990, conducted in the era before cladribine became the standard of care.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Australia; internationally approved for Multiple Sclerosis |
| Predicted New Indication | Hairy Cell Leukaemia |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this evidence pack. Based on established scientific knowledge, IFN-β-1b shares the same Type I interferon receptor complex (IFNAR1/IFNAR2) as IFN-α, activating the JAK1/TYK2 → STAT1/STAT2 → interferon-stimulated gene (ISG) signalling cascade. This pathway confers antiproliferative and pro-apoptotic effects on tumour cells. Critically, IFN-α was the historical standard of care for HCL prior to the introduction of purine analogues (cladribine, pentostatin) in the 1990s. Since IFN-β-1b operates through the same receptor system, it carries plausible mechanistic grounds for anti-HCL activity — the TxGNN model's high prediction score almost certainly reflects this shared receptor biology.

HCL is a B-cell malignancy characterised by the abnormal proliferation of hairy cells, and Type I interferons are well-established modulators of B-cell survival and differentiation. Early clinical series published between 1987 and 1990 demonstrated that recombinant beta-serine interferon (the same molecular form as IFN-β-1b) produced haematological responses in HCL patients, with response rates broadly comparable to IFN-α in direct comparison cohorts. Bone marrow clearance, however, was incomplete in all reported cases, foreshadowing the superiority of later purine analogue therapies.

It is essential to contextualise this prediction within the current treatment landscape. Modern HCL therapy with cladribine or pentostatin achieves durable complete remissions in over 90% of patients. IFN-β-1b in HCL would now be most relevant as a salvage option in patients who have exhausted purine analogue therapy, or as a historical reference point for understanding Type I interferon biology in HCL. Regulatory and access considerations in Australia — where neither IFN-β-1b nor IFN-α is registered for HCL — add a further practical constraint.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Interferon beta-1b in Hairy Cell Leukaemia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [3312839](https://pubmed.ncbi.nlm.nih.gov/3312839/) | 1987 | Retrospective Case Series | Leukaemia | UCLA experience with 51 HCL patients across IFN types; 71% of patients on recombinant beta-serine-IFN achieved haematological improvement; early response rates broadly comparable to IFN-α, establishing proof-of-concept for Type I IFN class activity |
| [2736487](https://pubmed.ncbi.nlm.nih.gov/2736487/) | 1989 | Prospective Comparative (non-randomised) | Cancer | 10 HCL patients treated with rIFN-β-ser (90 × 10⁶ units SC, 3×/week); 63% achieved normalisation of peripheral blood counts and a further 25% showed partial haematological improvement; all patients had persistent hairy cells in bone marrow at the time of reporting |
| [2082943](https://pubmed.ncbi.nlm.nih.gov/2082943/) | 1990 | Case Series / Pilot Clinical | American Journal of Haematology | 12 HCL patients (10 heavily pre-treated) received IV beta-ser IFN 90 MU 3×/week; demonstrated activity of IFN-β in patients with 90–100% bone marrow involvement, including prior-therapy failures |
| [1702309](https://pubmed.ncbi.nlm.nih.gov/1702309/) | 1990 | Translational / Biomarker | British Journal of Haematology | Monoclonal antibody panel used to monitor residual HCL disease in 20 patients treated with IFN-α or IFN-β; hairy cells retained characteristic immunophenotype (CD22, CD11c, CD25, CD32) despite treatment; methodology relevant to response assessment in future trials |
| [2198792](https://pubmed.ncbi.nlm.nih.gov/2198792/) | 1990 | Case Report | American Journal of Clinical Oncology | 3 HCL patients who failed alpha- or beta-IFN were rescued with 2'-deoxycoformycin (DCF); all achieved complete response; establishes the feasibility of sequential therapy after IFN-β failure and contextualises IFN-β's role as a bridging rather than definitive agent |

---

## Safety Considerations

Please refer to internationally available Product Information (PI) documents for safety information — for example, the US FDA label for Betaseron®/Extavia® or the EMA Summary of Product Characteristics for Betaferon®. Interferon beta-1b is not currently registered on the Australian Register of Therapeutic Goods (ARTG) and no Australian-specific PI is available. Key considerations known from international labelling include hepatotoxicity (AST/ALT elevation), depression and suicidal ideation, injection site reactions, and flu-like symptoms. Liver function monitoring is particularly relevant when considering use in HCL patients, who may already have hepatic involvement.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base for IFN-β-1b in HCL is entirely historical (1987–1990), derived from small uncontrolled case series conducted before modern effective therapies existed. Although biological plausibility is supported by shared IFNAR signalling with IFN-α (the former HCL standard of care), there is no registered clinical trial evidence, no Australian product registration, and no comparative data against cladribine or current second-line agents (vemurafenib, rituximab, moxetumomab pasudotox). This is appropriately classified as a research question rather than an actionable clinical recommendation.

**To proceed, the following is needed:**

- Retrieval of full DrugBank mechanism of action data (DrugBank DB00068) to formally document IFNAR binding affinity and downstream ISG pathway activity relative to IFN-α
- Safety assessment via international PI review (Betaseron®/Betaferon® prescribing information), with particular attention to hepatotoxicity and haematological monitoring requirements relevant to HCL patients
- Feasibility assessment of a defined clinical niche: for example, salvage therapy after cladribine and pentostatin failure, or use in patients with contraindications to purine analogues or BRAF-targeted therapy
- Comparative efficacy mapping against current second- and third-line HCL options (rituximab, vemurafenib for BRAF V600E-positive HCL, moxetumomab pasudotox)
- If clinical use is contemplated in Australia, assessment of access pathways: TGA Special Access Scheme Category B (SAS-B) or Authorised Prescriber designation, as no ARTG registration exists
- Assessment of whether the repurposing rationale warrants a formal investigator-initiated trial or systematic review of historical IFN-β HCL data in the context of modern response assessment criteria
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

