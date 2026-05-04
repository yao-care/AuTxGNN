---
layout: default
title: Crizotinib
parent: 僅模型預測 (L5)
nav_order: 131
evidence_level: L5
indication_count: 10
---

# Crizotinib
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

# Crizotinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

---

## One-Sentence Summary

Crizotinib (Xalkori®) is an oral tyrosine kinase inhibitor (TKI) targeting ALK, ROS1, and MET receptor kinases, originally approved for the treatment of ALK-rearranged non-small cell lung cancer (NSCLC). The TxGNN model predicts it may be effective for **Gingival Fibromatosis**, with a prediction score of **99.81%**; however, **no clinical trials or published literature** currently support this specific indication, and no mechanistic link between Crizotinib's known targets and the genetic drivers of this condition has been established. This prediction is assessed as a knowledge graph topological association rather than a clinically actionable repurposing signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK-positive non-small cell lung cancer (FDA-approved 2011; also approved for ROS1-rearranged NSCLC and MET exon 14-skipping NSCLC) |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action (MOA) data is not available from the Australian regulatory database for this drug. Based on published literature retrieved during evidence collection, Crizotinib is an ATP-competitive small-molecule inhibitor of three receptor tyrosine kinases: **ALK (Anaplastic Lymphoma Kinase)**, **ROS1**, and **MET/c-Met** (PMID 24756793, 30069759). By blocking constitutive activation of these kinases — typically caused by chromosomal rearrangements such as EML4-ALK fusions or ROS1 fusions — Crizotinib disrupts downstream pro-survival signalling (RAS/MAPK, PI3K/AKT, JAK/STAT pathways), leading to tumour cell apoptosis and growth arrest. The drug was first approved by the US FDA in 2011 for ALK-rearranged NSCLC, a subset representing 3–5% of all NSCLC patients.

Gingival fibromatosis is a benign fibrous overgrowth of gingival tissue. The condition is caused by mutations in genes such as **SOS1** (a RAS guanine nucleotide exchange factor) and **PTCH1** (a Hedgehog pathway regulator). Critically, neither of these genetic drivers has a documented functional intersection with the ALK, ROS1, or MET kinase pathways that Crizotinib targets. There is currently no preclinical or clinical evidence suggesting that ALK/ROS1/MET inhibition would attenuate fibrous overgrowth in this condition.

The high TxGNN score (0.9981) most likely reflects **knowledge graph topological proximity** rather than biological plausibility: within the TxGNN knowledge graph, gingival fibromatosis nodes likely share neighbours with other fibroproliferative or mesenchymal proliferative conditions (e.g., ALK-positive inflammatory myofibroblastic tumour, IMT) for which Crizotinib has established mechanistic relevance. This is a known limitation of graph-based predictive models — topological similarity does not reliably translate to pharmacological or clinical applicability.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Crizotinib in gingival fibromatosis.

---

## Literature Evidence

Currently no related literature available for Crizotinib in gingival fibromatosis.

---

## Australia Market Information

Crizotinib is currently **not registered on the Australian Register of Therapeutic Goods (ARTG)** and has no approved market presence in Australia. There are **0 ARTG entries** for any Crizotinib-containing product.

Australian patients who require Crizotinib may potentially access it through:
- **TGA Special Access Scheme (SAS Category B or C)** — for individual patient access to unapproved therapeutic goods
- **Authorised Prescriber pathway** — following TGA approval for a specific practitioner and indication
- **Clinical trial enrolment** — through registered studies involving Crizotinib

Prescribers should note that Crizotinib (brand name Xalkori®, Pfizer) is approved in multiple other jurisdictions including the US (FDA), EU (EMA), and Japan (PMDA) for ALK-positive and ROS1-positive advanced NSCLC.

---

## Cytotoxicity

Crizotinib is an antineoplastic agent (targeted therapy for ALK/ROS1/MET-driven malignancies). The following cytotoxicity profile applies:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — receptor tyrosine kinase inhibitor (ALK/ROS1/MET inhibitor); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low to moderate — neutropenia and lymphopenia are reported but less severe than conventional chemotherapy; monitor FBC |
| Emetogenicity Classification | Low to moderate (oral TKI; nausea reported commonly) |
| Monitoring Items | Full blood count (FBC) with differential; liver function tests (ALT, AST, bilirubin) — severe hepatotoxicity including fatal liver failure reported (PMID 26898609); renal function; ECG for QTc interval (QT prolongation and bradycardia documented — PMID 29717400); ophthalmological review for visual disturbances (diplopia, photopsia) |
| Handling Protection | Handle as per institutional cytotoxic/hazardous drug handling policy; standard oral cytotoxic precautions apply (avoid crushing or opening capsules without PPE) |

---

## Safety Considerations

Safety data from the Australian regulatory database is not currently available for Crizotinib. Please refer to the prescribing information from an approved jurisdiction (e.g., US FDA label for Xalkori®, or EMA SmPC) for comprehensive safety information until a TGA-approved Product Information (PI) becomes accessible.

The following adverse effects have been highlighted in the retrieved published literature and are relevant to clinical risk assessment:

- **Hepatotoxicity**: Severe and potentially fatal hepatotoxicity has been reported, including a case of fulminant liver failure after only 24 days of treatment (PMID 26898609). Baseline and regular LFT monitoring is essential.
- **Cardiac toxicity**: QT prolongation, bradycardia, and rare simultaneous multiple cardiac events (ventricular fibrillation, pericarditis, sick sinus syndrome) have been documented (PMID 29717400, 29413968, 25922742). Baseline ECG and monitoring are recommended.
- **Interstitial lung disease (ILD) / Pneumonitis**: A recognised class effect of ALK inhibitors, including Crizotinib; can be life-threatening (PMID 41617059).
- **Visual disturbances**: Common adverse effect; patients should be counselled regarding diplopia, photopsia, and blurred vision, particularly when driving.
- **Skin reactions**: Erythema multiforme has been reported (PMID 25994067).
- **Drug interactions**: Crizotinib is a CYP3A4 substrate and a moderate CYP3A4 inhibitor; formal DDI data was not retrievable in this evidence pack. Concomitant use of strong CYP3A4 inducers or inhibitors, and QT-prolonging agents, warrants careful clinical review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.81%), gingival fibromatosis is driven by SOS1/PTCH1 mutations that have no established intersection with Crizotinib's pharmacological targets (ALK, ROS1, MET). There is no supporting clinical trial evidence, no published literature specific to this indication, and no preclinical mechanistic data to suggest activity. The elevated score is attributable to knowledge graph topology artefact — a recognised source of false-positive predictions in this modelling approach. The evidence level is L5 (model prediction only), and clinical translation cannot be justified at this stage.

**To proceed, the following would be required:**
- Identification of ALK, ROS1, or MET pathway activation in gingival fibromatosis tissue through genomic profiling (e.g., RNA-seq, NGS, IHC)
- Published preclinical evidence (in vitro cell models or in vivo animal studies) demonstrating measurable anti-fibrotic activity of Crizotinib in gingival fibromatosis
- A mechanistically credible hypothesis linking Crizotinib's known targets to SOS1/PTCH1-driven fibroproliferation
- MOA data retrieval from DrugBank API (flagged as Data Gap DG002)
- TGA PI or equivalent prescribing information for full safety profiling (flagged as Data Gap DG001)

**Clinician note:** Within the same TxGNN prediction run (top 10 indications), several **lung tumour entities** achieve comparably high scores with substantially stronger mechanistic rationale through the ALK pathway — most notably **ALK-positive inflammatory myofibroblastic tumour (IMT)** (surfaced under "lung benign neoplasm", rank 5, L3 evidence) and **lung hilum carcinoma with ALK/ROS1 rearrangement** (rank 4, L4 evidence). These indications may warrant separate evaluation reports with a higher likelihood of clinical utility.

---

> **Disclaimer:** This report is generated for research purposes only and does not constitute medical advice. All repurposing candidates require prospective clinical validation before any therapeutic application. Healthcare professionals should refer to TGA-approved Product Information and exercise independent clinical judgement.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

