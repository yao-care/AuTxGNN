---
layout: default
title: Naloxone
parent: Model Prediction Only (L5)
nav_order: 492
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Naloxone: predicted new indication Top-ranked: continuous spikes and waves during sleep. Best-evidenced:… (evidence level L5). Approved use: Opiate dependence, substance abuse/dependence, morphine de…"
monitor_inn: "Naloxone"
predicted_indications: ["continuous spikes and waves during sleep", "lissencephaly with cerebellar hypoplasia", "progressive encephalopathy with leukodystrophy due to DECR deficiency", "schizophreniform disorder", "nasal cavity disease", "psychotic disorder", "hypoglycemia", "acute pulmonary heart disease", "drug-induced dyskinesia", "acute laryngopharyngitis"]
---

# Naloxone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Naloxone: From Opioid Dependence to Hypoglycaemia (Impaired Awareness)

## One-Sentence Summary

Naloxone is an opioid receptor antagonist, originally used for opioid dependence and substance abuse and, in practice, for reversing opioid overdose.
The TxGNN model's top-ranked prediction is **continuous spikes and waves during sleep**, but this has no supporting evidence. The best-supported candidate is **hypoglycaemia (prevention of hypoglycaemia-associated autonomic failure)**, with **3 small, terminated clinical trials** and **20 publications**.
Overall evidence is early and limited, so this report presents the highest-ranked prediction alongside the best-evidenced candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Opiate dependence, substance abuse/dependence, morphine dependence (from the knowledge graph; no approved indication text is available for the Australian product) |
| Predicted New Indication | Top-ranked: continuous spikes and waves during sleep. Best-evidenced: hypoglycaemia (rank 7) |
| TxGNN Prediction Score | 88.2% (rank 1); 81.5% (hypoglycaemia, rank 7) |
| Evidence Level | L5 (rank 1); L2 (hypoglycaemia) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold (rank 1); Proceed with Guardrails limited to further research (hypoglycaemia) |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Naloxone is a well-known opioid receptor antagonist, which is the basis of its use in opioid dependence and overdose reversal.

**Top-ranked prediction (continuous spikes and waves during sleep):** No trials or literature were found, and no plausible mechanistic link between opioid antagonism and this sleep-related epileptic encephalopathy can be established. This is a model prediction only.

**Best-supported candidate (hypoglycaemia):** Opioid signalling blunts the body's counter-regulatory responses during low blood sugar. By blocking opioid receptors, naloxone may restore the hormonal and sympathoadrenal responses and so help prevent hypoglycaemia-associated autonomic failure (HAAF) and impaired awareness of hypoglycaemia. The target is prevention of HAAF, not treatment of an acute hypoglycaemic episode. Separate case reports of opioid-induced hypoglycaemia point in the same direction.

**Other candidates (ranks 4-9):**
- *Schizophreniform and psychotic disorders:* Based on the 1980s endogenous opioid hypothesis. Results were small, old and inconsistent, including a negative double-blind study in mania.
- *Drug-induced dyskinesia:* Primate models show naloxone reduces levodopa-induced dyskinesia, but human data are small and Cochrane reviews found no reliable benefit.
- *Nasal cavity disease, acute pulmonary heart disease:* The literature is indirect and likely reflects artefacts in the model.
- *Lissencephaly with cerebellar hypoplasia, DECR deficiency encephalopathy, acute laryngopharyngitis:* No evidence and no apparent mechanism.

---

## Clinical Trial Evidence

No trials are registered for the top-ranked prediction. The table below shows trials for the best-supported candidate (hypoglycaemia).

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02700048](https://clinicaltrials.gov/study/NCT02700048) | Phase 1/2 | Terminated | 11 | Intranasal naloxone vs saline during experimental hypoglycaemia, effect on next-day responses in impaired awareness of hypoglycaemia (most directly relevant; underpowered) |
| [NCT03608163](https://clinicaltrials.gov/study/NCT03608163) | Phase 4 | Terminated | 4 | Naloxone and diazoxide to prevent HAAF in healthy subjects; too small to draw conclusions |
| [NCT00678145](https://clinicaltrials.gov/study/NCT00678145) | Phase 2 | Terminated | 39 | Mechanisms of HAAF in type 1 diabetes; mechanistically relevant, but the naloxone-specific design is not confirmed |

For psychotic disorder, one early Phase 1 trial, [NCT01591629](https://clinicaltrials.gov/study/NCT01591629) (completed, n=6), examined opioid antagonism and the effects of THC in cannabis use disorder. It is not a trial of psychosis treatment and has low relevance.

No ANZCTR trials were identified in the data compiled for this report.

---

## Literature Evidence

Hypoglycaemia (best-supported candidate):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39026458](https://pubmed.ncbi.nlm.nih.gov/39026458/) | 2025 | Clinical trial report | J Clin Endocrinol Metab | Effects of intranasal naloxone on HAAF in susceptible individuals; opioid blockade with IV naloxone ameliorates HAAF experimentally but is not feasible therapeutically |
| [39331519](https://pubmed.ncbi.nlm.nih.gov/39331519/) | 2025 | Review/Commentary | J Clin Endocrinol Metab | Discusses whether intranasal naloxone can prevent HAAF |
| [20811039](https://pubmed.ncbi.nlm.nih.gov/20811039/) | 2011 | Preclinical | Diabetes | Naloxone, but not valsartan, preserved responses to hypoglycaemia after antecedent hypoglycaemia |
| [37106491](https://pubmed.ncbi.nlm.nih.gov/37106491/) | 2023 | Case report | Adv Emerg Nurs J | Possible opioid-induced hypoglycaemia and the potential role of naloxone |
| [23467779](https://pubmed.ncbi.nlm.nih.gov/23467779/) | 2013 | Preclinical (mouse) | Cell Mol Neurobiol | Methadone-induced hypoglycaemia in mice, antagonised by naloxone |

Psychosis-related candidates (schizophreniform and psychotic disorders):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6121545](https://pubmed.ncbi.nlm.nih.gov/6121545/) | 1982 | Double-blind clinical study | Arch Gen Psychiatry | WHO collaborative study: symptom reduction in schizophrenic patients on neuroleptics (n=19), not in medication-free patients |
| [7435717](https://pubmed.ncbi.nlm.nih.gov/7435717/) | 1980 | Clinical study (negative) | Am J Psychiatry | Naloxone failed to reduce manic symptoms |
| [24733134](https://pubmed.ncbi.nlm.nih.gov/24733134/) | 2014 | Case report | Am J Health Syst Pharm | Nalbuphine-induced psychosis resolved with naloxone (drug-induced scenario) |

Drug-induced dyskinesia:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12804390](https://pubmed.ncbi.nlm.nih.gov/12804390/) | 2003 | Cochrane review | Cochrane Database Syst Rev | Miscellaneous treatments for tardive dyskinesia; no reliable evidence of benefit |
| [12373562](https://pubmed.ncbi.nlm.nih.gov/12373562/) | 2002 | Preclinical (primate) | J Neural Transm | Naloxone reduced levodopa-induced dyskinesias in marmoset models |
| [3070611](https://pubmed.ncbi.nlm.nih.gov/3070611/) | 1988 | Clinical study | Psychiatry Res | High-dose IV naloxone in 20 patients with tardive dyskinesia |

Nasal cavity disease: one observational paper ([28829521](https://pubmed.ncbi.nlm.nih.gov/28829521/), 2017) examined nasal obstruction as a barrier to intranasal naloxone delivery. It does not show that naloxone treats nasal disease.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 10783M | Naloxone Hydrochloride (DBL) | Injection containing naloxone hydrochloride 400 micrograms in 1 mL ampoule | Not available in the data compiled for this report |

Only an injectable form is registered in the data compiled. This may limit practical use for chronic or preventive indications, such as the intranasal route studied in HAAF.

---

## Safety Considerations

**Contraindication-related disease associations (knowledge graph, not label text):** The knowledge graph links naloxone with caution or contraindication in the following groups, which should be verified against the Product Information:
- Cardiovascular: long QT syndrome, torsades de pointes, sudden cardiac arrest, heart conduction disease, orthostatic hypotension, hypotensive disorder, postural orthostatic tachycardia syndrome, multiple system atrophy
- Neurological/respiratory: epilepsy, chronic obstructive pulmonary disease, respiratory failure
- Hepatic/renal: liver disease, kidney disease, chronic hepatitis B and C infection, gallbladder disease
- Endocrine: adrenal insufficiency, Addison disease, hypothyroidism, myxoedema
- Other: inflammatory bowel disease, benign prostatic hyperplasia

**Drug Interactions:** 88 interactions were identified. The main ones are:
- **Major:** droperidol
- **Moderate:** opioid agonists, including fentanyl, morphine, codeine, tramadol, oxycodone, methadone, hydrocodone, alfentanil, remifentanil and sufentanil; and opioid-related agents such as methylnaltrexone, naldemedine, naloxegol, butorphanol and binimetinib
- **Minor:** hydrocortisone

Naloxone can precipitate withdrawal in opioid-dependent patients. Preclinical data also report naloxone-induced seizures in the context of encephalitis. Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold for the top-ranked prediction (continuous spikes and waves during sleep). Proceed with Guardrails, as a research question only, for hypoglycaemia (HAAF prevention).**

**Rationale:**
- The top-ranked prediction rests on a model score alone, with no trials, no literature and no plausible mechanism.
- Hypoglycaemia is the only candidate with directly relevant trials and recent publications, but all three trials were terminated with small enrolments (4, 11 and 39), so efficacy is unproven.
- The remaining candidates rely on old, small or inconsistent studies, or on indirect and likely artefactual associations.

**To proceed, the following is needed:**
- A larger, adequately powered randomised controlled trial of intranasal naloxone for HAAF or impaired awareness of hypoglycaemia
- Review of the full results of NCT02700048 and the 2025 clinical trial report (PMID 39026458)
- Detailed mechanism-of-action data
- TGA-approved Product Information, including the approved indication text, warnings and contraindications
- Assessment of route availability, since only an injectable product is currently registered in Australia
- A safety plan covering withdrawal precipitation in opioid-dependent patients, cardiovascular risk, and interactions with opioids and droperidol
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

