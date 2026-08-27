---
layout: default
title: Pravastatin
parent: 僅模型預測 (L5)
nav_order: 554
evidence_level: L5
indication_count: 10
---

# Pravastatin
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

# Pravastatin: From Hypercholesterolaemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Pravastatin is a long-established HMG-CoA reductase inhibitor (statin) used to lower cholesterol and reduce cardiovascular risk. The TxGNN model predicts it may also have a role in **Homozygous Familial Hypercholesterolemia (HoFH)**, with **1 clinical trial** and **13 publications** currently identified — though, as detailed below, the trial evidence does not directly test pravastatin in this population and the underlying biology limits how much benefit can realistically be expected.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolaemia / dyslipidaemia (general statin-class use — no TGA-specific approved wording available in this dataset) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L3 |
| Australia Market Status | Not Marketed (per this dataset) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for pravastatin in this evidence pack. Based on known pharmacology, pravastatin is a member of the HMG-CoA reductase inhibitor (statin) class, and its cholesterol-lowering effect in general hypercholesterolaemia is well established. Mechanistically, statins reduce intracellular cholesterol synthesis, which up-regulates hepatic LDL-receptor expression and increases clearance of LDL cholesterol from the blood — the same pathway implicated in familial hypercholesterolaemia.

However, this mechanism is markedly attenuated in HoFH specifically. Patients with HoFH have little to no functional LDL receptor activity (due to biallelic LDLR, or related PCSK9/APOB, mutations), so the LDL-receptor up-regulation that statins rely on cannot produce a full effect. In clinical practice, statins are used only as **adjunctive** therapy in HoFH — alongside PCSK9 inhibitors, lomitapide, or LDL apheresis — rather than as a standalone effective treatment. The mechanistic link between pravastatin and HoFH is real, but its expected clinical effect is limited, and this should be clearly flagged to prescribers.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label study of **alirocumab** (not pravastatin) in children/adolescents with HoFH, evaluating LDL-C reduction at 12/24/48 weeks on top of background therapy. Pravastatin is not the study intervention — relevance is limited to population overlap (HoFH paediatric cohort). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Cochrane Systematic Review | Cochrane Database Syst Rev | Reviews statin use in children with familial hypercholesterolaemia, including homozygous cases; supports short/medium-term safety and LDL-C-lowering efficacy. |
| [28685504](https://pubmed.ncbi.nlm.nih.gov/28685504/) | 2017 | Systematic Review | Cochrane Database Syst Rev | Earlier version of the same Cochrane review on statins in paediatric familial hypercholesterolaemia. |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline (AACE/ACE) | Endocr Pract | US clinical practice guideline for dyslipidaemia management and cardiovascular disease prevention, covering statin therapy across FH severity. |
| [31358055](https://pubmed.ncbi.nlm.nih.gov/31358055/) | 2019 | Mechanistic (iPSC model) | Stem Cell Res Ther | LDL-receptor-deficient hepatocytes derived from iPSCs used to model FH and test CRISPR-based genetic correction — mechanistic, not a pravastatin efficacy study. |
| [34425670](https://pubmed.ncbi.nlm.nih.gov/34425670/) | 2021 | Genetic case study | Iran Biomed J | Identifies a novel LDLRAP1 splice-site variant causing familial hypercholesterolaemia in an affected family; genetics, not treatment. |
| [28416195](https://pubmed.ncbi.nlm.nih.gov/28416195/) | 2017 | RCT (INTREPID) | Lancet HIV | Phase 4 RCT comparing pitavastatin vs pravastatin in HIV-associated dyslipidaemia — direct pravastatin efficacy/safety data, but not in an HoFH population. |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clin Ther | Review of rosuvastatin, noting HoFH as an approved indication for that agent and comparing lipid-lowering potency across statins including pravastatin. |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | Review | Drugs | Review of rosuvastatin showing it outperformed pravastatin, atorvastatin and simvastatin on lipid parameters in hypercholesterolaemic patients. |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Review | Am J Cardiovasc Drugs | Review of ezetimibe as a cholesterol-absorption inhibitor, relevant as a comparator/add-on class in severe hypercholesterolaemia. |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Review of atorvastatin pharmacology and efficacy in hyperlipidaemia, used here as a general statin-class comparator. |

Three further hits (ezetimibe, atorvastatin general reviews, and PCSK9/CETP background literature) were lower relevance and are omitted for brevity.

---

## Australia Market Information

No ARTG entries are present in this dataset (`total_licenses: 0`, `market_status: 未上市`). No product name, dosage form, or approved indication text could be extracted. This does not necessarily reflect pravastatin's true Australian market status generally — it reflects a gap in the data source queried for this evidence pack and should be verified directly against the ARTG before any decision is finalised.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No key warnings, contraindications, or drug interaction data were retrievable in this evidence pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale for pravastatin in HoFH is biologically plausible but inherently limited — HoFH patients have minimal functional LDL receptor activity, so statins can only ever be adjunctive, not primary, therapy. No trial or publication in this evidence pack directly tests pravastatin's efficacy in HoFH; the strongest evidence (Cochrane reviews, AACE/ACE guideline) supports statins as a drug class in paediatric FH generally, not pravastatin specifically in the homozygous form.

**To proceed, the following is needed:**
- TFDA/TGA-equivalent Product Information (warnings, contraindications) — currently a **blocking** data gap preventing any safety pre-assessment (DG001)
- Confirmed mechanism of action data for pravastatin (DG002)
- Verification of actual ARTG listing status, as the "not marketed" flag in this dataset conflicts with pravastatin's well-known long-standing generic availability and should be checked directly
- A treatment-positioning statement clarifying that pravastatin would only be considered as an **adjunct** to PCSK9 inhibitors, lomitapide, or LDL apheresis in HoFH, not as monotherapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

