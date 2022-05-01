

## Fetch Some Charts

- Start by listing repositories that Helm knows:  
**helm repo list**  
(If Helm was just installed, you should see only one repository)
- Fetch some charts:  
**helm fetch stable/jenkins**  
**helm fetch stable/spark**
- Use **ls** to see the **packaged charts** downloaded.
- Index your charts:  
**helm repo index ./1-chart-repositories/**
- See the indexing result:  
** ls -l**
