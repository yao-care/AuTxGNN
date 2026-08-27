---
layout: default
title: Itraconazole
parent: 僅模型預測 (L5)
nav_order: 369
evidence_level: L5
indication_count: 10
---

# Itraconazole
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

# Itraconazole: From Systemic Fungal Infections to Pneumocystosis

## One-Sentence Summary

Itraconazole is a broad-spectrum triazole antifungal used globally for systemic fungal infections including aspergillosis, histoplasmosis, and candidiasis, but is currently not registered in Australia (no ARTG entries).
The TxGNN model predicts it may be effective for **Pneumocystosis** (Pneumocystis jirovecii pneumonia, PCP),
with **0 clinical trials** and **20 publications** available — however, all publications provide indirect rather than direct evidence for this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Australia; globally used for systemic fungal infections (aspergillosis, histoplasmosis, onychomycosis, candidiasis) |
| Predicted New Indication | Pneumocystosis (Pneumocystis jirovecii pneumonia) |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed in Australia |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Itraconazole is a triazole antifungal that works by inhibiting the fungal enzyme CYP51 (lanosterol 14α-demethylase), which blocks ergosterol biosynthesis and disrupts cell membrane integrity. This mechanism is highly effective against fungi whose membranes are predominantly composed of ergosterol — such as *Aspergillus* species, *Histoplasma capsulatum*, and *Cryptococcus neoformans*. Its broad-spectrum activity across diverse fungal pathogens makes it a logical candidate for knowledge-graph-based repurposing predictions.

However, the mechanistic basis for treating PCP with itraconazole is weak. *Pneumocystis jirovecii* has an unusual cell membrane composition with very low ergosterol content, and its CYP51 enzyme is structurally insensitive to azole-class drugs. A key 2003 molecular biology study (PMID 12606318) cloned the *P. carinii* Erg11 gene and identified structural differences at known azole-resistance sites — providing a clear biological explanation for why itraconazole lacks clinically meaningful activity against *Pneumocystis* in practice.

The TxGNN high score (0.993) most likely reflects knowledge-graph co-associations between PCP and other fungal infections in immunocompromised patients, rather than direct pharmacological evidence. PCP frequently co-occurs with invasive fungal infections that itraconazole does treat, creating indirect graph-level connections that do not translate into clinical efficacy. Standard first-line treatment for PCP remains trimethoprim-sulfamethoxazole (TMP-SMX), and no guideline recommends azole antifungals as primary or salvage therapy for this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | RCT | HIV Medicine | Phase III double-blind RCT of itraconazole prophylaxis against deep fungal infections in HIV-immunocompromised patients (n not specified for PCP arm); primary endpoint was invasive fungal disease prevention — PCP was not the target; does not support itraconazole for PCP |
| [12606318](https://pubmed.ncbi.nlm.nih.gov/12606318/) | 2003 | Basic Science | Am J Respir Cell Mol Biol | Molecular characterisation of lanosterol 14α-demethylase (Erg11) from *P. carinii*; identified structural differences at 2 of 13 azole-resistance sites — provides direct mechanistic evidence for intrinsic azole insensitivity in Pneumocystis |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Guideline/Review | BMJ Clinical Evidence | HIV opportunistic infection prophylaxis guidelines; TMP-SMX confirmed as first-line for PCP prophylaxis and treatment; itraconazole not listed as an option for PCP |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Comprehensive review of therapy and prophylaxis for systemic protozoan infections including *P. carinii*; covers MOA, dosing, and efficacy but focuses on non-azole agents |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Case Report | Front Immunol | *Talaromyces marneffei* + *P. jirovecii* co-infection in a child with STAT1 mutation; itraconazole was used for the talaromycosis component only — indirect association with PCP context |
| [30429396](https://pubmed.ncbi.nlm.nih.gov/30429396/) | 2018 | Observational | Indian J Med Microbiol | Retrospective study of respiratory fungal pathogens in immunocompetent vs. immunocompromised hosts; PCP discussed as background pathogen alongside invasive moulds and yeasts treated with itraconazole |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Review | Semin Respir Infect | Post-lung transplant infection management review; PCP discussed in context of prophylaxis strategies — itraconazole mentioned for other fungal pathogens, not for PCP |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Curr Clin Top Infect Dis | BMT infection prophylaxis review; itraconazole discussed as antifungal prophylaxis agent; PCP prevention addressed separately with TMP-SMX — no mechanistic or clinical link between itraconazole and PCP |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Retrospective Cohort | Transplant Proc | Invasive fungal infections in kidney transplant recipients; PCP listed as co-morbidity background; itraconazole used for other fungal pathogens in this cohort |
| [8967681](https://pubmed.ncbi.nlm.nih.gov/8967681/) | 1996 | Case Report | Ann Intern Med | Uveitis associated with rifabutin prophylaxis and concurrent itraconazole therapy in an HIV patient with a history of PCP; highlights a drug-drug interaction, not itraconazole efficacy for PCP |

---

## Australia Market Information

Itraconazole (DrugBank ID: DB01167) has no current ARTG registration in Australia. As at the data cut-off (22 June 2026), the drug is **not marketed** in Australia, with zero ARTG entries recorded.

For reference purposes, itraconazole is registered in comparable markets including the United States (FDA), the European Union (EMA), and New Zealand (Medsafe), where it is approved for systemic fungal infections such as aspergillosis, histoplasmosis, blastomycosis, and onychomycosis.

> Clinicians requiring current safety and prescribing information should consult international Product Information documents (e.g., FDA label or EMA SmPC) or liaise with a clinical pharmacist.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> **Note:** No TGA-registered Product Information is currently available for itraconazole in Australia. Until Australian registration is obtained, clinicians should refer to international prescribing information and standard clinical pharmacy resources for guidance on dosing, contraindications, and drug interactions. Key considerations from international data include significant CYP3A4-mediated drug interactions, negative inotropic effects (contraindicated in ventricular dysfunction), and QTc prolongation risk with concomitant agents.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis for itraconazole in PCP is absent — *P. jirovecii* has very low ergosterol content and its CYP51 is structurally insensitive to azole-class drugs (confirmed molecularly, PMID 12606318). None of the 20 identified publications provide direct evidence of itraconazole efficacy in PCP, and the high TxGNN prediction score most likely reflects knowledge-graph co-morbidity associations rather than genuine pharmacological activity. The TxGNN prediction does not carry clinical translation value for this indication.

**To proceed, the following would be needed:**

- Identification of an alternative pharmacological target in *P. jirovecii* that itraconazole could plausibly modulate beyond CYP51 ergosterol synthesis
- Direct in vitro susceptibility testing of itraconazole against *P. jirovecii* under standardised conditions (acknowledging that *P. jirovecii* is notoriously difficult to culture)
- A formal hypothesis-generating preclinical or computational mechanistic study before any clinical investigation could be justified
- Review of whether TxGNN model architecture can be refined to down-weight co-morbidity-driven graph associations that do not reflect direct drug–pathogen pharmacology
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

