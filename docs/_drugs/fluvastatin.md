---
layout: default
title: Fluvastatin
parent: 僅模型預測 (L5)
nav_order: 290
evidence_level: L5
indication_count: 10
---

# Fluvastatin
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

# Fluvastatin: From Hypercholesterolaemia (Statin Class) to Hyperlipoproteinemia

## One-Sentence Summary

Fluvastatin is a synthetic HMG-CoA reductase inhibitor (statin), a drug class already used to lower LDL-cholesterol and triglycerides in hypercholesterolaemia/dyslipidaemia. The TxGNN model predicts it may be effective for **Hyperlipoproteinemia**, with **5 clinical trials** and **20 publications** currently identified — however, as detailed below, this appears to be a reconfirmation of fluvastatin's known lipid-lowering pharmacology rather than a genuinely novel indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolaemia/dyslipidaemia (statin class; no locally approved indication text available — drug is not marketed in this jurisdiction) |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for fluvastatin is not available in this evidence pack (flagged as a data gap requiring DrugBank API lookup). Based on well-established pharmacological knowledge, fluvastatin belongs to the statin (HMG-CoA reductase inhibitor) class, which inhibits hepatic cholesterol synthesis and upregulates LDL-receptor expression — a mechanism proven effective for lowering LDL-C and triglycerides.

Hyperlipoproteinemia is, clinically, a closely related (largely overlapping) disease concept to the hypercholesterolaemia/mixed dyslipidaemia indications statins are already used for. The evidence pack's own repurposing rationale is explicit on this point: the mechanistic link is described as "the core pharmacological action of statins in lowering LDL/TC, which *is* the treatment of hyperlipoproteinemia/mixed hyperlipidaemia — this is a known indication rather than a new signal, and the high TxGNN score likely reflects dense pre-existing drug–disease connections in the knowledge graph" rather than a genuinely novel repurposing discovery.

This distinction matters for decision-making: unlike a true repurposing candidate (e.g., a cardiovascular drug predicted for an oncology indication), this prediction largely restates fluvastatin's existing pharmacological class effect. The practical value of this evidence pack is therefore less about "is this biologically plausible" (it clearly is) and more about confirming local regulatory status, formal indication wording, and safety documentation before any use in this jurisdiction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04608474](https://clinicaltrials.gov/study/NCT04608474) | Phase 4 | Unknown | 120 | Pilot study of PCSK9 inhibitor evolocumab for lipid management in renal transplant recipients with hyperlipidaemia; different drug class from fluvastatin (Relevance: C) |
| [NCT00726362](https://clinicaltrials.gov/study/NCT00726362) | N/A | Completed | 3270 | Surveillance study comparing efficacy of commercially available statins (including fluvastatin) in hyperlipidaemia under local clinical practice, not a fluvastatin-specific trial (Relevance: B) |
| [NCT00532311](https://clinicaltrials.gov/study/NCT00532311) | Phase 3 | Terminated | 411 | Lapaquistat acetate (a different cholesterol-lowering agent, since discontinued) co-administered with statins in hypercholesterolaemia; not fluvastatin (Relevance: C) |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Alirocumab (PCSK9 inhibitor) in children/adolescents with homozygous familial hypercholesterolaemia; different drug class (Relevance: C) |
| [NCT01634906](https://clinicaltrials.gov/study/NCT01634906) | N/A | Completed | 55 | Non-randomised study of erythrocyte-bound apolipoprotein B changes after statin withdrawal; statin-class relevant but not fluvastatin-specific (Relevance: B) |

**Note:** None of the identified trials directly test fluvastatin in hyperlipoproteinemia specifically; most are class-level (any statin) or test unrelated drug classes (PCSK9 inhibitors).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10856536](https://pubmed.ncbi.nlm.nih.gov/10856536/) | 2000 | RCT | Atherosclerosis | FACT study: fluvastatin + bezafibrate combination vs monotherapy in 333 patients with mixed hyperlipidaemia |
| [11219479](https://pubmed.ncbi.nlm.nih.gov/11219479/) | 2001 | RCT | Clinical Therapeutics | Extended-release vs immediate-release fluvastatin 80mg in primary hypercholesterolaemia |
| [15598476](https://pubmed.ncbi.nlm.nih.gov/15598476/) | 2004 | RCT | Clinical Therapeutics | 12-month RCT: fluvastatin + fenofibrate vs fluvastatin monotherapy in combined hyperlipidaemia with type 2 diabetes and CHD |
| [11347136](https://pubmed.ncbi.nlm.nih.gov/11347136/) | 2001 | Review | Nihon Rinsho | General review of fluvastatin pharmacology and clinical use |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clinical Therapeutics | Review of rosuvastatin (class-comparator) in hyperlipidaemia management |
| [10067240](https://pubmed.ncbi.nlm.nih.gov/10067240/) | 1998 | Cohort | Terapevticheskii Arkhiv | Variability of hypolipidaemic response to simvastatin vs fluvastatin in primary hyperlipoproteinemia |
| [7604789](https://pubmed.ncbi.nlm.nih.gov/7604789/) | 1995 | Cohort | Am J Cardiology | Effects of fluvastatin on lipid profile/apolipoproteins in Chinese hypercholesterolaemic patients |
| [9271817](https://pubmed.ncbi.nlm.nih.gov/9271817/) | 1997 | Cohort | Thrombosis Research | Fluvastatin and tissue factor pathway inhibitor in type IIA/IIB hyperlipidaemia and AMI |
| [8192170](https://pubmed.ncbi.nlm.nih.gov/8192170/) | 1994 | Cohort | Am J Medicine | Fluvastatin-bezafibrate vs fluvastatin-cholestyramine combinations in familial hypercholesterolaemia |
| [8967021](https://pubmed.ncbi.nlm.nih.gov/8967021/) | 1996 | Case series | Vnitrni Lekarstvi | Initial clinical experience with fluvastatin in hyperlipoproteinemia |

---

## Australia Market Information

Fluvastatin is currently **not marketed** in this jurisdiction — there are no ARTG (or equivalent local registry) entries on record (0 of 0 licenses). No product name, dosage form, or approved indication text is available for this market.

---

## Safety Considerations

No safety data (key warnings, contraindications, or drug interactions) are available in this evidence pack — the drug–drug interaction query returned no results, and warning/contraindication fields are flagged as data gaps. As fluvastatin is not currently marketed in this jurisdiction, no local Product Information exists; safety data would need to be sourced from a jurisdiction where fluvastatin is registered (e.g., TGA-equivalent PI from another regulator) before any clinical use is considered.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic plausibility is strong (fluvastatin is a statin, and lipid-lowering is its established pharmacology), and several RCTs support fluvastatin's efficacy in hyperlipoproteinemia-related conditions. However, the evidence pack itself notes this is likely a reconfirmation of known statin activity rather than a novel repurposing signal, and two blocking/high-severity data gaps (local safety labelling, and formal MOA data) remain unresolved.

**To proceed, the following is needed:**
- TFDA/local regulatory Product Information (PI) — warnings, contraindications, and drug interaction data (currently blocking; drug not locally registered)
- Detailed mechanism-of-action data from DrugBank
- Confirmation of local regulatory pathway, since fluvastatin has zero ARTG-equivalent entries and is not currently marketed in this jurisdiction
- Clarification of whether "hyperlipoproteinemia" as a target indication is meaningfully distinct from fluvastatin's existing statin-class indications, or represents label-expansion/registration work rather than new clinical evidence generation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

