---
layout: default
title: Fluvastatin
parent: Model Prediction Only (L5)
nav_order: 312
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Fluvastatin: predicted new indication Hyperlipoproteinaemia (evidence level L5). Approved use: Atherosclerosis and hyperlipidaemia (familial combined hyperlipidaemi…"
monitor_inn: "Fluvastatin"
predicted_indications: ["hyperlipoproteinemia", "HIV infectious disease", "cholesterol-ester transfer protein deficiency", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "fibroma of prostate"]
---

# Fluvastatin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Fluvastatin: From Atherosclerosis and Hyperlipidaemia to Hyperlipoproteinaemia

## One-Sentence Summary

Fluvastatin is an HMG-CoA reductase inhibitor (statin) originally used for atherosclerosis and familial combined hyperlipidaemia.
The TxGNN model predicts it may be effective for **hyperlipoproteinaemia** (score 99.99%), but this is essentially a lipid-lowering use close to its existing indications rather than a true repurposing.
Support is solid: **1 registered trial** was retrieved for this prediction (an alirocumab study with no direct bearing on fluvastatin) and **20 publications** were retrieved, including 2 RCTs of fluvastatin.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atherosclerosis and hyperlipidaemia (familial combined hyperlipidaemia). The Australian ARTG entry carries no indication text, so this is based on the knowledge-graph indications. |
| Predicted New Indication | Hyperlipoproteinaemia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (as assigned in the compiled data; see the note under Clinical Trial Evidence) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on established pharmacology, fluvastatin inhibits HMG-CoA reductase, which lowers hepatic cholesterol synthesis and upregulates LDL receptors, reducing circulating LDL cholesterol.

Hyperlipoproteinaemia is the same underlying problem as its original indications (hyperlipidaemia and atherosclerosis). The mechanism applies directly, so the prediction is best viewed as an on-label or near-label use. Fluvastatin-specific studies cover elderly patients, Chinese patients, familial hypercholesterolaemia, combination with bezafibrate, extended-release versus immediate-release formulations, and paediatric use.

Other predictions in the same output, in brief:
- **Familial hypercholesterolaemia (rank 4):** Strongest direct evidence, including a completed Phase 3 fluvastatin paediatric trial (NCT00171236, n=84). Also Proceed with Guardrails.
- **Homozygous familial hypercholesterolaemia (rank 2):** Little or no functional LDL receptor activity is expected to limit statin response, and there is no fluvastatin-specific evidence. A research question only.
- **HIV infection (rank 5):** Studies concern antiretroviral-associated dyslipidaemia, not antiviral activity. A research question only.
- **Ranks 3 and 6 to 10** (including CETP deficiency, 7alpha-hydroxylase deficiency, and veterinary or animal-model viral conditions): prediction only with no supporting evidence. Hold.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Alirocumab (a PCSK9 inhibitor) in children and adolescents with homozygous familial hypercholesterolaemia. Does not test fluvastatin, so it gives no direct evidence. |

For the closely related prediction of heterozygous **familial hypercholesterolaemia**, a directly relevant trial exists: [NCT00171236](https://clinicaltrials.gov/study/NCT00171236) (Phase 3, completed, n=84), assessing fluvastatin safety and efficacy in children with heterozygous familial hypercholesterolaemia.

No ANZCTR trials were identified in the data compiled.

**Note on evidence level:** The L1 grade for hyperlipoproteinaemia rests mainly on the fluvastatin RCTs in the literature below, not on the registered trial listed above.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11219479](https://pubmed.ncbi.nlm.nih.gov/11219479/) | 2001 | RCT | Clin Ther | Compared fluvastatin 80 mg extended-release with immediate-release formulations in primary hypercholesterolaemia (the formulation held on the ARTG). |
| [17062478](https://pubmed.ncbi.nlm.nih.gov/17062478/) | 2006 | RCT | Acta Paediatr | Fluvastatin in children and adolescents with heterozygous familial hypercholesterolaemia: lipid profile and vascular effects. |
| [10856536](https://pubmed.ncbi.nlm.nih.gov/10856536/) | 2000 | Clinical trial | Atherosclerosis | FACT study: fluvastatin plus bezafibrate in 333 patients with coronary artery disease and mixed hyperlipidaemia (double-blind). |
| [15598476](https://pubmed.ncbi.nlm.nih.gov/15598476/) | 2004 | Randomised, double-blind trial | Clin Ther | 12-month comparison of fluvastatin plus fenofibrate versus fluvastatin alone in combined hyperlipidaemia, type 2 diabetes and coronary heart disease. |
| [8157036](https://pubmed.ncbi.nlm.nih.gov/8157036/) | 1993 | Clinical trial | Eur J Clin Pharmacol | High-dose fluvastatin in 52 patients with familial hypercholesterolaemia (double-blind). |
| [7517835](https://pubmed.ncbi.nlm.nih.gov/7517835/) | 1994 | Clinical trial | Drugs | Efficacy and safety of fluvastatin 40 mg in elderly women with hypercholesterolaemia (n=22). |
| [7604789](https://pubmed.ncbi.nlm.nih.gov/7604789/) | 1995 | Clinical trial | Am J Cardiol | Effects of fluvastatin on lipids and apolipoproteins in 31 Chinese patients with hypercholesterolaemia. |
| [10067240](https://pubmed.ncbi.nlm.nih.gov/10067240/) | 1998 | Clinical study | Ter Arkh | Variability of lipid-lowering response to simvastatin and fluvastatin in primary hyperlipoproteinaemia. |
| [8462180](https://pubmed.ncbi.nlm.nih.gov/8462180/) | 1993 | Review | Circulation | Overview of drug treatment of dyslipoproteinaemia, focusing on fluvastatin. |
| [11347136](https://pubmed.ncbi.nlm.nih.gov/11347136/) | 2001 | Review | Nihon Rinsho | Review of fluvastatin. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 13558N | Lescol XL | Tablet (prolonged release) 80 mg (as sodium) | Not stated in the data compiled |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** liver disease, gallbladder disease, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, hypotensive disorder, substance abuse/dependence, rhabdomyolysis, nodular fasciitis, injury.
- **Drug interactions:** 100 potential interactions were identified. Moderate-level examples include aprepitant, metronidazole, oxandrolone, naltrexone, nateglinide, nitisinone, rosuvastatin, simvastatin (additive statin exposure and myopathy risk), tinidazole, glyburide and pectin. Several others (for example calcitriol, doxycycline, cimetidine, famotidine, pantoprazole and acetylsalicylic acid) have an unclassified interaction level. Fluvastatin is a CYP2C9 substrate.

For label warnings and contraindications, please refer to the TGA-approved Product Information (PI).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Hyperlipoproteinaemia shares its mechanism with fluvastatin's established lipid-lowering use, and several fluvastatin-specific randomised and controlled studies support efficacy. The evidence comes mainly from older literature, and no fluvastatin-specific trial was retrieved for this exact prediction. The Australian ARTG entry carries no indication text, and the safety data are incomplete.

**To proceed, the following is needed:**
- The TGA-approved Product Information, to confirm the registered indication, warnings and contraindications (label data were unavailable)
- Confirmation of the mechanism of action from DrugBank
- A medication review for interaction risk, especially CYP2C9 inhibitors and co-prescribed statins, fibrates and antivirals
- Monitoring of liver function and muscle symptoms, with extra care in paediatric and elderly patients
- Confirmation that the predicted use falls within, or close to, the existing registered lipid-lowering indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

