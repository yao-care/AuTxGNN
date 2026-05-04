---
layout: default
title: Ezetimibe
parent: 僅模型預測 (L5)
nav_order: 213
evidence_level: L5
indication_count: 10
---

# Ezetimibe
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

# Ezetimibe: From Hypercholesterolaemia to Hyperlipoproteinemia

## One-Sentence Summary

Ezetimibe is a well-established selective cholesterol absorption inhibitor approved globally for hypercholesterolaemia, though no TGA/ARTG-registered products were retrieved in this evidence pack.
The TxGNN model predicts it may be effective for **Hyperlipoproteinemia** with a score of **99.63%**, supported by **50 registered clinical trials** (including multiple completed Phase 3 RCTs) and **19 publications**.
Evidence is rated at **L1** — the highest level — reflecting robust, Phase 3 RCT-quality data directly relevant to the predicted indication.

> **Data Note:** No TGA/ARTG-registered products for ezetimibe were returned in this query (market status: not marketed, 0 ARTG entries). This is likely a data retrieval limitation. Verification against the current [TGA ARTG database](https://www.tga.gov.au/resources/artg) is recommended before drawing any regulatory conclusions.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from TGA/ARTG records (potential data gap) |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 (multiple completed Phase 3 RCTs) |
| Australia Market Status | Not marketed (0 ARTG entries found — verify against current TGA records) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ezetimibe exerts its lipid-lowering effect by selectively inhibiting the Niemann-Pick C1-Like 1 (NPC1L1) protein located on intestinal epithelial brush border cells. NPC1L1 is the primary transporter responsible for absorbing both dietary and biliary cholesterol from the gut lumen. By blocking this transporter, ezetimibe reduces hepatic cholesterol delivery, which in turn upregulates LDL receptor (LDLR) expression and enhances LDL-C clearance from plasma — typically achieving a 15–20% reduction in LDL-C as monotherapy. When combined with a statin (which inhibits hepatic cholesterol synthesis via HMG-CoA reductase), the two complementary mechanisms produce additive LDL-C reductions of 50–60%, making ezetimibe a clinically important combination partner.

Hyperlipoproteinemia is characterised by pathologically elevated plasma lipoprotein concentrations — particularly LDL — driving accelerated atherosclerosis and premature cardiovascular disease. This condition shares the same core pharmacological target as the indications for which ezetimibe is globally established: excess circulating LDL-C arising from increased intestinal absorption, impaired receptor-mediated clearance, or combined causes. The NPC1L1 inhibition mechanism directly reduces the intestinal contribution to cholesterol burden and is relevant regardless of the specific aetiology of the hyperlipoproteinaemia (dietary, polygenic, or monogenic).

This TxGNN prediction is strongly corroborated by multiple completed Phase 3 RCTs, including large multicentre studies enrolling over 1,000 participants, and aligns with current international guidelines from the European Atherosclerosis Society (EAS), American College of Cardiology (ACC), and American Heart Association (AHA). Ezetimibe is currently positioned as a first-line adjunct to statins — or as an alternative for statin-intolerant patients — across multiple hyperlipoproteinaemia subtypes including primary hypercholesterolaemia, mixed dyslipidaemia, and familial hypercholesterolaemia.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00271817](https://clinicaltrials.gov/study/NCT00271817) | Phase 3 | Completed | 1,220 | Multicentre, double-blind RCT evaluating efficacy and safety of ezetimibe/simvastatin co-administered with niacin extended-release in patients with Type IIa or IIb hyperlipidaemia; core Phase 3 registration-quality evidence for ezetimibe in hyperlipoproteinaemia |
| [NCT01043380](https://clinicaltrials.gov/study/NCT01043380) | Phase 4 | Completed | 245 | PRECISE-IVUS: compared coronary plaque regression between ezetimibe (cholesterol absorption inhibitor) and statin (synthesis inhibitor) using intravascular ultrasound (IVUS); demonstrated cardiovascular endpoint benefits supporting the role of cholesterol absorption inhibition |
| [NCT00651560](https://clinicaltrials.gov/study/NCT00651560) | Phase 3 | Completed | 167 | Evaluated Vytorin® (ezetimibe+simvastatin) vs atorvastatin in adults with dyslipidaemia using ATP-III lipid goal achievement and cardiovascular risk reduction as primary endpoints; supported ezetimibe combination as a clinically superior strategy |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe 10 mg added to atorvastatin or simvastatin in homozygous familial hypercholesterolaemia (HoFH); demonstrated meaningful LDL-C reduction even in the most severe hyperlipoproteinaemia subtype with markedly impaired LDL receptor function |
| [NCT02748057](https://clinicaltrials.gov/study/NCT02748057) | Phase 3 | Completed | 135 | 52-week open-label safety and tolerability study of ezetimibe 10 mg + rosuvastatin in Japanese patients with hypercholesterolaemia uncontrolled on monotherapy; provided long-term safety data relevant to Asian populations |
| [NCT05661552](https://clinicaltrials.gov/study/NCT05661552) | Phase 4 | Completed | 108 | RCT evaluating early initiation of evolocumab plus combination lipid-lowering therapy (statin + ezetimibe) in ACS patients undergoing PCI; confirmed ezetimibe's established role in intensive lipid management following acute coronary events |
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Phase 3 | Completed | 611 | Assessed cholesterol-lowering effects of ezetimibe/simvastatin co-administered with fenofibrate in patients with mixed hyperlipidaemia (elevated cholesterol and triglycerides); extended the efficacy evidence to combined hyperlipoproteinaemia subtypes |
| [NCT02942602](https://clinicaltrials.gov/study/NCT02942602) | N/A | Completed | 58 | Evaluated comprehensive HDL function and composition changes with lipid-modifying drugs including ezetimibe in hyperlipidaemia patients; provided mechanistic insight into beyond-LDL effects on cardiovascular risk markers |
| [NCT04895098](https://clinicaltrials.gov/study/NCT04895098) | N/A | Completed | 1,000 | Large retrospective observational study comparing statin monotherapy vs statin+ezetimibe combination for lipid-lowering in both primary and secondary CVD prevention; real-world efficacy and safety data |
| [NCT03434613](https://clinicaltrials.gov/study/NCT03434613) | Phase 4 | Completed | 64 | RCT comparing rosuvastatin monotherapy vs rosuvastatin+ezetimibe in patients with hyperlipidaemia and non-alcoholic fatty liver disease (NAFLD); demonstrated additional hepatic steatosis and lipid benefits with ezetimibe add-on therapy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | Phase 3 RCT | Lancet | TANDEM trial: fixed-dose combination of obicetrapib (CETP inhibitor) and ezetimibe significantly reduced LDL-C vs placebo; positioned ezetimibe as a pivotal combination partner in next-generation lipid-lowering regimens for hyperlipoproteinaemia |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | Phase 3 RCT of oral PCSK9 inhibitor enlicitide in heterozygous FH; ezetimibe used as the active comparator, directly confirming its standard-of-care benchmark status in clinical trials for familial hyperlipoproteinaemia |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Focused Review | J Am Coll Cardiol | JACC Focus Seminar on emerging LDL-C-lowering therapies; summarised ezetimibe and PCSK9 inhibitors as the established foundation for combination lipid management in patients not achieving LDL-C targets on maximally tolerated statin therapy |
| [37762244](https://pubmed.ncbi.nlm.nih.gov/37762244/) | 2023 | Review | Int J Mol Sci | Comprehensive review of postprandial hyperlipidaemia pathophysiology and treatment; discussed ezetimibe's specific role in reducing postprandial cholesterol excursions via NPC1L1 inhibition and its implications for atherogenesis |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Review | J Cardiovasc Pharmacol Ther | Comprehensive review of PCSK9 inhibitors and lipid-lowering agents; positioned ezetimibe as an essential adjunct for statin-intolerant patients and those with familial hypercholesterolaemia failing to achieve guideline-recommended LDL-C goals |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Review | Cardiology Clinics | Clinical review of familial hypercholesterolaemia management; ezetimibe recommended alongside statins, bile acid sequestrants, and newer agents as a core component of treatment to prevent premature cardiovascular morbidity and mortality |
| [29219151](https://pubmed.ncbi.nlm.nih.gov/29219151/) | 2017 | Review | Nat Rev Dis Primers | Disease primer on familial hypercholesterolaemia (Nature Reviews); ezetimibe described as providing an additional 15–20% LDL-C reduction on top of maximally tolerated statin therapy, with well-documented short-to-medium term safety |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | EAS Consensus Statement | Eur Heart J | European Atherosclerosis Society consensus on screening and treatment of familial hypercholesterolaemia; formally recommended ezetimibe as adjunct therapy when LDL-C targets cannot be achieved with statins alone |
| [19654419](https://pubmed.ncbi.nlm.nih.gov/19654419/) | 2009 | Drug Review | Drug Ther Bull | Updated evidence review of ezetimibe following the ENHANCE trial controversy; acknowledged ezetimibe's robust LDL-C-lowering efficacy while noting that cardiovascular outcome data were still emerging at time of publication |
| [18638604](https://pubmed.ncbi.nlm.nih.gov/18638604/) | 2008 | Commentary | Am J Cardiol | Commentary on the ENHANCE trial (ezetimibe+high-dose simvastatin vs simvastatin alone in heterozygous FH); argued that the mechanistic plausibility and LDL-C-lowering data support continued clinical use, and cautioned against over-interpreting surrogate endpoint results |

---

## Australia Market Information

No TGA-registered products for ezetimibe were identified in this data query.

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|-------------|--------------|-------------|---------------------|
| — | No entries found | — | — |

> **Important:** This result likely reflects a data retrieval limitation. Ezetimibe (brand name Ezetrol®) and fixed-dose combinations containing ezetimibe (e.g., Vytorin® / Inegy® with simvastatin) may hold current TGA ARTG approval. Please verify directly via the [TGA ARTG public portal](https://www.tga.gov.au/resources/artg) and obtain the current Product Information (PI) before any clinical prescribing decision.

---

## Safety Considerations

No safety-specific data (key warnings, contraindications, or drug interaction data) was retrieved for ezetimibe in this evidence pack.

Please refer to the TGA-approved Product Information (PI) for comprehensive safety information. Based on the well-characterised global safety profile of ezetimibe, the following areas warrant particular attention:

- **Ciclosporin co-administration**: Ciclosporin may significantly increase ezetimibe plasma concentrations; dose adjustment and monitoring may be required
- **Fibrate co-administration**: Concomitant use with fibrates may increase the risk of cholelithiasis and gallbladder disease
- **Statin combination**: Monitor for muscle-related symptoms (myalgia, myopathy) when used in combination with statins, particularly at higher statin doses
- **Hepatic impairment**: Use in moderate or severe hepatic impairment is not recommended
- **Pregnancy and lactation**: Safety has not been established; refer to TGA PI for current guidance

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ezetimibe's efficacy in reducing LDL-C in patients with hyperlipoproteinemia is supported by the highest level of evidence available (L1), with multiple completed Phase 3 multicentre RCTs, large post-marketing surveillance studies across diverse populations including Asian patients, and consistent endorsement in major international cardiovascular guidelines. The NPC1L1 inhibition mechanism specifically and directly addresses the pathophysiology of hyperlipoproteinemia. The guardrails reflect the absence of TGA registration data and complete safety information in this evidence pack, which must be resolved before proceeding to clinical application.

**To proceed, the following is needed:**
- Verify current TGA ARTG registration status for ezetimibe and all fixed-dose combinations (Ezetrol®, Vytorin®, Inegy®) directly via the TGA portal
- Obtain the full TGA-approved Product Information (PI) to confirm approved indications, dosage regimens, contraindications, and drug interaction warnings applicable in Australia
- Confirm current PBS (Pharmaceutical Benefits Scheme) listing status, any authority prescription requirements, and streamlined versus restricted benefit categories for Australian reimbursement
- Establish a prescriber monitoring plan consistent with the TGA PI (e.g., liver function testing at baseline, muscle symptom surveillance with concurrent statin therapy)
- If ezetimibe is not currently PBS-listed for the relevant hyperlipoproteinaemia subtype, consider preparing a PBS submission supported by the strong L1 evidence base documented in this report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

