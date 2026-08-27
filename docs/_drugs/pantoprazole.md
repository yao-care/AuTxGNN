---
layout: default
title: Pantoprazole
parent: 僅模型預測 (L5)
nav_order: 510
evidence_level: L5
indication_count: 10
---

# Pantoprazole
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

# Pantoprazole: From Erosive Oesophagitis to Active Peptic Ulcer Disease

## One-Sentence Summary

Pantoprazole is a proton pump inhibitor (PPI) whose labelled use, per literature in this evidence pack, is short-term treatment of erosive oesophagitis and related acid disorders. The TxGNN model predicts it may be effective for **Active Peptic Ulcer Disease**, with **3 clinical trials** and **19 publications** currently supporting this direction — though this looks more like confirmation of an existing PPI-class use than a genuinely novel repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented via TFDA/ARTG licensing data (Data Gap DG001). Literature in this pack (PMID 11402494) notes pantoprazole's labelled indication as short-term treatment of erosive oesophagitis, as part of the broader PPI class (GORD, ulcer healing, H. pylori eradication) |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L1 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data was not returned for this candidate (Data Gap DG002). However, several literature sources within the evidence pack describe pantoprazole's mechanism directly: it is a substituted benzimidazole PPI that accumulates in the acidic compartment of the gastric parietal cell, undergoes acid activation, and then covalently and irreversibly inhibits H⁺/K⁺-ATPase — the final common step of gastric acid secretion (PMID 8930575, PMID 9017763, PMID 19938880).

Active peptic ulcer disease and erosive oesophagitis/GORD sit on the same acid-related disease spectrum, and acid suppression via H⁺/K⁺-ATPase blockade is the standard mechanistic basis for healing both mucosal injury types. This is reflected directly in the evidence: NCT02084420 is a completed Phase 3, multicentre, randomised, double-blind, active-controlled trial comparing pantoprazole-based triple therapy against ilaprazole specifically for H. pylori eradication in gastric and/or duodenal ulcer patients — a direct efficacy trial in this exact disease area.

Because pantoprazole (and the PPI class generally) already carries peptic ulcer disease and H. pylori eradication as an established indication in most jurisdictions, this prediction is best read as the model correctly recovering a well-established pharmacological relationship rather than surfacing a novel therapeutic hypothesis. That is a reassuring internal-validity signal for the TxGNN pipeline, but it tempers the "new indication" framing for regulatory/commercial purposes.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Completed | 323 | Multicentre, randomised, double-blind, active-controlled trial comparing ilaprazole vs. pantoprazole triple therapy for H. pylori eradication in gastric and/or duodenal ulcer patients — direct efficacy evidence |
| [NCT02197039](https://clinicaltrials.gov/study/NCT02197039) | N/A | Completed | 316 | Prospective study identifying risk factors for poor healing/recurrent bleeding after endoscopic haemostasis and high-dose PPI infusion in peptic ulcer bleeding — informs second-look endoscopy selection criteria |
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | Completed | 320 | Evaluated effect of various PPIs, including pantoprazole, on platelet aggregation/clopidogrel interaction in PCI patients — mechanistic/interaction study, not a primary ulcer-efficacy endpoint |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18824852](https://pubmed.ncbi.nlm.nih.gov/18824852/) | 2008 | RCT | Digestion | Intermittent vs. continuous pantoprazole infusion compared for rebleeding prevention in peptic ulcer bleeding |
| [10632647](https://pubmed.ncbi.nlm.nih.gov/10632647/) | 2000 | RCT | Aliment Pharmacol Ther | Pantoprazole + amoxycillin + azithromycin/clarithromycin for H. pylori eradication in duodenal ulcer |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Review | Clin Drug Investig | Overview of pantoprazole pharmacology; notes no drug interactions identified across numerous interaction studies |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Systematic Review/Meta-analysis | Am J Gastroenterol | Network meta-analysis: P-CAB vs. PPI efficacy/safety for healing Grade C/D erosive oesophagitis |
| [16677158](https://pubmed.ncbi.nlm.nih.gov/16677158/) | 2006 | RCT | J Gastroenterol Hepatol | Pantoprazole infusion as adjuvant to endoscopic therapy improved outcomes in peptic ulcer bleeding |
| [12752349](https://pubmed.ncbi.nlm.nih.gov/12752349/) | 2003 | Comparative trial | Aliment Pharmacol Ther | Compared three pantoprazole-based triple therapies for H. pylori eradication and gastric ulcer healing |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | Comparative trial | Hepatogastroenterology | Lansoprazole vs. pantoprazole in active duodenal ulcer treatment and H. pylori eradication |
| [8930575](https://pubmed.ncbi.nlm.nih.gov/8930575/) | 1996 | Mechanism review | Eur J Gastroenterol Hepatol | Describes pantoprazole's precise, acid-activated H+/K+-ATPase inhibition mechanism |
| [9017763](https://pubmed.ncbi.nlm.nih.gov/9017763/) | 1997 | Review | Pharmacotherapy | PPIs (including pantoprazole) more effective than H2RAs for acid-related disease control |
| [38652367](https://pubmed.ncbi.nlm.nih.gov/38652367/) | 2024 | Preclinical (animal) | Inflammopharmacology | Pantoprazole + mesenchymal stem cells improved experimental gastric ulcer healing via oxidative stress/inflammation/apoptosis pathways |

## Australia Market Information

Pantoprazole is not currently listed on the ARTG in this evidence pack (0 entries; market status: Not Marketed). No product name, dosage form, or approved indication text is available to report.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information — key warnings, contraindications, and drug-drug interaction data were not returned for this candidate (query status: not found).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 RCT (NCT02084420) and a substantial body of RCT/comparative-trial literature directly support pantoprazole's efficacy in peptic ulcer healing and H. pylori eradication, giving this an L1 evidence level. However, this largely reflects pantoprazole's known PPI-class activity rather than a novel indication, and Australian market presence, TGA-approved safety information, and confirmed mechanism-of-action data are all currently missing.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications, drug interactions) — currently a blocking gap (DG001)
- Confirmed mechanism-of-action data from DrugBank (DG002)
- Verification of Australian supply/registration pathway, since the ARTG currently shows no listed entries for pantoprazole
- Clarification of the drug's original approved indication, since `original_indications` was returned empty in this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

