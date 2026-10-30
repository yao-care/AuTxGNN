---
layout: default
title: Cetrorelix
parent: Model Prediction Only (L5)
nav_order: 149
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Cetrorelix: predicted new indication Hypertrichosis (evidence level L5). Approved use: Inhibition of premature LH surges in women undergoing controlled ovar…"
monitor_inn: "Cetrorelix"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "persistent fetal circulation syndrome", "familial isolated trichomegaly", "familial male-limited precocious puberty", "aromatase excess syndrome", "centra precocious puberty 1"]
---

# Cetrorelix
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

## Cetrorelix: From Controlled Ovarian Stimulation (Fertility Treatment) to Hypertrichosis
{: .text-alpha }

## One-Sentence Summary

Cetrorelix is a GnRH receptor antagonist used to prevent premature LH surges in women undergoing controlled ovarian stimulation as part of fertility treatment.
The TxGNN model predicts it may be effective for **hypertrichosis**, but there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Inhibition of premature LH surges in women undergoing controlled ovarian stimulation (the ARTG indication text was not available in the data compiled for this report; this is taken from the pharmacology record) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| Australia Market Status | Listed on the PBS Schedule (1 of 1 items) – TGA (ARTG) registration status is not included in this data |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Cetrorelix is a peptide antagonist of the GnRH receptor (GNRHR). By blocking this receptor it suppresses LH and FSH release, which lowers gonadal sex hormone production, including androgens. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description draws on the pharmacology record.

In theory, lower androgen signalling could help androgen-dependent hirsutism. However, hypertrichosis is generally androgen-independent, so the mechanistic link is weak. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It is not backed by any clinical or literature data. It should be read as a hypothesis only.

The other top-ranked predictions are also doubtful:

- **Ambras type hypertrichosis universalis congenita, isolated genetic hair shaft abnormality and familial isolated trichomegaly:** these are gene-driven hair conditions. GnRH antagonism has no plausible direct effect on them, and the scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.
- **Malformation syndrome with odontal/periodontal component and syndrome with Dandy-Walker malformation:** these are structural developmental conditions with no identifiable mechanistic connection to GnRH blockade.
- **Persistent fetal circulation syndrome:** this neonatal pulmonary hypertension condition has no known GnRH pathway involvement, and cetrorelix has no neonatal indication or safety data.
- **Aromatase excess syndrome:** the problem lies downstream of the GnRH axis, and aromatase inhibitors are the mechanistically appropriate approach.
- **Familial male-limited precocious puberty:** this is the most hormonally relevant prediction, flagged as a research question. It is caused by activating LHCGR mutations that act independently of gonadotropins, so a GnRH antagonist acting upstream is unlikely to work. Standard treatment uses antiandrogens plus aromatase inhibitors.
- **Central precocious puberty 1:** this was not yet assessed (score 0.9929).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 9599F | Cetrotide | Powder for injection 250 micrograms (as acetate) with diluent | Not available in the data compiled for this report |

Cetrorelix is available in Australia only as an injectable.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Warnings and contraindications were not available in the data compiled for this report.

The only interaction-type record is pharmacological: cetrorelix acts on the human GnRH1 receptor (GNRHR). No drug-drug interactions were identified.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for hypertrichosis has a very high model score but no clinical trials or literature, and the mechanistic link is weak because hypertrichosis is generally androgen-independent. Evidence is at L5 (model prediction only).

**To proceed, the following is needed:**
- Retrieval of the TGA Product Information to confirm the approved indication, warnings and contraindications
- Mechanism-of-action data from DrugBank
- A literature and trial search for GnRH antagonists in hypertrichosis and hirsutism, to find any human or preclinical evidence
- If the hormonal predictions are pursued, a focused review of central precocious puberty (the most biologically plausible target, though it has not yet been assessed) and of whether cetrorelix offers any advantage over established GnRH agonists
- Assessment of route and formulation compatibility (cetrorelix is injectable only in Australia) and of the paediatric safety data that any of these predicted conditions would require
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

