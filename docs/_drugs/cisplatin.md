---
layout: default
title: Cisplatin
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 10
---

# Cisplatin
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

# Cisplatin: From Germ Cell Tumours to Female Breast Carcinoma

---

## One-Sentence Summary

Cisplatin is a platinum-based cytotoxic chemotherapy agent internationally established as the cornerstone of BEP (Bleomycin, Etoposide, Cisplatin) chemotherapy for germ cell tumours — one of oncology's greatest success stories, with cure rates of 70–90% in metastatic testicular cancer — though it is not currently registered on the Australian ARTG.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with particularly compelling evidence in BRCA-mutated and triple-negative breast cancer subtypes,
backed by **46 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Germ cell tumours (testicular cancer, ovarian GCT, and related malignancies; established internationally — not currently registered on the Australian ARTG) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 97.39% |
| Evidence Level | L1 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on published pharmacology, Cisplatin is a platinum-containing compound that forms covalent DNA adducts — predominantly G-G intrastrand crosslinks — that physically block DNA replication and transcription. These lesions activate the DNA damage response pathway, leading to cell cycle arrest and apoptosis. Tumours with defective homologous recombination (HR) repair — particularly those harbouring BRCA1/2 mutations — cannot efficiently resolve platinum-DNA crosslinks and are therefore exquisitely sensitive to Cisplatin. This is the same mechanism underpinning its proven efficacy in germ cell tumours, where high p53 activity and low nucleotide excision repair (NER) capacity make these cancers among the most chemosensitive known.

The connection to female breast carcinoma is mechanistically well-founded. Triple-negative breast cancer (TNBC) — which lacks oestrogen receptor, progesterone receptor, and HER2 expression — frequently displays a "BRCAness" phenotype characterised by homologous recombination deficiency (HRD), even in the absence of a germline BRCA mutation. For patients with documented BRCA1/2 germline mutations, multiple Phase 2 clinical trials have directly evaluated Cisplatin as neoadjuvant or metastatic therapy, with the rationale that these tumours cannot repair platinum-induced DNA damage. An early randomised trial comparing Cisplatin plus etoposide against standard CMF chemotherapy in metastatic breast cancer demonstrated a numerically superior response rate with the platinum regimen (63% vs 48%).

Beyond the BRCA pathway, multiple additional mechanistic layers support this prediction. Preclinical data show that sub-cytotoxic Cisplatin doses inhibit epithelial–mesenchymal transition (EMT) in breast cancer cells, potentially reducing metastatic spread (PMID: 33500735). Network pharmacology analyses identify shared molecular targets between Cisplatin and the PARP inhibitor olaparib in breast carcinoma models, providing a rational basis for combination strategies (PMID: 40295796). Emerging chronotherapy research suggests that timed Cisplatin administration may improve the therapeutic index in mammary carcinoma models (PMID: 34998857). Taken together, these findings provide multi-layered biological and clinical rationale for Cisplatin use in breast carcinoma.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03201861](https://clinicaltrials.gov/study/NCT03201861) | Phase 3 | Recruiting | 762 | Weekly paclitaxel + cisplatin as adjuvant chemotherapy in high-risk HER2-negative breast cancer; the largest ongoing RCT directly evaluating cisplatin in this setting |
| [NCT01670500](https://clinicaltrials.gov/study/NCT01670500) | Phase 2 | Completed | 118 | Randomised neoadjuvant cisplatin vs doxorubicin/cyclophosphamide (AC) in newly diagnosed breast cancer with germline BRCA mutations; directly compares platinum against anthracycline standard |
| [NCT04126525](https://clinicaltrials.gov/study/NCT04126525) | Phase 2 | Active, not recruiting | 53 | Neoadjuvant trastuzumab/pyrotinib + weekly paclitaxel/cisplatin in HER2-positive locally advanced breast cancer; evaluates dual HER2 blockade combined with platinum-taxane backbone |
| [NCT00535509](https://clinicaltrials.gov/study/NCT00535509) | Phase 2 | Completed | 285 | Neoadjuvant FEC100 followed by cisplatin-docetaxel ± trastuzumab in HER2-overexpressed/amplified locally advanced breast cancer |
| [NCT01611727](https://clinicaltrials.gov/study/NCT01611727) | Phase 2 | Completed | 20 | Single-arm Phase 2 of cisplatin monotherapy in BRCA1-positive metastatic breast cancer; explored differential platinum chemosensitivity in BRCA1 mutation carriers |
| [NCT01031446](https://clinicaltrials.gov/study/NCT01031446) | Phase 1/2 | Completed | 55 | Cisplatin + paclitaxel + everolimus (mTOR inhibitor) in metastatic breast cancer; evaluated triple combination targeting DNA damage and PI3K/mTOR pathways simultaneously |
| [NCT02365805](https://clinicaltrials.gov/study/NCT02365805) | Phase 2 | Completed | 30 | Randomised neoadjuvant chemotherapy personalised by BRCA1 mRNA expression in HER2-negative breast cancer; cisplatin-based regimen assigned to BRCA1-high (taxane-resistant) tumours |
| [NCT00002772](https://clinicaltrials.gov/study/NCT00002772) | Phase 3 | Terminated | 602 | Intensive sequential cisplatin-containing chemotherapy vs high-dose chemotherapy + autologous stem cell support in breast cancer with 4–9 involved axillary lymph nodes; large sample despite termination |
| [NCT00003032](https://clinicaltrials.gov/study/NCT00003032) | Phase 3 | Completed | 224 | Randomised comparison of high-dose chemotherapy (including cisplatin) + autologous stem cell transplant vs standard therapy in anthracycline/taxane-responsive metastatic breast cancer |
| [NCT00002836](https://clinicaltrials.gov/study/NCT00002836) | Phase 3 | Completed | 184 | Comparison of high-dose chemotherapy + G-CSF vs G-CSF alone for peripheral blood stem cell (PBSC) mobilisation prior to autologous transplant in responsive metastatic or high-risk early breast cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [2066763](https://pubmed.ncbi.nlm.nih.gov/2066763/) | 1991 | RCT | J Clin Oncol | Prospective randomised trial of cisplatin + etoposide (PE) vs CMF as first-line treatment in 140 metastatic breast cancer patients; PE achieved 63% response rate vs 48% for CMF (p=0.08), with comparable time to progression |
| [24824628](https://pubmed.ncbi.nlm.nih.gov/24824628/) | 2015 | Phase 2 trial | Int J Cancer | Single-arm Phase 2 (NCT00601159): cisplatin + gemcitabine as first-line therapy in metastatic triple-negative breast cancer; assessed efficacy and tolerability in a population lacking standard treatment options |
| [2643295](https://pubmed.ncbi.nlm.nih.gov/2643295/) | 1989 | Clinical series | Am J Clin Oncol | Cisplatin 100 mg/m² + etoposide 300 mg/m² in 29 evaluable patients with heavily pretreated refractory metastatic breast carcinoma; 38% overall response rate (11% CR, 28% PR); supported further evaluation |
| [22593470](https://pubmed.ncbi.nlm.nih.gov/22593470/) | 2012 | Clinical series | Anticancer Res | Salvage cisplatin + 5-fluorouracil in heavily pretreated metastatic breast cancer; demonstrated notable activity against liver metastases; proposed as a viable option for cisplatin-naïve patients with hepatic disease |
| [24344005](https://pubmed.ncbi.nlm.nih.gov/24344005/) | 2013 | Clinical series | J BUON | Capecitabine + cisplatin doublet in anthracycline- and taxane-pretreated HER-2 negative metastatic breast carcinoma; characterised activity and toxicity profile in a real-world salvage setting |
| [33500735](https://pubmed.ncbi.nlm.nih.gov/33500735/) | 2021 | In vivo pre-clinical | Theranostics | Sub-cytotoxic cisplatin doses block early epithelial–mesenchymal transition (EMT) in breast cancer cells and retard tumour growth in combination with paclitaxel; identifies a potential metastasis-prevention strategy |
| [40295796](https://pubmed.ncbi.nlm.nih.gov/40295796/) | 2025 | Network pharmacology | Sci Rep | Olaparib + cisplatin synergism in breast cancer characterised via network pharmacology; identifies shared targets across DNA repair and apoptosis pathways; supports rational PARP inhibitor combination design |
| [27448297](https://pubmed.ncbi.nlm.nih.gov/27448297/) | 2016 | Review | Tumour Biol | Comprehensive review of miRNA-mediated cisplatin resistance in breast cancer; covers mechanisms including altered DNA damage response, cell survival signalling, and modification of drug transport |
| [34998857](https://pubmed.ncbi.nlm.nih.gov/34998857/) | 2022 | Pre-clinical | Toxicol Appl Pharmacol | Circadian disruption impairs cisplatin chronotherapy in triple-negative mammary carcinoma mouse model; timed cisplatin administration under normal circadian conditions shows improved therapeutic index |
| [37067747](https://pubmed.ncbi.nlm.nih.gov/37067747/) | 2023 | In vitro/In vivo | Cell Oncol (Dordr) | Gallium maltolate synergises with cisplatin in human breast carcinoma cells via nucleolar stress and ferroptosis; offers a potential strategy to overcome cisplatin resistance, particularly relevant in TNBC |

---

## Australia Market Information

Cisplatin is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)**. No ARTG product entries were identified in this evidence pack. Despite this, Cisplatin is a well-established cytotoxic chemotherapy agent used globally in multiple cancer indications and may be accessed in Australia via the TGA Special Access Scheme (SAS Category B) or through enrolment in approved clinical trials. Healthcare professionals should consult the TGA website for current regulatory guidance and applicable access pathways.

---

## Cytotoxicity

Cisplatin is a conventional cytotoxic antineoplastic agent and belongs to the platinum-based chemotherapy class. It meets all criteria for mandatory cytotoxic handling precautions.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic (Platinum compound — alkylating-like DNA crosslinking agent) |
| Myelosuppression Risk | Moderate (anaemia is most common; neutropenia and thrombocytopenia also reported; nadir typically at days 18–23; monitor FBC with differential before each cycle) |
| Emetogenicity Classification | High (Cisplatin is among the most highly emetogenic chemotherapy agents; multimodal antiemetic prophylaxis is mandatory, including NK1 receptor antagonist, 5-HT3 antagonist, and dexamethasone) |
| Monitoring Items | FBC with differential and platelets; serum creatinine and eGFR (nephrotoxicity is the primary dose-limiting toxicity — mandatory IV hydration pre and post administration); serum electrolytes (Mg²⁺, K⁺, Ca²⁺, Na⁺); audiometry (baseline and follow-up — ototoxicity risk); peripheral neurological assessment (cumulative sensory neuropathy) |
| Handling Protection | Must be prepared and administered in accordance with cytotoxic drug handling regulations (e.g., SHPA Guidelines for Cytotoxic Drugs); preparation in biological safety cabinet or isolator; chemotherapy-rated gloves, impervious gown, and eye protection required |

---

## Safety Considerations

Safety data (including key warnings, contraindications, and drug-drug interactions) are not available in the current evidence pack.

Please refer to the relevant Product Information (PI) — such as the TGA-approved PI where available, or the manufacturer's international prescribing information — for comprehensive safety details. Key areas to review include:

- **Nephrotoxicity**: Dose-limiting toxicity; adequate pre- and post-chemotherapy IV hydration with saline is mandatory; concurrent nephrotoxic agents (e.g., aminoglycosides, NSAIDs) should be avoided
- **Ototoxicity**: Irreversible high-frequency sensorineural hearing loss; baseline audiometry is recommended, particularly in elderly patients and those with pre-existing hearing impairment
- **Neurotoxicity**: Cumulative peripheral sensory neuropathy; may become dose-limiting with repeated cycles
- **Nausea and vomiting**: Highly emetogenic; prophylactic antiemetic regimens are essential prior to administration
- **Electrolyte disturbances**: Hypomagnesaemia, hypokalaemia, and hypocalcaemia are common; monitor and replace proactively
- **Myelosuppression**: Anaemia, neutropenia, and thrombocytopenia; manage according to institutional cytopenia protocols

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 2 clinical trials have directly evaluated Cisplatin in breast carcinoma, particularly in BRCA-mutated and triple-negative subtypes, supported by a completed randomised trial (PMID: 2066763) and a large ongoing Phase 3 study (NCT03201861, n=762). The TxGNN prediction score of 97.39% aligns with this substantial clinical evidence base, meeting L1 criteria. While Cisplatin is not currently ARTG-registered in Australia, the strength of international evidence and compelling mechanistic rationale support pursuing regulated access pathways for appropriately selected patients.

**To proceed, the following is needed:**
- **Regulatory pathway**: Cisplatin is not ARTG-registered in Australia; initiate assessment for access via TGA Special Access Scheme (SAS Category B) or enrolment in an approved clinical trial
- **Mechanism of action data**: DrugBank API query recommended to formally populate the MOA field (currently a High-severity data gap that impacts mechanistic analysis completeness)
- **Patient selection biomarkers**: BRCA1/2 germline mutation testing and/or validated HRD assay (e.g., Myriad myChoice CDx) to identify patients most likely to benefit from platinum-based therapy
- **Safety monitoring protocol**: Comprehensive plan covering nephrotoxicity (mandatory IV hydration protocol), ototoxicity (baseline and serial audiometry), peripheral neuropathy assessment, and electrolyte management across the treatment course
- **Drug-drug interaction review**: Complete DDI data currently unavailable; formal pharmacological review is required prior to prescribing, particularly for patients receiving concurrent nephrotoxic agents or combination chemotherapy regimens
- **Informed consent documentation**: Ensure patients are counselled on risks of investigational use in this indication and the lack of current Australian regulatory approval

---

> ⚠️ **YMYL Disclaimer**: This report is intended for research purposes only and does not constitute medical advice. Drug repurposing candidates identified by the TxGNN model require clinical validation before therapeutic application. Healthcare professionals should exercise independent clinical judgement and refer to current TGA-approved prescribing information and institutional protocols when making treatment decisions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

