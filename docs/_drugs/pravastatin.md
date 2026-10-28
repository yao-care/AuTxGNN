---
layout: default
title: Pravastatin
parent: Moderate Evidence (L3-L4)
nav_order: 596
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-28
monitor_inn: "Pravastatin"
predicted_indications: ["HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "hypoalphalipoproteinemia", "cholesterol-ester transfer protein deficiency"]
description: "Pravastatin: predicted new indication HIV infectious disease (evidence level L4). Approved use: Not recorded in the local data"
---

# Pravastatin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Pravastatin: HIV infectious disease
{: .text-alpha }

## One-Sentence Summary

Pravastatin is a statin (HMG-CoA reductase inhibitor) originally used for lipid disorders, atherosclerosis and stroke prevention.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolaemia**, with **1 registered clinical trial** (which tests a different drug, alirocumab) and **12 publications** that mostly cover other lipid-lowering agents or paediatric heterozygous disease, so direct evidence for pravastatin is very limited.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L4 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, pravastatin inhibits HMG-CoA reductase, reducing hepatic cholesterol synthesis and upregulating hepatic LDL receptors, which lowers LDL cholesterol.

Homozygous familial hypercholesterolaemia is a severe lipid disorder, so the link to pravastatin's original lipid-lowering indications is understandable. However, the mechanism also explains the main limitation: in this condition LDL receptor function is absent or severely reduced, so statin efficacy depends on residual receptor activity and is limited. One review in the data notes that statins are not very effective in homozygous disease.

The high model score therefore likely reflects network proximity within the lipid pathway rather than proven benefit. This is an extension of an existing lipid-lowering use rather than a truly novel repurposing.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label study of alirocumab in children and adolescents (8 to 17 years) with homozygous FH, measuring LDL-C change at Week 12. It does not test pravastatin; statins are at most background therapy, so this is indirect evidence. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28685504](https://pubmed.ncbi.nlm.nih.gov/28685504/) | 2017 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Statins for children with familial hypercholesterolaemia (mainly heterozygous disease) |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Updated review of statins in children with familial hypercholesterolaemia |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE guidelines for dyslipidaemia management and cardiovascular prevention |
| [15532136](https://pubmed.ncbi.nlm.nih.gov/15532136/) | 2004 | Commentary | Prescrire Int | Simvastatin and pravastatin are reference statins for heterozygous FH; statins are not very effective in homozygous FH |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | Review | Drugs | Rosuvastatin superior to pravastatin and other statins for lipid profile (not pravastatin-focused) |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clin Ther | Rosuvastatin indicated in homozygous FH (different drug) |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Review | Am J Cardiovasc Drugs | Ezetimibe, a cholesterol absorption inhibitor (different drug) |
| [14647533](https://pubmed.ncbi.nlm.nih.gov/14647533/) | 2003 | Review | Cardiovasc Drug Rev | Ezetimibe lipid-lowering and antiatherosclerotic activity (different drug) |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13432Y | Pravachol | Tablet containing pravastatin sodium 40 mg | Not available in the data compiled for this report |

## Safety Considerations

- **Conditions linked to contraindication in the knowledge graph** (not taken from label text): liver disease, kidney disease, myopathy and other muscle diseases, rhabdomyolysis, thrombocytopenia, gallbladder disease, peptic ulcer disease and gout, among others.
- **Drug Interactions** (100 interactions recorded; examples of moderate-level ones): metronidazole, clarithromycin, eluxadoline, naltrexone, pectin, rosuvastatin, simvastatin and tinidazole. Combining pravastatin with other statins is of particular note.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only registered trial tests alirocumab, not pravastatin, and the literature is mostly reviews of other lipid-lowering drugs or paediatric heterozygous FH studies. Because homozygous FH involves absent or severely reduced LDL receptor function, statin benefit is expected to be limited. The prediction is supported by model score and mechanism only.

**To proceed, the following is needed:**
- Pravastatin-specific clinical data in homozygous FH (for example, LDL-C response by residual LDL receptor activity)
- Comparison with established options for this condition and the role of pravastatin as add-on therapy
- Mechanism of action data and TGA Product Information warnings and contraindications for formal safety screening
- A decision on whether this use is better framed as an extension of the existing hyperlipidaemia indication than as new repurposing

*Note on other predictions:* the related predictions of heterozygous familial hypercholesterolaemia (evidence level L3, supported by paediatric pravastatin studies and Cochrane reviews) and HIV-associated dyslipidaemia (L3, small randomised studies plus interaction studies) have stronger evidence than the lead prediction. Both are closer to existing lipid-lowering use and may warrant separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

