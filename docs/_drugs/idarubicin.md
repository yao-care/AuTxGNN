---
layout: default
title: Idarubicin
parent: Model Prediction Only (L5)
nav_order: 365
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Idarubicin: predicted new indication Bulbar polio (evidence level L5). Approved use: Acute myeloid leukaemia (AML) and related myeloid leukaemia subtypes"
monitor_inn: "Idarubicin"
predicted_indications: ["bulbar polio", "5q35 microduplication syndrome", "neuralgic amyotrophy", "amyotrophic neuralgia", "familial thrombocytosis", "reactive thrombocytosis", "ganglioneuroblastoma (disease)", "retroperitoneal neoplasm", "vertebral anomalies and variable endocrine and T-cell dysfunction", "obsolete Hodgkin's granuloma"]
---

# Idarubicin
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

## Idarubicin: From Acute Myeloid Leukaemia to Bulbar Polio
{: .text-alpha }

## One-Sentence Summary

Idarubicin is an anthracycline chemotherapy agent originally used to treat acute myeloid leukaemia (AML) and related myeloid conditions.
The TxGNN model predicts it may be effective for **bulbar polio**, but **no clinical trials and no publications** currently support this prediction.
It is a computational prediction only, and no mechanistic rationale has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute myeloid leukaemia (AML) and related myeloid leukaemia subtypes (the ARTG entry in the data compiled for this report has no indication text) |
| Predicted New Indication | Bulbar polio |
| TxGNN Prediction Score | 97.05% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, idarubicin is an anthracycline that inhibits topoisomerase II and intercalates into DNA. Its efficacy is established in haematological malignancies such as AML.

Bulbar polio is a viral infection of the motor neurons in the brainstem. It is not a malignancy, and nothing in the available data links a cytotoxic DNA-damaging agent to its underlying biology. The high TxGNN score is a statistical output of a knowledge-graph model and is not backed by trials, literature or a plausible mechanism. In this setting, an anthracycline would also carry unfavourable risks, including myelosuppression and cardiotoxicity.

Other predictions in the same list (for example, ganglioneuroblastoma and Hodgkin lymphoma) have a class-level rationale because anthracyclines such as doxorubicin are used in those diseases. They are not the lead prediction and also lack idarubicin-specific evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for bulbar polio.

For context, the only publication retrieved across the top ten predictions relates to a different prediction (retroperitoneal neoplasm): [PMID 39588445](https://pubmed.ncbi.nlm.nih.gov/39588445/) (2024, case report with review, *Cureus*) describes cervical granulocytic sarcoma without acute leukaemia and 42 additional cases. It does not address bulbar polio and does not establish efficacy of idarubicin.

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 4440Q | Zavedos Solution | Solution for I.V. injection containing idarubicin hydrochloride 5 mg in 5 mL | Not available in the data compiled for this report |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (anthracycline class) |
| Myelosuppression Risk | High (severe myelosuppression is a recognised effect of anthracyclines; please confirm in the Product Information) |
| Emetogenicity Classification | Moderate (class-based; please confirm in the Product Information) |
| Monitoring Items | FBC with differential, liver and renal function, cardiac function (e.g. echocardiography or MUGA) |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Please refer to the Product Information (PI) warnings and precautions for product-specific details.

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** kidney disease, liver disease, gallbladder disease, anaemia, sudden cardiac arrest, heart conduction disease, cardiomyopathy (including hypertrophic), endomyocardial fibrosis, myocardial disorders, pericarditis, myocarditis, enterocolitis and gastroenteritis. These come from a model knowledge graph and must be verified against the PI.
- **Drug interactions:** The interaction search returned 100 records; 20 were available for review. Major interactions include:
  - Dolasetron
  - Cisapride
  - Papaverine
  - Deferiprone
  - Macimorelin

  Moderate interactions include ondansetron, granisetron, palonosetron, clarithromycin, levofloxacin, famotidine, loperamide, promethazine, rolapitant, eliglustat and palifermin. Several of these are QT-prolonging or antiemetic agents, which is relevant to a drug with cardiac toxicity. Bowel-preparation products (picosulfuric acid, polyethylene glycol with electrolytes, sodium sulfate) are also listed as moderate interactions. Metronidazole is a minor interaction.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bulbar polio prediction rests on a model score alone, with no clinical trials, no literature and no plausible mechanistic link. A cytotoxic anthracycline would carry substantial myelosuppressive and cardiac risk in a non-malignant viral disease.

**To proceed, the following is needed:**
- A credible mechanistic rationale, supported by mechanism of action data (currently unavailable)
- Preclinical or literature evidence of idarubicin activity in poliovirus or motor neuron disease models
- TGA Product Information review for warnings, contraindications and approved indications
- A benefit-risk assessment, given that vaccination and supportive care are the established approaches to polio
- If anthracycline repurposing is of interest, consider reviewing lower-ranked predictions with class-level rationale (e.g. ganglioneuroblastoma), starting with a literature review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

