# IT149IU Lab 6 - Dictionaries & Sets (Phase A + Phase B)

**Student:** Nguyễn Viết Huy  
**Student ID:** ITDSIU24021  
**Class / Group:** IT149IU – Group 01

## What is included
- `notebooks/IT149IU_Lab6_A_ITDSIU24021.ipynb`: Phase A only (compulsory Tasks 1-4).
- `notebooks/IT149IU_Lab6_B_ITDSIU24021.ipynb`: complete notebook (Phase A + optional Phase B Tasks 5-6).
- Root copy `IT149IU_Lab6_B_ITDSIU24021.ipynb`: complete notebook for the Phase B submission.
- `codes/`: standalone Python scripts, one per task.
- `outputs/`: executed text transcripts and PNG transcript images; includes the Task 3 chart.
- `FoP_Lab6_Report.pdf`: report for Form C.

## Exact notebook submission workflow
1. **Form A (compulsory):** submit the Phase A notebook as `IT149IU_Lab6_A_ITDSIU24021.ipynb` by the minute-60 checkpoint.
2. **Form B (optional):** submit the full notebook as `IT149IU_Lab6_B_ITDSIU24021.ipynb` by the minute-110 checkpoint.
3. **Form C:** submit the report within 24 hours. The starter says late work is counted at 50% and only if it improves on the on-time work.

## Run locally
Use Python 3.10+ and Jupyter Notebook/JupyterLab/Colab. For the word-frequency chart, install Matplotlib if needed:
```bash
pip install matplotlib
```
Run the notebook from top to bottom. The setup cell uses a seed derived from the student ID, so the generated sample data is reproducible.

## Implementation conventions
- Email normalization: strip spaces and lowercase; malformed entries are ignored. `unique_emails` de-duplicates while preserving first-seen order; `domain_counts` counts each valid raw entry, including duplicates.
- Word frequency: lowercase alphanumeric words (optional internal apostrophe); ties are alphabetical.
- Staff functions: `by_branch` returns branch to a list of `(employee_id, record_copy)` pairs. `raise_salary` changes matching records in place and accepts `0.05` or `5` for a five-percent increase.
- Anagram groups with only one word are omitted. Search is case-insensitive.

## Source limitation
The uploaded starter notebook references an accompanying PDF handout, but that PDF was not supplied or found in the accessible file library. The implementation and checks therefore follow the notebook's own task text, required function names, setup variables, and docstrings. Check any examples specific to the PDF handout before submitting.

## AI-use disclosure
ChatGPT was used to help draft and review the code, tests, pseudocode, and report. Review and understand each function before submission, and retain this disclosure in the Form C notes if required.
