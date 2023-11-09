# 0x19. Postmortem - When the Authentication Gremlins Attacked

- DevOps
- SysAdmin

> ## Postmortem

## Issue Summary
- **Duration**: 4 hours, from 11:00 AM to 3:00 PM (PST)
- **Impact**: The authentication service went on a coffee break, leaving users stranded outside the gates. About 30% of users were left frantically refreshing their screens, hoping for a miracle.
- **Root Cause**: It turns out our authentication service had a bad hair day due to a mischievous misconfiguration update, leading to a dramatic database connection meltdown.

## Timeline
- **11:00 AM**: The first sign of trouble was a sudden influx of error logs in the authentication service. It was like the gremlins were throwing a party in there.
- **Actions Taken**: We delved into the database connection and scanned through the logs, initially blaming it on a pesky network glitch. Oh, the naivety!
- **Misleading Investigation**: Our quest began with a wild goose chase for network connectivity issues. It felt like we were trying to catch shadows.
- **Escalation**: By 12:00 PM, the authentication drama had reached its peak, and we had to call in the senior backend engineering heroes. The gremlins were putting up a fierce fight.
- **Resolution**: At the stroke of 3:00 PM, after an intense battle with the misconfiguration beast, we finally exorcised the gremlins by rolling back to the last stable version and giving the authentication service a good old restart.

## Root Cause and Resolution
- **Root Cause**: The gremlins, in the form of a misconfiguration, disrupted the database connection, pushing our authentication service into a full-blown crisis mode.
- **Resolution**: With our holy rollback spell and a dash of optimized database connection parameters, we managed to restore peace in the kingdom, ensuring the gremlins wouldn't dare show their faces again.

## Corrective and Preventative Measures
- **Improvements**: We're reinforcing our fortress by fortifying the monitoring system to catch any mischievous misconfigurations and database connection dramas. We're also conjuring automated rollback spells for those critical services.
- **Tasks to Address the Issue**:
    1. Putting misconfigurations on a strict diet by implementing rigorous code review processes.
    2. Training our crystal ball to proactively monitor critical service parameters, including database connections and error logs.
    3. Crafting automated rollback spells to swiftly banish any mischievous gremlins that dare disturb our service peace.
    4. Hosting a "Lessons from the Gremlin War" seminar with the engineering team to ensure we all know how to spot and tackle these shenanigans in the future.

## Additional Details and Images

### Error Spike in Authentication Service
![Error Spike](https://queue-it.com/media/jwmdupq1/load-testing-vs-stress-testing-vs-spike-testing.jpg)

### Misconfigured Update in Authentication Microservice
![Misconfiguration](https://camo.githubusercontent.com/b20cd5cb2979187f267b696657e4cbb7e29a3a051efb1ba9845304296a01481e/68747470733a2f2f7665676c6f732e6769746875622e696f2f6173736574732f696d672f323032312d31312d30382d646f746e65742d617574682d6d6963726f736572766963652d776974682d636c65616e2d6172636869746563747572652f617574682d6d6963726f736572766963652e6a7067)

### Rollback and Service Restart
![Rollback and Restart](data:image/png;base64,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)