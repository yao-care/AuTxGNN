---
layout: default
title: Gemtuzumab Ozogamicin
parent: 僅模型預測 (L5)
nav_order: 310
evidence_level: L5
indication_count: 10
---

# Gemtuzumab Ozogamicin
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

# Gemtuzumab Ozogamicin: From Acute Myeloid Leukemia to Chronic Myeloid Leukemia, Blast Phase (BCR-ABL1 Positive)

## One-Sentence Summary

Gemtuzumab ozogamicin (Mylotarg) is a CD33-targeted antibody-drug conjugate originally used for CD33-positive acute myeloid leukemia (AML). Among the 10 indications TxGNN predicted for this drug, **Chronic Myeloid Leukemia, Blast Phase (BCR-ABL1 Positive)** is the only candidate with a plausible biological mechanism and meaningful supporting evidence — **3 clinical trials** and **13 publications** — while the model's top-scoring predictions (e.g. Richter syndrome, bulbar polio, malignant spiradenoma) were assessed in the evidence pack itself as likely model noise with no mechanistic basis or supporting data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | CD33-positive Acute Myeloid Leukemia (AML) — derived from literature within the evidence pack; no structured original-indication record was available |
| Predicted New Indication | Chronic Myeloid Leukemia, Blast Phase (BCR-ABL1 Positive) |
| TxGNN Prediction Score | 97.89% |
| Evidence Level | L3 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

**Note on candidate selection:** This evidence pack scored gemtuzumab ozogamicin against 10 predicted indications. Six of them (Richter syndrome, bulbar polio, malignant spiradenoma, 5q35 microduplication syndrome, neuralgic amyotrophy, and its duplicate "amyotrophic neuralgia") received the highest TxGNN scores but have zero supporting trials or literature, and the evidence pack's own mechanistic review flags them as implausible or as likely ontology/false-positive noise (all scored L5, Hold). CML blast phase, ranked third by score, is the only candidate with a coherent CD33-related mechanism and a real evidence base, and is therefore the focus of this report.

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data for gemtuzumab ozogamicin was not available in this evidence pack (flagged as a High-severity data gap). However, the literature retrieved within the pack itself is consistent and specific: gemtuzumab ozogamicin is a humanized anti-CD33 monoclonal antibody conjugated to the cytotoxic agent calicheamicin, designed to deliver a cytotoxic payload to CD33-expressing myeloid blasts (PMID 15454492, 15886328).

The drug's approved use is in CD33-positive AML. Chronic myeloid leukemia in blast phase (CML-BP) is pathologically similar to AML at that stage — blast-phase disease is managed largely like AML because of shared histological and clinical features (PMID 35536916). Critically, CD34+/CD38- leukemic stem cells in CML have been shown to express CD33 (Siglec-3) and to respond to gemtuzumab ozogamicin in vitro (PMID 21993666), giving a direct molecular rationale for activity in this setting.

This mechanistic plausibility is reinforced by real-world clinical use: gemtuzumab ozogamicin has been combined with fludarabine/cytarabine in CML-BP patients (PMID 22534616) and used together with blinatumomab in refractory mixed-phenotype CML blast crisis (PMID 34764108), indicating clinicians have already explored this off-label use in difficult, CD33-expressing blast-phase disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00038831](https://clinicaltrials.gov/study/NCT00038831) | Phase 1/2 | Completed | 47 | Mylotarg combined with melphalan/fludarabine as reduced-intensity conditioning before allogeneic transplant in high-risk acute leukemia, CML, or MDS |
| [NCT03589729](https://clinicaltrials.gov/study/NCT03589729) | Phase 2 | Recruiting | 100 | Dexrazoxane cardioprotection during chemotherapy regimens (including gemtuzumab ozogamicin) in AML, high-risk MDS, myeloid blast phase CML, and Ph+ AML |
| [NCT00038805](https://clinicaltrials.gov/study/NCT00038805) | Phase 2/3 | Terminated (n=3) | 3 | Nonmyeloablative allogeneic transplant using Mylotarg-based conditioning in high-risk ALL, CML, or MDS |

None of these trials is a dedicated randomised efficacy trial of gemtuzumab ozogamicin specifically for CML blast phase — all are transplant-conditioning or supportive-care studies that include CML-BP as one of several eligible diagnoses.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35536916](https://pubmed.ncbi.nlm.nih.gov/35536916/) | 2022 | Systematic Review | Expert Review of Hematology | CML myeloid blast phase resembles AML clinically and histologically; management is drawn from AML strategies |
| [22534616](https://pubmed.ncbi.nlm.nih.gov/22534616/) | 2012 | Cohort (n=107) | Clin Lymphoma Myeloma Leuk | Fludarabine + cytarabine ± gemtuzumab ozogamicin in relapsed/refractory AML, high-risk MDS, and CML blast phase; 26% complete remission rate overall |
| [34764108](https://pubmed.ncbi.nlm.nih.gov/34764108/) | 2021 | Case Report | BMJ Case Reports | Gemtuzumab ozogamicin plus blinatumomab used in refractory mixed-phenotype CML blast crisis |
| [21993666](https://pubmed.ncbi.nlm.nih.gov/21993666/) | 2012 | Mechanistic Study | Haematologica | CD34+/CD38- leukemic stem cells in CML express CD33 (Siglec-3) and respond to gemtuzumab ozogamicin in vitro |
| [17353625](https://pubmed.ncbi.nlm.nih.gov/17353625/) | 2007 | Review | Gan to Kagaku Ryoho | Overview of hematological malignancy therapy including CD33-targeted gemtuzumab ozogamicin in AML |
| [15454492](https://pubmed.ncbi.nlm.nih.gov/15454492/) | 2005 | Mechanistic Study | Blood | CD33 expression level and internalization kinetics determine gemtuzumab ozogamicin cytotoxicity |
| [15487459](https://pubmed.ncbi.nlm.nih.gov/15487459/) | 2004 | Review | American Journal of Clinical Pathology | Overview of targeted cancer therapies including gemtuzumab ozogamicin and BCR-ABL–targeted imatinib in CML |
| [15886328](https://pubmed.ncbi.nlm.nih.gov/15886328/) | 2005 | Clinical Trial | Blood | Dose-escalation safety/efficacy study of gemtuzumab ozogamicin in pediatric CD33+ AML |
| [11895761](https://pubmed.ncbi.nlm.nih.gov/11895761/) | 2002 | Case Series (n=23) | Blood | Hepatic sinusoidal obstruction (veno-occlusive disease) following gemtuzumab ozogamicin in transplant patients |
| [11466696](https://pubmed.ncbi.nlm.nih.gov/11466696/) | 2001 | Case Series | Cancer | Hepatic veno-occlusive disease associated with gemtuzumab ozogamicin even without prior stem cell transplant |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — antibody-drug conjugate (anti-CD33 monoclonal antibody linked to the cytotoxic agent calicheamicin) |
| Myelosuppression Risk | Please refer to the Product Information (PI) warnings and precautions — no myelosuppression-specific toxicity data available in this evidence pack |
| Emetogenicity Classification | Please refer to the Product Information (PI) warnings and precautions |
| Monitoring Items | Liver function tests are a priority — hepatic sinusoidal obstruction syndrome/veno-occlusive disease is a recurring toxicity signal in the literature (PMID 11466696, 11895761); full blood count given the CD33+ myeloid cell target |
| Handling Protection | Cytotoxic drug handling precautions apply (antibody-drug conjugate with a cytotoxic payload) |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No structured warnings, contraindications, or drug-interaction data were available in this evidence pack, and this is flagged as a **Blocking** data gap preventing formal safety pre-assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Mechanistic plausibility and some real-world clinical use exist for gemtuzumab ozogamicin in CML blast phase (CD33 expression on CML leukemic stem cells, combination use in refractory blast crisis), but no trial has directly tested efficacy for this indication — all identified trials are transplant-conditioning or supportive-care studies, and no completed Phase 2/3 RCT exists.
- A TGA-equivalent Product Information gap (warnings/contraindications) is a Blocking issue that prevents even an initial safety assessment, and the drug is not currently marketed in Australia (0 ARTG entries).

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications, drug interactions)
- Structured mechanism-of-action data from DrugBank to confirm the CD33/calicheamicin pathway formally
- A dedicated efficacy study (ideally prospective) in CML blast-phase patients rather than reliance on mixed-diagnosis transplant/conditioning trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

