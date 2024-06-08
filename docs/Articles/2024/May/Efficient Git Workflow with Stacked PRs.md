---
tags:
  - topic/platform-engineering
  - topic/devops
categories:
  - Engineering
title: Efficient Git Workflow with Stacked PRs
coverImage: https://upload.wikimedia.org/wikipedia/commons/2/2e/Sport-Stacking.jpg
public: true
ShowToc: true
date: 2024-05-11
---
# Efficient Git Workflow with Stacked PRs

Engineering teams are only as fast as their PR merges. As seasoned engineers, its our task to streamling the process of merging PRs as smoothly as possible. 
This challege becomes multiple folds when we factor in code ownership, large meta repos and non-negotiable need for good code reviews. 
Today I want to share a stacked PR worflow which has worked great for our teams specially in context of remote first organizations. 

<!-- more -->
## Illustrate the problem

![Efficient Git Workflow with Stacked PRs-image-20231228203144373](Assets/media/Efficient%20Git%20Workflow%20with%20Stacked%20PRs/Efficient%20Git%20Workflow%20with%20Stacked%20PRs-image-20231228203144373.png)


### Big PRs
- %% statistics about time spent by senior devs in PR reviews. short 2-3lines. quote with reference+statistics from mid sized startups %%
- %% why big PRs are harder to make sense of . general intro - 2 lines.  %%
	- %% define BIG PR.  400line changes as per google's guidelines.   short , 2 lines %%
	- %% types of PR changes. chore vs feature, vs hotfix vs bugfix vs improvement.  refer to conventional commits.  Any PR mixing these changes into one single Big PR is trying to do too much. violates KISS.  elaborate with 3-4lines %%
- %% The need to make a PR reviewer responsible/accountable for PRs they accept. can't expect this, if PRs aren't easy to understand/work with %%
	- %% where does the buck stop when changes cause issues.  PR reviewers will happily take responsibility, if they knew what they were signing off on.  %%
	- %% people delay proper reviews, or only do code-read reviews if the changes are large.  smaller changes are easier to pull, run and verify %%

### Meta-repos and PR Reviews
- %% Rise of meta-repos. infra as code, documentation as code, client side components, microservice backends, multiple languages %%
- %% code ownership models and multiple owners for large PR dilutes responsibility %%
- %% mixing multiple component changes into one PR always puts the focus on the most changed component. ideally should have focus on ALL components. non-negotiable for quality %%
### PRs with separation of concern. 
- %% Difficulty building tools for CI/CD when PRs get more complex %%
	- %% easier to write workflows and CI for small PRs which are isolated to components. QA needs this to guarantee tests provide a safety net for velocity. 3-4 lines %%


## Talk about the Core Idea of the Solution


## Evidence about the Solution Approach


## Solution Playbook 


## Call to Action


## Footnotes
1. [How to visualize stacked git branches | by Greg Foster | Medium](https://gregmfoster.medium.com/how-to-visualize-stacked-git-branches-e10827242304)
2. [Stacked Diffs: Keeping Phabricator Diffs Small | by Kurtis Nusbaum | Medium](https://kurtisnusbaum.medium.com/stacked-diffs-keeping-phabricator-diffs-small-d9964f4dcfa6)
3. [Stacked pull requests: make code reviews faster, easier, and more effective - Dr. McKayla](https://www.michaelagreiler.com/stacked-pull-requests/)
4. [Stacked Diffs Versus Pull Requests | Jackson Gabbard's Blog](https://jg.gg/2018/09/29/stacked-diffs-versus-pull-requests/)
5. [Stacked Diffs versus Pull Requests (2018) | Hacker News](https://news.ycombinator.com/item?id=26922633)
6. [GitHub - timothyandrew/gh-stack: Manage PR stacks/chains on Github](https://github.com/timothyandrew/gh-stack/)
7. [Graphite - How the fastest developers ship code | Graphite](https://graphite.dev/)
8. [spr | Stacked Pull Requests on GitHub](https://ejoffe.github.io/spr/)
9. [Stacked PRs](https://www.aviator.co/stacked-prs)
10. [Stacked Pull Requests · GitHub Marketplace · GitHub](https://github.com/marketplace/stacked-pull-requests)
11. [How to Handle Stacked Pull Requests on GitHub | PSPDFKit](https://pspdfkit.com/blog/2021/how-to-handle-stacked-pull-requests-on-github/)
12. [Stacked Pull Requests](https://matt-rickard.com/stacked-pull-requests)
13. [A Better Model for Stacked (GitHub) Pull Requests • Timothy Andrew](https://timothya.com/blog/git-stack/)
14. Experimental Ideas as used in Linux Kernel
	1. [GitHub - arxanas/git-branchless: High-velocity, monorepo-scale workflow for Git](https://github.com/arxanas/git-branchless)
