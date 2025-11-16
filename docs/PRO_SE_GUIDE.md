# Pro Se Medical Malpractice Research Guide

This guide explains how to use the new CourtListener MCP Server APIs for Pro Se (self-represented) litigants researching medical malpractice cases.

## New APIs for Pro Se Research

### 1. Financial Disclosure Tools

These tools help you research the financial interests of judges who may preside over your case.

#### Search Financial Disclosures
```python
search_financial_disclosures(
    q="medical investments",
    person_name="Smith",
    year=2023,
    order_by="year desc",
    limit=20
)
```

**Use Cases:**
- Research potential conflicts of interest
- Understand judge financial holdings
- Identify judges with medical industry investments

#### Get Specific Financial Disclosure
```python
get_financial_disclosure(disclosure_id="12345")
```

### 2. Judge Background Research

#### Get Judge Position Information
```python
get_position(position_id="67890")
```

**Information Includes:**
- Court assignments
- Appointment dates
- Appointing authority
- Position type and status

#### Get Judge Education
```python
get_education(education_id="11223")
```

**Information Includes:**
- Law school attended
- Degrees obtained
- Graduation dates

#### Get Law School Information
```python
get_school(school_id="44556")
```

### 3. Case Document Research

#### Get Docket Entry Details
```python
get_docket_entry(entry_id="78901")
```

**Use Cases:**
- Track motions and filings
- Review court orders
- Understand case progression
- Research similar medical malpractice filings

**Information Includes:**
- Filing date and description
- Associated documents
- Entry number and sequence
- Document text (when available)

#### Get Originating Court Information
```python
get_originating_court_information(oci_id="23456")
```

**Use Cases:**
- Understand case transfer history
- Research trial court decisions
- Track appeals process

## Pro Se Medical Malpractice Research Workflow

### Step 1: Research Similar Cases
Use existing search tools to find relevant medical malpractice precedents:
```python
search_opinions(
    q="medical malpractice wrong implant",
    court="orctapp",  # Oregon Court of Appeals
    filed_after="2020-01-01"
)
```

### Step 2: Research Presiding Judges
Once you know which judges may hear your case:

1. Search for the judge:
```python
search_people(q="Judge Name", position_type="jud")
```

2. Get judge details:
```python
get_person(person_id="<from_search>")
```

3. Check financial disclosures:
```python
search_financial_disclosures(
    q="",
    person_name="Judge Name",
    year=2023
)
```

4. Review judge's positions and education:
```python
get_position(position_id="<from_person_details>")
get_education(education_id="<from_person_details>")
```

### Step 3: Review Case Documents
For cases with detailed docket entries:

1. Search for similar cases:
```python
search_dockets_with_documents(
    q="medical malpractice",
    court="<court_id>",
    date_filed_after="2020-01-01"
)
```

2. Get specific docket entries:
```python
get_docket_entry(entry_id="<from_docket>")
```

### Step 4: Research Case History
For appealed cases:
```python
get_originating_court_information(oci_id="<from_docket>")
```

## Important Notes for Pro Se Litigants

1. **Conflicts of Interest**: Financial disclosures can help identify potential judicial conflicts, but this is complex legal territory. Consider consulting with a lawyer about what constitutes a disqualifying conflict.

2. **Judicial Research**: Understanding a judge's background, education, and prior rulings can help you prepare your case presentation.

3. **Document Access**: Not all documents are available through the API. Some may require PACER access or direct court requests.

4. **Precedent Research**: Use search tools to find similar cases and understand how courts have ruled on similar medical malpractice issues.

5. **Proper Citation**: When citing cases in your filings, use the citation tools to ensure proper formatting:
```python
verify_citation_format(citation="123 F.3d 456")
```

## Additional Resources

- [CourtListener API Documentation](https://www.courtlistener.com/api/rest/v4/)
- [Main README](../README.md)
- [API Reference](../app/README.md)
- [Test Examples](../tests/test_new_tools.py)

## Disclaimer

This tool provides access to public legal information but does not constitute legal advice. Pro Se litigants should:
- Understand court rules and procedures
- Consider consulting with an attorney
- Follow all court deadlines and requirements
- Review local court rules for your jurisdiction

The information provided through these APIs is for research purposes only.
