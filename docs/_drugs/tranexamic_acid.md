---
layout: default
title: Tranexamic Acid
parent: Model Prediction Only (L5)
nav_order: 746
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tranexamic Acid: predicted new indication Amenorrhoea (evidence level L5). Approved use: Endometriosis . The Australian ARTG entry has no approved indication…"
monitor_inn: "Tranexamic acid"
predicted_indications: ["amenorrhea (disease)", "heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "hypospadias 3, autosomal", "sella turcica, bridged", "triphalangeal thumb, Nonopposable", "hypercarotenemia and vitamin A deficiency, autosomal recessive", "hyperparathyroidism, primary, caused by water clear cell hyperplasia", "glaucoma with elevated episcleral venous pressure"]
---

# Tranexamic Acid
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

# Tranexamic Acid: From Endometriosis to Amenorrhoea

## One-Sentence Summary

Tranexamic acid is an antifibrinolytic agent. The knowledge graph records its original indication as endometriosis, although it is best known clinically for bleeding control, including heavy menstrual bleeding.
The TxGNN model predicts it may be effective for **amenorrhoea**, but only **2 review articles** and **no clinical trials** are available, and neither article supports it as a treatment for amenorrhoea.
The prediction should be treated as a research question, not a therapeutic lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometriosis (per the knowledge graph). The Australian ARTG entry has no approved indication text recorded in the data compiled for this report. |
| Predicted New Indication | Amenorrhoea |
| TxGNN Prediction Score | 99.19% |
| Evidence Level | L4 (review literature only, no trials; the mechanistic link is indirect) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Tranexamic acid is generally understood to be a lysine analogue that blocks plasminogen binding to fibrin, which reduces fibrinolysis and bleeding.

The relationship between the original and predicted indications is weak. Tranexamic acid reduces menstrual blood loss but does not induce amenorrhoea (absence of menses). Both retrieved papers discuss it within bleeding-management strategies, not as a treatment for amenorrhoea itself. The high TxGNN score most likely reflects shared gynaecological bleeding-disorder context in the knowledge graph rather than a true therapeutic signal. Treating absent menses with an agent that reduces bleeding is mechanistically questionable.

Other predictions in the list are also poorly supported. The thrombophilia-related predictions (heparin cofactor 2 deficiency, factor 5 excess with spontaneous thrombosis, antithrombin deficiency type 2) are mechanistically implausible and raise safety concerns. An antifibrinolytic would be expected to increase, not reduce, thrombotic risk. The remaining lower-scoring predictions (scores of about 0.67–0.68, e.g. hypospadias, glaucoma with elevated episcleral venous pressure) have no plausible mechanistic link and no supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Review | Menopause | Evidence-based review of pharmacological therapy for abnormal uterine bleeding. Treatment choice depends on cause, bleeding volume, contraception or fertility needs, and perimenopausal status. It does not establish a role in amenorrhoea. |
| [39043214](https://pubmed.ncbi.nlm.nih.gov/39043214/) | 2024 | Review | J Oncol Pharm Pract | Systematic approach to menses prophylaxis and suppression in premenopausal women with haematological cancers. It notes limited comparative data on available agents. |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 2180R | Cyklokapron | Tablet 500 mg (oral) | Not recorded in the data compiled for this report |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (drug-disease links in the graph, not label text; they need confirmation against the Product Information):
  - Cardiovascular and thrombotic: hypertension, coronary artery disease, stroke and cerebrovascular disorders, thrombophlebitis
  - Hormone-sensitive cancers: female breast carcinoma, endometrial cancer
  - Metabolic: diabetes mellitus, diabetic ketoacidosis, hyperglycaemia, hyperlipidaemia, hypertriglyceridaemia, obesity
  - Hepatic and biliary: liver disease, gallbladder disease
  - Porphyria
  - Neurological and psychiatric: migraine, brain oedema, anxiety and neurotic disorders, dysthymic disorder
- **Drug Interactions** (35 interactions identified; the first 20 are listed in the data compiled for this report):
  - **Major**: oestrogens and hormonal contraceptives (ethinylestradiol, estradiol, conjugated and esterified oestrogens, estrone, diethylstilbestrol, norethisterone, drospirenone, etonogestrel), estramustine, carfilzomib, anti-inhibitor coagulant complex, and Factor IX complex. The main concern is additive thrombotic risk.
  - **Moderate**: thrombolytics (alteplase, anistreplase), which have opposing pharmacological effects.
- **Thrombosis risk**: the 1991 case series (PMID 1782339) describes drugs, particularly oral contraceptives, triggering thrombosis in patients with congenital coagulation-inhibitor defects. This is safety context, not therapeutic evidence.

Please refer to the TGA-approved Product Information (PI) for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there are no clinical trials, only two reviews that do not support use for amenorrhoea, and a mechanism that points the other way (reducing bleeding, not restoring menses). Several of the other predictions are thrombophilic conditions where an antifibrinolytic could cause harm.

**To proceed, the following is needed:**
- Detailed mechanism of action data
- A clear clinical rationale for how an antifibrinolytic could benefit amenorrhoea, or a reassessment of whether the prediction reflects a graph artefact
- The TGA Product Information, to confirm approved indications, warnings and contraindications
- Mechanistic and clinical evidence (preclinical or clinical studies) before any further evaluation
- A thrombosis risk assessment, particularly for patients using hormonal therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

