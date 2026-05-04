---
layout: default
title: Aluminium
parent: 僅模型預測 (L5)
nav_order: 36
evidence_level: L5
indication_count: 10
---

# Aluminium
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

# Aluminium: From Antacid/Mucosal Protectant to Peptic Ulcer Disease

---

## One-Sentence Summary

Aluminium (DrugBank DB01370) is the active metal component of established gastrointestinal mucosal protective agents — including sucralfate (aluminium sucrose sulfate) and aluminium hydroxide antacids — which have been used internationally for upper gastrointestinal conditions for decades, but are not currently registered on the Australian Register of Therapeutic Goods (ARTG) under this DrugBank entry.

The TxGNN model predicts it may be effective for **Peptic Ulcer Disease (PUD)**, with **4 clinical trials** and **20 publications** currently supporting this direction.

Notably, the evidence base largely validates the well-established historical use of aluminium-containing formulations in PUD management; the key question for this evaluation is whether the evidence base is sufficient to support formal TGA registration of a specific aluminium-based preparation in Australia.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered indication (not currently marketed in Australia) |
| Predicted New Indication | Peptic Ulcer Disease |
| TxGNN Prediction Score | 97.34% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from DrugBank for this entry. However, based on the well-characterised pharmacology of aluminium-based compounds documented in the supporting literature, several established mechanisms directly explain the predicted association with peptic ulcer disease.

Aluminium compounds exert mucosal protective and acid-neutralising effects through multiple complementary pathways. Sucralfate — a basic aluminium salt of sulphated sucrose — polymerises in the acidic gastric environment (pH < 4) to form a viscous, adherent gel that binds to negatively charged proteins at the ulcer site, creating a physical protective barrier lasting more than six hours. In parallel, aluminium ions stimulate local prostaglandin synthesis and enhance mucosal bicarbonate secretion, providing a cytoprotective effect that extends beyond simple acid buffering. Aluminium hydroxide antacids act through a distinct but complementary mechanism, directly neutralising gastric acid and raising intragastric pH to 3.5–4.5, which concurrently reduces pepsin proteolytic activity and decreases mucosal irritation.

Peptic ulcer disease is fundamentally characterised by disruption of the gastroduodenal mucosal barrier combined with excess acid-pepsin exposure — precisely the pathophysiological conditions that aluminium-based compounds are mechanistically suited to address. The strong TxGNN prediction score (97.34%) is highly consistent with decades of clinical use of sucralfate and aluminium hydroxide antacids for both gastric and duodenal ulcer healing internationally, including regulatory approvals in the United States, Japan, and Europe. The outstanding clinical questions are not whether a mechanistic rationale exists, but rather whether a specific modern aluminium-based formulation offers advantages over established first-line treatments (proton pump inhibitors, *H. pylori* eradication therapy) and whether a clear regulatory pathway to TGA registration is feasible.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT07310927](https://clinicaltrials.gov/study/NCT07310927) | Phase 2/3 | Recruiting | 140 | Most directly relevant ongoing RCT: directly compares sucralfate (an aluminium compound) against alginate for symptomatic relief of GERD and ulcer symptoms in combination with PPIs — results will directly inform evidence level for aluminium-based compounds in upper GI mucosal disease |
| [NCT01964131](https://clinicaltrials.gov/study/NCT01964131) | Phase 1 | Completed | 34 | Bioequivalence study of D961H (aluminium-based formulation) capsule vs sachet assessed by intragastric pH monitoring and pharmacokinetics in Japanese healthy male subjects; provides pharmacodynamic reference data for aluminium-based preparations |
| [NCT06526455](https://clinicaltrials.gov/study/NCT06526455) | Phase 4 | Not Yet Recruiting | 196 | Multicentre double-blind RCT comparing vonorasan vs esomeprazole for post-ESD ulcer healing, with aluminium phosphate gel used as an adjunct intervention; aluminium compound is a secondary rather than primary study drug, limiting direct applicability |
| [NCT00854776](https://clinicaltrials.gov/study/NCT00854776) | N/A | Unknown | 300 | Observational study examining PUD incidence in ischaemic heart disease patients on aspirin/clopidogrel ± proton pump inhibitor; provides epidemiological context for antiplatelet-associated peptic ulcer burden but is not an aluminium treatment intervention trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [7590572](https://pubmed.ncbi.nlm.nih.gov/7590572/) | 1995 | Clinical Study | Hepato-Gastroenterology | Single-centre RCT in 50 endoscopically verified duodenal/gastric ulcer patients comparing sucralfate effervescent tablet vs granular formulation (2g twice daily); includes serial monitoring of serum aluminium concentrations — key safety data point |
| [789170](https://pubmed.ncbi.nlm.nih.gov/789170/) | 1975 | Clinical Study | Gastroenterologia Japonica | Multi-institutional double-blind controlled study in 302 gastric ulcer patients comparing N-acetyl-L-glutamine aluminium complex, basic aluminium sucrose sulfate, and placebo over 12 weeks; demonstrates significant ulcer healing advantage over placebo |
| [4571693](https://pubmed.ncbi.nlm.nih.gov/4571693/) | 1973 | Clinical Trial | Drug and Therapeutics Bulletin | Early clinical trial of Caved-S (aluminium-containing compound) and Ulcedal for peptic ulcer — among the earliest controlled clinical evidence for aluminium-based PUD treatment |
| [6764389](https://pubmed.ncbi.nlm.nih.gov/6764389/) | 1982 | Review | Clinical Pharmacy | Comprehensive pharmacology review of sucralfate for PUD: mucosal barrier formation, local acid neutralisation without systemic pH change, pepsin inhibition, and bile salt adsorption; foundational reference for the mechanism of aluminium-based mucosal protection |
| [6368184](https://pubmed.ncbi.nlm.nih.gov/6368184/) | 1984 | Review | Drugs | Definitive pharmacodynamics review of sucralfate: controlled trials demonstrating efficacy equivalent to H2-antagonists in healing duodenal and gastric ulcers over 4–8 weeks at 1g four times daily; minimal systemic absorption (3–5%) noted |
| [38192](https://pubmed.ncbi.nlm.nih.gov/38192/) | 1979 | Review | Gut | Critical reappraisal of antacid therapy in PUD: intensive aluminium-containing antacid regimens shown to be effective for duodenal ulcer healing and prevention of stress ulcer haemorrhage, comparable in efficacy to cimetidine |
| [8912126](https://pubmed.ncbi.nlm.nih.gov/8912126/) | 1996 | Clinical Study | Journal of Gastroenterology and Hepatology | Prospective study measuring aluminium accumulation in liver tissue and cerebrospinal fluid in 15 patients each taking sucralfate or aluminium hydroxide for one month; documents measurable hepatic and CSF aluminium deposition — critical safety reference for systemic exposure |
| [2865092](https://pubmed.ncbi.nlm.nih.gov/2865092/) | 1985 | Review | Digestive Diseases and Sciences | Pharmacological classification of anti-ulcer drugs by mechanism; aluminium-based agents categorised as cytoprotective/mucosal protectants, distinct from antisecretory agents — contextualises the role of aluminium compounds within the PUD treatment armamentarium |
| [6095662](https://pubmed.ncbi.nlm.nih.gov/6095662/) | 1984 | Review | American Journal of Medicine | Practical review of PUD pharmacotherapy including sucralfate and H2-antagonists; highlights that aluminium-containing agents (sucralfate, antacids) were among the four main drug classes available in the US at that time |
| [2401189](https://pubmed.ncbi.nlm.nih.gov/2401189/) | 1990 | Clinical Study | Drugs Under Experimental and Clinical Research | Retrospective study in 267 paediatric patients with peptic symptoms including assessment of aluminium-containing compounds; relevant for understanding PUD management across age groups and paediatric safety considerations |

---

## Australia Market Information

Aluminium (DrugBank DB01370) is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)**. No TGA-approved products exist under this DrugBank entry in Australia.

Aluminium-containing formulations with established PUD use internationally (e.g., sucralfate, aluminium hydroxide antacid gels) would each require a separate TGA registration pathway as distinct therapeutic goods before any PUD indication could be formally approved in Australia.

---

## Safety Considerations

**Key safety signal — aluminium systemic accumulation:** Short-course oral therapy with sucralfate or aluminium hydroxide antacids is generally considered safe in patients with normal renal function. However, PMID 8912126 documents measurable aluminium deposition in liver tissue and cerebrospinal fluid following standard one-month therapeutic courses. Risk is substantially elevated in renally impaired patients, in whom aluminium clearance is reduced. Renal function monitoring is warranted prior to initiation and during prolonged courses.

**Important adverse signal — aluminium as a contact allergen (Rank 3 prediction):** Evidence retrieved for the dermatitis prediction indicates that aluminium can **cause** rather than treat dermatitis. Aluminium-adsorbed vaccines are associated with injection-site granulomas and Type IV delayed hypersensitivity reactions; aluminium in sunscreens and antiperspirants can induce allergic contact dermatitis, particularly in previously sensitised individuals (PMID 33797096 — systematic review and meta-analysis). This is a clinically important adverse signal for any **topical or parenteral** aluminium-containing formulation and should be factored into formulation selection and patient screening.

For complete safety information on any specific aluminium-based formulation, please refer to the relevant Product Information (PI) for that preparation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction for peptic ulcer disease is strongly supported by decades of clinical and pharmacological evidence for aluminium-based compounds, and the mechanistic basis for mucosal protection and acid neutralisation is well-characterised in the published literature. However, aluminium-based preparations for PUD are not currently registered on the ARTG, the supporting evidence largely pre-dates modern regulatory standards, and first-line PUD therapy has evolved significantly (PPIs, *H. pylori* eradication) since the period when aluminium-based agents were most widely studied.

**To proceed, the following is needed:**

- **Formulation specification:** Identify the precise aluminium-containing formulation intended for evaluation (sucralfate vs aluminium hydroxide vs aluminium phosphate gel), as clinical evidence profiles, safety data, and regulatory requirements differ substantially between forms
- **Formal MOA data:** Retrieve complete mechanism of action documentation from DrugBank or equivalent authoritative source to support the regulatory dossier
- **Comparative efficacy assessment:** Evaluate evidence relative to contemporary Australian first-line PUD management (PPI therapy, *H. pylori* eradication per current gastroenterological guidelines), given the predominantly historical evidence base
- **Safety monitoring plan:** Develop a renal function monitoring protocol addressing aluminium absorption risk, particularly for renally impaired patients, elderly populations, and extended-treatment courses; reference PMID 8912126 for aluminium accumulation baseline data
- **Adverse signal management:** Formally risk-stratify the contact allergy/dermatitis adverse signal for the intended route of administration; implement pre-treatment aluminium sensitisation screening if a topical formulation is being considered
- **TGA regulatory pathway:** Engage with the TGA to identify the most appropriate registration pathway (e.g., new chemical entity vs. established substance with new indication vs. bibliographic application) for the intended formulation and indication

---

> ⚠️ **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before clinical application. All content should be interpreted in conjunction with TGA-approved Product Information and current Australian clinical practice guidelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

