---
layout: default
title: Simvastatin
parent: 僅模型預測 (L5)
nav_order: 631
evidence_level: L5
indication_count: 10
---

# Simvastatin
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

Using the txgnn-pipeline skill is not applicable here — this is a direct report-writing task per the supplied prompt template, not a training/deployment task. Proceeding directly.

# Simvastatin: From Hypercholesterolaemia to Familial Hypercholesterolemia

## One-Sentence Summary

Simvastatin is an HMG-CoA reductase inhibitor (statin) originally used to treat hypercholesterolaemia/dyslipidaemia and reduce cardiovascular risk. The TxGNN model predicts it may be effective for **Familial Hypercholesterolemia (FH)**, with **19 clinical trials** and **18 publications** currently supporting this direction — though as detailed below, this largely reflects an already-established use of statins rather than a genuinely novel indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolaemia / dyslipidaemia (well-established statin indication; no ARTG-registered indication text is available in this evidence pack because the product is not currently marketed in Australia) |
| Predicted New Indication | Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

A structured DrugBank mechanism-of-action record was not returned for this evidence pack. Based on well-established pharmacological knowledge, simvastatin is an HMG-CoA reductase inhibitor: it blocks hepatic cholesterol biosynthesis and, as a compensatory response, upregulates hepatocyte LDL-receptor expression, increasing clearance of LDL-cholesterol from the circulation.

Familial hypercholesterolemia is caused by defective or reduced LDL-receptor function, leading to impaired clearance of circulating LDL-C from birth. Statins' core mechanism — upregulating the activity of residual, functional LDL receptors — maps directly onto FH's underlying pathophysiology rather than being an indirect or coincidental association.

In practice, simvastatin (alone or combined with ezetimibe) is already an internationally guideline-recommended cornerstone therapy for both heterozygous and homozygous FH, which is reflected in the unusually large volume of Phase 3 trial and Cochrane systematic-review evidence returned below. This should be interpreted as TxGNN correctly recovering an already-established clinical use of the drug, rather than surfacing a genuinely novel repurposing hypothesis — the "new" element for this evidence pack is the absence of a corresponding Australian ARTG registration/indication text, not the underlying pharmacology.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE trial: ezetimibe + high-dose simvastatin vs. simvastatin alone on carotid atherosclerosis progression in heterozygous FH — directly evaluates simvastatin as core intervention |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe 10mg added to atorvastatin or simvastatin in homozygous FH |
| [NCT01070966](https://clinicaltrials.gov/study/NCT01070966) | N/A | Completed | 2089 | Large post-marketing re-examination of VYTORIN (ezetimibe/simvastatin) safety and efficacy in routine practice |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | Completed | 248 | Ezetimibe + simvastatin efficacy/safety/tolerability in adolescents with heterozygous FH |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | Long-term (24-month) open-label safety/tolerability of ezetimibe added to atorvastatin or simvastatin in homozygous FH |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | Completed | 442 | Renal effects of rosuvastatin vs. simvastatin in Fredrickson Type IIa/IIb dyslipidaemia including heterozygous FH |
| [NCT01954394](https://clinicaltrials.gov/study/NCT01954394) | Phase 3 | Completed | 986 | Long-term open-label extension assessing alirocumab safety/efficacy added to lipid-lowering therapy (including statin background) in heterozygous FH |
| [NCT02107898](https://clinicaltrials.gov/study/NCT02107898) | Phase 3 | Completed | 216 | Alirocumab add-on to stable statin therapy vs. placebo in heterozygous FH/high CV-risk hypercholesterolemia |
| [NCT03510884](https://clinicaltrials.gov/study/NCT03510884) | Phase 3 | Completed | 153 | Alirocumab vs. placebo on top of optimal statin therapy in children/adolescents with heterozygous FH |
| [NCT00145574](https://clinicaltrials.gov/study/NCT00145574) | Phase 4 | Completed | 194 | Colesevelam added to stable statin monotherapy (including simvastatin) in pediatric heterozygous FH |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | RCT | New England Journal of Medicine | ENHANCE trial primary publication: simvastatin with or without ezetimibe in familial hypercholesterolemia |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Review (Cochrane) | Cochrane Database of Systematic Reviews | Systematic review of statins (including simvastatin) for children with FH |
| [28685504](https://pubmed.ncbi.nlm.nih.gov/28685504/) | 2017 | Review (Cochrane) | Cochrane Database of Systematic Reviews | Earlier version of the same Cochrane review on statins for children with FH |
| [10669649](https://pubmed.ncbi.nlm.nih.gov/10669649/) | 2000 | RCT | Arteriosclerosis, Thrombosis, and Vascular Biology | Stanol ester margarine alone and with simvastatin lowers cholesterol in FH-North Karelia families |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Review | Expert Opinion on Drug Safety | Benefits and risks assessment of simvastatin in familial hypercholesterolaemia |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Review | Drug Safety | Benefits and risks of simvastatin in patients with familial hypercholesterolaemia |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Cohort | Journal of the American College of Cardiology | Statin use in heterozygous FH associated with reduced coronary artery disease events and all-cause mortality |
| [2083515](https://pubmed.ncbi.nlm.nih.gov/2083515/) | 1990 | Review | Drugs | Review of simvastatin's pharmacological properties and therapeutic potential in hypercholesterolaemia |
| [32800790](https://pubmed.ncbi.nlm.nih.gov/32800790/) | 2020 | Case Report | Journal of Clinical Lipidology | Decade-long pharmacological management of a child with compound heterozygous severe FH |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | Cross-sectional Study | Journal of Clinical Medicine | Effects of simvastatin on innate and acquired cellular immunity in children with FH |

---

## Australia Market Information

Currently no ARTG entries are recorded for this product — the evidence pack indicates simvastatin (under this candidate) is **not currently marketed in Australia**, so no product/dosage-form/indication data is available to tabulate.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

*(Note: a formal DDI/warnings/contraindications lookup returned no data for this candidate. Separately, the evidence pack's literature review for the lower-ranked "HIV infectious disease" candidate flags known simvastatin–CYP3A4 interactions with HIV protease inhibitors and case reports of rhabdomyolysis (e.g. PMID 12240878, PMID 36409337) — relevant general statin safety context, though not part of this candidate's formal DDI dataset.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between statin pharmacology and FH pathophysiology is direct and well-established, and is supported by an unusually deep evidence base (19 trials, including multiple completed Phase 3 studies, plus two Cochrane systematic reviews). However, this candidate cannot proceed to full "Go" status because the drug has no current ARTG registration/marketing status in Australia and formal TGA PI safety data (warnings, contraindications) is missing (Blocking data gap DG001).

**To proceed, the following is needed:**
- TFDA/TGA-equivalent Product Information (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmation of Australian regulatory/marketing pathway, since `market_status` is "Not Marketed" and no ARTG entries exist
- Formal DrugBank mechanism-of-action record (DG002) to replace the literature-derived MOA summary used in this report
- Resolution of "pending" relevance grades on the remaining unclassified trials/literature in the evidence pack

**Other candidates not detailed above:** the pack contains 9 further TxGNN-predicted indications for simvastatin (e.g. "hypercholesterolemia, autosomal dominant" — effectively the same disease entity as FH, also L1/Proceed with Guardrails; "HIV infectious disease" — L4/Hold, evidence limited to pharmacokinetic drug-interaction studies rather than efficacy data). The remaining candidates (brain stem infarction, CETP deficiency, ABri amyloidosis, and others) are rated L4–L5 with a **Hold** recommendation due to absent or purely preclinical/model-only evidence, and are not pursued further in this report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

