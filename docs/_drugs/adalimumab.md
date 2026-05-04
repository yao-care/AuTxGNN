---
layout: default
title: Adalimumab
parent: 僅模型預測 (L5)
nav_order: 24
evidence_level: L5
indication_count: 10
---

# Adalimumab
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

# Adalimumab: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Adalimumab is a fully human anti-TNF-α monoclonal antibody, approved internationally for a range of chronic inflammatory conditions including rheumatoid arthritis, though it is currently not listed on the Australian Register of Therapeutic Goods (ARTG).
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis** — one of the most severe extra-articular complications of rheumatoid arthritis — with **1 systematic review and multiple case-level publications** supporting this direction, though no directly relevant clinical trials were identified.
The biological rationale is compelling, as TNF-α is a central driver of the vascular inflammation seen in rheumatoid vasculitis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid Arthritis (approved internationally; no current ARTG listing) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L3 |
| Australia Market Status | Not on market |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this dataset. Based on established clinical knowledge, adalimumab is a recombinant fully human IgG1 monoclonal antibody that binds with high specificity to both soluble and membrane-bound TNF-α, blocking its interaction with the p55 and p75 cell surface TNF receptors. This disrupts downstream NF-κB activation and suppresses the production of pro-inflammatory mediators — including IL-1, IL-6, IL-8, matrix metalloproteinases, and RANKL — thereby attenuating systemic inflammation at a fundamental level.

Rheumatoid vasculitis (RV) is a severe extra-articular manifestation of longstanding, poorly controlled rheumatoid arthritis, affecting approximately 1–5% of patients with severe RA. Its pathology is characterised by TNF-α–driven immune complex deposition in vessel walls, complement activation, and neutrophil infiltration causing fibrinoid necrosis of small-to-medium vessels. This is precisely the inflammatory axis that adalimumab targets. The mechanistic link between the drug and rheumatoid vasculitis is therefore biologically well-founded.

RA and RV share the same fundamental immunological substrate — dysregulated TNF-α signalling — making this prediction a logical extension of the drug's known mechanism rather than a speculative leap. The systematic review by Cerqueira et al. (2021) confirmed that TNF-α inhibitors, including adalimumab, are now incorporated into the therapeutic approach for RV. Direct case evidence further documents successful use of adalimumab in digital vasculitis and prevention of recurrent pulmonary hypertension in the RV setting. Clinicians should nonetheless be aware of a paradoxical risk: in a minority of patients, TNF-α inhibitors can themselves induce vasculitis-like reactions — a nuance that requires careful clinical differentiation.

---

## Clinical Trial Evidence

> ⚠️ **Important note:** All 5 retrieved trials carry Grade C relevance — none directly evaluate adalimumab for rheumatoid vasculitis. They are listed for background context only. The low incidence of RV (1–5% of severe RA patients) makes dedicated RCT conduct inherently challenging.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Multicentre observational study of tocilizumab in RA patients with inadequate response to DMARDs or one prior biologic; provides general biologic use context in RA but does not assess a vasculitis subgroup |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large epidemiological study assessing the risk of developing new immune-mediated inflammatory diseases (IMIDs) in patients treated with biologics or immunosuppressants for a single IMID; relevant as safety background only |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Evaluates immunosuppressant management protocols in rheumatology patients undergoing elective total shoulder arthroplasty; no direct relevance to vasculitis treatment |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Completed | 808 | Cross-sectional study of bDMARD treatment patterns in RA patients in China; describes demographics and treatment patterns but does not study vasculitis outcomes |
| [NCT05111743](https://clinicaltrials.gov/study/NCT05111743) | N/A | Completed | 9,261 | Real-world safety study of brolucizumab for neovascular (wet) AMD — **entirely unrelated** to adalimumab or rheumatoid vasculitis; likely a search indexing mismatch |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Systematic Review | Clinical Rheumatology | PRISMA-based systematic review on biological therapy in rheumatoid vasculitis; confirms that TNF-α inhibitors are now part of the therapeutic armamentarium for RV alongside corticosteroids and immunosuppressants; summarises adalimumab case series evidence |
| [34068884](https://pubmed.ncbi.nlm.nih.gov/34068884/) | 2021 | Narrative Review | Journal of Clinical Medicine | Overview of RA-associated episcleritis and scleritis (vascular ocular manifestations); RA accounts for 8–15% of scleritis cases; reviews biologic management including TNF-α inhibitors |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohort | RMD Open | BSRBR-RA registry study comparing lupus-like and vasculitis-like event rates in TNFi-treated vs. non-biologic DMARD-treated RA patients; characterises drug-specific vasculitis risk profiles |
| [30773522](https://pubmed.ncbi.nlm.nih.gov/30773522/) | 2019 | Case Report | Internal Medicine (Tokyo) | Acute pulmonary hypertension crisis emerged 8 months after adalimumab dose reduction in a patient with rheumatoid vasculitis — directly supports adalimumab's role in suppressing active RV |
| [25133007](https://pubmed.ncbi.nlm.nih.gov/25133007/) | 2014 | Case Report | Case Reports in Rheumatology | A 42-year-old woman with 15-year RA history presenting with necrotising digital ulcers responded well to adalimumab therapy; one of the most direct case reports of therapeutic benefit |
| [37699653](https://pubmed.ncbi.nlm.nih.gov/37699653/) | 2024 | Cohort | Annals of the Rheumatic Diseases | HLA-DRB1 and HLA-DQA1 alleles associated with anti-adalimumab antibody formation in RA patients; relevant for identifying patients at risk of immunogenicity-driven treatment failure |
| [38931826](https://pubmed.ncbi.nlm.nih.gov/38931826/) | 2024 | PK Study | Pharmaceutics | Population pharmacokinetic modelling of adalimumab and etanercept biosimilar dosing intervals in RA; evaluates whether modified dosing achieves target drug levels faster |
| [28719435](https://pubmed.ncbi.nlm.nih.gov/28719435/) | 2018 | Case Report | American Journal of Dermatopathology | ⚠️ **Paradoxical reaction:** First reported case of leukocytoclastic vasculitis with perivascular hemophagocytosis as an **adverse effect** of adalimumab therapy — clinicians must distinguish TNF inhibitor-induced vasculitis from RV being treated |
| [36418100](https://pubmed.ncbi.nlm.nih.gov/36418100/) | 2023 | Case Report | Internal Medicine (Tokyo) | ANCA-associated nephritis with elevated MPO-ANCA developed during combined abatacept + adalimumab therapy for RA; subsequently attenuated by tocilizumab — highlights risk of immune-mediated renal adverse events |
| [21385558](https://pubmed.ncbi.nlm.nih.gov/21385558/) | 2011 | Case Report | Clinical and Experimental Rheumatology | Successful treatment with tocilizumab (anti-IL-6R) in a patient with multidrug-refractory, **anti-TNF-resistant** systemic RV — highlights that a subset of RV does not respond to TNF-axis blockade and may require alternative biologics |

---

## Australia Market Information

Adalimumab is **not currently listed on the Australian Register of Therapeutic Goods (ARTG)**. This data pack returned zero ARTG entries. This is a notable finding, as adalimumab (Humira® and multiple biosimilars) is approved in the USA, EU, UK, Japan, and numerous other jurisdictions across a broad range of inflammatory indications.

Australian clinicians wishing to prescribe adalimumab should explore the following TGA access pathways:
- **Special Access Scheme (SAS)** — for individual patients with unmet clinical needs
- **Authorised Prescriber (AP) pathway** — for practitioners treating specific patient populations

No ARTG product entries are available to display.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) — or international equivalent (e.g., TGA SAS submission PI, or Humira® Australian PI if available via the manufacturer) — for comprehensive safety information, as no local safety data were retrievable from this dataset.

> **Clinical advisory based on published literature:** As a class, TNF-α inhibitors carry well-established risks that require pre-treatment screening and ongoing monitoring. These include:
> - **Serious infections**, particularly reactivation of latent tuberculosis (mandatory TB screening before initiation) and hepatitis B
> - **Malignancy risk** (FDA black-box warning, including lymphoma)
> - **Paradoxical autoimmune reactions**, including drug-induced vasculitis, lupus-like syndrome, and demyelinating disease
> - **Cardiac caution** in patients with congestive heart failure (use not recommended in moderate-to-severe CHF)
>
> In the specific context of rheumatoid vasculitis, clinicians must carefully distinguish between RV being **treated** with adalimumab and TNF inhibitor-**induced** vasculitis, which requires drug withdrawal rather than continuation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The biological case for adalimumab in rheumatoid vasculitis is strong — TNF-α neutralisation directly targets the immunopathological driver of RV — and is supported by one systematic review and direct case evidence of therapeutic benefit. However, the absence of any registered RCT evidence for this specific indication, the absence of ARTG registration in Australia, and the important paradoxical risk of TNF inhibitor-induced vasculitis collectively necessitate close clinical oversight before broader application.

**To proceed, the following is needed:**

- **Regulatory pathway confirmed:** Identify the appropriate TGA access mechanism (SAS or Authorised Prescriber) given the absence of an ARTG listing for adalimumab in Australia
- **PI and safety data obtained:** Download and review the manufacturer's Australian Product Information document or international equivalent through TGA SAS application
- **Pre-treatment screening completed:** Mandatory TB screening (Mantoux/IGRA + chest X-ray), hepatitis B serology, and baseline malignancy risk assessment
- **Vasculitis subtype clarification:** Ensure the diagnosis is confirmed as **rheumatoid vasculitis** (RA-driven, TNF-mediated) rather than drug-induced vasculitis, which requires the opposite approach
- **Specialist rheumatology-led management plan:** Multidisciplinary input recommended depending on organ involvement (nephrology for renal vasculitis, dermatology for cutaneous vasculitis, ophthalmology for ocular involvement)
- **Monitoring plan established:** Clinical assessment, inflammatory markers (ESR, CRP, ANCA where relevant), and safety bloods (FBC, LFTs, renal function) at regular intervals
- **Biosimilar consideration:** Multiple adalimumab biosimilars are available internationally; if ARTG listing is sought, biosimilar registration may offer a more accessible pathway

> **Research priority:** Given the rarity of RV, a prospective multicentre Australian registry or investigator-initiated study of biologic therapy in RV would provide the controlled evidence needed to establish Level 2 evidence for this indication.

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Data cutoff: 4 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

