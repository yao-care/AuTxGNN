---
layout: default
title: Famciclovir
parent: 僅模型預測 (L5)
nav_order: 214
evidence_level: L5
indication_count: 10
---

# Famciclovir
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

# Famciclovir: From Herpes Zoster / Herpes Simplex to Post-Infectious Neuralgia

## One-Sentence Summary

Famciclovir is an orally active antiviral agent (prodrug of penciclovir) widely used internationally for the treatment of herpes zoster (shingles) and herpes simplex virus infections, though it is not currently registered with the TGA in Australia.
The TxGNN model predicts it may have utility for **Post-Infectious Neuralgia** (PHN — the persistent neuropathic pain that follows herpes zoster),
with **no directly applicable clinical trials** and **no supporting literature** identified for this specific indication, placing this prediction at **Evidence Level L4** based on mechanistic rationale alone.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Herpes zoster (shingles), herpes simplex virus infections |
| Predicted New Indication | Post-Infectious Neuralgia |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L4 (mechanistic rationale only) |
| Australia Market Status | Not marketed (not TGA-registered) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this Evidence Pack. Based on established pharmacology, Famciclovir is the oral prodrug of penciclovir — a nucleoside analogue that, once inside herpesvirus-infected cells, undergoes selective phosphorylation by the virus-encoded thymidine kinase (TK). The resulting penciclovir triphosphate is a potent, competitive inhibitor of viral DNA polymerase, with approximately 4,000-fold greater selectivity for the viral enzyme over host cell polymerases, causing viral DNA chain termination and halting replication.

Post-infectious neuralgia (PHN), defined as pain persisting beyond 90 days after herpes zoster rash resolution, arises from VZV-mediated damage to peripheral sensory neurons and dorsal root ganglia during the acute infection phase. The biological rationale connecting Famciclovir to PHN is therefore **indirect ("treat-to-prevent")**: by aggressively suppressing VZV replication early in the acute episode, Famciclovir may limit neuronal inflammation and ganglion destruction, thereby reducing the likelihood and severity of subsequent PHN. This concept is already embedded in standard clinical guidelines, where oral antivirals commenced within 72 hours of rash onset are recommended for high-risk patients (age >50, ophthalmic involvement, or immunocompromise).

However, this TxGNN prediction warrants careful interpretation. The high score of 99.75% most likely reflects the close disease-ontology relationship between herpes zoster and PHN in the knowledge graph — PHN is a direct sequela of the same viral infection Famciclovir treats — rather than an independent signal for direct PHN efficacy. Famciclovir has **no established direct effect on established neuropathic pain**, and this distinction is clinically critical.

---

## Clinical Trial Evidence

No clinical trials directly evaluating Famciclovir for post-infectious neuralgia were identified. The two retrieved trials investigate non-antiviral interventions for pain management and have no famciclovir component:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | NA | Unknown | 140 | Evaluates early oxycodone (opioid analgesic) during acute herpes zoster to prevent PHN — opioid analgesic intervention, not an antiviral study; no famciclovir component |
| [NCT06798662](https://clinicaltrials.gov/study/NCT06798662) | NA | Not Yet Recruiting | 120 | Multimodal nerve block with liposomal bupivacaine/ropivacaine plus pulse radiofrequency for acute herpes zoster pain — interventional pain procedure, no antiviral component |

> No clinical trials directly investigating Famciclovir for post-infectious neuralgia are registered.

---

## Literature Evidence

Currently no literature specifically investigating Famciclovir for post-infectious neuralgia is available.

---

## Safety Considerations

Please refer to international prescribing information (FDA/EMA-approved Product Information) for full safety details, as TGA-specific warnings, contraindications, and drug interaction data were not available in this Evidence Pack.

Famciclovir is a well-established antiviral with an extensive international safety record. Clinicians should be aware of the following when consulting the current international PI:

- **Renal impairment**: Dose adjustment is required based on creatinine clearance; penciclovir is renally eliminated
- **Pregnancy and lactation**: Category B3 in Australia's legacy classification; caution advised
- **Drug interactions**: No interactions were identified in the current search, but clinicians should verify against current references, particularly for patients on immunosuppressants or nephrotoxic agents

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
The TxGNN prediction most likely reflects the ontological proximity of PHN to herpes zoster in the knowledge graph, rather than an independent efficacy signal. No clinical evidence directly supports Famciclovir for *established* PHN, and Famciclovir is not currently registered with the TGA in Australia, making immediate clinical application challenging.

**To proceed, the following is needed:**

- **Clarify the clinical question**: Prevention of PHN during acute herpes zoster (where broad antiviral evidence already exists — including two completed Phase 3 trials for famciclovir in VZV infections; see chickenpox/herpes zoster evidence, rank #7 in the TxGNN predictions) versus direct treatment of *established* PHN (where no famciclovir evidence exists)
- **Prospective study design**: If the prevention question is pursued, design studies with PHN incidence as a primary endpoint, comparing famciclovir-treated versus untreated herpes zoster cohorts in Australian populations
- **Full MOA and safety data**: Obtain complete mechanism of action documentation and TGA-aligned product information to support any regulatory submission
- **TGA registration pathway**: Assess whether access via the Special Access Scheme (SAS Category B/C) or Authorised Prescriber pathway is required for any clinical use prior to formal TGA registration
- **Regulatory precedent review**: Note that famciclovir holds approved indications in multiple comparable jurisdictions (US FDA, EMA) for herpes zoster and HSV — a bridging data package may support an expedited TGA registration pathway

---

> ⚠️ **Important Notice**: This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. This report has been generated from the TxGNN AI prediction system (AuTxGNN) and should be reviewed by qualified healthcare professionals in conjunction with current TGA guidelines and approved Product Information.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

