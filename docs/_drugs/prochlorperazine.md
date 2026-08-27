---
layout: default
title: Prochlorperazine
parent: 僅模型預測 (L5)
nav_order: 562
evidence_level: L5
indication_count: 10
---

# Prochlorperazine
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

# Prochlorperazine: From Nausea/Vomiting and Psychotic Symptom Control to Manic Bipolar Affective Disorder

> **Note on candidate selection:** The evidence pack's top-scored prediction (rank 1, *retinal dystrophy with or without extraocular anomalies*, score 99.998%) and ranks 2–9 are all congenital/genetic disorders. The evidence pack's own analyst notes for every one of these state there is **no mechanistic link and no drug-specific literature or trial support** — they are flagged as likely knowledge-graph co-occurrence noise (`decision_stage: S0`, `recommendation: Hold`). This report therefore focuses on **rank 10, manic bipolar affective disorder**, the only prediction with a biologically plausible mechanism, a `decision_stage` of S1, and supporting literature.

## One-Sentence Summary

Prochlorperazine is a phenothiazine-class D2-receptor antagonist, used clinically for nausea/vomiting and psychotic symptom control. The TxGNN model predicts possible efficacy in **manic bipolar affective disorder**, a mechanistically plausible extension of its antipsychotic class effect, but the evidence base is currently limited to **0 clinical trials** and **12 pieces of literature** — mostly class-level reviews and case reports rather than drug-specific trial data.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in ARTG records — prochlorperazine is not currently marketed in Australia. Per evidence-pack rationale text, it is used clinically for nausea/vomiting and psychotic symptom control. |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed structured mechanism-of-action data is not available for prochlorperazine in this evidence pack (flagged as a High-severity data gap). Based on known information in the evidence pack's own rationale, prochlorperazine is a phenothiazine-class dopamine D2-receptor antagonist, in the same pharmacological family as first-generation antipsychotics such as chlorpromazine and haloperidol.

D2 antagonism is the established mechanism behind the antimanic efficacy of first-generation antipsychotics in acute mania — dopamine blockade reduces the excess dopaminergic transmission associated with manic states. This gives the TxGNN prediction a degree of biological plausibility that is absent from the model's higher-scored but mechanistically unrelated congenital-disease predictions.

However, prochlorperazine itself is not established as a first-line (or even routinely used) antimanic agent — it is used almost exclusively for nausea/vomiting and short-term psychotic/anxiety symptom control. The supporting literature reflects this: it is largely class-level evidence (phenothiazines/antipsychotics in general) rather than trial data on prochlorperazine specifically in mania. One historical case report (1959) does describe a confusional reaction to prochlorperazine in a patient with mild manic-depressive illness, but this documents an adverse psychiatric effect during use for another indication, not therapeutic efficacy in mania.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [13617778](https://pubmed.ncbi.nlm.nih.gov/13617778/) | 1959 | Case Report | Annales médico-psychologiques | Confusional dream-like episode caused by prochlorperazine in a patient with mild manic-depressive illness — direct drug-specific observation, but describes an adverse effect, not antimanic efficacy |
| [19461391](https://pubmed.ncbi.nlm.nih.gov/19461391/) | 2009 | Review | J Psychiatric Practice | Use and safety of antipsychotic drugs (class review) during pregnancy, incl. bipolar-spectrum indications |
| [15863814](https://pubmed.ncbi.nlm.nih.gov/15863814/) | 2005 | Review | American Journal of Psychiatry | Quetiapine discontinuation syndrome — antipsychotic class context |
| [26819726](https://pubmed.ncbi.nlm.nih.gov/26819726/) | 2015 | Pharmacovigilance/Adverse Event Analysis | J Pharmaceutical Health Care and Sciences | FAERS analysis of hyperglycaemic adverse events across dopamine-antagonist antipsychotics used in schizophrenia and bipolar disorder |
| [235013](https://pubmed.ncbi.nlm.nih.gov/235013/) | 1975 | Case Report | Journal of the Neurological Sciences | Tardive dyskinesia induced by phenothiazines, treated with pimozide — class-level toxicity data |
| [6069087](https://pubmed.ncbi.nlm.nih.gov/6069087/) | 1967 | Case Series | Neurology | Spontaneous seizures and EEG changes during phenothiazine therapy |
| [4238455](https://pubmed.ncbi.nlm.nih.gov/4238455/) | 1969 | Review | Clinical Pharmacology and Therapeutics | General review of psychotherapeutic drug use, including phenothiazines |
| [14233737](https://pubmed.ncbi.nlm.nih.gov/14233737/) | 1964 | Review/Survey | American Journal of Psychiatry | ECT combined with phenothiazines and reserpine — historical psychiatric management survey |
| [14242542](https://pubmed.ncbi.nlm.nih.gov/14242542/) | 1965 | Review | Obstetrics and Gynecology | Management of severe psychologic disorders of the puerperium, including phenothiazine use |
| [14222730](https://pubmed.ncbi.nlm.nih.gov/14222730/) | 1964 | Review | L'Encéphale | Psychodysleptic manifestations occurring during treatment with psycholeptic drugs |

## Australia Market Information

Prochlorperazine currently has no ARTG entries and is not marketed in Australia (0 licences on record).

## Safety Considerations

No structured safety data (key warnings, contraindications, or drug interactions) is currently available for this candidate, and this is flagged as a **Blocking** data gap (DG001) in the evidence pack. As prochlorperazine is not currently ARTG-listed, there is no Australian TGA-approved Product Information to reference; safety review would need to draw on comparable overseas regulatory documentation (e.g. UK/US product information) as an interim source.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Prochlorperazine is not currently marketed in Australia, and the manic bipolar affective disorder prediction — while mechanistically plausible — is supported only by class-level (phenothiazine/antipsychotic) literature rather than drug-specific trial evidence; no clinical trials exist for this indication. The model's higher-scored predictions (ranks 1–9) were assessed by the evidence pack itself as likely artifacts with no mechanistic or literature support and are not viable candidates.

**To proceed, the following is needed:**
- Confirmed original mechanism-of-action data (DG002, High severity)
- TGA/TFDA-equivalent product warnings and contraindications (DG001, Blocking severity) — required before any S1 safety screening can occur
- An Australian market-entry regulatory pathway assessment, since there are currently 0 ARTG entries
- Prospective or retrospective clinical evidence evaluating prochlorperazine specifically (not the phenothiazine class generally) in mania/bipolar disorder
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

