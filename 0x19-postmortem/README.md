## **# Postmortem: Database Connection Failure Impacting User Authentication**

## **Issue Summary**
**Duration:** March 10, 2025, 14:30 - 15:15 UTC (45 minutes)  
**Impact:** User authentication service was down, preventing 80% of users from logging in. Some users with active sessions could still browse but could not make new requests requiring authentication.
**Root Cause:** A misconfigured database connection pool limit caused the application servers to exhaust available connections, leading to authentication failures.

## **Timeline**
- **14:30 UTC** - Monitoring alert detected an increase in failed login attempts.
- **14:32 UTC** - Engineers confirmed the issue through logs showing repeated database connection failures.
- **14:35 UTC** - Initial assumption: Possible network outage between the application and database servers.
- **14:40 UTC** - Network engineers confirmed no connectivity issues.
- **14:45 UTC** - Debugging efforts focused on database performance metrics; CPU and memory were within normal ranges.
- **14:50 UTC** - Deeper investigation into database connection limits revealed that the maximum connection pool size had been reduced in a recent deployment.
- **15:00 UTC** - Temporary fix applied by increasing the connection pool limit and restarting affected services.
- **15:15 UTC** - Full recovery confirmed, with normal login rates restored.

## **Root Cause and Resolution**
### **Root Cause**
A configuration update during a routine deployment unintentionally reduced the maximum database connection pool size from 200 to 50. As a result, the application quickly exhausted available connections, preventing new authentication requests from succeeding.

### **Resolution**
Engineers increased the connection pool limit back to 200 and restarted the application servers to allow new connections. This immediately restored authentication services.

## **Corrective and Preventative Measures**
### **Improvements Needed:**
- Better validation of configuration changes before deployment.
- More comprehensive monitoring of database connection usage.
- Automated rollback for configuration-related failures.

### **Action Items:**
1. **Add a pre-deployment check** to ensure database connection limits are not reduced unintentionally.
2. **Implement database connection monitoring** to detect and alert on connection saturation earlier.
3. **Introduce automated rollback mechanisms** to revert configurations when critical failures occur.
4. **Improve documentation and change review processes** to ensure awareness of configuration changes.

This incident highlighted the importance of **thorough change validation** and **better monitoring** to prevent service disruptions. Going forward, these measures will help mitigate similar issues.


