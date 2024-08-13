# Postmortem: API Rate Limiting Outage

## Issue Summary
- **Duration:** August 10, 2024, 1:00 PM to 3:45 PM PDT
- **Impact:** The primary API service was down, affecting 70% of users. Users experienced errors when making API calls, including timeouts and 500 Internal Server Errors.
- **Root Cause:** A misconfigured rate limiting policy caused excessive throttling, preventing legitimate API requests from being processed.

![API Rate Limiting Error](link_to_error_screenshot.png)  <!-- Placeholder for screenshot showing API error -->

## Timeline
- **1:00 PM PDT:** Issue detected; users reported API errors.
- **1:05 PM PDT:** Monitoring alert triggered for high API error rates.
  ![Monitoring Alert](link_to_alert_screenshot.png)  <!-- Placeholder for screenshot of monitoring alert -->
- **1:10 PM PDT:** Initial investigation focused on server logs; no hardware issues found.
- **1:30 PM PDT:** Assumed issue might be related to recent deployment; rollback initiated.
  ![Rollback Process](link_to_rollback_screenshot.png)  <!-- Placeholder for screenshot of deployment rollback process -->
- **2:00 PM PDT:** Rolled back deployment did not resolve issue; escalation to the API team.
- **2:15 PM PDT:** API team identified incorrect rate limiting configuration as the root cause.
  ![Rate Limiting Config](link_to_rate_limiting_config_screenshot.png)  <!-- Placeholder for screenshot showing rate limiting configuration -->
- **2:30 PM PDT:** Adjusted rate limiting policy; changes deployed to the live environment.
- **3:00 PM PDT:** Gradual restoration of service observed; monitoring confirmed stability.
  ![Service Restoration](link_to_service_restoration_screenshot.png)  <!-- Placeholder for screenshot showing API service restoration -->
- **3:45 PM PDT:** Full resolution; normal API performance restored.

## Root Cause and Resolution
- **Root Cause:** The issue was due to an overzealous rate limiting policy applied to the API service. A recent configuration change set the rate limits too low, resulting in legitimate API requests being throttled excessively.
  ![Rate Limiting Impact](link_to_rate_limiting_impact_screenshot.png)  <!-- Placeholder for screenshot illustrating the impact of rate limiting -->
- **Resolution:** The rate limiting policy was adjusted to more appropriate thresholds. The configuration was reviewed and corrected to align with expected traffic patterns. Additional tests were conducted to ensure no further impact.
  ![Fixed Configuration](link_to_fixed_configuration_screenshot.png)  <!-- Placeholder for screenshot showing corrected rate limiting configuration -->

## Corrective and Preventative Measures
- **Improvements:**
  - **Configuration Management:** Enhance review processes for configuration changes.
  - **Monitoring:** Improve monitoring for API rate limits and error rates with more granular alerts.

- **Tasks:**
  - **Review Process:** Implement a change review checklist for configuration changes, including rate limits.
  - **Monitoring:** Set up specific alerts for API rate limit thresholds and error rates.
  - **Documentation:** Update documentation to include rate limiting policies and their impact on API performance.
  - **Testing:** Introduce automated tests for rate limiting changes to ensure proper configurations before deployment.

![Preventative Measures](link_to_preventative_measures_screenshot.png)  <!-- Placeholder for screenshot illustrating preventative measures -->

