---
layout: default
title: Clavulanic Acid
parent: Model Prediction Only (L5)
nav_order: 169
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Clavulanic Acid: predicted new indication Ureaplasma urethritis (evidence level L3). Approved use: Urinary tract infection, bacterial pneumonia…"
monitor_inn: "clavulanic acid"
predicted_indications: ["Ureaplasma urethritis", "gonococcal urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "urogenital tuberculosis", "celiac trunk compression syndrome", "abdominal ectopic pregnancy", "abdominal cystic lymphangioma", "lymph node palisaded myofibroblastoma", "disease of uterine broad ligament"]
---

# Clavulanic Acid
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

## Clavulanic Acid: From Bacterial Infections to Ureaplasma urethritis
{: .text-alpha }

## One-Sentence Summary

Clavulanic acid is a beta-lactamase inhibitor, used in combination with amoxicillin to treat bacterial infections such as urinary tract infections and bacterial pneumonia.
The TxGNN model predicts it may be effective for **gonococcal urethritis** (the highest-ranked prediction with any real supporting literature), with **no registered clinical trials** and **9 publications**, mostly small, older studies from the 1980s.
This is largely a historical indication, so the evidence is limited in current relevance.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, bacterial pneumonia, staphylococcal infection, Escherichia coli infection, Klebsiella pneumonia and related bacterial infections (the approved indication text for the Australian listing was not available) |
| Predicted New Indication | Gonococcal urethritis (the top-ranked prediction, Ureaplasma urethritis, has a mechanistic mismatch; see below) |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

**Note on prediction ranking:** The rank 1 prediction, Ureaplasma urethritis (score 0.9993), is not recommended for evaluation. Ureaplasma lacks a cell wall, so beta-lactams are not expected to work. Gonococcal urethritis has the same score and the only meaningful clinical literature, so it is presented as the lead candidate.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, clavulanic acid is a beta-lactamase inhibitor. It has little antibacterial activity of its own, but it protects amoxicillin from being broken down by bacterial beta-lactamase enzymes.

Penicillinase-producing *Neisseria gonorrhoeae* (PPNG) resists plain amoxicillin by destroying it with beta-lactamase. Adding clavulanic acid restores amoxicillin activity against these strains. This is mechanistically coherent with the drug's existing use in other bacterial infections, including urinary tract infections.

However, resistance to gonorrhoea treatment has since shifted to non-beta-lactamase mechanisms (such as chromosomal and penicillin-binding protein changes), and current guidelines favour ceftriaxone. The prediction is therefore plausible pharmacologically but of limited current clinical relevance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3533755](https://pubmed.ncbi.nlm.nih.gov/3533755/) | 1986 | Randomised comparative trial | Genitourin Med | Amoxicillin 3 g + clavulanic acid 0.25 g (with probenecid) compared with cefuroxime axetil for uncomplicated urogenital and rectal gonorrhoea in 500 patients |
| [6365235](https://pubmed.ncbi.nlm.nih.gov/6365235/) | 1984 | Comparative clinical trial | Br J Vener Dis | In 121 men, single-dose oral amoxicillin-clavulanate had 9.4% culture-positive at day 7 vs 26.3% with intramuscular procaine penicillin |
| [6428699](https://pubmed.ncbi.nlm.nih.gov/6428699/) | 1984 | Clinical study | Br J Vener Dis | Two-dose Augmentin cured 95.9% of 97 men vs 87.4% with kanamycin; equally effective against PPNG |
| [4007860](https://pubmed.ncbi.nlm.nih.gov/4007860/) | 1985 | Clinical study (dose comparison) | Genitourin Med | Single-dose amoxicillin 3 g + clavulanic acid 125 mg plus probenecid cured 97 of 100 patients; 11 of 13 PPNG infections cured |
| [3004176](https://pubmed.ncbi.nlm.nih.gov/3004176/) | 1985 | Clinical study | Afr J Med Med Sci | Single-dose Augmentin tested in Ibadan, Nigeria, where about 80% of strains were PPNG |
| [6757686](https://pubmed.ncbi.nlm.nih.gov/6757686/) | 1982 | Clinical study | Med J Malaysia | Single-dose oral amoxicillin-clavulanate in males with gonococcal urethritis (no abstract available) |
| [3147528](https://pubmed.ncbi.nlm.nih.gov/3147528/) | 1988 | Clinical study | Sex Transm Dis | Review of treatment options for antibiotic-resistant gonorrhoea, including clavulanic acid added to amoxicillin |
| [3132029](https://pubmed.ncbi.nlm.nih.gov/3132029/) | 1988 | Laboratory study | Hinyokika Kiyo | Susceptibility testing of 89 gonococcal isolates, including amoxicillin-clavulanate |
| [21947096](https://pubmed.ncbi.nlm.nih.gov/21947096/) | 2011 | Review | Rev Esp Quimioter | Best empirical treatment of urethritis in Madrid |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 11933C | APO-Amoxycillin and Clavulanic Acid | Oral tablet containing 875 mg amoxicillin (as trihydrate) with 125 mg clavulanic acid (as potassium clavulanate) | Not available in the compiled data |

---

## Safety Considerations

The following scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence; they do not come from product label text.

- **Disease associations listed as contraindications or cautions:** kidney disease, liver disease, gallbladder disease, cholestasis (including benign recurrent and familial intrahepatic forms), *Clostridium difficile* colitis, perinatal necrotising enterocolitis, pyoureter, infectious mononucleosis, and chronic Epstein-Barr virus infection syndrome.
- **Drug Interactions:** 16 interactions were identified.
  - **Major:** leflunomide, teriflunomide
  - **Moderate:** methotrexate, tioguanine, epirubicin, clofarabine, trabectedin, idelalisib, brentuximab vedotin, asparaginase (*E. coli*), pegaspargase, interferon beta-1a, interferon beta-1b, peginterferon beta-1a, naltrexone, balsalazide

Please refer to the TGA-approved Product Information (PI) for authoritative warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is sound, and 1980s studies showed high cure rates for gonococcal urethritis. The evidence is old, small and not from Phase 3 RCTs, and current guidelines favour ceftriaxone because of widespread resistance. The other nine predictions have no human trial evidence or lack a plausible mechanism (for example, Ureaplasma urethritis, celiac trunk compression syndrome and abdominal ectopic pregnancy).

**To proceed, the following is needed:**
- Current Australian gonococcal resistance surveillance data for amoxicillin-clavulanate
- Comparison with current guideline-recommended therapy
- Mechanism of action data and TGA Product Information warnings and contraindications (currently missing)
- The approved indication text for the ARTG entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

