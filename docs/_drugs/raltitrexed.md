---
layout: default
title: Raltitrexed
parent: Model Prediction Only (L5)
nav_order: 580
evidence_level: L5
indication_count: 10
---

# Raltitrexed
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

# Raltitrexed: From Colorectal Cancer to Sclerosing Cholangitis

## One-Sentence Summary

Raltitrexed is a thymidylate synthase inhibitor historically used in colorectal cancer chemotherapy. The TxGNN model predicts it may be effective for **Sclerosing Cholangitis**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only hypothesis with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Colorectal cancer (established clinical use; no ARTG-registered indication text available in this Evidence Pack) |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack (flagged as a High-severity data gap). Based on the information present, Raltitrexed is a thymidylate synthase inhibitor that blocks DNA synthesis, and its efficacy in colorectal cancer chemotherapy is well established.

Sclerosing cholangitis, however, is an autoimmune/inflammatory biliary disease driven by bile duct fibrosis and immune dysregulation — a pathology with no known direct link to nucleotide synthesis inhibition. The evidence pack's own mechanistic rationale for this candidate describes it as a "weak mechanistic hypothesis" likely arising from indirect knowledge-graph connections (e.g., shared comorbidity or drug-metabolism nodes) rather than genuine pharmacological plausibility, and notes it has no supporting literature or trial evidence.

It is also worth noting that the other nine TxGNN-predicted indications in this pack (myelodysplastic syndrome and several sickle-cell/thalassemia syndromes) are flagged in their own rationale text as mechanistically **conflicting** rather than supportive — Raltitrexed's myelosuppressive antimetabolite action runs counter to the therapeutic goals for these blood disorders. This pattern across the full candidate list reinforces that the current prediction set should be treated as hypothesis-generating only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

Raltitrexed is a thymidylate synthase inhibitor (antimetabolite), a conventional cytotoxic chemotherapy class, consistent with its established use in colorectal cancer.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antifolate / thymidylate synthase inhibitor) |
| Myelosuppression Risk | High — the Evidence Pack's own mechanistic notes identify myelosuppression as a known effect of thymidylate synthase inhibition; specific severity/nadir data not available — please refer to the Product Information (PI) |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | FBC with differential recommended given known myelosuppressive potential; liver and renal function per PI |
| Handling Protection | Standard cytotoxic drug handling precautions apply |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Every predicted indication in this pack — including the top-ranked Sclerosing Cholangitis — is Evidence Level L5, backed only by a TxGNN model score with zero clinical trials or literature. Several lower-ranked candidates are explicitly flagged as mechanistically conflicting (myelosuppression risk vs. treatment goals for MDS and sickle-cell syndromes). The drug is also not currently marketed in Australia (0 ARTG entries), and safety/PI data required for even a preliminary risk assessment is missing (Blocking data gap).

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications) — currently blocking
- Confirmed mechanism of action detail via DrugBank
- Primary literature or trial evidence specific to sclerosing cholangitis (or any candidate indication) before advancing past model-only status
- Confirmation of Australian regulatory/import pathway, given the drug is not currently marketed here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

