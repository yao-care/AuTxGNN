---
layout: default
title: Telmisartan
parent: Model Prediction Only (L5)
nav_order: 656
evidence_level: L5
indication_count: 10
---

# Telmisartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Telmisartan: From Hypertension to Prinzmetal Angina

## One-Sentence Summary

Telmisartan (DrugBank DB00966) is an angiotensin II receptor blocker (ARB) conventionally used for hypertension; no original-indication text is recorded in this evidence pack, so this is inferred from its DrugBank classification only.
The TxGNN model predicts it may be effective for **Prinzmetal angina**, with a prediction score of **99.98%**, but **no clinical trials and no literature** currently support this specific link.
This is a model-only signal (Evidence Level L5) and should not be acted on without further investigation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (Telmisartan is classified as an angiotensin II receptor blocker, typically used for hypertension) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Telmisartan in this evidence pack. Based on known pharmacology, Telmisartan belongs to the angiotensin II receptor blocker (ARB) class, acting primarily via AT1 receptor antagonism to regulate blood pressure and vascular tone.

Prinzmetal (variant) angina is caused by transient coronary artery vasospasm, a mechanism distinct from the systemic blood pressure regulation that ARBs are established for. The link proposed by the model is therefore theoretical rather than mechanistically established.

No clinical trials, literature, or ICTRP-registered trials evaluating Telmisartan specifically in Prinzmetal angina were identified in any of the source databases queried (ClinicalTrials.gov, ICTRP, PubMed). The prediction rests solely on the TxGNN knowledge-graph score, with no empirical corroboration at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Telmisartan is not currently marketed in Australia (0 ARTG entries), and no TGA-approved Product Information is available in this evidence pack. Key warnings, contraindications, and drug-interaction data all returned as not found in this evidence pack — please refer to the TGA-approved Product Information (PI), once available, or overseas regulatory PI, for safety information before any clinical use is considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only evidence supporting Telmisartan for Prinzmetal angina is the TxGNN model score; there are no clinical trials or published literature to substantiate a mechanistic or empirical link, and the drug is not currently registered in Australia.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank (currently a Blocking/High-severity data gap in this pack)
- TFDA/TGA product information — warnings and contraindications (currently a Blocking data gap)
- Preclinical or clinical studies specifically evaluating Telmisartan in coronary vasospasm/Prinzmetal angina
- A regulatory pathway assessment, since Telmisartan holds no ARTG entries in Australia at present

**Note:** This evidence pack also contains other TxGNN-predicted indications for Telmisartan with substantially stronger evidence — notably *intracerebral hemorrhage* (L1, "Proceed with Guardrails," supported by the completed 1,671-patient Phase 3 TRIDENT trial) and *cerebral artery occlusion* (L2, "Research Question," supported by 17 literature reports and a completed Phase 4 trial). These may warrant separate evaluation reports given their materially higher evidence maturity.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

