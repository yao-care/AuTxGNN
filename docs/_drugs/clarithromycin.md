---
layout: default
title: Clarithromycin
parent: 僅模型預測 (L5)
nav_order: 115
evidence_level: L5
indication_count: 10
---

# Clarithromycin
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

# Clarithromycin: From Respiratory Tract Infection to Monoclonal Gammopathy

## One-Sentence Summary

Clarithromycin is a macrolide antibiotic widely used for respiratory tract infections, *Helicobacter pylori* eradication, and *Mycobacterium avium* complex (MAC) infections.
The TxGNN model predicts it may be effective for **Monoclonal Gammopathy** (including Monoclonal Gammopathy of Undetermined Significance [MGUS] and Multiple Myeloma) — the highest-evidence prediction among 10 candidates in this analysis — supported by **1 completed Phase 2 clinical trial** and **19 publications**.

> **Note on report focus**: TxGNN's highest-ranked prediction (Rank 1: hyperamylasemia) carries only L5 evidence with a Hold recommendation and no direct mechanistic basis. This report focuses on **Monoclonal Gammopathy** (TxGNN Global Rank 11,923), which carries L2 evidence and the strongest mechanistic rationale — making it the most actionable and clinically meaningful prediction in this pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Respiratory tract infections, *H. pylori* eradication, MAC infections (antibiotic) |
| Predicted New Indication | Monoclonal Gammopathy (MGUS / Multiple Myeloma) |
| TxGNN Prediction Score | 98.81% |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed (0 ARTG entries — data gap; verify with TGA directly) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Clarithromycin is a semi-synthetic macrolide antibiotic that inhibits bacterial protein synthesis by binding to the 50S ribosomal subunit. Beyond its antimicrobial activity, clarithromycin has well-characterised **immunomodulatory and anti-inflammatory properties**, including inhibition of the NF-κB signalling pathway and suppression of the pro-inflammatory cytokine IL-6. These secondary properties form the biological basis of this repurposing prediction.

The mechanistic link between clarithromycin and monoclonal gammopathy is anchored in IL-6 biology. IL-6 is the principal growth and survival factor for plasma cells — the malignant cell type in Multiple Myeloma, and the dysregulated cell type in MGUS. By suppressing IL-6 signalling and NF-κB activity, clarithromycin can sensitise myeloma cells to immunomodulatory drugs (IMiDs) such as lenalidomide, thalidomide, and pomalidomide, and there is clinical evidence suggesting it can reverse IMiD resistance in relapsed/refractory disease. In vitro data further confirm synergistic cytotoxicity when clarithromycin is combined with thalidomide in myeloma cell lines.

MGUS and Multiple Myeloma sit on a continuum of plasma cell dyscrasias sharing the hallmark of abnormal monoclonal immunoglobulin production. The fact that the BiRD regimen (clarithromycin + lenalidomide + dexamethasone) and BLT-D regimen (clarithromycin + thalidomide + dexamethasone) have each been studied in multiple Phase 2 trials — and that one randomised Phase 2 trial (NCT00006219) directly evaluated clarithromycin as chemoprevention in MGUS — makes the TxGNN prediction biologically coherent and clinically grounded.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00006219](https://clinicaltrials.gov/study/NCT00006219) | Phase 2 | Completed | N/A | Randomised Phase 2 trial directly targeting MGUS and borderline-significant monoclonal gammopathy. Compared DHEA vs clarithromycin in patients at high risk of progressing to Multiple Myeloma. Evaluated clarithromycin as a chemoprevention strategy. Completed December 2006. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [34021118](https://pubmed.ncbi.nlm.nih.gov/34021118/) | 2021 | RCT | *Blood Cancer Journal* | Phase 3 RCT (n=286) of Rd ± clarithromycin in transplant-ineligible MM. No significant PFS benefit from adding clarithromycin to continuous Rd — tempers enthusiasm for this specific combination in this population. |
| [36394758](https://pubmed.ncbi.nlm.nih.gov/36394758/) | 2022 | Systematic Review / Meta-analysis | *Eur Rev Med Pharmacol Sci* | Meta-analysis of triplet regimens based on pomalidomide + dexamethasone (including clarithromycin-containing arms) for relapsed/refractory MM; compares safety and efficacy across regimens. |
| [30792190](https://pubmed.ncbi.nlm.nih.gov/30792190/) | 2019 | Phase 2 | *Blood Advances* | Phase 2 trial of ClaPd (clarithromycin + pomalidomide + dexamethasone) in 120 RRMM patients with prior lenalidomide exposure; demonstrates meaningful activity in a heavily pretreated population (median 5 prior lines). |
| [34424561](https://pubmed.ncbi.nlm.nih.gov/34424561/) | 2021 | Phase 2 | *Am J Hematol* | Car-BiRd sequential regimen (carfilzomib induction → lenalidomide + clarithromycin + dexamethasone consolidation → lenalidomide maintenance) in newly diagnosed MM; evaluates reduced toxicity approach. |
| [17989313](https://pubmed.ncbi.nlm.nih.gov/17989313/) | 2008 | Phase 2 | *Blood* | Landmark BiRD trial (clarithromycin + lenalidomide + dexamethasone) as first-line therapy for symptomatic MM; high complete response and overall response rates in treatment-naive patients, established BiRD as a standard non-transplant option. |
| [24576165](https://pubmed.ncbi.nlm.nih.gov/24576165/) | 2014 | Phase 2 | *Leukemia & Lymphoma* | T-BiRD (thalidomide + clarithromycin + lenalidomide + dexamethasone) in newly diagnosed symptomatic MM; 26 patients, high overall response rate. |
| [24723438](https://pubmed.ncbi.nlm.nih.gov/24723438/) | 2014 | Clinical Study | *Am J Hematol* | Clarithromycin added to lenalidomide + dexamethasone at time of Rd progression; ~48% haematological response rate in 24 patients with median 3 prior therapy lines — direct evidence of resistance reversal. |
| [28355602](https://pubmed.ncbi.nlm.nih.gov/28355602/) | 2017 | Phase 2 | *Acta Haematol* | Two consecutive post-ASCT consolidation studies with BLT-D followed by BiRD in MM; acceptable toxicity and meaningful responses in the post-transplant setting. |
| [12685831](https://pubmed.ncbi.nlm.nih.gov/12685831/) | 2003 | Phase 2 | *Leukemia & Lymphoma* | BLT-D (clarithromycin + low-dose thalidomide + dexamethasone) in previously untreated and treated MM and Waldenström's macroglobulinaemia; early proof-of-concept for clarithromycin in plasma cell dyscrasias. |
| [18759764](https://pubmed.ncbi.nlm.nih.gov/18759764/) | 2008 | Phase 2 | *Br J Haematol* | Phase 2 study of clarithromycin (250 mg BD) + low-dose thalidomide + low-dose dexamethasone in relapsed/refractory MM (n=30); well-tolerated, particularly suitable for elderly or frail patients. |

---

## Australia Market Information

The evidence pack records **0 ARTG entries** and a market status of "not marketed" for clarithromycin in Australia. This appears inconsistent with clarithromycin's known widespread global availability and likely reflects a **data gap** in the current dataset rather than a genuine regulatory absence.

Clinicians should verify the current registration status directly via the [TGA ARTG Public Summary](https://www.tga.gov.au/resources/artg).

> **Practical implication**: If clarithromycin is confirmed to hold a current ARTG listing (for its registered indications such as respiratory tract infections), off-label use for monoclonal gammopathy within an approved clinical trial or under the TGA Special Access Scheme (SAS) Category B would be the appropriate regulatory pathway.

---

## Safety Considerations

TGA-specific Product Information data (including approved warnings and contraindications) was not available in this evidence pack. Please refer to the **TGA-approved Product Information (PI)** for comprehensive safety information.

Based on published clinical trial data for clarithromycin-containing haematology regimens, Australian healthcare professionals should note:

- **QT Prolongation**: Clarithromycin prolongs the QT interval and is a potent **CYP3A4 inhibitor**. Baseline and monitoring ECGs are prudent, particularly in elderly myeloma patients with cardiac comorbidities or concurrent QT-prolonging medications.
- **Drug–Drug Interactions**: CYP3A4-mediated interactions are clinically significant. Co-administration with lenalidomide, pomalidomide, thalidomide, corticosteroids, and proteasome inhibitors requires careful review. No specific DDI data was captured in this evidence pack.
- **Peripheral Neuropathy**: Post-marketing reports link clarithromycin to peripheral neuropathy. This safety signal warrants particular attention in combination regimens containing thalidomide (which is independently neurotoxic) or bortezomib.
- **Hepatic Effects**: Hepatotoxicity has been reported with macrolide antibiotics; liver function monitoring is advisable in combination chemotherapy settings.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 2 clinical trials and one completed randomised Phase 2 study (NCT00006219) directly targeting MGUS support clarithromycin's activity in the monoclonal gammopathy spectrum. The BiRD regimen is already in use at haematology centres globally, the mechanistic basis via NF-κB/IL-6 inhibition is well-established, and there is direct evidence of resistance reversal in relapsed/refractory myeloma. A completed Phase 3 RCT did not show PFS benefit for the Rd + clarithromycin combination in transplant-ineligible MM, which narrows the target population but does not negate the overall signal.

**To proceed, the following is needed:**
- **TGA ARTG verification**: Confirm current Australian registration status and approved indications for clarithromycin products
- **TGA Product Information review**: Obtain complete safety, warnings, and contraindication data from the approved PI
- **Target population definition**: Clarify whether the clinical question is MGUS chemoprevention or active MM treatment — these carry fundamentally different risk-benefit profiles
- **DDI assessment**: Conduct a formal drug interaction review, particularly for CYP3A4-mediated interactions with planned co-medications (IMiDs, dexamethasone, antifungals)
- **Regulatory pathway**: Establish access route — SAS Category B, clinical trial enrolment, or compassionate access — given the absence of a registered oncology indication in Australia
- **Haematologist input**: Specialist haematology/myeloma team review required before any clinical application

---

> ⚠️ **Disclaimer**: This report is generated for research purposes only and does not constitute medical advice. All drug repurposing predictions require clinical validation before patient application. TxGNN predictions are computational outputs and must be interpreted by qualified Australian healthcare professionals in the context of individual patient circumstances.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

