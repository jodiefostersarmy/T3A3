## Why?
**User story #1:** As a user, I want to filter search results, so that I can find more specific relevent content.

**User story #2:**  As a business, we want to use more targeted hashtags, so that local users can find our products/profile easily.

**User story #3:** As part of the Facebook ad team, we would like to connect more users with businesses, so that we can monetise the hashtag feature.

### Stakeholders

- users - access to public interface
- developers - access to MVC for maintence and deployment

## Goals

- Provide deeper hashtag search functionality.
- Allows users to filter their searches and return hard search results.

## Application Views

- Main: explore page will contain images of random hashtags
- search bar

## Roadmap
- [ ] Set up EC2, DB, RDS, VPC
- [ ] create application layer interface for CRUD resource
- [ ] create authentication mechanism to verify users
- [ ] database to store user hashtag searches
- [ ] 
- [ ] 
- [ ] 


## Report Questions

Q: How can we handle cross-site request forgery (CSRF), and is this a threat to our app? In what instance would it be? 
Q: Is the CSRF the same as a JWT token to stop an outside form being submitted to our servers with malicious code?