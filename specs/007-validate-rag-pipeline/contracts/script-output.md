# Contract: Script Output Format

**Feature**: 007-validate-rag-pipeline

## Description

This document defines the expected structure and content of the `backend/test_retrieval.py` script's output to standard output (stdout). The output is designed to be human-readable and provide clear validation results for each query.

## Output Structure

The script will output results for each test query in a structured format, separated by clear delimiters.

### Per Query Output Block

For each query, the script will print a block similar to the following:

```
============================================================
Query: '[User Query Text]'
  Latency: [X.XXX]s
  Matches Found (Score >= [threshold]): [N]
  -> [Optional: "No relevant results found above threshold." message]

    [Result Index]. [Score] [Title]
       URL: [Source URL]
       Snippet: [Text Snippet (truncated)]...
    --------------------
    [Next Result]
    ...

------------------------------------------------------------
```

### Fields

-   **`Query`**: The original natural language query string.
-   **`Latency`**: The time taken for the entire retrieval process (embedding + Qdrant search), formatted as `X.XXXs`.
-   **`Matches Found (Score >= [threshold])`**: The count of results that passed the similarity threshold filter.
-   **`No relevant results found above threshold.`**: An optional message displayed if `Matches Found` is 0.
-   **`[Result Index]`**: A sequential number for each displayed result (e.g., `1.`, `2.`, `3.`).
-   **`[Score]`**: The similarity score of the retrieved chunk, formatted as `[0.XXX]`.
-   **`[Title]`**: The `title` metadata field from the retrieved chunk's payload.
-   **`URL`**: The `source_url` metadata field from the retrieved chunk's payload.
-   **`Snippet`**: A truncated version of the `text` content from the retrieved chunk's payload, followed by `...`.

### Delimiters

-   `============================================================`: Marks the beginning of a new test query's results.
-   `------------------------------------------------------------`: Marks the end of a test query's results.
-   `--------------------`: Separates individual search hits within a query's results.

## Error Handling

- If an error occurs during embedding or Qdrant querying, an error message will be printed, and subsequent results for that query will be skipped.
- The script will continue processing other queries even if one fails.
