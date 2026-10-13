---
layout: default
title: Acyclovir
parent: Model Prediction Only (L5)
nav_order: 24
evidence_level: L5
indication_count: 10
---

# Acyclovir
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

# Acyclovir: From Herpesvirus Infections to Common Wart

## One-Sentence Summary

Acyclovir is an antiviral drug originally used to treat herpes simplex infections, herpes zoster (shingles), chickenpox, herpes labialis, herpes simplex encephalitis and genital herpes.
The TxGNN model's top-ranked prediction is **punctate epithelial keratoconjunctivitis**, but it has no supporting trials. The best-supported prediction is **common wart**, with **4 clinical trials** and a **published randomised controlled trial (RCT)** with several smaller comparative studies of intralesional acyclovir.
This report therefore evaluates the common wart prediction (rank 2) as the main candidate and covers the other predictions briefly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Herpes simplex infections, herpes zoster, chickenpox, herpes labialis, herpes simplex encephalitis, genital herpes (the ARTG entry has no indication text recorded) |
| Predicted New Indication | Common wart (the top-ranked prediction, punctate epithelial keratoconjunctivitis, has no clinical support) |
| TxGNN Prediction Score | 99.46% for common wart (99.67% for punctate epithelial keratoconjunctivitis) |
| Evidence Level | L2 (common wart) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails (as a research question, not for routine use) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Acyclovir is a nucleoside analogue (a guanosine analogue) that is known to work against herpes simplex virus and varicella-zoster virus. Its efficacy in these infections is established.

Common warts are caused by human papillomavirus (HPV), a DNA virus. HPV does not have the viral thymidine kinase that acyclovir normally relies on to be activated, so a direct antiviral effect is unlikely. Proposed explanations for the observed effect of intralesional (injected into the lesion) or oral acyclovir include non-specific immune stimulation and a local irritation-triggered immune response. These explanations are hypotheses rather than established mechanisms.

The clinical signal is nonetheless consistent. Several small randomised studies have compared intralesional acyclovir with cryotherapy, Candida antigen, vitamin D3, 5-fluorouracil, HPV vaccine, hepatitis B vaccine and PPD immunotherapy. These trials are small (40–92 participants), mostly single-centre, and several have unknown registry status. Confirmatory Phase 3 evidence is lacking.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06261684](https://clinicaltrials.gov/study/NCT06261684) | Phase 2/3 | Unknown | 92 | Intralesional acyclovir vs cryotherapy in plantar warts (RCT); published as PMID 40889709 |
| [NCT05429151](https://clinicaltrials.gov/study/NCT05429151) | Phase 4 | Unknown | 40 | Intralesional acyclovir vs Candida antigen in plantar warts, with dermoscopic assessment |
| [NCT07448844](https://clinicaltrials.gov/study/NCT07448844) | Phase 4 | Recruiting | 40 | Intralesional vitamin D3 vs acyclovir in cutaneous viral warts (people aged 12 and over); no results yet |
| [NCT05324904](https://clinicaltrials.gov/study/NCT05324904) | Not specified | Unknown | 44 | Intralesional vitamin D3 vs acyclovir in plantar warts |

No ANZCTR identifiers were available in the data compiled for this report.

For **disease of orbital region** (rank 9, mostly herpetic eye disease), the relevant registered trials are small:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT06757907](https://clinicaltrials.gov/study/NCT06757907) | Not specified | Completed | 20 | Topical ganciclovir vs systemic acyclovir in herpetic keratitis (acyclovir is the comparator) |
| [NCT03389191](https://clinicaltrials.gov/study/NCT03389191) | Not specified | Unknown | 30 | Oral acyclovir in refractory viral uveitis |
| [NCT05313828](https://clinicaltrials.gov/study/NCT05313828) | Not specified | Unknown | 40 | Comparison of treatment modalities for dendritic viral ulcer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40889709](https://pubmed.ncbi.nlm.nih.gov/40889709/) | 2026 | RCT | J Am Acad Dermatol | Intralesional acyclovir vs cryotherapy in plantar warts |
| [40488756](https://pubmed.ncbi.nlm.nih.gov/40488756/) | 2025 | RCT/Comparative | Arch Dermatol Res | Intralesional acyclovir vs intralesional 5-fluorouracil in recalcitrant warts |
| [40056255](https://pubmed.ncbi.nlm.nih.gov/40056255/) | 2025 | RCT/Comparative | Arch Dermatol Res | Intralesional acyclovir vs quadrivalent HPV vaccine in recalcitrant cutaneous warts (60 patients) |
| [38822848](https://pubmed.ncbi.nlm.nih.gov/38822848/) | 2024 | RCT | Arch Dermatol Res | Intralesional acyclovir vs hepatitis B vaccine in resistant plantar warts (48 patients) |
| [41686619](https://pubmed.ncbi.nlm.nih.gov/41686619/) | 2026 | Systematic review and network meta-analysis | Medicine | Comparison of treatment modalities for cutaneous warts, including intralesional acyclovir |
| [37303436](https://pubmed.ncbi.nlm.nih.gov/37303436/) | 2023 | Comparative study | Cureus | Intralesional acyclovir vs intralesional PPD immunotherapy in viral warts |
| [34412535](https://pubmed.ncbi.nlm.nih.gov/34412535/) | 2022 | Clinical study | J Cutan Med Surg | Intralesional acyclovir as a potential option for cutaneous warts |
| [38793636](https://pubmed.ncbi.nlm.nih.gov/38793636/) | 2024 | Case series and review | Viruses | Remission of HPV-related disease (e.g. penile condyloma) with acyclovir or valaciclovir |
| [26885794](https://pubmed.ncbi.nlm.nih.gov/26885794/) | 2016 | Case report | J Drugs Dermatol | Persistent plantar warts resolved after oral acyclovir given for herpes zoster |
| [6467981](https://pubmed.ncbi.nlm.nih.gov/6467981/) | 1984 | Report | Cutis | Verrucae vulgares and acyclovir ointment |

Evidence for the other predictions is weak:
- **Punctate epithelial keratoconjunctivitis (rank 1):** the two retrieved papers concern microsporidial keratoconjunctivitis and corneal lipidosis in AIDS, and neither supports acyclovir use.
- **Sequela of COVID-19 (rank 6):** the literature mostly describes herpesvirus reactivation during or after COVID-19, where acyclovir treats the herpesvirus. One hypothesis paper ([35446232](https://pubmed.ncbi.nlm.nih.gov/35446232/)) is speculative.
- **Disease of orbital region (rank 9):** only case reports and a review of herpes zoster ophthalmicus, which largely extends the approved zoster indication.
- **Hepatitis C cirrhosis, vulvovaginal candidiasis, epidemic keratoconjunctivitis:** acyclovir has no expected activity against HCV, Candida or adenovirus, and the retrieved papers give no acyclovir-specific support.
- **Post-infectious neuralgia, eosinophilic pustular folliculitis, papular urticaria:** no trials or literature were retrieved.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1002R | XOROX | Eye ointment 30 mg per g, 4.5 g | Not recorded in the data compiled for this report |

The only registered product is an ophthalmic ointment. There is no registered intralesional or oral product in the data compiled for this report, so the route used in the wart studies (injection into the lesion) does not match the registered form. Route compatibility has not been assessed.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** the TxGNN knowledge graph links acyclovir to a long list of conditions, including hypertension, kidney disease and impaired renal function, diabetes mellitus and diabetic ketoacidosis, hyperglycaemia, adrenocortical insufficiency (Addison disease), obesity, stroke and cerebrovascular disorders, myocardial infarction, haemolytic-uraemic syndrome, thrombocytopenic purpura, peripheral vascular disease and skin atrophy. These come from graph relationships, not product labelling, and should be verified against the Product Information.
- **Drug interactions:** 454 interactions were identified. The Moderate-level interactions are with balsalazide, mesalazine, olsalazine, sulfasalazine and trospium. Other listed interactions have an unclassified severity, including amphotericin B, mannitol, calcitriol, metformin, glimepiride, rosiglitazone, morphine, doxycycline, epinephrine and the proton pump inhibitors omeprazole, pantoprazole and lansoprazole.

For key warnings and label contraindications, please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for common wart, as a research question only; Hold for all other predictions)

**Rationale:**
- Several small randomised studies, including a published RCT against cryotherapy, point in a consistent direction for intralesional acyclovir in warts. However, the trials are small and mostly single-centre, the mechanism is unclear, and no Phase 3 confirmation exists. The other nine predictions have little or no supporting evidence and should be held. The herpetic eye conditions (orbital region) largely extend existing approved uses.

**To proceed, the following is needed:**
- A larger, multicentre, preferably placebo- or standard-of-care-controlled Phase 3 trial of intralesional acyclovir in warts, with long-term recurrence follow-up
- Clarification of the mechanism of action, since the standard antiviral mechanism does not apply to HPV
- A formulation and route assessment, because the only ARTG-listed product is an eye ointment and no injectable or oral product was identified
- Review of the TGA Product Information for warnings and contraindications, which were not available in the data compiled for this report
- Verification of the knowledge-graph contraindications and the interaction list against the PI, particularly for patients with renal impairment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

