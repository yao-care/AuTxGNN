---
layout: default
title: Apalutamide
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 10
---

# Apalutamide
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

# Apalutamide: From Prostate Cancer to Male Reproductive Organ Cancer

## One-Sentence Summary

Apalutamide (Erleada®) is a second-generation androgen receptor (AR) inhibitor globally approved for prostate cancer treatment, but currently not registered in Australia (0 ARTG entries).
The TxGNN model assigns a high prediction score of **97.41%** to **Male Reproductive Organ Cancer** — encompassing prostate cancer and related malignancies — supported by **50+ clinical trials** and **18 publications**, including the landmark Phase 3 TITAN and SPARTAN randomised controlled trials.
Among all 10 TxGNN predictions in this Evidence Pack, male reproductive organ cancer is the only indication reaching Level 1 evidence, making it the sole actionable candidate for clinical translation in the Australian setting.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prostate cancer (globally approved by FDA and EMA; not currently registered in Australia) |
| Predicted New Indication | Male Reproductive Organ Cancer |
| TxGNN Prediction Score | 97.41% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Apalutamide binds with high affinity to the androgen receptor (AR) ligand-binding domain (Ki ≈ 16 nM, approximately 8-fold more potent than bicalutamide), comprehensively blocking: (1) AR nuclear translocation, (2) AR binding to androgen response elements (ARE) on DNA, and (3) assembly of the AR transcriptional activation complex. This mechanism of action directly targets the primary oncogenic driver of prostate cancer — the dominant subtype within male reproductive organ cancers. Critically, AR signalling remains active even in castration-resistant states through AR amplification, point mutations, and splice variants (e.g. AR-V7), all of which continue to be suppressed by apalutamide's non-competitive binding mechanism.

Prostate cancer accounts for the vast majority of male reproductive organ cancers, and the biological link between AR pathway inhibition and tumour suppression is among the best validated in all of oncology. The TITAN Phase 3 study demonstrated that adding apalutamide to androgen deprivation therapy (ADT) significantly improved both radiographic progression-free survival and overall survival in metastatic castration-sensitive prostate cancer (mCSPC). The SPARTAN Phase 3 study similarly showed a near-two-year improvement in metastasis-free survival for high-risk non-metastatic castration-resistant prostate cancer (nmCRPC), with a confirmed overall survival benefit at final analysis.

The TxGNN model's high confidence score (97.41%) for this indication should be interpreted as a mechanistic confirmation rather than a speculative repurposing hypothesis. This validates the model's ability to correctly identify established drug–disease relationships via knowledge graph topology. The principal barrier to clinical use in Australia is the absence of TGA registration, not a lack of clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT03767244](https://clinicaltrials.gov/study/NCT03767244) | Phase 3 | Active, Not Recruiting | 2,517 | Double-blind RCT: apalutamide + ADT vs placebo + ADT as perioperative therapy for high-risk localised/locally advanced prostate cancer; co-primary endpoints are pathological complete response and metastasis-free survival |
| [NCT02489318](https://clinicaltrials.gov/study/NCT02489318) | Phase 3 | Active, Not Recruiting | 1,052 | TITAN study: apalutamide + ADT vs ADT alone in mHSPC; demonstrated superior radiographic PFS and overall survival — the foundational registration trial for mCSPC indication |
| [NCT04557059](https://clinicaltrials.gov/study/NCT04557059) | Phase 3 | Active, Not Recruiting | 694 | Apalutamide added to radiotherapy + LHRH agonist in high-risk hormone-sensitive prostate cancer assessed by PSMA-PET; primary endpoint is delay in metastatic progression or death |
| [NCT01171898](https://clinicaltrials.gov/study/NCT01171898) | Phase 1/2 | Completed | 127 | Foundational safety, pharmacokinetics and proof-of-concept study of apalutamide (ARN-509) in advanced CRPC; established dose (240 mg daily), tolerability and preliminary efficacy across multiple disease subtypes |
| [NCT03124433](https://clinicaltrials.gov/study/NCT03124433) | Phase 2 | Completed | 30 | NEAR trial: neoadjuvant apalutamide monotherapy prior to radical prostatectomy in D'Amico intermediate–high risk prostate cancer; assessed tumour downstaging and oncological efficacy as single-agent AR inhibition |
| [NCT03436654](https://clinicaltrials.gov/study/NCT03436654) | Phase 2 | Active, Not Recruiting | 102 | Multi-arm study in very high-risk localised and low-volume metastatic prostate adenocarcinoma; apalutamide + abiraterone + prednisone treatment arm with neoadjuvant surgical intent |
| [NCT03899077](https://clinicaltrials.gov/study/NCT03899077) | Phase 2 | Unknown | 202 | Randomised comparison of salvage radiotherapy + 6-month LHRH-based ADT versus apalutamide 240 mg daily in hormone-naïve biochemically recurrent post-prostatectomy patients; evaluates apalutamide as a standalone alternative to conventional ADT |
| [NCT04179864](https://clinicaltrials.gov/study/NCT04179864) | Phase 1b/2 | Terminated | 102 | CELLO-1: tazemetostat (EZH2 inhibitor) combined with apalutamide or abiraterone in chemotherapy-naïve mCRPC; provides combination safety and PK interaction data despite early termination |
| [NCT03840200](https://clinicaltrials.gov/study/NCT03840200) | Phase 1 | Completed | 51 | Ipatasertib (PI3K/Akt inhibitor) combined with apalutamide in advanced prostate cancer; explores co-blockade of AR and PI3K pathways as a strategy to overcome resistance |
| [NCT06865547](https://clinicaltrials.gov/study/NCT06865547) | Phase 4 | Enrolling by Invitation | 94 | ProA study: evaluates the 4A ProActive Management Model in mHSPC patients receiving apalutamide; real-world adherence, toxicity management and patient support outcomes |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [33914595](https://pubmed.ncbi.nlm.nih.gov/33914595/) | 2021 | RCT — Phase 3 Final OS Analysis | J Clin Oncol | TITAN final analysis: after placebo-to-apalutamide crossover, apalutamide + ADT demonstrated sustained improvement in overall survival and rPFS in mCSPC; confirmed durable long-term benefit |
| [31150574](https://pubmed.ncbi.nlm.nih.gov/31150574/) | 2019 | RCT — Phase 3 | N Engl J Med | TITAN initial analysis: apalutamide + ADT vs placebo + ADT in mCSPC; statistically significant improvements in rPFS and OS at pre-specified interim analysis |
| [29420164](https://pubmed.ncbi.nlm.nih.gov/29420164/) | 2018 | RCT — Phase 3 | N Engl J Med | SPARTAN trial: apalutamide improved median metastasis-free survival by ~24 months versus placebo in high-risk nmCRPC; first Phase 3 evidence supporting AR inhibition in the non-metastatic castration-resistant setting |
| [32907777](https://pubmed.ncbi.nlm.nih.gov/32907777/) | 2021 | RCT — OS Analysis | Eur Urol | SPARTAN final OS analysis: apalutamide significantly prolonged overall survival in nmCRPC with PSA doubling time ≤10 months, confirming that the MFS benefit translates to a meaningful survival advantage |
| [39417629](https://pubmed.ncbi.nlm.nih.gov/39417629/) | 2025 | Comparative Study | The Prostate | Multi-centre real-world comparison of abiraterone, enzalutamide and apalutamide in mHSPC; provides differential efficacy and safety data relevant to agent selection in clinical practice |
| [36167599](https://pubmed.ncbi.nlm.nih.gov/36167599/) | 2023 | RCT — Phase 2 | Eur Urol | ARNEO trial: neoadjuvant degarelix with or without apalutamide prior to radical prostatectomy in high-risk prostate cancer; assessed pathological response rates and biomarker correlates |
| [35091711](https://pubmed.ncbi.nlm.nih.gov/35091711/) | 2022 | RCT — Phase 2 | Prostate Cancer Prostatic Dis | NEAR trial primary outcomes: neoadjuvant apalutamide monotherapy + radical prostatectomy in intermediate–high risk prostate cancer; demonstrated tumour downstaging with manageable safety profile |
| [36000794](https://pubmed.ncbi.nlm.nih.gov/36000794/) | 2022 | RCT — Phase 2 PRO Sub-study | Int J Urol | NEAR trial patient-reported outcomes: health-related quality of life during 12-week neoadjuvant apalutamide; sexual function and hormonal symptom burden characterised during AR monotherapy |
| [32930958](https://pubmed.ncbi.nlm.nih.gov/32930958/) | 2020 | Systematic Review | Drugs | Comprehensive review of apalutamide in mCSPC; synthesises TITAN Phase 3 data, pharmacology, regulatory approval context in EU and USA, and practical prescribing considerations |
| [33480983](https://pubmed.ncbi.nlm.nih.gov/33480983/) | 2021 | Review | Endocrine Reviews | Hormonal therapy for prostate cancer: detailed mechanistic review from castration to second-generation AR inhibitors including apalutamide; contextualises therapeutic evolution and resistance pathways |

---

## Australia Market Information

Apalutamide is **not currently listed on the Australian Register of Therapeutic Goods (ARTG)**. There are no ARTG entries for this drug.

> **Note for Australian Clinicians:** Apalutamide (Erleada®) holds regulatory approval from the US FDA (nmCRPC since 2018; mCSPC since 2019) and the European Medicines Agency (EMA). TGA registration would be required before routine clinical use in Australia. Prior to registration, individual patient access may be sought via:
> - **TGA Special Access Scheme (SAS) Category B** — for seriously ill patients where no alternative therapy is available
> - **Clinical Trial pathway** — participation in an active registered trial

---

## Cytotoxicity

Apalutamide is an antineoplastic agent (AR pathway inhibitor) and this section applies accordingly. It is **not** a conventional cytotoxic drug.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Second-generation Androgen Receptor (AR) Pathway Inhibitor; distinct from conventional cytotoxic agents (not a fluoropyrimidine, platinum compound, or taxane) |
| Myelosuppression Risk | Low; apalutamide is not conventionally myelosuppressive. Anaemia and thrombocytopenia are reported at low frequencies in Phase 3 trials. Routine FBC monitoring is recommended. |
| Emetogenicity Classification | Low; not associated with clinically significant chemotherapy-induced nausea or vomiting |
| Monitoring Items | Full blood count (FBC) with differential; liver function tests (ALT, AST, bilirubin); thyroid function (hypothyroidism reported in TITAN/SPARTAN); cardiovascular monitoring (QTc interval, ischaemic cardiac events, blood pressure); falls and fracture risk assessment (increased risk reported — bone mineral density monitoring if on prolonged ADT combination); cognitive function and seizure history (apalutamide may lower seizure threshold) |
| Handling Protection | Standard precautions for oral antineoplastic agents apply; intact tablets should not be crushed or split; pregnant healthcare workers should avoid direct contact with broken tablets; no intravenous preparation involved; standard safe handling per institutional cytotoxic policy |

---

## Safety Considerations

Detailed safety data including TGA-specific Product Information warnings, contraindications, and a full drug interaction profile were not available in this Evidence Pack.

> Please refer to the TGA-approved Product Information (PI) — or the FDA/EMA-approved labelling as a reference pending TGA registration — for complete safety information. Key areas to review include: **falls and fractures** (increased risk with AR inhibition + ADT combination); **cardiovascular events** (ischaemic heart disease, QTc prolongation); **severe skin reactions** (including Stevens-Johnson syndrome); **seizures** (apalutamide crosses the blood–brain barrier); **ischaemic cerebrovascular events**; and **drug–drug interactions** (apalutamide is a strong inducer of CYP3A4 and CYP2C19 — clinically significant interactions with anticoagulants, anticonvulsants, and other oncology agents are expected).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Apalutamide has robust Level 1 evidence from two landmark Phase 3 RCTs (TITAN for mCSPC; SPARTAN for nmCRPC), both demonstrating statistically significant and clinically meaningful improvements in overall survival and radiographic progression-free survival. The mechanistic basis — competitive AR inhibition — is directly validated for male reproductive organ cancers and constitutes one of the most thoroughly characterised drug–target relationships in oncology. The barrier to clinical use in Australia is not evidential but regulatory and administrative.

**To proceed, the following is needed:**

- **TGA registration submission** for Erleada® (apalutamide 60 mg tablet), citing the TITAN and SPARTAN dossiers; alternatively, initiate SAS Category B applications for individual patients with nmCRPC or mCSPC where no registered alternative is suitable
- **TGA Product Information document** — retrieval and local adaptation to provide Australian prescribers with a complete safety, contraindication, and drug interaction profile (addresses data gap DG001)
- **Mechanism of action confirmation** via DrugBank API query for DB11901 (addresses data gap DG002; expected to confirm competitive AR ligand-binding domain inhibitor with nuclear translocation blockade)
- **Drug–drug interaction assessment** — particularly for strong CYP3A4 inducers/inhibitors commonly co-prescribed in this patient population (anticoagulants, anticonvulsants, cardiovascular agents)
- **PBS listing evaluation** — assessment of cost-effectiveness and subsidisation pathway via the Pharmaceutical Benefits Advisory Committee (PBAC) if TGA registration is granted
- **Pharmacovigilance plan** — covering known priority adverse events: falls and fractures, cardiovascular events, severe cutaneous reactions, and seizure risk in patients with predisposing conditions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

