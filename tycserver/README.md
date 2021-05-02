


```bash
curl -i -X POST -H "X-Auth-Token: gAAAAABggrZNDtccG8BUfXDfOw3IKYz09HLmxvPpERinkDwJYGOzMBoxZEUWRIAydO4y0hyg4nmCQ-DNi4XO8-wvnR5A-U9n-tMiMHsnxwe9JyyHLFFQk4pBa9qADzapb6DjtwqqiuDCWHUhLZjtxSnjf5aKkrJHf3BxJ-TLoqfAlJgG4MOIkoM" 192.168.122.102:8088/v1
```

```bash
curl -X GET -H "X-Auth-Token: gAAAAABgicgiYNpw7c_q8y1uINutd6-ID-bOmqP4YyseryLCsvR2189YrloyG13-7QCGkswDFLk8YE0pypqUNahHGMpBBXmp_hNTwqgTVwMgPfepr6-iQG3acDaMcJ9bl3qKYWcQuveI0Gcx-6QSNl5AGwiZ_mAgvVAvYLgnWR0cd83OgPdwG8s" 192.168.122.102:8088/v1/nodes
```

```bash
curl -X POST -H "X-Auth-Token: gAAAAABgicI-pSOjS2QAbeXfnEC-r5ymh0z2lNc0YdQLgik9WC_8OYrh3789nVefu9Lc0_e0Qi0CAP4MKMpYojpr-STBXruCi_gehM3-uuWV6yt5uyNBxYLUip5gT5beZucbcjTnHTXA17TcpLzvlFtURZBUZU9-WNbFbiCBgvqBOmL2RsASGxw" -H "Content-Type: application/json" -d '{"name":"compute-node-01", "ipaddress": "192.168.122.201", "password": "asdasdasasdasd", "user": "santos"}' 192.168.122.102:8088/v1/nodes
```


