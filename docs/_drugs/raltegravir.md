---
layout: default
title: Raltegravir
parent: 僅模型預測 (L5)
nav_order: 579
evidence_level: L5
indication_count: 10
---

# Raltegravir
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

# Raltegravir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Raltegravir is a globally established antiretroviral (an HIV-1 integrase strand transfer inhibitor), though no original indication or original mechanism-of-action text is recorded in this evidence pack.
The TxGNN model's top-ranked prediction is **Simian Immunodeficiency Virus (SIV) Infection** — an animal (macaque) lentiviral disease, not a human condition —
supported by only **1 withdrawn clinical trial (0 enrolled)** and **19 publications**, all of which are preclinical/animal or in-vitro studies.
This top-ranked prediction is not clinically actionable for human patients; more clinically relevant signals exist lower in the ranked list (see *Additional Observations* below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (raltegravir is internationally established as an antiretroviral for HIV-1 infection, but no source indication text was captured here) |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L3 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action text for raltegravir is not available in this dataset (data gap DG002). Based on the drug's well-established pharmacological identity — referenced repeatedly across this pack's own repurposing rationales — raltegravir is an HIV-1 **integrase strand transfer inhibitor (INSTI)**, blocking the strand-transfer step by which retroviral DNA integrates into the host genome.

SIV and HIV are both lentiviruses, and the integrase enzyme is highly conserved between the two. This conservation is exactly why raltegravir shows direct antiviral activity against SIV in vitro and in macaque models — several of the retrieved papers document this explicitly (e.g., PMID 20233398, "Response of a simian immunodeficiency virus to raltegravir").

However, this mechanistic overlap only demonstrates cross-species antiviral activity in a **laboratory/animal-model context** used by researchers to study lentiviral persistence and integrase-inhibitor resistance — it is not a human disease indication. SIV infection occurs in nonhuman primates, not in Australian patients, so this prediction should be read as confirmation of raltegravir's known antiviral class mechanism rather than a genuine new human therapeutic opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | N/A | Withdrawn | 0 | Titled around HIV/SIV decay kinetics with raltegravir, but per this pack's own relevance review this is actually a **human** HIV pharmacodynamics study, not an SIV animal trial — it was withdrawn before enrolment and contributes no usable evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20233398](https://pubmed.ncbi.nlm.nih.gov/20233398/) | 2010 | Animal study | Retrovirology | Foundational paper: raltegravir-based ART regimen (with two NRTIs) suppresses SIVmac251 in rhesus macaques, establishing an SIV/ART model for lentiviral persistence research. |
| [29643246](https://pubmed.ncbi.nlm.nih.gov/29643246/) | 2018 | Animal study | J Virol | Analyses dynamics of 2-LTR circles (failed integration products) in raltegravir-treated, SIV-infected macaques with/without CD8+ cell depletion. |
| [29466356](https://pubmed.ncbi.nlm.nih.gov/29466356/) | 2018 | Animal study | PLoS One | Documents emergence of integrase resistance mutations in SIV-infected macaques receiving non-suppressive raltegravir-containing ART. |
| [31597776](https://pubmed.ncbi.nlm.nih.gov/31597776/) | 2019 | Animal study | J Virol | Evaluates intactness of persistent viral genomes in SIV-infected macaques after early ART initiation (integrase-inhibitor-containing regimens). |
| [32166319](https://pubmed.ncbi.nlm.nih.gov/32166319/) | 2020 | Animal study | Clin Infect Dis | Raltegravir and dolutegravir exert proadipogenic/profibrotic effects and induce insulin resistance in human/simian adipose tissue — a safety-relevant mechanistic finding, not an efficacy signal. |
| [26378179](https://pubmed.ncbi.nlm.nih.gov/26378179/) | 2015 | Animal study | J Virol | Characterises drug-resistance profiles of integrase inhibitors (including raltegravir) in SIVmac239, confirming cross-species relevance of known HIV resistance mutations. |
| [24622515](https://pubmed.ncbi.nlm.nih.gov/24622515/) | 2014 | Animal study | Sci Transl Med | Topical integrase inhibitors given post-coitally protect macaques from vaginal SHIV infection — a prevention/microbicide model, not a treatment indication. |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Animal study | mBio | Shows lentiviral (SIV/HIV) persistence in brain tissue despite effective ART, including integrase-inhibitor-based regimens. |
| [28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/) | 2017 | In vitro | Antimicrob Agents Chemother | Compares antiviral activity of newer integrase inhibitors (bictegravir, cabotegravir) against integrase-inhibitor-resistant SIVmac239 and HIV-1; raltegravir referenced as an older comparator with a lower resistance barrier. |
| [23365453](https://pubmed.ncbi.nlm.nih.gov/23365453/) | 2013 | In vitro | J Virol | In-vitro susceptibility screen of simian retrovirus type 4 (a different simian retrovirus) to antiretrovirals including raltegravir. |

---

## Australia Market Information

No ARTG entries are recorded for raltegravir in this evidence pack (Australia market status: Not Marketed, 0 licenses on file).

> This should be treated as a data gap requiring verification rather than a confirmed regulatory fact — raltegravir is an internationally established antiretroviral, and its current TGA/ARTG registration status should be independently confirmed before this "Not Marketed" status is relied upon.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No structured warnings, contraindications, or drug–drug interaction data were returned for this record in the current evidence pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (SIV infection) targets a nonhuman primate disease with no direct relevance to human patients. Its only associated clinical trial was withdrawn with zero enrolment, and its literature base consists exclusively of preclinical/animal and in-vitro mechanism studies (Evidence Level L3) — sufficient to confirm raltegravir's antiviral mechanism against lentiviruses generally, but not to support any human clinical development pathway for this specific "indication."

**To proceed, the following is needed:**
- TFDA/TGA-approved PI warnings and contraindications (currently a **Blocking** data gap — required before any safety screening)
- Structured mechanism-of-action data from DrugBank (**High**-priority data gap)
- Verification of raltegravir's current Australian TGA/ARTG registration status, given it is a well-established antiretroviral internationally
- This candidate itself requires no further clinical investigation; effort is better directed to the more evidence-supported candidates below

---

## Additional Observations: Higher-Evidence Candidates Further Down the Ranking

While the top-ranked prediction has no human clinical relevance, two lower-ranked candidates carry substantially stronger evidence (**L1**, "Proceed with Guardrails") and warrant separate mention — with the important caveat that both sit **within raltegravir's existing HIV/AIDS therapeutic class** rather than representing a genuinely novel disease area.

### Rank 4 — AIDS Related Complex (Score 96.49%, L1, Proceed with Guardrails)

Raltegravir's integrase-inhibitor mechanism directly applies to AIDS-related complex as part of the HIV/AIDS disease spectrum. This is best understood as confirmatory overlap with raltegravir's core use rather than new-indication repurposing.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02383355](https://clinicaltrials.gov/study/NCT02383355) | Phase 4 | Completed | 40 | Switch from NNRTI/PI-based regimen to raltegravir-based regimen in virologically suppressed HIV patients; assessed platelet reactivity and inflammatory/thrombotic markers. |
| [NCT00485264](https://clinicaltrials.gov/study/NCT00485264) | Phase 1/2 | Completed | 153 | IMPAACT study of raltegravir safety, tolerability, PK and antiviral activity in HIV-1-infected children and adolescents. |
| [NCT01076179](https://clinicaltrials.gov/study/NCT01076179) | N/A | Completed | 502 | Tolerability of lopinavir/ritonavir combined with newer agents including integrase inhibitors. |

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25394095](https://pubmed.ncbi.nlm.nih.gov/25394095/) | 2014 | Cohort | J Int AIDS Soc | Raltegravir shown to have a favourable drug-interaction profile, efficacy and safety in HIV patients undergoing concurrent antineoplastic chemotherapy. |
| [33886444](https://pubmed.ncbi.nlm.nih.gov/33886444/) | 2022 | Case Report | Acta Clin Belg | MAC and *Cryptococcus neoformans* co-infection in an AIDS patient. |
| [37568163](https://pubmed.ncbi.nlm.nih.gov/37568163/) | 2023 | Case Report | AIDS Res Ther | Heart transplant in an HIV patient, navigating ART/immunosuppressant drug interactions. |

### Rank 5 — Congenital/Perinatal HIV (Score 96.49%, L1, Proceed with Guardrails)

Vertical (mother-to-child) HIV transmission is again within raltegravir's known antiretroviral use, with a genuine, dedicated evidence base in pregnancy and neonates — but also an identified **safety signal requiring monitoring**.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01780831](https://clinicaltrials.gov/study/NCT01780831) | Phase 1 | Completed | 52 | Safety and PK of raltegravir in HIV-1-exposed neonates at risk of acquiring infection. |
| [NCT01828073](https://clinicaltrials.gov/study/NCT01828073) | N/A | Completed | 40 | Washout PK and safety of in-utero/intrapartum raltegravir exposure in infants born to mothers on raltegravir. |
| [NCT00105157](https://clinicaltrials.gov/study/NCT00105157) | Phase 2 | Completed | 179 | Raltegravir (MK0518) plus optimised background therapy vs background therapy alone in resistant HIV infection. |
| [NCT04518228](https://clinicaltrials.gov/study/NCT04518228) | N/A | Completed | 205 | PK of antiretroviral and anti-TB drugs during pregnancy and postpartum, including raltegravir-containing regimens. |

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30531300](https://pubmed.ncbi.nlm.nih.gov/30531300/) | 2019 | Cohort/Surveillance | J Acquir Immune Defic Syndr | UK/Ireland surveillance of congenital anomalies after raltegravir or elvitegravir exposure in pregnancy — no clear excess signal for raltegravir specifically, in contrast to dolutegravir. |
| [39086081](https://pubmed.ncbi.nlm.nih.gov/39086081/) | 2024 | Pharmacovigilance | Pharmacol Res Perspect | VigiBase case/non-case analysis of integrase-inhibitor exposure in pregnancy and congenital anomalies. |
| [33048878](https://pubmed.ncbi.nlm.nih.gov/33048878/) | 2021 | Cohort | AIDS | Risk of birth defects and perinatal outcomes with integrase-inhibitor exposure in pregnancy. |
| [38864586](https://pubmed.ncbi.nlm.nih.gov/38864586/) | 2024 | Cohort | AIDS | US cohort study of first-trimester exposure to newer antiretrovirals (including raltegravir) and congenital anomalies. |

> **Safety note:** Several of the above publications originated from a WHO pharmacovigilance signal on **neural tube defects with dolutegravir**; raltegravir/elvitegravir-specific data has generally been reassuring but is based on smaller sample sizes. Any perinatal use should be guided by current obstetric HIV-management guidelines and TGA PI, not by this evidence pack alone.

**Recommended handling:** Both candidates should be routed to a clinical pharmacology reviewer as *label-extension confirmations* rather than new repurposing candidates — they reaffirm raltegravir's core antiretroviral role rather than opening a new therapeutic area.

**Separately:** Ranks 2–3 and 6–10 (feline AIDS, an ultra-rare neurodevelopmental disorder, familial hyperlipidaemia, prostate fibroma, breast fibrocystic disease, benign reproductive neoplasm, Brenner tumour) all carry **L5** evidence with no supporting trials or literature, and in two cases (feline AIDS, SIV) the retrieved "clinical trials" were confirmed by the pack's own relevance review to be **mislabelled human HIV trials**, not genuine matches. This cluster of tightly-scored (~93–99%), zero-evidence predictions is consistent with a knowledge-graph hub-node/embedding artifact rather than genuine repurposing signal, and may warrant a modelling-team audit of similarly-scored candidates for other antiretroviral drugs.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

