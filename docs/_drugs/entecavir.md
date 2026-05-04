---
layout: default
title: Entecavir
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 10
---

# Entecavir
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

# Entecavir: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Entecavir is a guanosine nucleoside analogue approved internationally as a first-line treatment for chronic hepatitis B virus (HBV) infection, though it is not currently registered in Australia.
The TxGNN model predicts it may have potential activity against **Chronic Hepatitis C Virus Infection**,
with **40 clinical trials** and **20 publications** identified in the evidence search — the vast majority, however, relate to HBV management or HBV/HCV co-infection scenarios rather than direct HCV treatment.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic Hepatitis B virus (HBV) infection (internationally approved; not currently registered in Australia) |
| Predicted New Indication | Chronic Hepatitis C Virus Infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Australia Market Status | Not Registered |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Entecavir is a guanosine deoxyribose nucleoside analogue that selectively inhibits the hepatitis B virus (HBV) DNA polymerase. It acts by mimicking the natural substrate deoxyguanosine triphosphate: once incorporated into the growing viral DNA chain, it causes chain termination. This mechanism blocks all three critical activities of the HBV polymerase — base priming, reverse transcription of the negative-strand DNA from pregenomic RNA, and positive-strand HBV DNA synthesis. Although detailed mechanism of action data was not available in this evidence pack, entecavir is well-characterised internationally as a potent, highly selective HBV antiviral with an exceptionally high barrier to resistance — it is a recommended first-line agent in WHO, EASL, and APASL guidelines for chronic HBV.

The mechanistic rationale for repurposing entecavir to chronic hepatitis C virus (HCV) infection is, however, limited. HCV is an RNA virus that replicates via an RNA-dependent RNA polymerase (NS5B) — a structurally and functionally distinct enzyme from the HBV reverse transcriptase that entecavir targets. Approved anti-HCV nucleoside analogues such as sofosbuvir specifically inhibit NS5B, and entecavir has not demonstrated direct inhibitory activity against HCV NS5B in published preclinical data. Nonetheless, there are plausible reasons why the TxGNN knowledge graph would surface this prediction: both HBV and HCV are hepatotropic viruses causing chronic liver inflammation, drive shared pathological pathways (fibrosis → cirrhosis → hepatocellular carcinoma), and are commonly encountered together in overlapping at-risk patient populations.

Importantly, in clinical practice, entecavir IS used in patients receiving HCV treatment — but its role is limited to suppressing HBV reactivation triggered by direct-acting antiviral (DAA) therapy, not to treating HCV directly. This real-world co-management context is likely captured within the model's knowledge graph and has informed the prediction. This distinction is critical to interpreting the recommendation.

---

## Clinical Trial Evidence

The trials identified predominantly relate to HBV management; the most HCV-relevant studies are listed below.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Prospective study of DAA therapy in chronic HCV/HBV co-infected patients; determined incidence and risk factors of HBV reactivation during anti-HCV treatment — entecavir used as HBV prophylaxis rather than HCV treatment |
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | N/A | Unknown | 60 | Three-arm randomised study evaluating prophylactic nucleos(t)ide analogue (including entecavir) to prevent HBV reactivation in HCV/HBV co-infected patients receiving DAA therapy for chronic HCV; assessed 12-week vs 24-week prophylaxis duration |
| [NCT01018381](https://clinicaltrials.gov/study/NCT01018381) | N/A | Completed | 130 | Randomised study of arabinoxylan rice bran (MGN-3/Biobran) for HCC and hepatitis B and C infection; explored immunomodulatory adjuncts to standard antiviral therapy |
| [NCT01270178](https://clinicaltrials.gov/study/NCT01270178) | N/A | Unknown | 420 | Prospective trial of entecavir for chronic HBV in HCC patients post radiofrequency ablation; references anti-HCV therapy as a model for reducing HCC recurrence |
| [NCT00597259](https://clinicaltrials.gov/study/NCT00597259) | Phase 4 | Unknown | 294 | Pegasys plus entecavir vs entecavir alone for HBeAg-positive CHB; drew on HCV and HIV combination therapy experience as a conceptual framework for combination HBV strategies |
| [NCT00096785](https://clinicaltrials.gov/study/NCT00096785) | Phase 3 | Completed | 69 | Entecavir vs adefovir in nucleoside-naive CHB adults; established entecavir antiviral activity benchmark relevant to broad hepatitis research context |
| [NCT00065507](https://clinicaltrials.gov/study/NCT00065507) | Phase 3 | Completed | 195 | Phase IIIb comparison of entecavir 1.0 mg vs adefovir in CHB with hepatic decompensation; established entecavir efficacy in advanced liver disease |
| [NCT03662568](https://clinicaltrials.gov/study/NCT03662568) | Phase 1 | Completed | 56 | Open-label drug-drug interaction study of morphothiadine mesilate/ritonavir combined with entecavir or TDF in healthy subjects |
| [NCT02532413](https://clinicaltrials.gov/study/NCT02532413) | Phase 4 | Unknown | 180 | Entecavir monotherapy versus combination with Poly IC for chronic HBV; compared antiviral efficacy of combination immunostimulation approach |
| [NCT06566248](https://clinicaltrials.gov/study/NCT06566248) | Phase 2 | Recruiting | 90 | Randomised double-blind Phase IIa trial of TQA3810 tablets combined with or without nucleoside analogues (including entecavir) in CHB patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohort | Viruses | HCV reactivation in anti-HCV antibody-positive CHB patients following nucleos(t)ide analogue (entecavir/lamivudine) therapy; HCV RNA increased in ~40% of patients during HBV suppression, highlighting viral interaction dynamics |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opin Pharmacother | Advances in HBV/HCV co-infection treatment; entecavir's role in preventing HBV reactivation during direct-acting antiviral HCV therapy discussed |
| [22959099](https://pubmed.ncbi.nlm.nih.gov/22959099/) | 2013 | Case Report | Clin Res Hepatol Gastroenterol | HBV/HCV co-infected patient case report; therapeutic challenge of dual viral hepatitis management — entecavir used for HBV component while HCV was managed separately |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Comparative overview of antiviral medications for HBV and HCV and their renal effects; positions entecavir as HBV-specific with distinct pharmacological profile from HCV agents |
| [21497740](https://pubmed.ncbi.nlm.nih.gov/21497740/) | 2011 | Review | Best Pract Res Clin Gastroenterol | Antiviral treatment impact on fibrosis progression in chronic viral hepatitis B and C; demonstrated shared pathological outcome of fibrosis reversal in both conditions |
| [35327336](https://pubmed.ncbi.nlm.nih.gov/35327336/) | 2022 | Review | Biomedicines | Therapy of chronic viral hepatitis B, C, and D; entecavir and tenofovir contextualised within the broader hepatology treatment landscape |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Review | Clin Res Hepatol Gastroenterol | Present and future management of viral hepatitis B and C in children; contrasts HBV treatment (entecavir) with HCV management approaches and shared liver disease burden |
| [28487602](https://pubmed.ncbi.nlm.nih.gov/28487602/) | 2017 | Review | World J Gastroenterol | HBV infection and alcohol consumption; contextualises HBV and HCV as the two leading causes of HCC and future treatment burden following DAA-driven HCV eradication |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | Chronic hepatitis B and C treatment overview; compared pegylated interferon and lamivudine strategies for both infections within a single therapeutic framework |
| [24868325](https://pubmed.ncbi.nlm.nih.gov/24868325/) | 2014 | Review | World J Hepatol | Management of HBV and HCV before and after liver and kidney transplantation; entecavir/tenofovir identified as preferred approach for peri-transplant HBV suppression in dual-infected patients |

---

## Australia Market Information

Entecavir is not currently registered in the Australian Register of Therapeutic Goods (ARTG). No ARTG entries were identified in this evidence search.

For reference, entecavir (brand name Baraclude®, Bristol-Myers Squibb) is approved by the US FDA (since March 2005) and the European Medicines Agency for treatment of chronic HBV in adults with evidence of active viral replication and active liver disease. It is similarly approved in many Asian and European jurisdictions. Prescribers seeking full product information should refer to international product labelling (US FDA Prescribing Information or EMA Summary of Product Characteristics) or contact the relevant product sponsor regarding Australian availability.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. As entecavir is not currently registered in Australia, no Australian TGA PI is available.

For clinical reference, the following key warnings are documented in international labelling:

- **Lactic acidosis and severe hepatomegaly with steatosis**: A rare but potentially life-threatening class effect of nucleoside/nucleotide analogues; treatment should be suspended if clinical or laboratory findings suggestive of lactic acidosis develop.
- **Severe acute exacerbation of hepatitis B on discontinuation**: Hepatic function should be monitored closely for several months after stopping entecavir in patients with HBV infection.
- **HIV resistance risk**: Entecavir selects for the lamivudine-resistance mutation M184V in HIV; it must not be used as monotherapy in HIV/HBV co-infected patients without a fully suppressive antiretroviral regimen — this is particularly relevant given the HCV/HIV co-infection context of this prediction.
- **Renal impairment**: Dose adjustment required for patients with creatinine clearance below 50 mL/min.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite the TxGNN model's high confidence score (99.98%), the mechanistic rationale for entecavir treating HCV is weak — entecavir inhibits HBV DNA polymerase reverse transcriptase, which is a fundamentally different enzyme from the HCV NS5B RNA-dependent RNA polymerase targeted by approved HCV antivirals. The clinical trials and literature retrieved are primarily HBV-focused; HCV appears only in the context of co-infection prophylaxis. No direct evidence of anti-HCV efficacy for entecavir has been identified.

**To proceed, the following is needed:**

- Direct in vitro preclinical evidence of entecavir activity against HCV NS5B polymerase or other HCV replication targets
- Full mechanism of action (MOA) data from DrugBank to clarify any potential cross-viral enzyme inhibition
- Dedicated pharmacokinetic/pharmacodynamic modelling for HCV target engagement at clinically relevant concentrations
- Clinical evidence from trials specifically enrolling HCV mono-infected patients (not co-infection prophylaxis studies)
- TGA registration pathway assessment and Australian ARTG submission feasibility review
- Australian-specific safety review encompassing lactic acidosis risk, renal dosing guidance, HBV reactivation monitoring, and HIV resistance risk in at-risk populations
- Australian Product Information (PI) document with complete safety, contraindication, and drug interaction data

> ⚠️ **Disclaimer**: This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require rigorous clinical validation before therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

