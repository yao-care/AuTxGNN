---
layout: default
title: Epinephrine
parent: Model Prediction Only (L5)
nav_order: 258
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "Epinephrine"
predicted_indications: ["obstructive lung disease", "Rienhoff syndrome", "respiratory malformation"]
description: "Epinephrine: predicted new indication Obstructive lung disease (evidence level L5). In Australia: 10 PBS items (10 currently listed)"
---

# Epinephrine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Epinephrine: Obstructive lung disease
{: .text-alpha }

## One-Sentence Summary

Epinephrine (adrenaline) is a non-selective adrenergic agonist, originally used for anaphylaxis, asthma, bronchitis, bronchiectasis, pulmonary emphysema, hypotensive disorders and open-angle glaucoma.
The TxGNN model predicts it may be effective for **obstructive lung disease**, with **16 clinical trials** and **20 publications** currently supporting this direction.
Much of this is an on-label or near-label extension rather than true repurposing, and several Phase 3 trials concern an inhaled formulation, not the injectable product registered in Australia.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Obstructive lung disease |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (10 of 10 items) – TGA (ARTG) registration status is not included in this data |
| Number of PBS Items | 10 (valid: 10) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for epinephrine: "Epinephrine acts on both alpha and beta-adrenergic receptors. Through its action on alpha-adrenergic receptors, epinephrine lessens the vasodilation and increased vascular permeability that occurs during anaphylaxis, which can lead to loss of intravascular fluid volume and hypotension." ([DailyMed: Auvi-Q (epinephrine) prescribing information, Sportpharm LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5f40988b-8365-4f7b-84d1-b88e053725cf), label version 2026-09-18; accessed 2026-11-19.) Based on known pharmacology, epinephrine is a non-selective alpha/beta-adrenergic agonist. Beta-2 receptor activation relaxes bronchial smooth muscle and produces bronchodilation, while alpha-1 activation reduces mucosal oedema.

Asthma, bronchiectasis and emphysema are already among epinephrine's original indications, so extending to obstructive lung disease (which includes asthma and COPD) is largely a class effect. It is better seen as consolidation of existing use than as a new therapeutic direction.

An important caveat: the Phase 3 trials listed below mostly test an inhaled HFA metered-dose inhaler (E004), not the injectable epinephrine registered in Australia. The evidence therefore supports the drug's pharmacology, but does not directly establish efficacy of the injectable product for this indication.

---

## Clinical Trial Evidence

Ten of the 16 trials registered are shown below, prioritising those most relevant to obstructive airway disease.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01357642](https://clinicaltrials.gov/study/NCT01357642) | Phase 3 | Completed | 373 | 12-week efficacy and safety of epinephrine HFA inhaler vs placebo and Primatene Mist in adolescents and adults with asthma |
| [NCT01476904](https://clinicaltrials.gov/study/NCT01476904) | Phase 3 | Completed | 208 | 3-month safety extension of the E004-C study, giving 6-month safety data |
| [NCT01460511](https://clinicaltrials.gov/study/NCT01460511) | Phase 3 | Completed | 70 | 4-week placebo-controlled study of E004 in children aged 4-11 with asthma |
| [NCT01737905](https://clinicaltrials.gov/study/NCT01737905) | Phase 3 | Completed | 28 | Single-dose crossover study of E004 in children with asthma (small sample) |
| [NCT01705964](https://clinicaltrials.gov/study/NCT01705964) | Phase 4 | Completed | 49 | Intramuscular epinephrine as an adjunct to inhaled beta-2 agonists in severe paediatric asthma exacerbation |
| [NCT04207840](https://clinicaltrials.gov/study/NCT04207840) | Phase 4 | Completed | 28 | Systemic exposure of Primatene Mist vs intramuscular epinephrine and ProAir in healthy adults (pharmacokinetic) |
| [NCT01255709](https://clinicaltrials.gov/study/NCT01255709) | Phase 2 | Completed | 24 | Pharmacokinetics of inhaled epinephrine (E004) in healthy volunteers |
| [NCT01834820](https://clinicaltrials.gov/study/NCT01834820) | Phase 4 | Completed | 120 | Epinephrine, dexamethasone and hypertonic saline in infant bronchiolitis |
| [NCT00817466](https://clinicaltrials.gov/study/NCT00817466) | Phase 4 | Unknown | 500 | Optimal inhalation treatment for infants aged 0-12 months with acute bronchiolitis |
| [NCT00114478](https://clinicaltrials.gov/study/NCT00114478) | N/A | Unknown | 600 | Epinephrine vs albuterol in bronchiolitis |

---

## Literature Evidence

Ten of the 20 publications are shown, prioritising systematic reviews and randomised trials.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35093318](https://pubmed.ncbi.nlm.nih.gov/35093318/) | 2022 | RCT | J Pediatr | Corticosteroids plus inhaled epinephrine vs standard care in children with bronchiolitis in intensive care |
| [33893229](https://pubmed.ncbi.nlm.nih.gov/33893229/) | 2021 | Network meta-analysis | Pediatrics | Comparative efficacy of bronchiolitis interventions in acute care |
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Epinephrine for bronchiolitis |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Earlier Cochrane review of epinephrine for bronchiolitis |
| [35953216](https://pubmed.ncbi.nlm.nih.gov/35953216/) | 2022 | Review | Emerg Med Clin North Am | Evaluation and management of asthma and COPD exacerbations in the emergency department |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Review | Expert Rev Respir Med | Role of racemic epinephrine, corticosteroids, hypertonic saline and high-flow oxygen in infant bronchiolitis |
| [21157348](https://pubmed.ncbi.nlm.nih.gov/21157348/) | 2011 | Review | Curr Opin Pediatr | Update on bronchiolitis management; no treatment conclusively alters disease course |
| [23393929](https://pubmed.ncbi.nlm.nih.gov/23393929/) | 2012 | Review | Duodecim | Bronchiolitis overview, including inhaled racemic epinephrine when required |
| [11940264](https://pubmed.ncbi.nlm.nih.gov/11940264/) | 2002 | Review | Crit Care | Clinical review of severe asthma |
| [20876171](https://pubmed.ncbi.nlm.nih.gov/20876171/) | 2010 | Economic analysis | Pediatrics | Cost-effectiveness of epinephrine and dexamethasone in bronchiolitis |

---

## Australia Market Information

<!-- licenses:begin -->

| PBS Item Code | Product Name | Ingredients | Dosage Form | Status |
|------|------|------|------|------|
| 1016L | Link Medical Products Pty Ltd | Adrenaline (epinephrine) | Injection 1 mg (as acid tartrate) in 1 mL (1 in 1,000) | Valid |
| 3451P | Link Medical Products Pty Ltd | Adrenaline (epinephrine) | Injection 1 mg (as acid tartrate) in 1 mL (1 in 1,000) | Valid |
| 5004J | Link Medical Products Pty Ltd | Adrenaline (epinephrine) | Injection 1 mg (as acid tartrate) in 1 mL (1 in 1,000) | Valid |
| 8697R | EpiPen Jr. | Adrenaline (epinephrine) | I.M. injection 150 micrograms in 0.3 mL single dose syringe auto-injector | Valid |
| 8698T | EpiPen | Adrenaline (epinephrine) | I.M. injection 300 micrograms in 0.3 mL single dose syringe auto-injector | Valid |
| 12655C | Anapen 500 | Adrenaline (epinephrine) | I.M. injection 500 micrograms in 0.3 mL single dose syringe auto-injector | Valid |
| 15355E | Jext | Adrenaline (epinephrine) | I.M. injection 300 micrograms in 0.3 mL (as acid tartrate) single dose syringe auto-injector | Valid |
| 15359J | Jext Jnr | Adrenaline (epinephrine) | I.M. injection 150 micrograms in 0.15 mL (as acid tartrate) single dose syringe auto-injector | Valid |
| 15404R | neffy | Adrenaline (epinephrine) | Nasal spray device 2 mg in 1 actuation | Valid |
| 15414G | neffy | Adrenaline (epinephrine) | Nasal spray device 1 mg in 1 actuation | Valid |

Source: PBS Schedule, PBS public data API (Department of Health, Disability and Ageing); product names, ingredients and dosage forms as recorded there. "Valid" means the item is on the current PBS Schedule; TGA (ARTG) registration status is not included in these data.

<!-- licenses:end -->

The listed products are injections and a nasal spray (neffy). No inhaled epinephrine product appears in the data, which limits the direct applicability of the inhaled-formulation trials.

<!-- review:begin au-lic-20261117-epinephrine-1 -->

> **Review correction (2026-11-17)**: Originally stated: "The only registered product is an injectable. No inhaled epinephrine product appears in the data, which limits the direct applicability of the inhaled-formulation trials." Corrected: the earlier wording described the dosage forms of only the PBS items originally collected for this page. The current PBS items for this ingredient include other dosage forms (PBS public data API, Schedule effective 2026-11-01). PBS listing does not show TGA (ARTG) registration status. Source: [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/).

<!-- review:end au-lic-20261117-epinephrine-1 -->

---

## Safety Considerations

**Contraindications flagged in the TxGNN knowledge graph** (these come from graph edges, not product label text, and should be verified against the Product Information):
- Cardiovascular: hypertension, coronary artery disease, myocardial infarction, atrial fibrillation, heart conduction disease, sudden cardiac arrest, other heart disease
- Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hyperthyroidism, potassium deficiency
- Neurological: epilepsy, myasthenia gravis and neuromuscular junction disease
- Ocular: angle-closure glaucoma
- Organ function: liver disease and failure, kidney disease, respiratory failure, gallbladder disease
- Other: benign prostatic hyperplasia, hemoglobinopathy, butyrylcholinesterase deficiency, pyoureter

**Drug Interactions:** 100 interactions were identified. Major-level examples include the tricyclic antidepressants **amitriptyline** and **amoxapine**. Moderate-level examples include other beta-agonists (formoterol, salbutamol, arformoterol), beta-blockers (atenolol, acebutolol, betaxolol), stimulants (amphetamine, methylphenidate, atomoxetine), antidiabetic agents (acarbose, alogliptin, acetohexamide, albiglutide) and antipsychotics (aripiprazole, asenapine, amisulpride).

Please refer to the TGA-approved Product Information (PI) for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Several completed Phase 3 trials support epinephrine in asthma, and the prediction largely overlaps with existing indications. However, those trials used an inhaled formulation not registered in Australia, and the injectable product's ARTG entry carries no indication text.

**To proceed, the following is needed:**
- Review of the TGA Product Information to confirm approved indications, warnings and contraindications
- Clarification of route and formulation: whether the evidence applies to the injectable product or would require an inhaled product
- Mechanism of action data to complete the evidence summary
- A safety monitoring plan for patients with cardiovascular, metabolic and other comorbidities flagged above
- Review of high-risk interactions (tricyclic antidepressants, beta-blockers) before clinical use

---

## Other Predicted Indications (Brief Note)

| Predicted Indication | Evidence Level | Suggested Status |
|------|------|------|
| Laryngotracheitis (croup) | L1 | Proceed with Guardrails (established rescue therapy; one Phase 4 trial of unknown status plus published RCT evidence) |
| Food-dependent exercise-induced anaphylaxis | L4 | Research Question (strong mechanistic rationale, but evidence is reviews and case reports only) |
| Pseudoallergy | L4 | Research Question (indirect support only) |
| Respiratory malformation | L3 | Research Question (single trial in transient tachypnoea of the newborn, which is not a structural malformation) |
| Dry eye syndrome | L5 | Hold (preclinical data suggest adrenergic stimulation may worsen the condition) |
| Headache disorder | L5 | Hold (observational data only; headache is a known adverse effect) |
| Trigeminal autonomic cephalalgia | L5 | Hold (observational pathophysiology only) |
| Rienhoff syndrome | L5 | Hold (no supporting data; likely a model artefact) |
| Anorectal stricture | L5 | Hold (no supporting data) |

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Australian data (the PBS Schedule of the Department of Health and Aged Care, and the TGA's ARTG). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-17 | Corrected: dosage forms updated to the current PBS Schedule | Corrected | [PBS public data API – items, Schedule 4753 (effective 2026-11-01) (Department of Health, Disability and Ageing)](https://data-api.health.gov.au/pbs/api/v3/items); [PBS Schedule](https://www.pbs.gov.au/) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Auvi-Q (epinephrine) prescribing information, Sportpharm LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5f40988b-8365-4f7b-84d1-b88e053725cf) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

