# Web Stack Outage Postmortem: A Creative Incident
## Issue Summary
**Duration**: The outage occurred from _10:00_ AM to _12:30_ PM UTC on May 8, 2024. Impact: Our primary service, the Widgetify API, experienced a complete outage. Users were unable to retrieve widgets, resulting in a 100% service disruption.

## Timeline
* **10:00 AM**: The issue was detected when our monitoring system triggered an alert for unusually high error rates in the Widgetify API.
* **10:15 AM**: The incident response team (IRT) convened. Initial investigation revealed that the database connection pool was saturated.
* **10:30 AM**: Assumptions were made that the database server was overwhelmed due to a sudden spike in traffic.
* **10:45 AM**: Debugging paths included examining query logs, checking for slow queries, and reviewing recent code deployments.
* **11:00 AM**: The incident was escalated to the database administration team.
* **11:30 AM**: Further investigation revealed that the database server was not the root cause; it was a misconfigured caching layer.
* **12:00 PM**: The caching layer was disabled, and the API service was restored.
* **12:30 PM**: The incident was resolved.
## Root Cause and Resolution
### Root Cause:
The root cause was a misconfiguration in the Redis cache. The cache eviction policy was set too aggressively, causing frequent cache misses. As a result, the API service had to fetch data from the database for every request, leading to saturation of the database connection pool.

### Resolution:
**Immediate Fix**: We disabled the Redis cache to restore service availability.
**Long-Term Fix**:
**Tuning Cache Policies**: We adjusted the cache eviction policy to strike a balance between cache hit rates and memory usage.
Monitoring Enhancements: We added monitoring for cache hit rates and memory utilization.
* **Documentation Update**: We documented the correct cache configuration to prevent similar issues in the future.
Corrective and Preventative Measures
Code Review: Conduct a thorough review of caching-related code during deployments.
* **Automated Testing**: Implement automated tests to verify cache behavior under different load scenarios.
* **Capacity Planning**: Regularly assess resource utilization and scale the cache infrastructure accordingly.
* **Incident Response Training**: Train engineers on effective debugging techniques and escalation procedures.
