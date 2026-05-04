---
layout: default
title: Atorvastatin
parent: 僅模型預測 (L5)
nav_order: 63
evidence_level: L5
indication_count: 10
---

# Atorvastatin
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

# Atorvastatin: From Primary Hypercholesterolemia to Familial Hypercholesterolemia

> **Disclaimer**: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.

---

## One-Sentence Summary

Atorvastatin is a synthetic HMG-CoA reductase inhibitor (statin) used globally as a cornerstone treatment for primary hypercholesterolemia and cardiovascular risk reduction, though no TGA ARTG registration data was retrieved in this analysis cycle.
The TxGNN model predicts it may be effective for **familial hypercholesterolemia (FH)** — the genetically-driven form of severely elevated LDL cholesterol — reflecting mechanistic alignment with the drug's core pharmacology.
This prediction is backed by **34 clinical trials** and **19 publications**, representing one of the strongest evidence bases of any indication in this analysis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not retrieved from ARTG (globally registered for primary hypercholesterolemia and mixed dyslipidaemia — see note below) |
| Predicted New Indication | Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed (⚠️ likely data retrieval gap — see Australia Market Information section) |
| Number of ARTG Entries | 0 (⚠️ verification required) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Atorvastatin competitively inhibits HMG-CoA reductase, the rate-limiting enzyme in hepatic cholesterol biosynthesis. By reducing endogenous cholesterol production, the liver compensatorily upregulates LDL receptor expression, accelerating clearance of circulating LDL-C from the bloodstream. This direct, well-characterised mechanism has made atorvastatin the most widely prescribed statin globally for over two decades, with dose-dependent reductions in total cholesterol, LDL-C, and triglycerides across a broad population.

Familial hypercholesterolemia is defined by inherited loss-of-function variants in the *LDLR*, *APOB*, or gain-of-function variants in *PCSK9*, all of which impair LDL clearance and drive severely elevated LDL-C from birth. Heterozygous FH (HeFH) patients — who retain partial LDL receptor function — typically achieve 40–50% LDL-C reduction with maximally tolerated atorvastatin doses and constitute the primary responder group. Homozygous FH (HoFH) patients, with near-absent receptor function, have attenuated statin response and generally require combination therapy (ezetimibe, PCSK9 inhibitors, lomitapide, or LDL apheresis). International guidelines (ESC/EAS, AACE/ACE) universally recommend high-intensity statins as first-line pharmacotherapy for both FH subtypes.

The TxGNN prediction score of 99.42% reflects the knowledge graph's high-confidence linkage between atorvastatin's pharmacological targets (HMGCR, LDL receptor pathway) and the molecular drivers of FH. Rather than representing a novel repurposing discovery, this result validates atorvastatin's established clinical role within a genetically-defined patient subgroup — an important distinction for regulatory and reimbursement pathways in the Australian context.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00136981](https://clinicaltrials.gov/study/NCT00136981) | Phase 3 | Completed | 800 | 24-month double-blind RCT comparing torcetrapib/atorvastatin vs atorvastatin alone in HeFH patients; used carotid intima-media thickness as primary atherosclerosis endpoint — largest direct atorvastatin RCT in FH |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe co-administered with atorvastatin or simvastatin in HoFH; established the evidence base for standard dual-agent combination therapy in the most severe FH subtype |
| [NCT02107898](https://clinicaltrials.gov/study/NCT02107898) | Phase 3 | Completed | 216 | Double-blind RCT of alirocumab vs placebo added to stable statin (including atorvastatin) in HeFH or high-CVR patients; demonstrated significant LDL-C reduction at 24 weeks |
| [NCT01623115](https://clinicaltrials.gov/study/NCT01623115) | Phase 3 | Completed | 486 | Double-blind RCT of alirocumab vs placebo on background atorvastatin in HeFH patients with LDL-C ≥160 mg/dL; supports atorvastatin as the backbone of combination lipid-lowering in FH |
| [NCT01507831](https://clinicaltrials.gov/study/NCT01507831) | Phase 3 | Completed | 2,341 | Long-term safety of alirocumab in high-CVR patients on lipid-modifying therapy including atorvastatin; the largest enrolment trial in this evidence set, providing robust safety and efficacy data |
| [NCT00827606](https://clinicaltrials.gov/study/NCT00827606) | Phase 3 | Completed | 272 | Three-year prospective open-label study of atorvastatin in children and adolescents (aged 6–17) with HeFH; characterised growth and development alongside LDL-C reduction over an extended paediatric timeframe |
| [NCT01730040](https://clinicaltrials.gov/study/NCT01730040) | Phase 3 | Completed | 355 | Four-arm double-blind RCT comparing alirocumab add-on vs ezetimibe add-on vs atorvastatin dose increase vs switch to rosuvastatin in patients uncontrolled on atorvastatin; informs optimal treatment escalation strategy in HeFH |
| [NCT03882996](https://clinicaltrials.gov/study/NCT03882996) | Phase 3 | Completed | 432 | Long-term (up to 12 months) safety and tolerability of ezetimibe added to atorvastatin 10–80 mg in HeFH or CHD patients not controlled on atorvastatin monotherapy |
| [NCT00145574](https://clinicaltrials.gov/study/NCT00145574) | Phase 4 | Completed | 194 | RCT of colesevelam vs placebo in paediatric HeFH patients (aged 10–17) on stable statin monotherapy including atorvastatin; demonstrated additive LDL-C lowering with triple therapy |
| [NCT06686615](https://clinicaltrials.gov/study/NCT06686615) | N/A | Recruiting | 2,000 | Large-scale observational study of bempedoic acid + ezetimibe + atorvastatin or rosuvastatin in primary hypercholesterolaemia or mixed dyslipidaemia; will provide real-world combination effectiveness data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11058703](https://pubmed.ncbi.nlm.nih.gov/11058703/) | 2000 | Clinical Trial | Atherosclerosis | Atorvastatin at escalating doses (10–40 mg/day) evaluated in 9 HoFH patients on LDL apheresis; 5 of 9 responded well, with significant LDL-C and apolipoprotein B reduction — key early evidence in the most severe FH subtype |
| [9793596](https://pubmed.ncbi.nlm.nih.gov/9793596/) | 1998 | Clinical Trial Review | Annals of Pharmacotherapy | Comprehensive early review of atorvastatin efficacy and safety across dyslipidemias; established dose-response relationships and positioned atorvastatin as the highest-potency statin for LDL-C reduction at launch |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Review | Current Atherosclerosis Reports | Up-to-date review of novel pharmacological therapies for HoFH; contextualises statins including atorvastatin alongside PCSK9 inhibitors, inclisiran, evinacumab and LDL apheresis in contemporary treatment algorithms |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Clinical Guideline | Endocrine Practice | AACE/ACE dyslipidaemia and cardiovascular prevention guidelines; endorses high-intensity statins as first-line in FH with LDL-C targets stratified by cardiovascular risk category |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Cohort Analysis | Journal of the American College of Cardiology | Quantified statin-induced reduction in coronary artery disease events and all-cause mortality in a large HeFH cohort; first robust real-world estimate of clinical event benefit from statins in FH |
| [27678432](https://pubmed.ncbi.nlm.nih.gov/27678432/) | 2016 | Prospective Cohort | Journal of Clinical Lipidology | Three-year efficacy and safety of atorvastatin in children aged 6–17 with HeFH; confirmed sustained LDL-C reduction without adverse effects on growth, pubertal development or hepatic safety |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Foundational pharmacology review of atorvastatin; describes HMG-CoA reductase inhibition mechanism, prolonged half-life of active metabolites, and dose-dependent lipid effects relevant to FH dosing |
| [26988948](https://pubmed.ncbi.nlm.nih.gov/26988948/) | 2016 | Review | Journal of the American College of Cardiology | Expert commentary on improving monitoring and care in FH patients; highlights under-diagnosis, under-treatment, and the critical role of statins as the therapeutic cornerstone |
| [35361995](https://pubmed.ncbi.nlm.nih.gov/35361995/) | 2022 | Genomic Study | The Pharmacogenomics Journal | Novel NGS approach combining FH gene panel with pharmacogenomic statin response markers; demonstrates clinical utility of genotype-guided atorvastatin dosing in FH patients |
| [32800790](https://pubmed.ncbi.nlm.nih.gov/32800790/) | 2020 | Case Report | Journal of Clinical Lipidology | Decade-long management of a child with compound heterozygous FH (presenting LDL-C 17.4 mmol/L); illustrates the evolution from bile acid sequestrants through atorvastatin combination therapy to PCSK9 inhibitors |

---

## Australia Market Information

> ⚠️ **Data Retrieval Alert**: This analysis returned **0 ARTG entries** for atorvastatin. This is inconsistent with atorvastatin's well-established global availability — it is widely marketed as Lipitor® (Pfizer) and multiple generic formulations and has been available in Australia for many years. This almost certainly reflects an incomplete data extraction rather than genuine absence from the Australian market.

| Item | Detail |
|------|--------|
| ARTG Entries Retrieved | 0 (data extraction incomplete) |
| Expected Market Status | Marketed — Lipitor® (brand) and multiple TGA-registered generics |
| PBS Listing | Atorvastatin is listed on the PBS for hypercholesterolaemia and mixed dyslipidaemia (verification recommended for specific FH PBS criteria) |
| Action Required | Verify current ARTG entries via [TGA ARTG Search](https://www.tga.gov.au/resources/artg) and PBS Schedule for funded indications |

Healthcare professionals should confirm ARTG numbers, approved indications and PBS subsidisation criteria — particularly whether FH as a specific genetic diagnosis carries distinct PBS eligibility requirements — directly through the TGA and Services Australia before clinical or prescribing decisions.

---

## Safety Considerations

Detailed TGA-specific safety data (Product Information warnings and contraindications) was not retrieved in this analysis cycle.

Please refer to the **TGA-approved Product Information (PI)** for atorvastatin for complete safety information. Key safety areas to review include:

- **Musculoskeletal toxicity**: Myopathy and rhabdomyolysis risk, particularly when combined with CYP3A4 inhibitors or other myotoxic agents
- **Hepatotoxicity**: Baseline and periodic liver function monitoring requirements
- **Pregnancy and lactation**: Atorvastatin is contraindicated in pregnancy (Pregnancy Category D in Australia) and breastfeeding
- **Drug–drug interactions**: Atorvastatin is a CYP3A4 substrate — significant interactions include azole antifungals, macrolide antibiotics, HIV protease inhibitors (ritonavir, lopinavir), and colchicine; these interactions are particularly relevant if atorvastatin is considered as adjunct therapy in HIV patients (see Rank 2 predicted indication)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Atorvastatin has an exceptionally strong evidence base for familial hypercholesterolemia, including multiple completed Phase 3 RCTs with thousands of participants, endorsement as first-line therapy in all major international dyslipidaemia guidelines, and a direct mechanistic link to the genetic pathophysiology of FH. The L1 evidence classification is well-justified. The primary barriers to a straightforward "Go" decision in the Australian context are the unresolved TGA ARTG data retrieval issue and the absence of formal MOA documentation in this evidence pack.

**To proceed, the following is needed:**

- **ARTG verification (Priority: Blocking)**: Manually search the TGA ARTG database to confirm current registration status, approved indications, and listed dosage forms for atorvastatin in Australia; resolve the data retrieval failure
- **PBS criteria review**: Confirm whether FH as a specific genetic or clinically-diagnosed condition carries distinct PBS subsidisation criteria beyond general hypercholesterolaemia — this affects access and cost for Australian patients
- **MOA formal documentation**: Retrieve and record atorvastatin's mechanism of action from DrugBank API (DB01076) to complete the evidence package — the mechanistic link to FH is clinically well-understood but must be formally captured for the repurposing dossier
- **FH subtype stratification**: Specify the target patient population — HeFH (strong evidence, atorvastatin monotherapy often adequate at maximally tolerated doses) vs HoFH (evidence supports use but response is limited by residual LDL receptor function; combination therapy with ezetimibe and/or PCSK9 inhibitors is standard of care)
- **TGA PI safety extraction**: Download and parse the TGA-approved Product Information PDF to populate the safety data fields (warnings, contraindications, interactions) currently flagged as data gaps
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

