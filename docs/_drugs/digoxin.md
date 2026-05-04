---
layout: default
title: Digoxin
parent: 僅模型預測 (L5)
nav_order: 155
evidence_level: L5
indication_count: 10
---

# Digoxin
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

# Digoxin: From Heart Failure and Atrial Fibrillation to Prinzmetal Angina

## One-Sentence Summary

Digoxin is a cardiac glycoside with centuries of clinical use, primarily indicated for chronic heart failure and ventricular rate control in atrial fibrillation.
The TxGNN model's top-ranked prediction suggests it may have potential in **Prinzmetal Angina** (vasospastic angina), achieving a prediction score of **99.81%**;
however, this indication is currently supported by **0 clinical trials** and only **2 tangentially related publications**, and — critically — Digoxin's known pharmacology may be mechanistically **contraindicated** in this setting.
Among all 10 TxGNN predictions evaluated in this pack, **stroke disorder** (ranked #10) carries the strongest clinical evidence base (Evidence Level L3, 23 clinical trials, 20 publications) and is the only indication reaching a "Proceed with Guardrails" recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic heart failure; Ventricular rate control in atrial fibrillation |
| Predicted New Indication | Prinzmetal Angina (Vasospastic Angina) |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (DrugBank MOA data gap — DG002). Based on well-established pharmacological knowledge, Digoxin inhibits the **Na⁺/K⁺-ATPase pump** in cardiac myocytes, raising intracellular sodium and consequently increasing intracellular calcium via the Na⁺/Ca²⁺ exchanger. This produces positive inotropy (stronger cardiac contraction), underpinning its use in heart failure. Separately, its vagomimetic effect — enhanced parasympathetic tone on the atrioventricular node — slows ventricular rate in atrial fibrillation.

Prinzmetal angina (also called variant or vasospastic angina) is caused by transient, often unprovoked **coronary artery spasm** at rest, driven by vascular smooth muscle hyperreactivity. The relationship between Digoxin's mechanism and this condition is, critically, **potentially contraindicated rather than therapeutic**: elevated intracellular calcium in vascular smooth muscle could theoretically **aggravate coronary vasospasm** — the very pathological event that defines Prinzmetal angina. Standard first-line treatment for Prinzmetal angina relies on calcium channel blockers (e.g., amlodipine, diltiazem) and long-acting nitrates — pharmacological agents with mechanisms directly opposing those of Digoxin. Several international cardiology guidelines identify Digoxin as a potential relative contraindication in vasospastic angina.

The TxGNN model's high prediction score most likely reflects the close proximity of cardiovascular disease nodes within the knowledge graph — a network artefact — rather than a genuine therapeutic link. The two identified publications address haemodynamic triggers of effort-related angina and circadian rhythms in antihypertensive therapy, neither of which constitutes supportive mechanistic or clinical evidence for Digoxin in Prinzmetal angina. This prediction should be treated with caution and a **Hold** decision is appropriate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Digoxin in Prinzmetal Angina.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [9206110](https://pubmed.ncbi.nlm.nih.gov/9206110/) | 1996 | Narrative Review | Chinese Medical Sciences Journal | Haemodynamic study of 30 angina decubitus patients; identifies increased myocardial oxygen consumption and pulmonary artery diastolic pressure elevation as onset triggers; describes this as effort-type angina — **no direct support for Digoxin use in vasospastic angina** |
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta Physiologica et Pharmacologica Bulgarica | Review of chronopharmacology and circadian rhythms in antihypertensive treatment; tangential relevance only; does not address Digoxin in the context of coronary vasospasm |

---

## Australia Market Information

Based on the TGA regulatory data query conducted on 9 March 2026, Digoxin currently has **no entries on the Australian Register of Therapeutic Goods (ARTG)**. Healthcare professionals requiring access to Digoxin for clinical use should consult the TGA for applicable access pathways, including the Special Access Scheme (SAS) or Authorised Prescriber pathway.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> **Clinical Safety Note Specific to This Repurposing Context:**
> Based on published pharmacological evidence and international clinical guidelines, the following concerns are directly relevant:
> - Digoxin elevates intracellular calcium in vascular smooth muscle cells, which may **worsen coronary vasospasm** — the defining feature of Prinzmetal angina
> - Standard Prinzmetal angina treatment (calcium channel blockers, nitrates) is mechanistically **opposite** to Digoxin's effects on vascular smooth muscle
> - Multiple cardiology guidelines list Digoxin as a **relative or absolute contraindication** in vasospastic/Prinzmetal angina
> - No drug interaction data was identified in the DDI query for this evaluation; formal DDI assessment against standard Prinzmetal angina medications (amlodipine, diltiazem, isosorbide mononitrate) would be required before any further evaluation

---

## Summary of All Predicted Indications

The following table provides context across all 10 TxGNN predictions evaluated in this evidence pack:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|----------------|----------------|
| 1 | Prinzmetal Angina | 99.81% | L4 | **Hold** |
| 2 | Duodenal Obstruction | 99.70% | L5 | Hold |
| 3 | Duodenal Ulcer | 99.59% | L5 | Hold |
| 4 | Duodenogastric Reflux | 99.53% | L5 | Hold |
| 5 | Ischemic Stroke Susceptibility *(obsolete term)* | 99.29% | L5 | Hold |
| 6 | Hypoalphalipoproteinaemia | 99.20% | L5 | Hold |
| 7 | Homozygous Familial Hypercholesterolaemia | 98.98% | L5 | Hold |
| 8 | Nephrogenic Syndrome of Inappropriate Antidiuresis | 98.83% | L5 | Research Question |
| 9 | Thrombotic Disease | 98.75% | L4 | Research Question |
| 10 | **Stroke Disorder** | **98.19%** | **L3** | **Proceed with Guardrails** |

Ranks 2–4 involve gastrointestinal conditions (obstruction, ulcer, reflux) for which Digoxin has no known therapeutic mechanism. Ranks 5–7 represent metabolic and vascular disease categories where Digoxin's Na⁺/K⁺-ATPase inhibition has no established link to disease pathophysiology. Ranks 8 and 9 carry speculative but biologically plausible mechanistic hypotheses worth initial literature exploration. **Rank 10 (stroke disorder)** is the most clinically substantiated prediction, supported by 23 clinical trials and 20 publications, with a plausible indirect mechanistic pathway through atrial fibrillation management.

---

## Conclusion and Next Steps

**Decision: Hold** *(for Prinzmetal Angina — the primary TxGNN-ranked prediction)*

**Rationale:**
Digoxin's core pharmacological mechanism — increasing intracellular calcium — is physiologically incompatible with the management of Prinzmetal angina and may carry a genuine safety risk by aggravating coronary vasospasm. No clinical trial evidence exists for this indication, and the two identified publications offer no supportive data. The high TxGNN prediction score is most likely a knowledge graph artefact reflecting cardiovascular disease node proximity rather than a validated therapeutic signal.

**To proceed with Prinzmetal Angina, the following would be required:**

- Formal mechanistic analysis clarifying whether Digoxin's vagomimetic coronary effects could override its pro-vasospastic calcium-mediated vascular effects — currently unsupported
- Systematic review of adverse event and safety reports in Digoxin-exposed patients with documented coronary vasospasm
- Resolution of the DrugBank MOA data gap (DG002) to enable complete mechanistic profiling via a DrugBank API query

**Priority Redirect — Stroke Disorder (Ranked #10):**
The evidence pack strongly suggests that **stroke disorder** represents the highest-priority repurposing opportunity for Digoxin. A dedicated evaluation report for this indication is recommended, incorporating:
- Review of Phase 4 randomised trial data from NCT02391337 (Digoxin vs. beta-blocker in permanent AF — direct relevance, Grade A)
- Analysis of large registry data from NCT02786095 (CODE-AF, n=20,000, stroke as primary composite endpoint — Grade B)
- Mechanistic review of vascular Na⁺,K⁺-ATPase in ischaemic stroke pathophysiology (PMID 37877226)
- Risk stratification given signals of increased cardiovascular mortality in Digoxin + beta-blocker combination therapy (PMID 38780748)

---

*This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. This evaluation reflects data available as at 4 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

