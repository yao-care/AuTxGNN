---
layout: default
title: Buprenorphine
parent: 僅模型預測 (L5)
nav_order: 108
evidence_level: L5
indication_count: 10
---

# Buprenorphine
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

# Buprenorphine: From Opioid Use Disorder to Schizophrenia

## One-Sentence Summary

Buprenorphine is a partial opioid agonist-antagonist established globally for the treatment of opioid use disorder (OUD) and pain management, though it holds no current TGA registration in Australia. The TxGNN model generated 10 predicted new indications; **Schizophrenia** presents the strongest evidence base among them, supported by **4 clinical trials** — including an active Phase 2 trial specifically targeting schizophrenia — and **20 publications**, making it the only indication meeting the threshold for further clinical consideration. The TxGNN prediction score is **98.98%** with an evidence level of **L2**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Opioid use disorder; pain management (not currently TGA-registered in Australia) |
| Predicted New Indication | Schizophrenia |
| TxGNN Prediction Score | 98.98% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank was not available for this evaluation. Based on established international pharmacology, buprenorphine is a partial agonist at the mu-opioid receptor (MOR) and — critically for this repurposing hypothesis — an **antagonist at the kappa-opioid receptor (KOR)**. It also exhibits partial agonism at the ORL1 (nociceptin) receptor. These properties form the mechanistic basis for predicting efficacy in schizophrenia.

Emerging translational evidence has firmly implicated the dynorphin/KOR pathway in the pathophysiology of schizophrenia. Overactivation of KOR by endogenous dynorphins suppresses dopamine neurotransmission in the prefrontal cortex, contributing to the **negative symptoms** (social withdrawal, avolition, blunted affect) and **cognitive impairment** that respond poorly to conventional D2-blocking antipsychotics. Buprenorphine's KOR antagonism could theoretically reverse this suppression, restoring prefrontal dopaminergic tone through a mechanism that is complementary to — rather than competing with — existing antipsychotic therapies. Additionally, its partial MOR agonism may modulate the social reward circuitry disrupted in schizophrenia, which aligns directly with the endpoint design of the currently recruiting Phase 2 trial (NCT05778591).

Importantly, this hypothesis is not purely speculative. A 1987 controlled clinical study (*American Journal of Psychiatry*, PMID 3310672) reported a **pronounced antipsychotic effect** in 10 neuroleptic-free patients with hallucinations, delusions, and formal thought disorders — including those with schizophreniform disorder and paranoid schizophrenia. A 2020 meta-analysis (PMID 32516800) subsequently confirmed across placebo-controlled trials that opioid antagonists, including buprenorphine, are associated with a significant reduction in both positive and negative symptoms of schizophrenia. The active registration of NCT05778591 since May 2024 confirms that the international research community has accepted this as a credible and clinically testable hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT05778591](https://clinicaltrials.gov/study/NCT05778591) | Phase 2 | Recruiting | 40 | Low-dose buprenorphine as a modulator of social motivation in schizophrenia — directly targets negative symptom domain (approach vs avoidance motivation) via KOR antagonism; estimated completion April 2026 |
| [NCT01407575](https://clinicaltrials.gov/study/NCT01407575) | Phase 3 | Completed | 13 | Buprenorphine vs placebo for treatment-resistant depression — indirect psychiatric evidence sharing the same KOR antagonism mechanism; completed August 2013; very small sample (n=13) substantially limits conclusions |
| [NCT05594121](https://clinicaltrials.gov/study/NCT05594121) | Phase 4 | Unknown | 90 | Subcutaneous buprenorphine depot (Sublocade®) vs daily sublingual buprenorphine/naloxone (Suboxone®) for OUD — provides formulation-specific adherence and safety data relevant to psychiatric populations who may benefit from depot delivery |
| [NCT00723697](https://clinicaltrials.gov/study/NCT00723697) | N/A | Completed | 1307 | Prospective real-world observational study of high-dose buprenorphine (BHD) for major opioid dependence — large-scale pharmacovigilance database including psychiatric adverse events, misuse patterns, and co-occurring mental illness |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [3310672](https://pubmed.ncbi.nlm.nih.gov/3310672/) | 1987 | Clinical Study | American Journal of Psychiatry | Buprenorphine demonstrated a pronounced antipsychotic effect (~4 hours duration) in 10 neuroleptic-free schizophrenic patients including those with schizophreniform disorder and paranoid schizophrenia — foundational proof-of-concept data |
| [32516800](https://pubmed.ncbi.nlm.nih.gov/32516800/) | 2020 | Meta-analysis | Neuropsychopharmacology | Meta-analysis of placebo-controlled trials of opioid antagonists (naloxone, naltrexone, nalmefene, buprenorphine) in schizophrenia — confirms statistically significant reduction in both positive and negative symptoms |
| [33459877](https://pubmed.ncbi.nlm.nih.gov/33459877/) | 2022 | Mechanistic Review | Handbook of Experimental Pharmacology | Comprehensive translational review of dynorphin/KOR pathway dysfunction in schizophrenia and major depression — provides the theoretical framework underpinning the entire repurposing rationale |
| [34286498](https://pubmed.ncbi.nlm.nih.gov/34286498/) | 2021 | Systematic Review | European Review for Medical and Pharmacological Sciences | Systematic review of psychotic symptoms following buprenorphine and other opioid withdrawal — key safety signal: abrupt buprenorphine cessation may precipitate transient psychosis |
| [31101511](https://pubmed.ncbi.nlm.nih.gov/31101511/) | 2019 | Cohort Study | Schizophrenia Research | Real-world cohort data on methadone and buprenorphine use in patients with schizophrenia — documents clinical feasibility, co-prescription patterns, and tolerability in this dual-diagnosis population |
| [40600600](https://pubmed.ncbi.nlm.nih.gov/40600600/) | 2025 | Case Analysis | Journal of Addiction Medicine | Reports a critical drug interaction between buprenorphine and olanzapine/samidorphan (Lybalvi®) — important safety alert for co-prescription in schizophrenia management |
| [25392062](https://pubmed.ncbi.nlm.nih.gov/25392062/) | 2014 | Case Report + Review | Journal of Dual Diagnosis | Review of opiate dependence in schizophrenia — characterises the clinical complexity and key therapeutic considerations for this dual-diagnosis population |
| [38023343](https://pubmed.ncbi.nlm.nih.gov/38023343/) | 2023 | Cohort Study | Drug and Alcohol Dependence Reports | Insurance claims analysis of buprenorphine initiation and discontinuation in OUD patients with co-occurring psychiatric disorders including schizophrenia — real-world utilisation data |
| [15982997](https://pubmed.ncbi.nlm.nih.gov/15982997/) | 2005 | Review | Journal of Psychopharmacology | Reviews partial agonism as a therapeutic modality in psychiatric disorders — provides pharmacological rationale for partial opioid agonists including buprenorphine in psychiatry |
| [40582093](https://pubmed.ncbi.nlm.nih.gov/40582093/) | 2025 | Systematic Review | Drug and Alcohol Dependence | Systematic review and meta-analysis on mental disorder comorbidity and opioid agonist treatment (OAT) retention — quantifies the impact of schizophrenia on buprenorphine treatment continuity |

---

## Australia Market Information

Buprenorphine is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)**. There are no ARTG product entries for buprenorphine in Australia at the time of this evaluation.

> **Note for Australian clinicians:** Although buprenorphine lacks a current ARTG listing, access may be available through the **TGA Special Access Scheme (SAS)** or **Authorised Prescriber (AP)** pathways for specific patient circumstances. Buprenorphine is a **Schedule 8 Controlled Drug** in Australia, requiring additional prescriber authority under relevant state and territory legislation. Clinicians should consult the TGA website (www.tga.gov.au) and their state/territory health authority for current requirements before prescribing.

---

## Safety Considerations

Please refer to international prescribing information (e.g., US FDA prescribing information, EMA Summary of Product Characteristics) for comprehensive safety data, as no TGA-approved Australian Product Information is available.

Key considerations particularly relevant to the schizophrenia indication, based on available literature:

- **Buprenorphine withdrawal may precipitate psychosis**: A systematic review (PMID 34286498) confirms that abrupt buprenorphine discontinuation can trigger transient psychotic symptoms — of direct clinical relevance when initiating or ceasing treatment in patients with schizophrenia.
- **Drug interaction with samidorphan-containing antipsychotics**: Co-prescription of buprenorphine with olanzapine/samidorphan (Lybalvi®) — an antipsychotic approved for schizophrenia — carries a significant risk of precipitated opioid withdrawal and pharmacodynamic antagonism (PMID 40600600).
- **Standard opioid-class risks**: Respiratory depression, CNS sedation, and dependence potential are class effects applicable to all clinical settings, including psychiatric inpatient environments.
- **Schedule 8 obligations**: All prescribing, dispensing, and monitoring in Australia must comply with Schedule 8 controlled substance requirements under state and territory law.

---

## Other TxGNN Predicted Indications (Summary)

The TxGNN model returned 10 predicted indications in this multi-candidate report. All nine remaining indications are rated **Hold** due to insufficient evidence, absent mechanistic support, or potential safety concerns. They are not recommended for clinical development at this time.

| Rank | Indication | TxGNN Score | Evidence Level | Recommendation | Assessment |
|------|-----------|-------------|---------------|---------------|-----------|
| 1 | Acute intermittent porphyria | 99.41% | L5 | Hold | One anaesthesia case report (PMID 8301837); buprenorphine used *safely in* AIP, not *as treatment for* AIP — prediction likely reflects pain pathway co-occurrence in knowledge graph |
| 2 | Lingual-facial-buccal dyskinesia | 99.32% | L4 | Hold | Highly speculative KOR/dopamine inference; no clinical trials; literature is largely unrelated to the indication |
| 3 | Chronic tic disorder | 99.13% | L5 | Hold | One case series on heroin addiction in Tourette syndrome (PMID 30395551); no evidence of buprenorphine as a tic treatment |
| 4 | Continuous spikes and waves during sleep | 99.05% | L5 | Hold | No evidence; opioids may lower seizure threshold — potential safety concern in this paediatric epilepsy syndrome |
| 5 | Benign shuddering attacks | 99.03% | L5 | Hold | No evidence; self-limiting paediatric condition with no known opioid pathway involvement |
| 6 | Extrapyramidal and movement disease | 99.03% | L5 | Hold | Indication too broad to assess meaningfully; no specific evidence for any subtype |
| 7 | Schizophreniform disorder | 98.99% | L4 | Research Question | Mechanistically plausible extrapolation from schizophrenia evidence; requires independent study before clinical consideration |
| 9 | Benign paroxysmal tonic upgaze with ataxia | 98.91% | L5 | Hold | Rare paediatric condition; no evidence; no plausible opioid pathway link |
| 10 | Psychogenic movement disorders | 98.89% | L5 | Hold | No evidence; functional neurological disorder with no established direct treatment rationale for buprenorphine |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Buprenorphine's KOR antagonism provides a mechanistically well-grounded and novel approach to treating schizophrenia's negative symptoms — a domain inadequately addressed by current antipsychotics. Early clinical proof-of-concept (PMID 3310672, 1987) and a confirmatory meta-analysis (PMID 32516800, 2020) provide an evidence foundation above the threshold of speculation, while the active Phase 2 trial (NCT05778591) signals international clinical confidence. The absence of completed Phase 3 schizophrenia-specific trials and Australia's lack of TGA registration are the primary barriers to broader adoption.

**To proceed, the following is needed:**
- **Await NCT05778591 results** (Phase 2, estimated completion April 2026) — this is the pivotal next data point before any Australian clinical programme can be designed
- **Establish a TGA access pathway**: Assess eligibility for Special Access Scheme (SAS Category B) or Authorised Prescriber status to enable clinical research or compassionate access in Australia
- **Conduct a comprehensive drug–drug interaction review** with antipsychotics commonly used in Australian clinical practice (quetiapine, olanzapine, risperidone, clozapine) — particularly given the samidorphan interaction signal
- **Develop an Australian Phase 2/3 investigator-initiated trial (IIT)** if NCT05778591 yields positive results, prioritising validated negative symptom endpoints (e.g., PANSS negative subscale, BNSS)
- **Engage addiction medicine specialists** from the outset, given buprenorphine's Schedule 8 status and the clinical complexity of managing opioid pharmacotherapy in a psychiatric population
- **Obtain full MOA and safety data from DrugBank** to complete the mechanistic and safety review (Data Gaps DG001, DG002 identified in this Evidence Pack)

> ⚠️ *This report is intended for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before any therapeutic application. Prescribers must comply with applicable TGA and state/territory regulations.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

