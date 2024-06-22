
# URL Tracking and Redirection Service

## Overview
This service is designed as a proxy to facilitate URL tracking and redirection. When users click on a shortened URL, this service captures their user-agent and IP address, logs this information, and then redirects them to the intended destination URL. This is particularly useful for analytics and tracking the effectiveness of marketing campaigns.

## How It Works
1. **Shortened URL Creation**: A user creates a shortened URL using an external service (like bit.ly). This shortened URL points to this proxy service with specific query parameters (`ref_code` and `dst`) that include the destination URL and an optional reference code for tracking purposes.

2. **Data Capture**: When the shortened URL is accessed, the service captures the following information from the user's request:
   - IP address
   - User-Agent
   - Reference code (if provided)
   - Timestamp of the access
   - Destination URL

3. **Redirection**: After logging the data, the service redirects the user to the actual destination URL specified in the `dst` parameter.

4. **Logging**: All captured data is appended to a text file, which can be used for further analysis.

## Usage
To use this service:
1. Ensure your application is running and accessible via a public IP or domain.
2. Generate a shortened URL using a service like bit.ly that points to `http://[your-service-url]/info?ref_code=[optional-ref-code]&dst=[destination-url]`.
3. Distribute the shortened URL. When accessed, user data will be logged, and they will be redirected to the destination URL.

Example URL:
```
http://your-service-url/info?ref_code=123&dst=http%3A%2F%2Fgoogle.com
```


## Logs
Logs are stored in a text file `user_data.txt` within the project directory.
