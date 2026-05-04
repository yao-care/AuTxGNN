---
layout: default
title: Bicalutamide
parent: 僅模型預測 (L5)
nav_order: 86
evidence_level: L5
indication_count: 10
---

# Bicalutamide
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

# Bicalutamide: From Prostate Cancer to Hypertrichosis

## One-Sentence Summary

Bicalutamide is a non-steroidal antiandrogen classically used in the treatment of prostate cancer, where it blocks androgen receptor (AR) signalling to suppress androgen-driven tumour growth.
The TxGNN model predicts it may be effective for **Hypertrichosis** (excessive unwanted hair growth), with **1 publication** currently referencing this connection.
The supporting evidence remains at the mechanistic/observational level only, and this prediction is best classified as a **research question** requiring prospective investigation before clinical application.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prostate cancer (androgen deprivation therapy) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L4 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

> **Data Note:** The ARTG query returned 0 entries. Clinicians should independently verify current TGA registration status at the [TGA ARTG public database](https://www.tga.gov.au/resources/artg), as Bicalutamide (e.g., Casodex®) may be available under brand name listings or accessible via the Special Access Scheme (SAS).

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in the current Evidence Pack. Based on established pharmacology, Bicalutamide is a non-steroidal antiandrogen that competitively and selectively binds to the androgen receptor (AR), blocking the action of testosterone and dihydrotestosterone (DHT) without reducing circulating androgen levels. It was originally developed for prostate cancer, where AR signalling drives tumour cell proliferation and survival. Its oral bioavailability, long half-life (~6 days), and tissue selectivity have made it a foundational agent in hormone-sensitive malignancies.

The connection to hypertrichosis is mechanistically plausible in androgen-dependent subtypes. Androgens are key regulators of hair follicle biology — they stimulate growth in androgen-sensitive follicles (facial, body) via AR activation and modulate follicle responsiveness to proliferative stimuli such as Minoxidil. By blocking AR signalling at the follicle level, Bicalutamide could theoretically attenuate androgen-driven or androgen-facilitated excessive hair growth. The sole identified publication is a commentary on a retrospective 35-patient study in which Bicalutamide appeared to mitigate Minoxidil-induced hypertrichosis in female pattern hair loss, suggesting follicular AR activity is clinically relevant in this context.

However, the strength of this prediction is substantially limited by the heterogeneity of hypertrichosis as a diagnostic category. Many subtypes — including Ambras-type congenital hypertrichosis universalis (ranked 3rd) and drug-induced forms — have genetic or non-androgenic aetiologies where AR blockade would have little mechanistic rationale. The TxGNN model prediction should therefore be interpreted narrowly, applying most plausibly to acquired androgen-dependent forms.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Bicalutamide in hypertrichosis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35304167](https://pubmed.ncbi.nlm.nih.gov/35304167/) | 2022 | Letter/Comment | Journal of the American Academy of Dermatology | Commentary responding to a retrospective study of 35 patients in which Bicalutamide was observed to improve Minoxidil-induced hypertrichosis in female pattern hair loss; authors discuss the AR-mediated mechanism by which Bicalutamide may modulate follicular sensitivity to growth stimuli |

---

## Australia Market Information

No ARTG entries were identified for Bicalutamide in the current data query (0 registered products). A table cannot be generated without registration records.

Clinicians requiring access to Bicalutamide for approved or off-label indications in Australia should consult:
- **TGA ARTG search** for current registration status under brand names (e.g., Casodex®)
- **TGA Special Access Scheme (SAS)** for unapproved therapeutic goods
- **TGA Product Information (PI)** for approved indications, dosing, and safety

---

## Cytotoxicity

Bicalutamide is classified as an antineoplastic agent (used in prostate cancer treatment); this section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Non-steroidal Androgen Receptor Antagonist (not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Low — Bicalutamide does not cause significant myelosuppression; haematological toxicity is not a primary concern at standard doses |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (LFTs) — hepatotoxicity is a known class effect; baseline and periodic monitoring recommended. Blood glucose monitoring in patients with diabetes. PSA where relevant to oncological use. |
| Handling Protection | Standard oral solid-dose handling precautions apply; dedicated cytotoxic handling procedures (as required for conventional chemotherapy) are not mandated for this agent |

---

## Safety Considerations

Safety data including key warnings, contraindications, and drug interaction records were not available in the current Evidence Pack.

Please refer to the TGA-approved Product Information (PI) for complete safety information.

> **Clinician Alert:** Although formal DDI data was not retrieved in this query, Bicalutamide is a known inhibitor of CYP3A4 and may significantly increase the anticoagulant effect of warfarin. This interaction is clinically significant and should be reviewed for any patient on concurrent anticoagulant therapy. Additionally, Bicalutamide carries known risks of hepatotoxicity, gynaecomastia, and hot flushes in male patients. Safety considerations for off-label use in non-prostate cancer populations (e.g., women, children) require separate, specialist evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between Bicalutamide and androgen-dependent hypertrichosis is biologically coherent but supported only by a single published commentary on a small retrospective study, with no registered clinical trials. L4 evidence is insufficient to justify clinical translation without a defined prospective research programme.

**To proceed, the following is needed:**
- A prospective pilot study or randomised controlled trial specifically evaluating Bicalutamide in androgen-dependent acquired hypertrichosis (e.g., Minoxidil-induced, idiopathic hirsutism)
- Detailed mechanism of action data from DrugBank or primary literature to strengthen the pharmacological rationale
- A safety monitoring plan tailored to off-label use in non-oncology populations, including women of reproductive potential and patients without prostate cancer comorbidities
- Verification of TGA/ARTG registration status and appropriate access pathway (SAS or approved indication) prior to any clinical use
- Review of TGA-approved Product Information for contraindications, warnings, and drug interactions

---

> **Attention — Higher-Priority Candidate Identified:**
> Among the 10 TxGNN-predicted indications evaluated for Bicalutamide, **female breast carcinoma (AR-positive Triple-Negative Breast Cancer, rank 9)** carries substantially stronger evidence (**Evidence Level L2; decision stage S3; Recommendation: Proceed with Guardrails**). This includes an active Phase 2 clinical trial ([NCT03650894](https://clinicaltrials.gov/study/NCT03650894) — Nivolumab + Bicalutamide + Ipilimumab in metastatic HER2-negative breast cancer, n=30, active not recruiting), a 2025 systematic review (PMID [40853613](https://pubmed.ncbi.nlm.nih.gov/40853613/)), multiple in vitro and preclinical studies, and a well-established mechanistic rationale (LAR subtype TNBC expressing AR in ~30–35% of cases). A dedicated, higher-priority evaluation report for this indication is strongly recommended.

---

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All website pages and clinical communications should include appropriate YMYL disclaimers.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

