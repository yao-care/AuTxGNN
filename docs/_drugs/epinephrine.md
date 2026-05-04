---
layout: default
title: Epinephrine
parent: 僅模型預測 (L5)
nav_order: 194
evidence_level: L5
indication_count: 10
---

# Epinephrine
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

# Epinephrine: From Anaphylaxis and Acute Bronchospasm to Obstructive Lung Disease

## One-Sentence Summary

Epinephrine (adrenaline) is a non-selective adrenergic receptor agonist with well-established emergency use for anaphylaxis, cardiac arrest, and acute bronchospasm, though no formal original indication was recorded in the Australian database for this query.
The TxGNN model predicts it may be effective for **Obstructive Lung Disease** — including bronchiolitis, asthma exacerbations, and COPD — with a prediction score of **99.71%**.
This prediction is supported by **2 Cochrane systematic reviews** and a **Phase 3 multicentre RCT (n=864)** directly evaluating nebulised epinephrine in obstructive airways disease, placing the evidence at **L1**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No formal indication recorded in the Australian (TGA) database for this query |
| Predicted New Indication | Obstructive Lung Disease (bronchiolitis, asthma, COPD) |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L1 |
| Australia Market Status | Not found in this data query (0 ARTG entries retrieved) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data was not retrieved from DrugBank during this data collection cycle. Based on established pharmacology, Epinephrine is a non-selective adrenergic receptor agonist acting simultaneously on α1, α2, β1, and β2 adrenoceptors. In the airways, β2-adrenoceptor activation on bronchial smooth muscle causes rapid, potent bronchodilation and reduces airway resistance. In parallel, α1-adrenoceptor activation induces mucosal vasoconstriction — reducing subepithelial oedema and airway secretions. These two complementary actions directly address the core pathophysiology of obstructive airway disease.

Obstructive lung disease encompasses a spectrum of conditions from viral bronchiolitis in infants through to acute severe asthma and COPD exacerbations. In viral bronchiolitis — the most common reason for infant hospitalisation in Australia — the primary pathology is subepithelial oedema, mucus plugging, and reflex bronchospasm, all of which are amenable to Epinephrine's dual adrenergic mechanism. Two Cochrane systematic reviews (2004 and 2011) confirm short-term bronchodilator benefit of nebulised epinephrine in bronchiolitis, and a large Phase 3 multicentre RCT (NCT03567473, n=864) specifically evaluated inhaled epinephrine combined with oral dexamethasone versus placebo in this setting. The US FDA's re-approval of Primatene Mist (epinephrine HFA inhaler) as an over-the-counter asthma inhaler in 2018 further reflects regulatory confidence in the epinephrine–obstructive lung disease indication.

The mechanistic rationale for this TxGNN prediction is well-grounded rather than speculative — it reflects an established pharmacological pathway with decades of supporting evidence. The core repurposing question is therefore not *whether* Epinephrine works in obstructive lung disease, but *how to optimise* its clinical application: selecting the right formulation, route (nebulised, intramuscular, inhaled MDI), dose, and patient population compared with more receptor-selective agents such as salbutamol.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03567473](https://clinicaltrials.gov/study/NCT03567473) | Phase 3 | Completed | 864 | Multicentre RCT: inhaled epinephrine + oral dexamethasone vs placebo for infant bronchiolitis; primary endpoint is hospitalisation rate at 7 days — the largest direct RCT for epinephrine in obstructive airway disease |
| [NCT03614273](https://clinicaltrials.gov/study/NCT03614273) | N/A | Completed | 60 | RCT directly comparing nebulised hypertonic saline (3%) vs nebulised adrenaline for bronchiolitis in a tertiary paediatric centre; also assessed benefit of continuing same therapy in non-responders |
| [NCT01834820](https://clinicaltrials.gov/study/NCT01834820) | Phase 4 | Completed | 120 | Pilot RCT evaluating epinephrine + dexamethasone + hypertonic saline triple combination to reduce hospitalisation rate in infant bronchiolitis |
| [NCT01705964](https://clinicaltrials.gov/study/NCT01705964) | Phase 4 | Completed | 49 | RCT assessing intramuscular epinephrine as adjunct to inhaled β2-agonists for severe paediatric asthma exacerbation presenting to the emergency department |
| [NCT00114478](https://clinicaltrials.gov/study/NCT00114478) | N/A | Unknown | 600 | RCT comparing epinephrine vs albuterol (salbutamol) for treatment of bronchiolitis in children; one of the earliest large comparative trials for this indication |
| [NCT02586961](https://clinicaltrials.gov/study/NCT02586961) | Phase 2/3 | Terminated | 195 | Multicentre RCT evaluating high-dose oral betamethasone + nebulised adrenaline to reduce hospitalisation for acute bronchiolitis in the emergency department; terminated early but contributes to the evidence base |
| [NCT00622817](https://clinicaltrials.gov/study/NCT00622817) | N/A | Completed | 65 | Double-blind RCT comparing xylometazoline nasal drops vs inhaled epinephrine for bronchiolitis treatment in infants |
| [NCT01216553](https://clinicaltrials.gov/study/NCT01216553) | Phase 4 | Unknown | 135 | Case-control study of home oxygen management for acute bronchiolitis; includes nebulised epinephrine (0.1% in bromhexine) treatment arm alongside 3% hypertonic saline |
| [NCT01255709](https://clinicaltrials.gov/study/NCT01255709) | Phase 2 | Completed | 24 | Crossover pharmacokinetic study of Epinephrine Inhalation Aerosol HFA (E004 MDI) using deuterium-labelled epinephrine to characterise systemic PK profile in healthy adults |
| [NCT01143051](https://clinicaltrials.gov/study/NCT01143051) | Phase 1/2 | Completed | 24 | Phase I/II safety and PK study of Epinephrine Inhalation Aerosol USP (HFA-MDI, E004) in healthy adults under augmented dose conditions |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | Cochrane Systematic Review / Meta-analysis | Cochrane Database of Systematic Reviews | Comprehensive meta-analysis of bronchodilators for acute bronchiolitis; confirms short-term clinical benefit of nebulised epinephrine, particularly in outpatient/emergency settings |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | Earlier systematic review demonstrating that bronchodilators including epinephrine produce modest but meaningful short-term benefit in mild-to-moderate bronchiolitis |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Narrative Review | Expert Review of Respiratory Medicine | Decade-long review (2009–2018) of therapeutic strategies in paediatric bronchiolitis; specifically evaluates evidence for racemic epinephrine, corticosteroids, hypertonic saline, and high-flow oxygen |
| [19444115](https://pubmed.ncbi.nlm.nih.gov/19444115/) | 2009 | Clinical Review | Current Opinion in Pediatrics | Comprehensive update on epinephrine applications in paediatric emergency medicine including bronchiolitis and asthma; reviews current evidence and dosing recommendations |
| [19135584](https://pubmed.ncbi.nlm.nih.gov/19135584/) | 2009 | Clinical Review | Pediatric Clinics of North America | Review of acute bronchiolitis and croup management; notes evidence supporting temporary symptomatic benefit from nebulised adrenaline, and good evidence for corticosteroids in croup |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Clinical Review | BMJ Clinical Evidence | Overview of bronchiolitis epidemiology and management; contextualises epinephrine within the broader treatment decision-making framework |
| [19450362](https://pubmed.ncbi.nlm.nih.gov/19450362/) | 2007 | Clinical Review | BMJ Clinical Evidence | BMJ Clinical Evidence review of bronchiolitis including evidence base for bronchodilator use in infants presenting to hospital |
| [4606289](https://pubmed.ncbi.nlm.nih.gov/4606289/) | 1974 | Clinical Study | Clinical Pharmacology and Therapeutics | Comparative study of bronchodilator effects of terbutaline vs epinephrine in obstructive lung disease; foundational evidence for epinephrine's bronchodilator role |
| [30856157](https://pubmed.ncbi.nlm.nih.gov/30856157/) | 2019 | Drug Review | The Medical Letter on Drugs and Therapeutics | Review of OTC Primatene Mist (epinephrine HFA inhaler) return to the US market; provides regulatory and clinical context for epinephrine in asthma management |
| [11339733](https://pubmed.ncbi.nlm.nih.gov/11339733/) | 2001 | Systematic Review | Prehospital Emergency Care | Systematic review of subcutaneous epinephrine use in the prehospital setting for asthma and anaphylaxis, including evidence review for its use in older patients |

---

## Australia Market Information

The automated data query returned **0 ARTG entries** for Epinephrine (query date: 9 March 2026, market status recorded as "not marketed"). This almost certainly reflects a **limitation of the automated data collection** rather than actual absence from the Australian market — adrenaline/epinephrine preparations are firmly established in Australian clinical practice and regulatory frameworks, including auto-injectors (e.g., EpiPen), parenteral adrenaline, and inhalation formulations.

Clinicians should verify current ARTG registration status directly via the [TGA ARTG Public Summary Search](https://www.tga.gov.au/resources/artg) using the search term "adrenaline" or "epinephrine."

---

## Safety Considerations

No specific safety data (TGA warnings, contraindications, or drug interactions) was retrieved during this data collection cycle.

Please refer to the TGA-approved Product Information (PI) for comprehensive safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic basis and clinical evidence supporting Epinephrine for obstructive lung disease — particularly bronchiolitis and acute asthma — is well-established, with two Cochrane systematic reviews and a completed Phase 3 multicentre RCT (NCT03567473, n=864) providing L1 evidence. The TxGNN prediction score of 99.71% accurately reflects this existing pharmacological evidence base rather than identifying a novel association. The primary value of this repurposing assessment lies in optimising formulation, route, and patient population for a structured clinical development or regulatory pathway in Australia.

**To proceed, the following is needed:**
- Verify current ARTG registration status via a direct TGA database search for "adrenaline" and "epinephrine" products to confirm market access
- Retrieve TGA-approved Product Information (PI) documents to complete the formal safety and contraindication assessment
- Clarify target indication specifics — paediatric bronchiolitis (nebulised), adult acute asthma (inhaled MDI or IM), or COPD rescue therapy may each require separate regulatory pathways and evidence packages
- Obtain and review the final published results of NCT03567473 (Phase 3, n=864, completion date May 2025), which represent the highest-quality evidence for this indication
- Search ANZCTR (Australian New Zealand Clinical Trials Registry) directly for any Australian-specific trials not captured by this automated ClinicalTrials.gov query
- Conduct a formal mechanism of action (MOA) review via DrugBank API to complete the pharmacological rationale documentation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

