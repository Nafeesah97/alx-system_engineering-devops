# Issue Summary

From 6:00 AM WAT to 6:16 AM WAT, requests to tayseer website resulted in 500 error responses (Internal server error). 100% of the HTTP request to this website failed and the user's browser could not get an HTTP response. The root cause of this outage was an invalid configuration in the PHP configuration file.
![Alt text](image-1.png)

# Timeline (all times West African Time)

- 6:00 AM: a function was added to the configuration file
- 6:03 AM: Outage began. HTTP response not sent to the clients
- 6:03 AM: Pager alerted team
- 6:04 AM: On-call engineer began troubleshooting
- 6:05 AM: The engineer looked at the load-balancer log files
- 6:10 AM: The engineer looked at the web servers’ logs
- 6:11 AM The engineer used strace to trace the problem on the webservers
- 6:13 AM:  The engineer found the PHP configuration to be invalid
- 6:15 AM: The engineer corrected the misspelling.
- 6:16 AM: Server restarts begin
- 6:16 AM: 100% traffic back online

![Alt text](image.png)

# Root cause and resolution

At 6:00 AM WAT, a configuration change was inadvertently released into the production without checking the validity of the newly updated configuration file. This update was done on all the servers which resulted in 100% HTTP request failure. Strace was used to trace back what was wrong when trying to load the website. It was discovered that something was wrong with a PHP extension file mentioned in the PHP configuration file due to a misspelling (‘p’ was typed twice). The configuration file was corrected for the misspelling and the server was restarted. At 6:16 AM, the website was fully functional.

# Corrective and preventative measures

 This outage was not a web server error, but an application error. To prevent such outages moving forward, please keep the following in mind.
Test! Test test test. Test the application before deploying. This error would have arisen and could have been addressed earlier had the app been tested.
Status monitoring. Enable some uptime-monitoring services such as UptimeRobot to alert instantly upon outage of the website.
Checking for the validity of configuration files to prevent unnecessary behaviors.

