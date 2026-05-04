---
layout: default
title: Albendazole
parent: 僅模型預測 (L5)
nav_order: 27
evidence_level: L5
indication_count: 10
---

# Albendazole
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

# Albendazole: From Intestinal Helminthiasis to Alveolar Echinococcosis

## One-Sentence Summary

Albendazole is a broad-spectrum benzimidazole anthelmintic with over 40 years of global clinical use, primarily established for soil-transmitted intestinal helminthiasis (roundworm, hookworm, and whipworm infections), though it is not currently registered in Australia.
The TxGNN model predicts it may be effective for **Alveolar Echinococcosis** — a severe, potentially fatal parasitic liver disease caused by *Echinococcus multilocularis* —
with **5 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Broad-spectrum anthelmintic for intestinal helminthiasis (not registered in Australia; no ARTG entries) |
| Predicted New Indication | Alveolar Echinococcosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Albendazole's mechanism of action data is not available within Australian regulatory records, as the drug is not registered on the ARTG. Based on established global pharmacological knowledge, albendazole belongs to the benzimidazole class of anthelmintics. Its primary active metabolite — albendazole sulfoxide — is highly lipophilic and capable of penetrating parasite cyst walls. The drug selectively inhibits β-tubulin polymerisation in tapeworm and nematode larval stages, blocking cellular mitosis and glucose uptake, ultimately depleting ATP and causing parasite death or calcified stasis. Critically, albendazole's affinity for mammalian (human) tubulin is substantially lower than for parasitic tubulin, providing a clinically acceptable therapeutic window.

Alveolar echinococcosis (AE) is caused by the larval metacestode stage of *Echinococcus multilocularis*. Unlike the cystic form caused by *E. granulosus*, AE invades the liver in an aggressive, pseudotumoral infiltrative pattern and, without treatment, carries a case fatality rate approaching 100% within 10–15 years of infection. Crucially, AE shares the same fundamental biological substrate as intestinal cestode infections — tapeworm-derived larval structures — making albendazole's anti-tubulin mechanism directly applicable across both disease contexts. Surgical resection is only feasible in 30–40% of cases, placing albendazole at the centre of long-term pharmacological management.

International guidelines from WHO and the European Register of Cystic Echinococcosis (ERCE) explicitly list albendazole as the long-term first-line pharmacotherapy for inoperable AE, and as perioperative adjuvant therapy to reduce recurrence risk. A completed Phase 2 clinical trial (NCT07182305, N=194, Kyrgyzstan) directly evaluated albendazole monotherapy in early-stage AE identified through ultrasound surveillance in a high-prevalence setting, providing the highest-grade direct clinical evidence for this indication to date.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT07182305](https://clinicaltrials.gov/study/NCT07182305) | Phase 2 | Completed | 194 | Direct evaluation of albendazole monotherapy in early-stage alveolar echinococcosis in Kyrgyzstan (prevalence ~6% in the study region). This is the highest-grade direct clinical evidence for albendazole in AE; confirms parasitostatic effect and establishes feasibility of early pharmacological intervention. |
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | NA | Completed | 50 | EchinoVISTA prospective study — evaluation of parasite viability markers and biological/imaging parameters in hepatic AE patients treated with albendazole. Aimed to optimise the timing of treatment withdrawal; indirectly supports the need for a robust therapeutic monitoring framework. |
| [NCT06483880](https://clinicaltrials.gov/study/NCT06483880) | NA | Unknown | 24 | Randomised controlled trial of adjuvant albendazole versus placebo following pulmonary hydatid cyst resection (cystic echinococcosis, *E. granulosus*). Mechanism is identical to AE treatment, though the *Echinococcus* subtype differs. Trial status is unknown; interpret with caution. |
| [NCT05824442](https://clinicaltrials.gov/study/NCT05824442) | NA | Recruiting | 43 | Development of multiplex quantitative PCR for echinococcosis diagnosis. Primarily a diagnostic technology study; does not directly assess albendazole efficacy. Confirms active research interest in AE management pathways. |
| [NCT07176598](https://clinicaltrials.gov/study/NCT07176598) | N/A | Completed | 1 | Single case report of misdiagnosed primary intramuscular hydatid cyst treated with albendazole following surgical excision. Evidence strength is very low; for reference only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [19931502](https://pubmed.ncbi.nlm.nih.gov/19931502/) | 2010 | Expert Consensus / Clinical Guideline | Acta Tropica | WHO-IWGE international expert consensus on diagnosis and treatment of cystic and alveolar echinococcosis. Establishes albendazole as the pharmacological cornerstone; reviews classification, follow-up, and treatment withdrawal criteria. |
| [30760475](https://pubmed.ncbi.nlm.nih.gov/30760475/) | 2019 | Comprehensive Review | Clinical Microbiology Reviews | Major 21st-century advances in echinococcosis — molecular epidemiology, diagnostic tools, and treatment techniques including benzimidazole pharmacotherapy for both CE and AE, with particular focus on western China as the highest-endemicity region. |
| [39254012](https://pubmed.ncbi.nlm.nih.gov/39254012/) | 2024 | Comprehensive Review | Tidsskrift for den Norske laegeforening | Current clinical review of AE including its pseudotumoral liver presentation, diagnosis, and treatment. Confirms prolonged albendazole combined with surgery as the standard approach; discusses emerging cases in previously non-endemic countries. |
| [36974024](https://pubmed.ncbi.nlm.nih.gov/36974024/) | 2022 | Systematic Progress Review | Chinese Journal of Schistosomiasis Control | Systematic review of albendazole research advances specifically in AE treatment. Covers efficacy for patients unsuitable for surgery, and novel formulations aimed at overcoming poor oral bioavailability. |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Clinical Practice Review | World Journal of Gastroenterology | 2025 update on liver echinococcosis management. Confirms surgical resection as cornerstone, with albendazole as essential adjuvant and primary therapy for inoperable cases; discusses imaging-guided interventional options alongside pharmacotherapy. |
| [38501660](https://pubmed.ncbi.nlm.nih.gov/38501660/) | 2024 | Pharmacological / Mechanistic Study | Antimicrobial Agents and Chemotherapy | Metabolic mechanism and pharmacokinetics of albendazole in a hepatic AE rat model. Evaluates novel solubilising formulations (ABZ-CSD, TABZ-HCl-H, TABZ-HES-H) to address the known limitation of poor oral bioavailability — directly relevant to optimising clinical use. |
| [25526545](https://pubmed.ncbi.nlm.nih.gov/25526545/) | 2014 | Treatment Comparative Review | Parasite (Paris) | Reviews albendazole and mebendazole as the two licensed options for echinococcosis, and explores novel chemotherapeutic candidates. Highlights that no curative non-surgical drug currently exists, underscoring the parasitostatic limitation of current therapy. |
| [34808118](https://pubmed.ncbi.nlm.nih.gov/34808118/) | 2022 | Novel Treatment Options Review | Acta Tropica | Confirms that albendazole and mebendazole remain the only licensed non-surgical treatments for both CE and AE despite extensive research. Reviews novel candidates including repurposed drugs, immunotherapy, and combination strategies. |
| [39508157](https://pubmed.ncbi.nlm.nih.gov/39508157/) | 2024 | Drug Repurposing Study | Parasitology | Drug repurposing approach identifies pyronaridine (antimalarial) as a promising candidate against *E. multilocularis*. Directly contextualises albendazole's current status as the sole non-surgical pharmacological option, and the urgent need for improved or complementary therapies. |
| [12667231](https://pubmed.ncbi.nlm.nih.gov/12667231/) | 2003 | Clinical Review | Fundamental & Clinical Pharmacology | Two-decade retrospective on albendazole in echinococcal disease. Documents its evolution from experimental use to established standard of care in both CE and AE, including adjuvant roles alongside surgery and minimally invasive procedures. |

---

## Australia Market Information

Albendazole is **not currently registered** on the Australian Register of Therapeutic Goods (ARTG). There are no ARTG entries, approved indications, or Product Information documents available through the TGA for this drug.

For clinical use in Australia, albendazole would need to be accessed through one of the following regulatory pathways:

- **TGA Special Access Scheme (SAS) Category B** — for individual patients with serious or life-threatening conditions (appropriate for AE given its high mortality without treatment)
- **Authorised Prescriber pathway** — for clinicians treating a class of patients
- **Clinical trial authorisation** — for formal efficacy studies in an Australian context
- **New ARTG registration** — if a long-term commercialisation strategy is pursued

---

## Safety Considerations

As albendazole is not registered in Australia, no TGA-approved Product Information (PI) is available. For prescribers accessing albendazole via the Special Access Scheme or Authorised Prescriber pathway, please refer to approved PI documents from comparable regulatory authorities (FDA, EMA, UK MHRA) and WHO Model Formulary guidance.

Key safety considerations for long-term AE treatment (typically months to years) include:

- **Hepatotoxicity**: Elevated liver enzymes occur in a proportion of patients on prolonged therapy; regular liver function monitoring is essential
- **Bone marrow suppression**: Leucopenia and thrombocytopenia have been reported; periodic full blood count monitoring is recommended
- **Teratogenicity**: Albendazole is teratogenic in animal studies; it is contraindicated in pregnancy and requires effective contraception during treatment
- **Pharmacokinetic interactions**: Cimetidine, dexamethasone, and praziquantel significantly increase plasma levels of the active metabolite albendazole sulfoxide; dose adjustment may be required

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 clinical trial (N=194) provides direct evidence supporting albendazole in early-stage alveolar echinococcosis, and WHO/ERCE international guidelines already endorse albendazole as the first-line non-surgical pharmacotherapy for this life-threatening condition. The mechanistic basis is sound, and the global evidence base is substantial. However, albendazole is not currently registered in Australia, requiring a formal regulatory access pathway before any clinical use. Given AE's high mortality without treatment, the risk-benefit profile strongly favours access under appropriate clinical governance.

**To proceed, the following is needed:**
- Establish a TGA regulatory access pathway (Special Access Scheme Category B is the most immediate option for individual patients)
- Obtain relevant international PI documents (FDA/EMA) and adapt a local clinical monitoring protocol
- Confirm pharmaceutical-grade albendazole supply chain and product availability in Australia
- Develop a structured clinical monitoring plan for long-term use: liver function tests (LFTs), full blood count (FBC), and pregnancy screening prior to and during treatment
- Engage a multidisciplinary team including infectious disease specialists, hepatobiliary surgeons, and clinical pharmacists
- Consider formal documentation of AE cases in Australia to support future ARTG registration or expanded access application

---

> **Disclaimer**: This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. Any use of albendazole in Australia must comply with TGA regulatory requirements.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

